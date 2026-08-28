---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/tgw-sg-updates-identify.html
---

# Identify AWS Transit Gateway referenced security groups
<a name="tgw-sg-updates-identify"></a>

To determine if your security group is being referenced in the rules of a security group in a VPC attached to the same transit gateway, use one of the following commands.
+ [describe-security-group-references](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-security-group-references.html) (AWS CLI)
+ [Get-EC2SecurityGroupReference](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2SecurityGroupReference.html) (AWS Tools for Windows PowerShell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
