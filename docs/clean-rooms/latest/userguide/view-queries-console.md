---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/view-queries-console.html
---

# Viewing recent queries
<a name="view-queries-console"></a>

You can view the queries that ran in the last 90 days on the **Analysis** tab.

**Note**
If your only member ability is **Contribute data**, and you aren't the [member paying for query compute costs](glossary.md#glossary-member-paying-for-query-compute), the **Analysis** tab doesn't appear on the console.

**To view recent queries**

Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Choose a collaboration.

1. On the **Analysis** tab, under **Analyses**, select **All queries** from the dropdown, and view the queries that have been run in the last 90 days.

1. To sort recent queries by **Status**, select a status from the **All statuses** dropdown list.

   The statuses are: **Submitted**, **Started**, **Cancelled**, **Success**, **Failed**, and **Timed out**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
