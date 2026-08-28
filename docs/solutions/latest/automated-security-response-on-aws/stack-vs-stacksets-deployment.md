---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/stack-vs-stacksets-deployment.html
---

# Stack vs StackSets deployment
<a name="stack-vs-stacksets-deployment"></a>

A *stack set* lets you create stacks in AWS accounts across AWS Regions by using a single AWS CloudFormation template. Starting with version 1.4, this solution supports stack set deployment by splitting resources based on where and how they are deployed. Multi-account customers, particularly those using AWS Organizations, can benefit from using stack sets for deployment across many accounts. It reduces the effort needed to install and maintain the solution. For more information about StackSets, refer to [Using AWS CloudFormation StackSets](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-stacksets.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
