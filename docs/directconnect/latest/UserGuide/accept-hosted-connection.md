---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/accept-hosted-connection.html
---

# Accept a Direct Connect hosted connection
<a name="accept-hosted-connection"></a>

If you are interested in purchasing a hosted connection, you must contact an AWS Direct Connect Partner in the AWS Direct Connect Partner Program. The partner provisions the connection for you. After the connection is configured, it appears in the **Connections** pane in the Direct Connect console.

Before you can begin using a hosted connection, you must accept the connection. You can accept a hosted connection using either the Direct Connect console or using the command line or API.

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**.

1. Select the hosted connection and choose **View details**.

1. Select the confirmation check box and choose **Accept**.

**To accept a hosted connection using the command line or API**
+ [confirm-connection](https://docs.aws.amazon.com/cli/latest/reference/directconnect/confirm-connection.html) (AWS CLI)
+ [ConfirmConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmConnection.html) (Direct Connect API)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
