---
source_url: https://docs.aws.amazon.com/glue/latest/dg/disable-auto-table-optimizers.html
---

# Disabling catalog-level table optimization
<a name="disable-auto-table-optimizers"></a>

 You can disable table optimization for new tables using the AWS Lake Formation console, the `glue:UpdateCatalog` API.

**To disable the table optimizations at the catalog level**

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. On the left navigation bar, choose **Catalogs**.

1. On the **Catalog summary** page, choose **Edit** under **Table optimizations**.

1. On the **Edit optimization** page, unselect the **Optimization options**.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
