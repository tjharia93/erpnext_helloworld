frappe.query_reports["Hello World"] = {
    onload: function(report) {
        frappe.msgprint("Hello World from JavaScript!");
    }
};
