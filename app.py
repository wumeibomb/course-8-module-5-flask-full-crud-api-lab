from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

@app.route("/", methods=["GET"])
def get_events():
    
    print (events)
    for eachevent in events:
        print(eachevent)
        test = eachevent.to_dict()
        print(test)
        output = {
        "data": test
        }
        return jsonify([output])


# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    Title = data["title"]
    event_id = len(events) + 1

    new_event = Event(id = event_id, title = Title)

    events.append(new_event)

    output = {"date": {
        "id": new_event.id,
        "title": new_event.title
    }}

    return jsonify(output)

# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data = request.get_json()
    Title = data["title"]

    find_event = next((test for test in events if test.id == event_id))

    if not find_event:
        return ("error, not found"), 404
    if "title" in data:
        find_event.title = Title
        
    return jsonify(find_event.to_dict())


# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    global events
    
    find_event = next((test for test in events if test.id == event_id))

    if not find_event:
        return ("Not found", 404)
    events = [test for test in events if test.id != event_id]
    return ("DELETED", 204)



if __name__ == "__main__":
    app.run(port = 5003, debug=True)
