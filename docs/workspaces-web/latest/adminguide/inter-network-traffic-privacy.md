---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/inter-network-traffic-privacy.html
---

# Inter-network traffic privacy in Amazon WorkSpaces Secure Browser
<a name="inter-network-traffic-privacy"></a>

To secure connections between WorkSpaces Secure Browser and on-premise applications, you use WorkSpaces Secure Browser to launch browser sessions inside of your own VPC. The connection to on-premise applications is configured in your own VPC, and is not controlled by WorkSpaces Secure Browser.

To secure connections between accounts, WorkSpaces Secure Browser uses a service-linked role to securely connect to customer accounts and run operations on behalf of the customer. For more information, see [Using service-linked roles for Amazon WorkSpaces Secure Browser](using-service-linked-roles.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
