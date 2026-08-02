---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_permissions_analyze_cross_account.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC03-BP07 Analyze public and cross-account access
<a name="sec_permissions_analyze_cross_account"></a>

Continuously monitor findings that highlight public and cross-account access. Reduce public access and cross-account access to only resources that require this type of access.

 **Common anti-patterns:**
+  Not following a process to govern access for cross-account and public access to resources.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

In AWS, you can grant access to resources in another account. You grant direct cross- account access using policies attached to resources (for example, [Amazon Simple Storage Service (Amazon S3) bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html)) or by allowing an identity to assume an IAM role in another account. When using resource policies, verify access is granted to identities in your organization and you are intentional about making resources public. Define a process to approve all resources which are required to be publicly available.

 [IAM Access Analyzer](https://aws.amazon.com/iam/features/analyze-access/) uses [provable security](https://aws.amazon.com/security/provable-security/) to identify all access paths to a resource from outside of its account. It reviews resource policies continuously, and reports findings of public and cross-account access to make it easy for you to analyze potentially broad access. Consider configuring IAM Access Analyzer with AWS Organizations to verify you have visibility through all your accounts. IAM Access Analyzer also allows you to [preview Access Analyzer findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-access-preview.html), before deploying resource permissions. This allows you to validate that your policy changes grant only the intended public and cross-account access to your resources. When designing for multi-account access, you can use [trust policies to control in what cases a role can be assumed](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/). For example, you could limit role assumption to a particular source IP range.

 You can also use [AWS Config to report and remediate resources](https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-Publicly-Accessible-Resources.html) for any accidental public access configuration, through AWS Config policy checks. Services like [AWS Control Tower](https://aws.amazon.com/controltower) and [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp.html) simplify deploying checks and guardrails across an AWS Organizations to identify and remediate publicly exposed resources. For example, AWS Control Tower has a managed guardrail which can detect if any [Amazon EBS snapshots are restorable by all AWS accounts](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html).

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html?ref=wellarchitected)
+  [Guardrails in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
+  [AWS Foundational Security Best Practices standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp.html)
+  [AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html)
+  [AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html)

 **Related videos:**
+ [Best Practices for securing your multi-account environment](https://www.youtube.com/watch?v=ip5sn3z5FNg)
+ [Dive Deep into IAM Access Analyzer](https://www.youtube.com/watch?v=i5apYXya2m0)
