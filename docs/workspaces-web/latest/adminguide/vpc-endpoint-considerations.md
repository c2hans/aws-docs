---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-endpoint-considerations.html
---

# Considerations for Amazon WorkSpaces Secure Browser
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for Amazon WorkSpaces Secure Browser APIs, make sure to review the "Prerequisites" in [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html). Amazon WorkSpaces Secure Browser supports making calls to all of its API actions through the interface VPC endpoint.

By default, full access to Amazon WorkSpaces Secure Browser is allowed through the endpoint. For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
