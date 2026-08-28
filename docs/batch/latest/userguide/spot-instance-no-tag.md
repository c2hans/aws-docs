---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/spot-instance-no-tag.html
---

# Spot Instances not tagged on creation
<a name="spot-instance-no-tag"></a>

Spot Instance tagging for AWS Batch compute resources is supported as of October 25, 2017. Before, the recommended IAM managed policy (`AmazonEC2SpotFleetRole`) for the Amazon EC2 Spot Fleet role didn't contain permissions to tag Spot Instances at launch. The new recommended IAM managed policy is called `AmazonEC2SpotFleetTaggingRole`. It supports tagging Spot Instances at launch.

To fix Spot Instance tagging on creation, follow the following procedure to apply the current recommended IAM managed policy to your Amazon EC2 Spot Fleet role. That way, any future Spot Instances that are created with that role have permissions to apply instance tags when they're created.

**To apply the current IAM managed policy to your Amazon EC2 Spot Fleet role**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Roles**, and choose your Amazon EC2 Spot Fleet role.

1. Choose **Attach policy**.

1. Select the **AmazonEC2SpotFleetTaggingRole** and choose **Attach policy**.

1. Choose your Amazon EC2 Spot Fleet role again to remove the previous policy.

1. Select the **x** to the right of the **AmazonEC2SpotFleetRole** policy, and choose **Detach**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
