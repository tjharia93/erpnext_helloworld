def execute(filters=None):
    columns = [
        {"label": "Message", "fieldname": "message", "fieldtype": "Data", "width": 200}
    ]
    data = [{"message": "Hello World"}]
    return columns, data
