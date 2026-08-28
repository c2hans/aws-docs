---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-move-groups.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Moving issues between groups
<a name="issues-move-groups"></a>

You can [group issues](issues-grouping.md) in the **All issues** and **Board** views by various parameters. If the issues are grouped, you can move issues from one group to another. Moving an issue from one group to another will automatically edit the field that the issues are grouped on to match the target group.

As an example scenario, assume there is a company using CodeCatalyst that has issues assigned to two people, Wang Xiulan and Saanvi Sarkar. The board is grouped by `Assignee`, and there are two groups, one for each assignee. Moving an issue from the Wang Xiulan group to the Saanvi Sarkar group will update the issue's assignee to Saanvi Sarkar.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
