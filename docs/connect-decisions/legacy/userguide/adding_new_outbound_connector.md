---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/adding_new_outbound_connector.html
---

# Adding a new outbound source for Supply Planning
<a name="adding_new_outbound_connector"></a>

You can use the new outbound source to upload the updated *Supply Planning* purchase order requests or plan enhancements.

1. On the AWS Supply Chain dashboard, on the left navigation pane, choose **Data Lake** and then choose the **Data Ingestion** tab.

   The **Data Ingestion** page appears.

1. Choose **Add Outbound Source**.

   The **Amazon S3 Connection details** page appears.

1. Under **Connection name**, enter a name for your Amazon S3 connection.

1. Under **Outbound Data**, select the outbound dataflow that you want to export. Purchase order request and Supply forecast data flows are supported.

1. Choose **Confirm**.

   The new outbound source is created and the **Connections** page appears.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
