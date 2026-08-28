---
source_url: https://docs.aws.amazon.com/glue/latest/dg/define-crawler-set-crawler-properties.html
---

# Step 1: Set crawler properties
<a name="define-crawler-set-crawler-properties"></a>

**To configure a crawler**

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue\). Choose **Crawlers** in the navigation pane.

1.  Choose **Create crawler**, and follow the instructions in the **Add crawler** wizard. The wizard will guide you the steps required to create a crawler. If you want to add custom classifiers to define the schema, see [Defining and managing classifiers](add-classifier.md).

1.  Enter a name for your crawler and description (optional). Optionally, you can tag your crawler with a **Tag key** and optional **Tag value**. Once created, tag keys are read-only. Use tags on some resources to help you organize and identify them. For more information, see AWS tags in AWS Glue.
**Name**
Name may contain letters (A-Z), numbers (0-9), hyphens (-), or underscores (\_), and can be up to 255 characters long.
**Description**
Descriptions can be up to 2048 characters long.
**Tags**
Use tags to organize and identify your resources. For more information, see the following:
   + [AWS tags in AWS Glue](monitor-tags.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
