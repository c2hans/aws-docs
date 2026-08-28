---
source_url: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/deactivate-built-in-tags.html
---

# Deactivating the AWS-generated tags cost allocation tags
<a name="deactivate-built-in-tags"></a>

Management account owners can deactivate the AWS-generated tags in the Billing and Cost Management console. When a management account owner deactivates the tag, it's also deactivated for all member accounts. After you deactivate the AWS-generated tags, AWS no longer applies the tag to new resources. Previously tagged resources remain tagged.<a name="deactivate-built-in-tag"></a>

**To deactivate the AWS-generated tags**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost allocation tags**.

1. Under **AWS-generated cost allocation tags**, choose **Deactivate**.

It can take up to 24 hours for tags to deactivate.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awsaccountbilling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
