---
source_url: https://docs.aws.amazon.com/glue/latest/dg/disable-auto-column-stats-generation.html
---

# Disabling catalog-level column statistics generation
<a name="disable-auto-column-stats-generation"></a>

 You can disable automatic column statistics generation for new tables using the AWS Lake Formation console, the `glue:UpdateCatalogSettings` API, or the `glue:DeleteColumnStatisticsTaskSettings` API.

**To disable the automatic column statistics generation at the account-level**

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. On the left navigation bar, choose **Catalogs**.

1. On the **Catalog summary** page, choose **Edit** under **Optimization configuration**.

1. On the **Table optimization configuration** page, unselect the **Enable automatic statistics generation for the tables of the catalog** option.

1. Choose **Submit**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
