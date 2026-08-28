---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_permissions_share_securely.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC03-BP08 Share resources securely
<a name="sec_permissions_share_securely"></a>

 Govern the consumption of shared resources across accounts or within your AWS Organizations. Monitor shared resources and review shared resource access.

 **Common anti-patterns:**
+  Using the default IAM trust policy when granting third party cross-account access.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

 As you manage your workloads using multiple AWS accounts, you may need to share resources between accounts. This will very often be cross-account sharing within an AWS Organizations. Several AWS services, such as [AWS Security Hub CSPM](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-securityhub.html), [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html), and [AWS Backup](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-backup.html) have cross-account features integrated with Organizations. You can use [AWS Resource Access Manager](https://aws.amazon.com/ram/) to share other common resources, such as [VPC Subnets or Transit Gateway attachments](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-vpc), [AWS Network Firewall](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-network-firewall), or [Amazon SageMaker Runtime pipelines](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-sagemaker). If you want to ensure that your account only shares resources within your Organizations, we recommend using [Service Control Policies (SCPs)](https://docs.aws.amazon.com/ram/latest/userguide/scp.html) to prevent access to external principals.

 When sharing resources, you should put measures in place to protect against unintended access. We recommend combining identity-based controls and network controls to [create a data perimeter for your organization](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html). These controls should place strict limits on what resources can be shared and prevent sharing or exposing resources that should not be allowed. For example, as a part of your data perimeter you could use VPC endpoint policies and the `aws:PrincipalOrgId` condition to ensure the identities accessing your Amazon S3 buckets belong to your organization.

 In some cases, you may want to allow share resources outside of your Organizations or grant third parties access to your account. For example, a partner may provide a monitoring solution that needs to access resources within your account. In those cases, you should create an IAM cross-account role with only the privileges needed by the third party. You should also craft a trust policy using the [external ID condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html). When using an external ID, you should generate a unique ID for each third party. The unique ID should not be supplied by or controlled by the third party. If the third party no longer needs access to your environment, you should remove the role. You should also avoid providing long-term IAM credentials to a third-party in all cases. Maintain awareness of other AWS services which natively support sharing. For example, the AWS Well-Architected Tool allows [sharing a workload](https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-sharing.html) with other AWS accounts.

 When using service such as Amazon S3, it is recommended to [disable ACLs for your Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) and use IAM policies to define access control. [For restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) from [Amazon CloudFront](https://aws.amazon.com/cloudfront/), migrate from origin access identity (OAI) to origin access control (OAC) which supports additional features including server-side encryption with [AWS KMS](https://aws.amazon.com/kms/).

## Resources
<a name="resources"></a>

 **Related documents:**
+ [Bucket owner granting cross-account permission to objects it does not own](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example4.html)
+ [How to use Trust Policies with IAM](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/)
+ [Building Data Perimeter on AWS](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html)
+ [How to use an external ID when granting a third party access to your AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html)

 **Related videos:**
+ [Granular Access with AWS Resource Access Manager](https://www.youtube.com/watch?v=X3HskbPqR2s)
+ [Securing your data perimeter with VPC endpoints](https://www.youtube.com/watch?v=iu0-o6hiPpI)
+ [ Establishing a data perimeter on AWS](https://www.youtube.com/watch?v=SMi5OBjp1fI)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
