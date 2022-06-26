// See online documentation for examples
// https://docs.getdrafts.com/docs/actions/scripting

// Token from API

var credential = Credential.create("Clickup", "need a valid token to access to ClickUp.");

credential.addTextField("authorizationToken", "AuthorizationToken");

credential.authorize();

const homura = 3653276;
const inboxId = "7837385";
const itsukatabunId = "7817267";

function createTask() {

    let title = draft.processTemplate("[[line|1]]")
    let listNum = draft.processTemplate("[[line|2]]")
    let description = draft.processTemplate("[[line|3..]]")
    let ddate = new Date()

    if (listNum == '') {
        listNum = inboxId;
    } else {
        listNum = itsukatabunId;
    }

    let url = "https://api.clickup.com/api/v2/list/" + listNum + "/task";

    let body = {
        'name': title,
        'description': description,
        'assignees': [homura],
        'due_date': ddate.getTime(),
  		};
    //alert(ddate.getTime());
    let http = HTTP.create();
    let response = http.request({
        "url": url,
        "method": "POST",
        "data": body,
        "headers": {
            "Content-Type": "application/json",
            "Authorization": credential.getValue("authorizationToken")
        }
    });
}
// List name ID (last digits from url
createTask();
