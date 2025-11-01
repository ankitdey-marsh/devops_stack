from flask import Blueprint, current_app, jsonify, request, abort, render_template
from datetime import datetime
import uuid

def register_routes(app):
    bp = Blueprint("api", __name__)

    # In-memory store for demonstration
    ITEMS = {}

    @bp.route("/health", methods=["GET"])
    def health():
        """Simple health check"""
        return jsonify({"status": "ok", "time": datetime.utcnow().isoformat() + "Z"}), 200

    @bp.route("/hello", methods=["GET"])
    def hello():
        """Greets caller, supports ?name= query"""
        name = request.args.get("name", "world")
        return jsonify({"message": f"Hello, {name}!"})

    @bp.route("/echo", methods=["POST"])
    def echo():
        """Echo back JSON payload"""
        if not request.is_json:
            return jsonify({"error": "Expected JSON body"}), 400
        payload = request.get_json()
        return jsonify({"echo": payload}), 200

    @bp.route("/add", methods=["GET"])
    def add():
        """Add two numbers via query params: /add?a=1&b=2"""
        try:
            a = float(request.args.get("a", "0"))
            b = float(request.args.get("b", "0"))
        except ValueError:
            return jsonify({"error": "a and b must be numbers"}), 400
        return jsonify({"a": a, "b": b, "sum": a + b})

    # Basic CRUD for items
    @bp.route("/items", methods=["GET"])
    def list_items():
        """List all items"""
        return jsonify({"items": list(ITEMS.values())})

    @bp.route("/items", methods=["POST"])
    def create_item():
        """Create a new item with JSON body {name, data}"""
        if not request.is_json:
            return jsonify({"error": "Expected JSON body"}), 400
        body = request.get_json()
        name = body.get("name")
        data = body.get("data", {})
        if not name:
            return jsonify({"error": "Missing 'name' field"}), 400
        item_id = str(uuid.uuid4())
        item = {"id": item_id, "name": name, "data": data, "created_at": datetime.utcnow().isoformat() + "Z"}
        ITEMS[item_id] = item
        return jsonify(item), 201

    @bp.route("/items/<item_id>", methods=["GET"])
    def get_item(item_id):
        item = ITEMS.get(item_id)
        if not item:
            return jsonify({"error": "Item not found"}), 404
        return jsonify(item)

    @bp.route("/items/<item_id>", methods=["PUT"])
    def update_item(item_id):
        if not request.is_json:
            return jsonify({"error": "Expected JSON body"}), 400
        body = request.get_json()
        item = ITEMS.get(item_id)
        if not item:
            return jsonify({"error": "Item not found"}), 404
        # allow updating name and data
        item["name"] = body.get("name", item["name"])
        item["data"] = body.get("data", item["data"])
        item["updated_at"] = datetime.utcnow().isoformat() + "Z"
        ITEMS[item_id] = item
        return jsonify(item)

    @bp.route("/items/<item_id>", methods=["DELETE"])
    def delete_item(item_id):
        item = ITEMS.pop(item_id, None)
        if not item:
            return jsonify({"error": "Item not found"}), 404
        return jsonify({"deleted": item_id})

    @bp.route("/docs", methods=["GET"])
    def docs():
        """API Documentation"""
        return render_template("docs.html")

    # register blueprint
    app.register_blueprint(bp, url_prefix="/api")