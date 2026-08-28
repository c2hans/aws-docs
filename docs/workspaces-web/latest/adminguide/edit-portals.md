---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/edit-portals.html
---

# Editing a web portal in Amazon WorkSpaces Secure Browser
<a name="edit-portals"></a>

To edit a web portal, follow these steps.

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/).

1. Choose **WorkSpaces Secure Browser**, **Web portals**, choose your web portal, and then choose **Edit**.
**Note**
Changes to networking settings or timeout settings immediately end any active portal sessions. Users are disconnected and must reconnect to begin a new session. Changes to **Clipboard permissions**, **File transfer permissions**, or **Print to local device** apply beginning with the first new session. Currently active sessions aren't disconnected. Users connected to active sessions aren't affected by the changes until they disconnect and connect to a new session.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
