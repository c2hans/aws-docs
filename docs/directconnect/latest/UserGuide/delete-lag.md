---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/delete-lag.html
---

# Delete a Direct Connect endpoint LAG
<a name="delete-lag"></a>

If you no longer need LAGs, you can delete them. You cannot delete a LAG if it has virtual interfaces associated with it. You must first delete the virtual interfaces, or associate them with a different LAG or connection. Deleting a LAG does not delete the connections in the LAG; you must delete the connections yourself. For more information, see [Delete a connection](deleteconnection.md).

You can delete a LAG using either the Direct Connect console or using the command line or API.

**To delete a LAG**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **LAGs**.

1. Select the LAGs, and then choose **Delete**.

1. In the confirmation dialog box, choose **Delete**.

**To delete a LAG using the command line or API**
+ [delete-lag](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-lag.html) (AWS CLI)
+ [DeleteLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteLag.html) (Direct Connect API)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
