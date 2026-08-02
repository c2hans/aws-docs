---
source_url: https://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html
---

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

# CIS AWS Benchmark v1.2.0
<a name="CIS-1-2"></a>

AWS Audit Manager provides two prebuilt frameworks that support the Center for Internet Security (CIS) Amazon Web Services (AWS) Benchmark v1.2.0*.*

**Note**
For information about the Audit Manager frameworks that support v1.3.0, see [CIS AWS Benchmark v1.3.0](CIS-1-3.md).
For information about the Audit Manager frameworks that support v1.4.0, see [CIS AWS Benchmark v1.4.0](CIS-1-4.md).

**Topics**
+ [What is CIS?](#what-is-CIS-1-2)
+ [Using this framework](#framework-CIS-1-2)
+ [Next steps](#next-steps-CIS-1-2)
+ [Additional resources](#resources-CIS-1-2)

## What is CIS?
<a name="what-is-CIS-1-2"></a>

The CIS is a nonprofit that developed the [CIS AWS Foundations Benchmark](https://d0.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf). This benchmark serves as a set of security configuration best practices for AWS. These industry-accepted best practices go beyond the high-level security guidance already available in that they provide you with clear, step-by-step implementation and assessment procedures.

For more information, see the [CIS AWS Foundations Benchmark blog posts](https://aws.amazon.com/blogs/security/tag/cis-aws-foundations-benchmark/) on the *AWS Security Blog*.

**Difference between CIS Benchmarks and CIS Controls**
*CIS Benchmarks* are security best practice guidelines that are specific to vendor products. Ranging from operating systems to cloud services and networks devices, the settings that are applied from a benchmark protect the specific systems that your organization use. *CIS Controls* are foundational best practice guidelines for organization-level systems to follow to help protect against known cyberattack vectors.

**Examples**
+ CIS Benchmarks are prescriptive. They typically reference a specific setting that can be reviewed and set in the vendor product.

  **Example:** CIS AWS Benchmark v1.2.0 - Ensure MFA is enabled for the "root user" account.

  This recommendation provides prescriptive guidance on how to check for this and how to set this on the root account for the AWS environment.
+ CIS Controls are for your organization as a whole. They aren't specific to only one vendor product.

  **Example:** CIS v7.1 - Use Multi-Factor Authentication for All Administrative Access

  This control describes what's expected to be applied within your organization. It doesn't describe how you should apply it for the systems and workloads that you're running (regardless of where they are).

## Using this framework
<a name="framework-CIS-1-2"></a>

You can use the CIS AWS Benchmark v1.2 frameworks in AWS Audit Manager to help you prepare for CIS audits. You can also customize these frameworks and their controls to support internal audits with specific requirements.

Using the frameworks as a starting point, you can create an Audit Manager assessment and start collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager starts to assess your AWS resources. It does this based on the controls that are defined in the CIS framework. When it's time for an audit, you—or a delegate of your choice—can review the evidence that Audit Manager collected. Either, you can browse the evidence folders in your assessment and choose which evidence you want to include in your assessment report. Or, if you enabled evidence finder, you can search for specific evidence and export it in CSV format, or create an assessment report from your search results. Either way, you can use this assessment report to show that your controls are working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager | Number of automated controls | Number of manual controls | Number of control sets |
| --- | --- | --- | --- |
| Center for Internet Security (CIS) Amazon Web Services (AWS) Benchmark v1.2.0, Level 1 | 33 | 3 | 4 |
| Center for Internet Security (CIS) Amazon Web Services (AWS) Benchmark v1.2.0, Level 1 and 2 | 45 | 4 | 4 |

**Important**
To ensure that these frameworks collect the intended evidence from AWS Security Hub CSPM, make sure that you enabled all standards in Security Hub CSPM.
To ensure that these frameworks collect the intended evidence from AWS Config, make sure that you enable the necessary AWS Config rules. To review a list of the AWS Config rules that are used as data source mappings for these standard frameworks, download the following files:
[AuditManager\_ConfigDataSourceMappings\_CIS-AWS-Benchmark-v1.2.0,-Level-1.zip](samples/AuditManager_ConfigDataSourceMappings_CIS-AWS-Benchmark-v1.2.0,-Level-1.zip)
[AuditManager\_ConfigDataSourceMappings\_CIS-AWS-Benchmark-v1.2.0,-Level-1-and-2.zip](samples/AuditManager_ConfigDataSourceMappings_CIS-AWS-Benchmark-v1.2.0,-Level-1-and-2.zip)

The controls in these frameworks aren't intended to verify if your systems are compliant with CIS AWS Benchmark best practices. Moreover, they can't guarantee that you'll pass a CIS audit. AWS Audit Manager doesn't automatically check procedural controls that require manual evidence collection.

### Prerequisites for using these frameworks
<a name="framework-CIS-1-2-prerequisites"></a>

Many controls in the CIS AWS Benchmark v1.2 frameworks use AWS Config as a data source type. To support these controls, you must [enable AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html) on all accounts in each AWS Region where you enabled Audit Manager. You must also make sure that specific AWS Config rules are enabled, and that these rules are configured correctly.

The following AWS Config rules and parameters are required to collect the correct evidence and capture an accurate compliance status for the CIS AWS Foundations Benchmark v1.2. For instructions on how to enable or configure a rule, see [Working with AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managing-aws-managed-rules.html).

| Required AWS Config rule | Required parameters |
| --- | --- |
| [ACCESS\_KEYS\_ROTATED](https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |
| [CLOUD\_TRAIL\_CLOUD\_WATCH\_LOGS\_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-cloud-watch-logs-enabled.html) | Not applicable |
| [CLOUD\_TRAIL\_ENCRYPTION\_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-encryption-enabled.html) | Not applicable |
| [CLOUD\_TRAIL\_LOG\_FILE\_VALIDATION\_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-log-file-validation-enabled.html) | Not applicable |
| [CMK\_BACKING\_KEY\_ROTATION\_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/cmk-backing-key-rotation-enabled.html) | Not applicable |
| [IAM\_PASSWORD\_POLICY](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |
| [IAM\_PASSWORD\_POLICY](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |
| [IAM\_PASSWORD\_POLICY](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |
| [IAM\_PASSWORD\_POLICY](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |
| [IAM\_PASSWORD\_POLICY](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |
| [IAM\_PASSWORD\_POLICY](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |
| [IAM\_PASSWORD\_POLICY](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |
| [IAM\_POLICY\_IN\_USE](https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-in-use.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |
| [IAM\_POLICY\_NO\_STATEMENTS\_WITH\_ADMIN\_ACCESS](https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-no-statements-with-admin-access.html) | Not applicable |
| [IAM\_ROOT\_ACCESS\_KEY\_CHECK](https://docs.aws.amazon.com/config/latest/developerguide/iam-root-access-key-check.html) | Not applicable |
| [IAM\_USER\_NO\_POLICIES\_CHECK](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-no-policies-check.html) | Not applicable |
| [IAM\_USER\_UNUSED\_CREDENTIALS\_CHECK](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-unused-credentials-check.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |
| [INCOMING\_SSH\_DISABLED](https://docs.aws.amazon.com/config/latest/developerguide/restricted-ssh.html) | Not applicable |
| [MFA\_ENABLED\_FOR\_IAM\_CONSOLE\_ACCESS](https://docs.aws.amazon.com/config/latest/developerguide/mfa-enabled-for-iam-console-access.html) | Not applicable |
| [MULTI\_REGION\_CLOUD\_TRAIL\_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/multi-region-cloudtrail-enabled.html) | Not applicable |
| [RESTRICTED\_INCOMING\_TRAFFIC](https://docs.aws.amazon.com/config/latest/developerguide/restricted-common-ports.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |
| [ROOT\_ACCOUNT\_HARDWARE\_MFA\_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/root-account-hardware-mfa-enabled.html) | Not applicable |
| [ROOT\_ACCOUNT\_MFA\_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/root-account-mfa-enabled.html) | Not applicable |
| [S3\_BUCKET\_LOGGING\_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-logging-enabled.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |
| [S3\_BUCKET\_PUBLIC\_READ\_PROHIBITED](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-public-read-prohibited.html) | Not applicable |
| [VPC\_DEFAULT\_SECURITY\_GROUP\_CLOSED](https://docs.aws.amazon.com/config/latest/developerguide/vpc-default-security-group-closed.html) | Not applicable |
| [VPC\_FLOW\_LOGS\_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/vpc-flow-logs-enabled.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/CIS-1-2.html)  |

## Next steps
<a name="next-steps-CIS-1-2"></a>

For instructions on how to view detailed information about these frameworks, including the list of standard controls that they contain, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md).

For instructions on how to create an assessment using these frameworks, see [Creating an assessment in AWS Audit Manager](create-assessments.md).

For instructions on how to customize these frameworks to support your specific requirements, see [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md).

## Additional resources
<a name="resources-CIS-1-2"></a>
+ [The CIS AWS Foundations Benchmark v1.2.0](https://d0.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf)
+ [CIS AWS Foundations Benchmark blog posts](https://aws.amazon.com/blogs/security/tag/cis-aws-foundations-benchmark/) on the *AWS Security Blog*
