---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/disassociate-config-table.html
---

# Disassociating configured tables
<a name="disassociate-config-table"></a>

As a collaboration member, you can disassociate a configured table from the collaboration. This action prevents the member who can query from querying the table.

**Warning**
Disassociating a configured table from a collaboration causes all dependent intermediate tables (and their descendants) to become unusable with a status of `BASE_TABLE_REMOVED`. The stored data in those intermediate tables is removed and storage-based billing stops. For more information, see [Deleting an intermediate table](delete-intermediate-table.md).

**To disassociate a configured table**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration.

1. Choose **Tables** tab.

1. For **Tables associated by you**, select the option button next to the table that you want to disassociate.

1. Choose **Disassociate**.

1. In the dialog box, confirm the decision to disassociate the configured table and prevent the member who can query from querying the table by choosing **Disassociate**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
