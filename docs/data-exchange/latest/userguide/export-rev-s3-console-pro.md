---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/export-rev-s3-console-pro.html
---

# Exporting AWS Data Exchange asset revisions to an S3 bucket as a provider (console)
<a name="export-rev-s3-console-pro"></a>

As a provider of AWS Data Exchange data products, you can use the AWS Data Exchange console to export AWS Data Exchange assets to an S3 bucket using the following instructions.

**To export a revision to an S3 bucket as a provider (console)**

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. In the left side navigation pane, for **Publish data**, choose **Owned data sets**.

1. In **Owned data sets**, choose the product that has the revision you want to export.

1. Navigate to the **Products** tab to make sure that the data set is associated with a published product.

1. On the **Revisions** tab, choose the revision.

1. For the **Imported assets **section, select the check box next to the asset name.

1. Select **Export actions** and then choose **Export selected assets to Amazon S3**.

1. Follow the prompts in the **Export to Amazon S3** window and then choose **Export**.

   A job is started to export your asset. After the job is finished, the **State** field in the **Jobs** section is updated to **Completed**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
