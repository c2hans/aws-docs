---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/org-management.html
---

# Org Management account
<a name="org-management"></a>

The following diagram illustrates the AWS security services that are configured in the Org Management account.

![Security services for the Org Management account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/20032423-a649-4f28-8127-9c1e71793b9d.png)

The sections [Using AWS Organizations for security](organizations-security.md) and [The management account, trusted access, and delegated administrators](management-account.md) earlier in this guide discussed the purpose and security objectives of the Org Management account in depth. Follow the [security best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html) for your Org Management account. These include using an email address that is managed by your business, maintaining the correct administrative and security contact information (such as attaching a phone number to the account in the event AWS needs to contact the owner of the account), enabling multi-factor authentication (MFA) for the all users, and regularly reviewing who has access to the Org Management account. Services deployed in the Org Management account should be configured with appropriate roles, trust policies, and other permissions so that the administrators of those services (who must access them in the Org Management account) cannot also inappropriately access other services.

## Service control policies
<a name="mgmt-scps"></a>

With [AWS Organizations](https://aws.amazon.com/organizations/), you can centrally manage policies across multiple AWS accounts. For example, you can apply [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html) (SCPs) across multiple AWS accounts that are members of an organization. SCPs allow you to define which AWS service APIs can and cannot be run by [IAM](https://aws.amazon.com/iam/) principals (such as IAM users and roles) in your organization's member AWS accounts. SCPs are created and applied from the Org Management account, which is the AWS account that you used when you created your organization. Read more about SCPs in the [Using AWS Organizations for security](organizations-security.md) section earlier in this reference.

If you use AWS Control Tower to manage your AWS organization, it will deploy [a set of SCPs as preventive guardrails](https://docs.aws.amazon.com/controltower/latest/userguide/guardrails-reference.html) (categorized as mandatory, strongly recommended, or elective). These guardrails help you govern your resources by enforcing organization-wide security controls. These SCPs automatically use an aws-control-tower tag that has a value of managed-by-control-tower.

**Design consideration:**
+ SCPs affect only *member* accounts in the AWS organization. Although they are applied from the Org Management account, they have no effect on users or roles in that account. To learn about how SCP evaluation logic works, and to see examples of recommended structures, see the AWS blog post [How to use service control policies in AWS Organizations](https://aws.amazon.com/blogs/security/how-to-use-service-control-policies-in-aws-organizations/).

## Resource control policies
<a name="mgmt-rcps"></a>

[Resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) (RCPs) offer centralized control over the maximum available permissions for resources in your organization. An RCP defines a permissions guardrail or sets limits on the actions that identities can take on resources in your organization. You can use RCPs to restrict who can access your resources and enforce requirements on how your resources can be accessed in your organization's member AWS accounts. You can attach RCPs directly to individual accounts, OUs, or the organization root. For a detailed explanation of how RCPs work, see [RCP evaluation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps_evaluation.html) in the AWS Organizations documentation. Read more about RCPs in the [Using AWS Organizations for security](organizations-security.md) section earlier in this reference.

If you use AWS Control Tower to manage your AWS organization, it will deploy a set of RCPs as preventative guardrails. These guardrails help you govern your resources by enforcing organization-wide security controls. These RCPs automatically use an `aws-control-tower` tag that has a value of `managed-by-control-tower`.

**Design considerations:**
+ RCPs affect only resources in ***member*** accounts in the organization. They have no effect on resources in the management account. This also means that RCPs apply to member accounts that are designated as delegated administrators.
+ RCPs apply to resources for a subset of AWS services. For more information, see [List of AWS services that support RCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html#rcp-supported-services) in the AWS Organizations documentation. You can use [AWS Config Rules](https://aws.amazon.com/config/) and [AWS Lambda functions](https://aws.amazon.com/pm/lambda/) to monitor and automate the enforcement of security controls on resources that aren't currently supported by RCPs.

## Declarative policies
<a name="mgmt-declarative-policies"></a>

A declarative policy is a type of AWS Organizations management policy that helps you centrally declare and enforce your desired configuration for a given AWS service at scale across an organization. How those policies affect the OUs and accounts that inherit them depends on the type of declarative policy that you apply in AWS Organizations. For the latest supported services and attributes, see [Declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/syntax-inheritance.html) in the AWS Organizations documentation.

You can enforce the baseline configuration for an AWS service by making a few selections on the AWS Organizations and AWS Control Tower consoles or by using a few AWS Command Line Interface (AWS CLI) and AWS SDK commands. Declarative policies are enforced in the service's control plane, which means that the baseline configuration for an AWS service is always maintained, even when the service introduces new features or APIs, when new accounts are added to an organization, or when new principals and resources are created. Declarative policies can be applied to an entire organization or to specific OUs or accounts. The *effective policy* is the set of rules that are inherited from the organization root and OUs along with the policies that are directly attached to the account. If a declarative policy is [detached](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_detach.html), the attribute state will roll back to its state before the declarative policy was attached.

You can use declarative policies to create custom error messages. For example, if an API operation fails because of a declarative policy, you can set the error message or provide a custom URL―such as a link to an internal wiki or a link to a message that describes the failure. This helps provide users with more information so they can troubleshoot the issue themselves. You can also audit the process of creating declarative policies, updating declarative policies, and deleting declarative policies by using AWS CloudTrail.

Declarative policies provide *account status reports,* which enable you to review the current status of all attributes that are supported by declarative policies for the accounts in scope. You can choose the accounts and OUs to include in the report scope or choose an entire organization by selecting the root. This report helps you assess readiness by providing a breakdown by AWS Region and specifying whether the current state of an attribute is *uniform across accounts* (through the `numberOfMatchedAccounts` value) or *inconsistent* *across accounts* (through the `numberOfUnmatchedAccounts` value).

**Design consideration: **
+ When you configure a service attribute by using a declarative policy, the policy might impact multiple APIs. Any noncompliant actions will fail. Account administrators will not be able to modify the value of the service attribute at the individual account level.

## Centralized root access
<a name="mgmt-central-root-access"></a>

All member accounts in AWS Organizations have their own root user, which is an identity that has complete access to all AWS services and resources in that member account. IAM provides centralized root access management to manage root access across all member accounts. This helps prevent member root user usage and helps provide recovery at scale. The centralized root access feature has two essential capabilities: root credentials management and root sessions.
+ The root credentials management capability allows central management and helps secure root user across all management accounts. This capability includes the removal of long-term root credentials, prevention of root credential recovery by member accounts, and provisioning of new member accounts with no root credentials by default. It also provides an easy way to demonstrate compliance. When root user management is centralized, you can remove root user passwords, access keys, and signing certificates, and deactivate multi-factor authentication (MFA) from all member accounts.
+ The root sessions capability enables you to perform privileged root user actions by using short-term credentials on member accounts from the Org Management account or from delegated administrator accounts. This capability helps you enable short-term root access that is scoped to specific actions, adhering to the principle of least privilege.

For centralized root credential management, you need to enable root credential management and root sessions capabilities at the organization level from the Org Management account or in a delegated administrator account. Following AWS SRA best practices, we delegate this capability to the Security Tooling account. For information about configuring and using centralized root user access, see the AWS Security blog post, [Centrally managing root access for customers using AWS Organizations](https://aws.amazon.com/blogs/aws/centrally-managing-root-access-for-customers-using-aws-organizations/).

## IAM Identity Center
<a name="mgmt-sso"></a>

[AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) is an identity federation service that helps you centrally manage SSO access to all your AWS accounts, principals, and cloud workloads. IAM Identity Center also helps you manage access and permissions to commonly used third-party software as a service (SaaS) applications. Identity providers integrate with IAM Identity Center by using SAML 2.0. Bulk and just-in-time provisioning can be done by using the System for Cross-Domain Identity Management (SCIM). IAM Identity Center can also integrate with on-premises or AWS-managed Microsoft Active Directory (AD) domains as an identity provider through the use of AWS Directory Service. IAM Identity Center includes a user portal where your end-users can find and access their assigned AWS accounts, IAM Identity Center, roles, cloud applications, and custom applications in one place.

IAM Identity Center natively integrates with AWS Organizations and runs in the Org Management account by default. However, to exercise least privilege and tightly control access to the management account, IAM Identity Center administration can be delegated to a specific member account. In the AWS SRA, the Shared Services account is the delegated administrator account for IAM Identity Center. Before you enable delegated administration for IAM Identity Center, review [these considerations](https://aws.amazon.com/blogs/security/getting-started-with-aws-sso-delegated-administration/#_Considerations_when_delegating). You will find more information about delegation in the [Shared Services account](shared-services.md) section. Even after you enable delegation, IAM Identity Center still needs to run in the Org Management account to perform certain [IAM Identity Center-related tasks](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin.html#delegated-admin-tasks-member-account), which include managing permission sets that are provisioned in the Org Management account.

Within the IAM Identity Center console, accounts are displayed by their encapsulating OU. This enables you to quickly discover your AWS accounts, apply common sets of permissions, and manage access from a central location.

IAM Identity Center includes an identity store where specific user information must be stored. However, IAM Identity Center does not have to be the authoritative source for workforce information. In cases where your enterprise already has an authoritative source, IAM Identity Center supports the following types of identity providers (IdPs).
+ **IAM Identity Center identity store –** Choose this option if the following two options are not available. Users are created, group assignments are made, and permissions are assigned in the identity store. Even if your authoritative source is external to IAM Identity Center, a copy of principal attributes will be stored with the identity store.
+ **Microsoft Active Directory (AD) –** Choose this option if you want to continue managing users in either your directory in AWS Directory Service for Microsoft Active Directory or your self-managed directory in Active Directory.
+ **External identity provider –** Choose this option if you prefer to manage users in an external third-party, SAML-based IdP.

You can rely on an existing IdP that is already in place within your enterprise. This makes it easier to manage access across multiple applications and services, because you are creating, managing, and revoking access from a single location. For example, if someone leaves your team, you can revoke their access to all applications and services (including AWS accounts) from one location. This reduces the need for multiple credentials and provides you with an opportunity to integrate with your human resources (HR) processes.

**Design consideration: **
+ Use an external IdP if that option is available to your enterprise. If your IdP supports System for Cross-domain Identity Management (SCIM), take advantage of the SCIM capability in IAM Identity Center to automate user, group, and permission provisioning (synchronization). This allows AWS access to stay in sync with your corporate workflow for new hires, employees who are moving to another team, and employees who are leaving the company. At any given time, you can have only one directory or one SAML 2.0 identity provider connected to IAM Identity Center. However, you can switch to another identity provider.

## IAM access advisor
<a name="mgmt-iam-advisor"></a>

IAM access advisor provides traceability data in the form of service last accessed information for your AWS accounts and OUs. Use this detective control to contribute to a [least privilege strategy](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege). For IAM principals, you can view two types of last accessed information: allowed AWS service information and allowed action information. The information includes the date and time when the attempt was made.

IAM access within the Org Management account lets you view service last accessed data for the Org Management account, OU, member account, or IAM policy in your AWS organization. This information is available in the IAM console within the management account and can also be obtained programmatically by using IAM access advisor APIs in AWS CLI or a programmatic client. The information indicates which principals in an organization or account last attempted to access the service and when. Last accessed information provides insight for actual service usage (see [example scenarios](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-example-scenarios.html)), so you can reduce IAM permissions to only those services that are actually used.

## AWS Systems Manager
<a name="mgmt-sys"></a>

Quick Setup and Explorer, which are capabilities of [AWS Systems Manager](https://aws.amazon.com/systems-manager/), both support AWS Organizations and operate from the Org Management account.

[Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html) is an automation feature of Systems Manager. It enables the Org Management account to easily define configurations for Systems Manager to engage on your behalf across accounts in your AWS organization. You can enable Quick Setup across your entire AWS organization or choose specific OUs. Quick Setup can schedule AWS Systems Manager Agent (SSM Agent) to run biweekly updates on your EC2 instances and can set up a daily scan of those instances to identify missing patches.

[Explorer](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer.html) is a customizable operations dashboard that reports information about your AWS resources. Explorer displays an aggregated view of operations data for your AWS accounts and across AWS Regions. This includes data about your EC2 instances and patch compliance details. After you complete Integrated Setup (which also includes Systems Manager OpsCenter) within AWS Organizations, you can aggregate data in Explorer by OU or for an entire AWS organization. Systems Manager aggregates the data into the AWS Org Management account before displaying it in Explorer.

The [Workloads OU](application.md) section later in this guide discusses the use of the SSM Agent on the EC2 instances in the Application account.

## AWS Control Tower
<a name="mgmt-tower"></a>

[AWS Control Tower](https://aws.amazon.com/controltower/) provides a straightforward way to set up and govern a secure, multi-account AWS environment, which is called a *landing zone*. AWS Control Tower creates your landing zone by using AWS Organizations, and provides ongoing account management and governance as well as implementation best practices. You can use AWS Control Tower to provision new accounts in a few steps while ensuring that the accounts conform to your organizational policies. You can even add existing accounts to a new AWS Control Tower environment.

AWS Control Tower has a broad and flexible set of features. A key feature is its ability to *orchestrate* the capabilities of several other [AWS services](https://docs.aws.amazon.com/controltower/latest/userguide/integrated-services.html), including AWS Organizations, AWS Service Catalog, and IAM Identity Center, to build a landing zone. For example, by default, AWS Control Tower uses AWS CloudFormation to establish a baseline, AWS Organizations service control policies (SCPs) prevent configuration changes, and AWS Config rules continuously detect non-conformance. AWS Control Tower employs blueprints that help you quickly align your multi-account AWS environment with [AWS Well-Architected security foundation design principles](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/security.html). Among governance features, AWS Control Tower offers guardrails that prevent deployment of resources that don't conform to selected policies.

You can get started implementing AWS SRA guidance with AWS Control Tower. For example, AWS Control Tower establishes an AWS organization with the recommended multi-account architecture. It provides blueprints to provide identity management, provide federated access to accounts, centralize logging, establish cross-account security audits, define a workflow for provisioning new accounts, and implement account baselines with network configurations.

In the AWS SRA, AWS Control Tower is within the Org Management account because AWS Control Tower uses this account to set up an AWS organization automatically and designates that account as the management account. This account is used for billing across your AWS organization. It's also used for Account Factory provisioning of accounts, to manage OUs, and to manage guardrails. If you are launching AWS Control Tower in an existing AWS organization, you can use the existing management account. AWS Control Tower will use that account as the designated management account.

**Design consideration:**
+ If you want to do additional baselining of controls and configurations across your accounts, you can use [Customizations for AWS Control Tower (CfCT)](https://aws.amazon.com/solutions/implementations/customizations-for-aws-control-tower/). With CfCT, you can customize your AWS Control Tower landing zone by using a CloudFormation template and SCPs. You can deploy the custom template and policies to individual accounts and OUs within your organization. CfCT integrates with AWS Control Tower lifecycle events to ensure that resource deployments stay in sync with your landing zone.

## AWS Artifact
<a name="mgmt-artifact"></a>

[AWS Artifact](https://aws.amazon.com/artifact/) provides on-demand access to AWS security and compliance reports and select online agreements. Reports available in AWS Artifact include System and Organization Controls (SOC) reports, Payment Card Industry (PCI) reports, and certifications from accreditation bodies across geographies and compliance verticals that validate the implementation and operating effectiveness of AWS security controls. AWS Artifact helps you perform your due diligence of AWS with enhanced transparency into our security control environment. It also lets you continuously monitor the security and compliance of AWS with immediate access to new reports.

AWS Artifact Agreements enable you to review, accept, and track the status of AWS agreements such as the Business Associate Addendum (BAA) for an individual account and for the accounts that are part of your organization in AWS Organizations.

You can provide the AWS audit artifacts to your auditors or regulators as evidence of AWS security controls. You can also use the responsibility guidance provided by some of the AWS audit artifacts to design your cloud architecture. This guidance helps determine the additional security controls you can put in place to support the specific use cases of your system.

AWS Artifact is hosted in the Org Management account to provide a central location where you can review, accept, and manage agreements with AWS. This is because agreements that are accepted at the management account flow down to the member accounts.

**Design consideration:**
+ Users within the Org Management account should be restricted to use only the Agreements feature of AWS Artifact and nothing else. To implement segregation of duties, AWS Artifact is also hosted in the Security Tooling account where you can delegate permissions to your compliance stakeholders and external auditors to access audit artifacts. You can implement this separation by defining fine-grained IAM permission policies. For examples, see [Example IAM policies](https://docs.aws.amazon.com/artifact/latest/ug/security-iam.html#example-iam-policies) in the AWS documentation.

## Distributed and centralized security service guardrails
<a name="mgmt-dist"></a>

In the AWS SRA, AWS Security Hub CSPM, AWS Security Hub, Amazon GuardDuty, AWS Config, IAM Access Analyzer, AWS CloudTrail organization trails, and often Amazon Macie are deployed with appropriate delegated administration or aggregation to the Security Tooling account. This enables a consistent set of guardrails across accounts and also provides centralized monitoring, management, and governance across your AWS organization. You will find this group of services in every type of account represented in the AWS SRA. These should be part of the AWS services that must be provisioned as part of your account onboarding and baselining process. The [GitHub code repository](https://github.com/aws-samples/aws-security-reference-architecture-examples) provides a sample implementation of AWS security-focused services across your accounts, including the AWS Org Management account.

In addition to these services, AWS SRA includes two security-focused services, Amazon Detective and AWS Audit Manager, which support the integration and delegated administrator functionality in AWS Organizations. However, those are not included as part of the recommended services for account baselining. We have seen that these services are best used in the following scenarios:
+ You have a dedicated team or group of resources that perform those digital forensics and IT audit functions. Detective is best utilized by security analyst teams, and Audit Manager is helpful to your internal audit or compliance teams.
+ You want to focus on a core set of tools such as AWS Config, Amazon GuardDuty, AWS Security Hub, and AWS Security Hub CSPM at the start of your project, and then build on these by using services that provide additional capabilities.
