---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/disassociate-key-connection.html
---

# Remove the association between a MACsec secret key and a Direct Connect connection
<a name="disassociate-key-connection"></a>

You can remove the association between the connection and the MACsec key using either the Direct Connect console or through the command-line or API.

**To remove an association between a connection and a MACsec key**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1.

1. In the left pane, choose **Connections**.

1. Select a connection, and then choose **View details**.

1. Select the MACsec secret to remove, and then choose **Disassociate key**.

1. In the confirmation dialog box, enter **disassociate**, and then choose **Disassociate**.

**To remove an association between a connection and a MACsec key using the command line or API**
+ [disassociate-mac-sec-key](https://docs.aws.amazon.com/cli/latest/reference/directconnect/disassociate-mac-sec-key.html) (AWS CLI)
+ [DisassociateMacSecKey](https://docs.aws.amazon.com/directconnect/latest/APIReference/API__DisassociateMacSecKey.html) (Direct Connect API)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
