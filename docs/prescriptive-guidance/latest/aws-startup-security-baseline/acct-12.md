---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-12.html
---

# ACCT.12 Monitor for and resolve AWS Trusted Advisor high-risk items
<a name="acct-12"></a>

AWS Trusted Advisor scans your AWS infrastructure for high-risk or high-impact issues related to security, performance, cost, and reliability. It provides detailed information about affected resources and remediation recommendations. For more information about checks and descriptions, see [AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html) in the AWS Support documentation. Access to Trusted Advisor checks varies by AWS Support plan.

Basic Support provides access to the following:
+ Checks in the Service Limits category
+ Selected checks in the Security and Fault Tolerance categories, including:
  + Amazon Elastic Block Store (Amazon EBS) public snapshots
  + Amazon Relational Database Service (Amazon RDS) public snapshots
  + Amazon S3 bucket permissions
  + MFA for the root user
  + Security groups that have specific ports unrestricted
  + AWS Security Token Service (AWS STS) global endpoint usage across AWS Regions

Full access to all Trusted Advisor checks requires one of the following paid support plans**:**
+ AWS Business Support\+
+ AWS Enterprise Support
+ AWS Unified Operations

Review Trusted Advisor findings regularly and remediate issues as they are identified. If you have AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations, you can subscribe to a weekly findings email. For more information, [Set up notification preferences](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor.html#notification-preferences) in the AWS Support documentation.

**To view Trusted Advisor findings**

1. See [View check categories](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor.html) in the AWS Support documentation.

1. Start by reviewing *action recommended* issues, which are marked in red*.*
