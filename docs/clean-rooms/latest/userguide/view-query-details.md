---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/view-query-details.html
---

# Viewing query details
<a name="view-query-details"></a>

You can view the query details as the member who can run queries or as a member who can receive results.

**To view the details of the query**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Choose a collaboration.

1. On the **Analysis** tab, do one of the following:
   + Choose the option button for the specific query you want to view, and then choose **View details**.
   + Choose the **Protected query ID**.

1. On the **Query details** page,
   + If you are the member who can run queries, view the **Query details**, **SQL text** and **Results**.

     You see a message confirming that the query results were delivered to the member who can receive results.
   + If you are the member who can receive results, view the **Query details** and **Results**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
