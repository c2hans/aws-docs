---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/design-principles-for-your-multi-account-strategy.html
---

# Design principles for your multi-account strategy
<a name="design-principles-for-your-multi-account-strategy"></a>

 The following design principles helped develop the best practices described in this paper. You can also use these principles to help guide your initial account design and evolve it over time.

 These design principles complement the [Benefits of using multiple accounts](benefits-of-using-multiple-aws-accounts.md) and [Benefits of using OUs](benefits-of-using-organizational-units-ous.md).

**Topics**
+ [Organize based on security and operational needs](#organize-based-on-security-and-operational-needs)
+ [Apply security controls to OUs rather than accounts](#apply-security-controls-to-ous-rather-than-accounts)
+ [Avoid deep OU hierarchies](#avoid-deep-ou-hierarchies)
+ [Start small and expand as needed](#start-small-and-expand-as-needed)
+ [Avoid deploying workloads to the organization's management account](#avoid-deploying-workloads-to-the-organizations-management-account)
+ [Separate production from non-production workloads](#separate-production-from-non-production-workloads)
+ [Assign a single or small set of related workloads to each production account](#assign-a-single-or-small-set-of-related-workloads-to-each-production-account)
+ [Use federated access to help simplify managing human access to accounts](#use-federated-access-to-help-simplify-managing-human-access-to-accounts)
+ [Use automation to support agility and scale](#use-automation-to-support-agility-and-scale)
+ [Use multi-factor authentication](#use-multi-factor-authentication)
+ [Multiple AWS Regions](#multiple-aws-regions)
+ [Break glass access](#break-glass-access)

## Organize based on security and operational needs
<a name="organize-based-on-security-and-operational-needs"></a>

 We recommend that you organize accounts using OUs based on function, compliance requirements, or a common set of controls rather than mirroring your organization's reporting structure.

## Apply security controls to OUs rather than accounts
<a name="apply-security-controls-to-ous-rather-than-accounts"></a>

 Where feasible, we recommend that you apply security controls (for example, SCPs) to OUs instead of accounts so that you can more efficiently manage the distribution of controls across accounts that have the same or similar requirements.

 For more information about managing security controls, refer to [Permissions management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/permissions-management.html) in the AWS Well-Architected Security Pillar.

## Avoid deep OU hierarchies
<a name="avoid-deep-ou-hierarchies"></a>

 Overly complicated structures can be difficult to understand and maintain. Although AWS Organizations supports a depth of five levels of OUs, the recommended structure strives to use OUs only when there is sufficient benefit.

 When you consider the addition of new OU levels, you should review the Benefits of using OUs and these principles to decide whether the additional complexity adds sufficient value.

## Start small and expand as needed
<a name="start-small-and-expand-as-needed"></a>

 We recommend that you start with a subset of the [Recommended OUs and accounts](recommended-ous-and-accounts.md) and expand the structure of your AWS accounts when your needs call for the creation of new OUs.

 You shouldn't need to invest a lot of time at the beginning of your adoption journey designing what you expect your AWS account structure will look like in several years.

## Avoid deploying workloads to the organization's management account
<a name="avoid-deploying-workloads-to-the-organizations-management-account"></a>

 Since privileged operations can be performed within an organization's management account and SCPs do not apply to the management account, we recommend that you limit access to an organization's management account. You should also limit the cloud resources and data contained in the management account to only those that must be managed in the management account.

 Many AWS services that integrate with Organizations enable you to reduce the usage of the management account. These services enable you to register one or more-member accounts as administrators that can manage all of the organization's accounts used in the service. These accounts are called [delegated administrators ](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_delegated_admin.html)for that specific service. By registering a member account as a delegated administrator for an AWS service you enable that account to have some administrative permissions for that service, reducing the number of users that require management account access.

## Separate production from non-production workloads
<a name="separate-production-from-non-production-workloads"></a>

 We recommend that you separate production workloads from non-production workloads. For overall recommendations on designing this separation, refer to [Organizing workload-oriented OUs](advanced-ous.md#organizing-workload-oriented-ous).

## Assign a single or small set of related workloads to each production account
<a name="assign-a-single-or-small-set-of-related-workloads-to-each-production-account"></a>

 In support of your production workloads, we recommend that you either assign a single workload to each production account or assign a small set of closely related workloads to each production account.

 Consider separating workloads that have different owners into their own production accounts to simplify access management, streamline change approval processes, and limit the scope of impact for misconfigurations.

## Use federated access to help simplify managing human access to accounts
<a name="use-federated-access-to-help-simplify-managing-human-access-to-accounts"></a>

 We recommend that you use AWS identity federation capabilities by using AWS IAM Identity Center. These capabilities enable you to use a common identity provider and your existing processes for controlling human user access to your AWS accounts.

 By using federated access and a common identity provider, you avoid the need to manage individual users in each account. Instead, your human users can use their existing credentials to access authorized accounts. You also gain the benefit of keeping personally identifiable information (PII) out of IAM.

 With federated access, your human users use temporary credentials instead of long-term access keys for programmatic access to their AWS environments.

 Use of federated access avoids the creation and management of users in your AWS accounts for humans. Instead, use of users can be limited to those exceptional cases such as third-party applications that do not support the use of roles.

 For more information about managing identities, refer to [Identity Management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/identity-management.html) in the AWS Well- Architected Security Pillar and [Identity federation in AWS.](https://aws.amazon.com/identity/federation/)

## Use automation to support agility and scale
<a name="use-automation-to-support-agility-and-scale"></a>

 It is important to design and manage your accounts so that you can rapidly respond to business needs without the need for a corresponding linear increase in headcount. When you consider moving beyond managing just a few accounts, you must consider the work to establish processes and automation that will enable you to do so in an efficient manner.

 For example, if you implement an account design in which new business initiatives call for the creation of new accounts, then you will benefit from having automation in place so that you can rapidly and reliably provision environments based on your standard configurations. Automation can also help you monitor compliance and apply updates to your baseline configurations over time.

## Use multi-factor authentication
<a name="use-multi-factor-authentication"></a>

 Multi-factor authentication (MFA) should be used by your root and all AWS users in your accounts regardless of privilege level or access mechanism. You can follow our current recommendation for MFA best practices for your AWS accounts ([management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html#best-practices_mgmt-acct_mfa) or [member accounts](https://docs.aws.amazon.com/organizations/latest/userguide/best-practices_member-acct.html#best-practices_mbr-acct_mfa)) to set up MFA across your AWS environment.

## Multiple AWS Regions
<a name="multiple-aws-regions"></a>

 If you plan to use multiple AWS Regions, keep the following considerations in mind as you design your overall AWS environment.

**Topics**
+ [Geographic scopes of data protection](#geographic-scopes-of-data-protection)
+ [Performance considerations](#performance-considerations)
+ [Log management](#log-management)

### Geographic scopes of data protection
<a name="geographic-scopes-of-data-protection"></a>

 If you use different AWS Regions that are in the same geographic scope defined by the data protection requirements applicable to your workloads, you can use the same IAM IdP or IdPs to federate to all accounts in live, disaster recovery, or load balanced live environments. You can replicate databases between environments using appropriate mechanisms, such as Amazon DynamoDB global tables or Amazon RDS read replicas. In such circumstances, it is also possible for you to distribute core elements of your foundational AWS environment such that the log archive bucket is in one Region and assets in other accounts in other Regions log cross-Region to it.

 You should carefully consider whether the data protection requirements applicable to your workload differ across countries, or are subject to data sovereignty requirements or export control.

 This might impact your ability to make cross-Region data transfers. (Note that cross-Region data transfers incur networking costs.)

### Performance considerations
<a name="performance-considerations"></a>

 There are also performance considerations to keep in mind for certain workloads. Some services are by their nature per-Region, which makes it more sensible for you to deploy such workloads with all assets in the same Region. For example, AWS KMS keys cannot be exported from a Region, and use of a KMS key in another Region is likely going to add latency to an application. We therefore recommend using AWS KMS in the same Region, unless specific governance policies, regulatory or corporate, mandate otherwise.

 Close collaboration between your security and architecture teams and your workload owning teams is important to properly using KMS. Your design of how Amazon S3 objects, EBS volumes, and other data are encrypted and potentially replicated across Regions should factor in low latency when required.

 Where cross-account replication of these assets is required, Amazon S3 Cross-Region Replication (CRR) enables on-the-fly re-encryption of an object with an AWS KMS key in the destination Region. Multi-Region duplication of AWS KMS keys for the decryption of cross-Region copied EBS volumes can be achieved using the techniques covered in Busy Engineer's Document Bucket.

### Log management
<a name="log-management"></a>

 When logs are generated, we recommend that you implement secondary controls to filter them before they are passed outside a compliance scope boundary associated with an account, or are passed cross-Region. If your logs contain sensitive data, this approach helps ensure that such sensitive data cannot escape your defined compliance scope boundary using AWS logging capabilities.

 Although AWS CloudTrail has built-in cross-account logging capability and AWS Config can aggregate configuration and compliance data across accounts and Regions, it might be more appropriate for you to aggregate logs in an account. You can use AWS Lambda functions or similar to filter the logs before sending them to another Region for aggregation into a multi-Region logging archive.

## Break glass access
<a name="break-glass-access"></a>

 The organization management account is used to provide break glass access to AWS accounts within the organization. Break glass (which draws its name from breaking the glass to pull a fire alarm) refers to a quick means for a person who does not have access privileges to certain AWS accounts to gain access in exceptional circumstances by using an approved process.

 The use cases for break glass access include:
+  Failure of the organization's IdP.
+  A security incident involving the organizations' IdP(s).
+  A failure involving IAM Identity Center.
+  A disaster involving the loss of an organization's entire cloud or IdP teams. It is important that access to these roles is monitored, and alarms and alerts are triggered when the roles are used to access the environment.

 In the case of an incident requiring remediation, we recommend that a user with access to an administrative federated role within the AWS account perform the required remediation. In cases where this user is unavailable to carry out a time sensitive action, we recommend that a highly- restricted group or set of groups be preconfigured within your IdP, each providing appropriate [federated access](https://aws.amazon.com/identity/federation/) into the appropriate set of AWS accounts. A user can either be added into one of these groups using a high-priority and temporary change request, or a select group of privileged and trusted users can be prepopulated into these groups.

 Security teams investigating an incident would use this mechanism to access a read-only role in an impacted account, or use the read-only access mechanism provided through the security tooling account. In summary, common high-priority irregular access scenarios need to be incorporated into standard federated access processes and procedures.

**Note**
 AWS Organizations Service Control Policies do not apply to the organization management account, and administrator access to this account would grant privileged status to the entire organization, given the trust relationship to the management account. Therefore, access to break glass IAM users must be tightly controlled, but accessible through a predefined and strict process. This process often involves one trusted individual having access to the password, and a different trusted individual having access to the hardware multi-factor authentication (MFA) key, meaning it typically requires two people to access any one set of break glass credentials.

 Human access to AWS accounts within the organization should be provided using federated access. Although the use and creation of AWS IAM users is highly discouraged, break glass users are an exception.

 To ensure human break-glass access to your environment, we recommend that you create the following in your AWS organization:
+  At least two IAM users with IAM login credentials to prevent lockdown in case one of them is not available, and additional users depending on your operating model. Do not create unnecessary IAM privileged users in your management account. These users will assume roles in the member accounts in your organization through trust policies.
+  A break glass role that is deployed to all the accounts in the organization, and that can only be assumed by the break glass users from the management account. These roles are needed to allow access from the management account to apply and update controls, to troubleshoot and resolve issues with the automation tooling from the security tooling account, or to remediate security and operational issues in one of the member accounts in the AWS organization. When setting up these roles in your organization, you need to ensure they can be used in emergency situations, bypassing established controls under the situations described earlier in the paragraph, such as service control policies.

**Note**
 If you are currently using AWS Identity Center and you are not using an external IdP (you are using the IAM Identity Center store or your domain service for your identity source), you can use this break glass access in case of Identity Center failure. Review how to set up [emergency access for your IAM Identity Center.](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access.html)
 We strongly recommend configuring these users with a hardware-based MFA device, which can be used in exceptional circumstances to gain access to the organization management account or sub-accounts within the organization by assuming a role. While we recommend the use of the organization management account for break glass access, some organizations might choose to add a dedicated break glass account. This does not eliminate the need for organizational break glass users in the organization management account.
