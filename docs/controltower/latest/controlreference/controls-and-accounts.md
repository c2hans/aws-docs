---
source_url: https://docs.aws.amazon.com/controltower/latest/controlreference/controls-and-accounts.html
---

# Considerations for controls and accounts
<a name="controls-and-accounts"></a>

When working with controls and accounts, consider the following properties:

**Controls and accounts**
+ Accounts created through the Account Factory in AWS Control Tower inherit the controls of the parent OU, and the associated resources are created.
+ When you enable optional controls, AWS Control Tower creates and manages certain additional AWS resources in your accounts. Do not modify or delete resources created by AWS Control Tower . Doing so could result in the controls entering an unknown state. For more information, see [The AWS Control Tower controls library](https://docs.aws.amazon.com/controltower/latest/controlreference/controls-reference.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
