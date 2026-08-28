---
source_url: https://docs.aws.amazon.com/athena/latest/ug/queries-viewing-history.html
---

# View recent queries in the Athena console
<a name="queries-viewing-history"></a>

You can use the Athena console to see which queries succeeded or failed, and view error details for the queries that failed. Athena keeps a query history for 45 days.

**To view recent queries in the Athena console**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. Choose **Recent queries**. The **Recent queries** tab shows information about each query that ran.

1. To open a query statement in the query editor, choose the query's execution ID.
![Choose the execution ID of a query to see it in the query editor.](http://docs.aws.amazon.com/athena/latest/ug/images/querying-view-query-statement.png)

1. To see the details for a query that failed, choose the **Failed** link for the query.
![Choose the Failed link for a query to view information about the failure.](http://docs.aws.amazon.com/athena/latest/ug/images/querying-view-query-failure-details.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
