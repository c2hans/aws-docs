---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-endpoint-create.html
---

# Creating an interface VPC endpoint for Amazon WorkSpaces Secure Browser
<a name="vpc-endpoint-create"></a>

You can create an interface VPC endpoint for the Amazon WorkSpaces Secure Browser service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create an interface VPC endpoint for Amazon WorkSpaces Secure Browser using the following service name:
+ com.amazonaws.{{region}}.workspaces-web

For FIPS-supported regions, create an interface VPC endpoint for Amazon WorkSpaces Secure Browser using the following service name:
+ com.amazonaws.{{region}}.workspaces-web-fips

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
