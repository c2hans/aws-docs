---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/Redshift-add-the-data-source.html
---

# Manually adding the Amazon Redshift data source
<a name="Redshift-add-the-data-source"></a>

## Prerequisites
<a name="Redshift-prerequisites"></a>
+  You have access to **Amazon Redshift** from your account.

**To add the Amazon Redshift data source:**

1. Attach the [AmazonRedshiftAccessPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonGrafanaRedshiftAccess) to your workspace user role.

1. Ensure your user role is admin or editor.

1.  Select the workspace you want to work on from the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/).

1.  In the Grafana console side menu, pause on the **Configuration** (gear) icon, then choose **Data Sources**.

1. Choose **Add data source**.

1. Choose the **AWS Redshift** data source. If necessary, you can start typing **Redshift** in the search box to help you find it.

1. This opens the **Connection Details** page. Follow the steps in configuring the [**Connection details** settings](Redshift-config.md#Redshift-connection-details).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
