---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/cloudwatch-cross-account.html
---

# Cross-account observability
<a name="cloudwatch-cross-account"></a>

**Warning**
This feature requires your Grafana workspace to be version 9 or later.

The CloudWatch plugin enables you to monitor and troubleshoot applications across multiple regional accounts. Using cross-account observability, you can seamlessly search, visualize and analyze metrics and logs without worrying about account boundaries.

To enable cross-account observability, first enable it in CloudWatch, then add the proper IAM actions to the role/user running the plugin. If your Amazon Managed Grafana workspace is running within a VPC, then you must also have a NAT gateway to support internet access.
+ To learn how to enable the feature, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) in the *Amazon CloudWatch User Guide*.
+ The following actions are the proper IAM actions to add for the role/user that is running the plugin.

  ```
  {
  "Sid":  "AllowReadingAcrossAccounts",
  "Effect":  "Allow",
  "Action": [
    "oam:ListSinks",
    "oam:ListAttachedLinks"
  ],
  "Resource":  "*"
  }
  ```
+ Cross-account observability for the CloudWatch data source relies on Amazon CloudWatch Observability Access Manager. The Observability Access Manager does not support a VPC endpoint. If your Amazon Managed Grafana workspace is running within a VPC, then you must also have a NAT Gateway that allows the workspace to call APIs on the internet.

**Note**
You must also have IAM permissions to read the CloudWatch data in the account you are trying to access.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
