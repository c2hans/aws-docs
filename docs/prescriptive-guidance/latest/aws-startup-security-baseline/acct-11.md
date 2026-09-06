---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-11.html
---

# ACCT.11 Enable IAM Access Analyzer
<a name="acct-11"></a>

Enable IAM Access Analyzer in each AWS Region you use. Because IAM Access Analyzer operates on a per-Region basis, you must enable it separately in each Region to gain visibility into resource sharing across your AWS footprint. This helps prevent accidental public or cross-account access to resources, such as Amazon S3 buckets, IAM roles, and AWS KMS keys.

**To enable IAM Access Analyzer**

1. Open the [IAM console](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, choose **Access Analyzer**.

1. Choose **Create analyzer**.

1. Enter a name for your analyzer.

1. For the analyzer scope, choose **Account** for a single account, or choose **Organization** if you are using AWS Organizations.

1. Choose **Create analyzer**.

Review the findings in the **Access Analyzer **console and update resource policies to remove unintended external access. For more information, see [Reviewing findings for IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html) in the IAM documentation. Prioritize high-impact findings, such as public Amazon S3 buckets or IAM roles that are shared outside of your AWS account.

**Note**
IAM Access Analyzer pricing depends on the analyzer type and features you use. An external access analyzer is available at no additional charge. Early-stage startups should start with an external access analyzer. For more information about pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing/).
