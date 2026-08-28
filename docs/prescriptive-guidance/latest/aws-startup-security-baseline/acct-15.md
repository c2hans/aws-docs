---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-15.html
---

# ACCT.15 Enable AWS Security Hub
<a name="acct-15"></a>

Enable [AWS Security Hub](https://aws.amazon.com/security-hub/) to gain a centralized view of your security posture. Security Hub runs automated compliance checks against the [AWS Foundational Security Best Practices (FSBP)](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html) standard and aggregates findings from services such as [Amazon GuardDuty](https://aws.amazon.com/guardduty/) and [IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/). The FSBP standard automatically checks many of the controls in this guide, including [Amazon S3 public access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-block-public-access-bucket.html) settings, [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) configuration, [Amazon EBS](https://aws.amazon.com/ebs/) encryption, [MFA on the root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html), and IAM Access Analyzer enablement.

**Prerequisites**
+ Enable AWS Config in the same Region. Security Hub uses [AWS Config](https://aws.amazon.com/config/) rules to evaluate resource configurations. For more information, see [Setting up AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html) in the AWS Config documentation.

**To enable Security Hub**

1. Open the [Security Hub console](https://console.aws.amazon.com/securityhub/).

1. Choose **Go to Security Hub**.

1. On the Welcome page, the **AWS Foundational Security Best Practices** standard is selected by default. Keep this standard enabled.

1. Choose **Enable Security Hub**.

Review the Security Hub dashboard periodically and address findings marked **Critical** or **High** first. For more information, see [Setting up Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) in the Security Hub documentation.

**Note**
Security Hub includes a 30-day free trial when you enable it for the first time. AWS Config recording charges apply separately. For more information about pricing, see [AWS Security Hub pricing](https://aws.amazon.com/security-hub/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
