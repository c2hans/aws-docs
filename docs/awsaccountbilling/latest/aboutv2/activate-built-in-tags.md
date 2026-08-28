---
source_url: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activate-built-in-tags.html
---

# Activating AWS-generated tags cost allocation tags
<a name="activate-built-in-tags"></a>

Management account owners can activate the AWS-generated tags in the Billing and Cost Management console. When a management account owner activates the tag, it's also activated for all member accounts. This tag is visible only in the Billing and Cost Management console and reports.

**Note**
You can activate the `createdBy` tag in the Billing and Cost Management console. This tag is available in specific AWS Regions. For more information, see [Using AWS-generated tags](aws-tags.md).<a name="activate-built-in-tag"></a>

**To activate the AWS-generated tags**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost allocation tags**.

1. Under **AWS-generated cost allocation tags**, choose the `createdBy` tag.

1. Choose **Activate**. It can take up to 24 hours for tags to activate.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awsaccountbilling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
