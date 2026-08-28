---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost08-bp01.html
---

# EUCCOST08-BP01 Monitor your Amazon WorkSpaces usage, and implement the Cost Optimizer for Amazon WorkSpaces
<a name="euccost08-bp01"></a>

 The Cost Optimizer for Amazon WorkSpaces generates reports you can use to understand the usage of individual WorkSpaces. Based on these reports, identify underutilized WorkSpaces or WorkSpaces that are no longer in use so that you can assess whether to terminate them.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-91"></a>

 Deploy the Cost Optimizer for Amazon WorkSpaces, and perform regular reviews of your WorkSpaces usage reported by the Cost Optimizer for Amazon WorkSpaces. Based on your findings, decide which WorkSpaces to terminate, and initiate a conversation with owners of underutilized WorkSpaces to understand if these are still needed. Agree on how, when, and by whom any changes are to be applied.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
