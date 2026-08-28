---
source_url: https://docs.aws.amazon.com/omics/latest/dev/analytics-setting-up-athena.html
---

# Configuring Athena for queries
<a name="analytics-setting-up-athena"></a>

**Important**
AWS HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md).

You can use Athena to query variants and annotations. Before you run any queries, perform the following setup tasks:

**Topics**
+ [Configure a query results location using the Athena console](#configure-athena-query)
+ [Configure a workgroup with Athena engine v3](#configure-athena-workgroup)

## Configure a query results location using the Athena console
<a name="configure-athena-query"></a>

To configure a query results location, follow these steps.

1. Open the Athena console: [Athena console](https://console.aws.amazon.com/athena)

1. In the primary navigation bar, choose **Query editor**.

1. In the query editor, choose the **Settings** tab, then choose **Manage**.

1. Enter an S3 prefix of a location to save the query result.

## Configure a workgroup with Athena engine v3
<a name="configure-athena-workgroup"></a>

To configure a workgroup, follow these steps.

1. Open the Athena console: [Athena console](https://console.aws.amazon.com/athena)

1. In the primary navigation bar, choose **Workgroups**, then **Create workgroup**.

1. Enter a name for the workgroup.

1. Select **Athena SQL** as the type of engine.

1. Under **Upgrade query engine**, select **Manual**.

1. Under **Query version engine**, select **Athena version 3**.

1. Choose **Create workgroup**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
