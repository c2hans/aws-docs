---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/sec_permissions_share_securely.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC03-BP08 Share resources securely within your organization
<a name="sec_permissions_share_securely"></a>

As the number of workloads grows, you might need to share access to resources in those workloads or provision the resources multiple times across multiple accounts. You might have constructs to compartmentalize your environment, such as having development, testing, and production environments. However, having separation constructs does not limit you from being able to share securely. By sharing components that overlap, you can reduce operational overhead and allow for a consistent experience without guessing what you might have missed while creating the same resource multiple times.

 **Desired outcome:** Minimize unintended access by using secure methods to share resources within your organization, and help with your data loss prevention initiative. Reduce your operational overhead compared to managing individual components, reduce errors from manually creating the same component multiple times, and increase your workloads’ scalability. You can benefit from decreased time to resolution in multi-point failure scenarios, and increase your confidence in determining when a component is no longer needed. For prescriptive guidance on analyzing externally shared resources, see [SEC03-BP07 Analyze public and cross-account access](sec_permissions_analyze_cross_account.md).

 **Common anti-patterns:**
+  Lack of process to continually monitor and automatically alert on unexpected external share.
+  Lack of baseline on what should be shared and what should not.
+  Defaulting to a broadly open policy rather than sharing explicitly when required.
+  Manually creating foundational resources that overlap when required.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Architect your access controls and patterns to govern the consumption of shared resources securely and only with trusted entities. Monitor shared resources and review shared resource access continuously, and be alerted on inappropriate or unexpected sharing. Review [Analyze public and cross-account access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_analyze_cross_account.html) to help you establish governance to reduce the external access to only resources that require it, and to establish a process to monitor continuously and alert automatically.

 Cross-account sharing within AWS Organizations is supported by [a number of AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html), such as [AWS Security Hub CSPM](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-securityhub.html), [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html), and [AWS Backup](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-backup.html). These services allow for data to be shared to a central account, be accessible from a central account, or manage resources and data from a central account. For example, AWS Security Hub CSPM can transfer findings from individual accounts to a central account where you can view all the findings. AWS Backup can take a backup for a resource and share it across accounts. You can use [AWS Resource Access Manager](https://aws.amazon.com/ram/) (AWS RAM) to share other common resources, such as [VPC subnets and Transit Gateway attachments](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-vpc), [AWS Network Firewall](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-network-firewall), or [Amazon SageMaker AI pipelines](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-sagemaker).

 To restrict your account to only share resources within your organization, use [service control policies (SCPs)](https://docs.aws.amazon.com/ram/latest/userguide/scp.html) to prevent access to external principals. When sharing resources, combine identity-based controls and network controls to [create a data perimeter for your organization](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) to help protect against unintended access. A data perimeter is a set of preventive guardrails to help verify that only your trusted identities are accessing trusted resources from expected networks. These controls place appropriate limits on what resources can be shared and prevent sharing or exposing resources that should not be allowed. For example, as a part of your data perimeter, you can use VPC endpoint policies and the `AWS:PrincipalOrgId` condition to ensure the identities accessing your Amazon S3 buckets belong to your organization. It is important to note that [SCPs do not apply to service-linked roles or AWS service principals](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html#scp-effects-on-permissions).

 When using Amazon S3, [turn off ACLs for your Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) and use IAM policies to define access control. For [restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) from [Amazon CloudFront](https://aws.amazon.com/cloudfront/), migrate from origin access identity (OAI) to origin access control (OAC) which supports additional features including server-side encryption with [AWS Key Management Service](https://aws.amazon.com/kms/).

 In some cases, you might want to allow sharing resources outside of your organization or grant a third party access to your resources. For prescriptive guidance on managing permissions to share resources externally, see [Permissions management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/permissions-management.html).

 **Implementation steps**

1.  **Use AWS Organizations.**

    AWS Organizations is an account management service that allows you to consolidate multiple AWS accounts into an organization that you create and centrally manage. You can group your accounts into organizational units (OUs) and attach different policies to each OU to help you meet your budgetary, security, and compliance needs. You can also control how AWS artificial intelligence (AI) and machine learning (ML) services can collect and store data, and use the multi-account management of the AWS services integrated with Organizations.

1.  **Integrate AWS Organizations with AWS services.**

    When you use an AWS service to perform tasks on your behalf in the member accounts of your organization, AWS Organizations creates an IAM service-linked role (SLR) for that service in each member account. You should manage trusted access using the AWS Management Console, the AWS APIs, or the AWS CLI. For prescriptive guidance on turning on trusted access, see [Using AWS Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) and [AWS services that you can use with Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html).

1.  **Establish a data perimeter.**

    The AWS perimeter is typically represented as an organization managed by AWS Organizations. Along with on-premises networks and systems, accessing AWS resources is what many consider as the perimeter of My AWS. The goal of the perimeter is to verify that access is allowed if the identity is trusted, the resource is trusted, and the network is expected.

   1.  Define and implement the perimeters.

       Follow the steps described in [Perimeter implementation](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/perimeter-implementation.html) in the Building a Perimeter on AWS whitepaper for each authorization condition. For prescriptive guidance on protecting network layer, see [Protecting networks](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-networks.html).

   1.  Monitor and alert continually.

       [AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) helps identify resources in your organization and accounts that are shared with external entities. You can integrate [IAM Access Analyzer with AWS Security Hub CSPM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-securityhub-integration.html) to send and aggregate findings for a resource from IAM Access Analyzer to Security Hub CSPM to help analyze the security posture of your environment. To integrate, turn on both IAM Access Analyzer and Security Hub CSPM in each Region in each account. You can also use AWS Config Rules to audit configuration and alert the appropriate party using [Amazon Q Developer in chat applications with AWS Security Hub CSPM](https://aws.amazon.com/blogs/security/enabling-aws-security-hub-integration-with-aws-chatbot/). You can then use [AWS Systems Manager Automation documents](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html) to remediate noncompliant resources.

   1.  For prescriptive guidance on monitoring and alerting continuously on resources shared externally, see [Analyze public and cross-account access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_analyze_cross_account.html).

1.  **Use resource sharing in AWS services and restrict accordingly.**

    Many AWS services allow you to share resources with another account, or target a resource in another account, such as [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) and [AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html). Restrict the `ModifyImageAttribute` API to specify the trusted accounts to share the AMI with. Specify the `ram:RequestedAllowsExternalPrincipals` condition when using AWS RAM to constrain sharing to your organization only, to help prevent access from untrusted identities. For prescriptive guidance and considerations, see [Resource sharing and external targets](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/perimeter-implementation.html).

1.  **Use AWS RAM to share securely in an account or with other AWS accounts.**

    [AWS RAM](https://aws.amazon.com/ram/) helps you securely share the resources that you have created with roles and users in your account and with other AWS accounts. In a multi-account environment, AWS RAM allows you to create a resource once and share it with other accounts. This approach helps reduce your operational overhead while providing consistency, visibility, and auditability through integrations with Amazon CloudWatch and AWS CloudTrail, which you do not receive when using cross-account access.

    If you have resources that you shared previously using a resource-based policy, you can use the [`PromoteResourceShareCreatedFromPolicy` API](https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html) or an equivalent to promote the resource share to a full AWS RAM resource share.

    In some cases, you might need to take additional steps to share resources. For example, to share an encrypted snapshot, you need to [share a AWS KMS key](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html#share-kms-key).

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [SEC03-BP07 Analyze public and cross-account access](sec_permissions_analyze_cross_account.md)
+  [SEC03-BP09 Share resources securely with a third party](sec_permissions_share_securely_third_party.md)
+  [SEC05-BP01 Create network layers](sec_network_protection_create_layers.md)

 **Related documents:**
+ [Bucket owner granting cross-account permission to objects it does not own](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example4.html)
+ [How to use Trust Policies with IAM](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/)
+ [Building Data Perimeter on AWS](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html)
+ [How to use an external ID when granting a third party access to your AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html)
+ [AWS services you can use with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html)
+ [ Establishing a data perimeter on AWS: Allow only trusted identities to access company data ](https://aws.amazon.com/blogs/security/establishing-a-data-perimeter-on-aws-allow-only-trusted-identities-to-access-company-data/)

 **Related videos:**
+ [Granular Access with AWS Resource Access Manager](https://www.youtube.com/watch?v=X3HskbPqR2s)
+ [Securing your data perimeter with VPC endpoints](https://www.youtube.com/watch?v=iu0-o6hiPpI)
+ [ Establishing a data perimeter on AWS](https://www.youtube.com/watch?v=SMi5OBjp1fI)

 **Related tools:**
+ [ Data Perimeter Policy Examples ](https://github.com/aws-samples/data-perimeter-policy-examples)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
