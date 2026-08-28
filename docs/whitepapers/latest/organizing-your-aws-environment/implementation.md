---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/implementation.html
---

# Implementation
<a name="implementation"></a>

**Topics**
+ [Getting started with your multi-account environment](#getting-started-with-your-multi-account-environment)
+ [New customers](#new-customers)
+ [Existing customers](#existing-customers)
+ [Available services](#available-services)

## Getting started with your multi-account environment
<a name="getting-started-with-your-multi-account-environment"></a>

 The earlier sections of this guide covered the benefits of using multiple accounts to organize your AWS environment, this section dives deeper into some implementation options you can use to build your multi-account environment.

 Your environment might start with a small number of accounts, and as the number of accounts in your environment increase, you will need automations to manage your cloud environment. These services offer features to help you manage your multi-account environment at scale.

## New customers
<a name="new-customers"></a>

### Managing your own operations
<a name="managing-your-own-operations"></a>

 When starting on AWS, you should evaluate your business goals and determine your future operating model, and decide on which technology to use when building your multi- account environment. If you are planning on managing your own environment, start by evaluating [AWS Control Tower.](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower)

 AWS Control Tower is a service built based on the guidance included in this paper, making it the preferred solution for new-to-the-cloud customers looking for a service-managed environment. AWS Control Tower offers a simplified experience and automatically deploys your initial environment, helping you manage the multi-account environment efficiently, using other AWS services. For a complete list of these services, refer to the [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower) user guide.

### Operations managed by AWS or AWS Partners
<a name="operations-managed-by-aws-or-aws-partners"></a>

 AWS and AWS Partners can help you operate, update, monitor, or deploy your environment and your workload infrastructure, with [AWS Managed Services](https://aws.amazon.com/managed-services/features/) and AWS Partners have offerings that can help with your operations.

### Hybrid operations (mix of customer and AWS managed)
<a name="hybrid-operations-mix-of-customer-and-aws-managed"></a>

 If your portfolio includes different operating models, you will need to consider a combination of the approaches described above. Proving the flexibility to decide what type of operations you will manage on your environment, and which operations you would like to be overseen. For example, you could manage the account vending process and the environment set up using AWS Control Tower, and use Amazon Managed Services for managing the operations related to moving to the cloud.

## Existing customers
<a name="existing-customers"></a>

 If you are not operating your current environment using AWS Organizations, or you are managing an AWS account structure that differs significantly from the strategies laid out in this whitepaper, consider examining your operational model and re-organizing your accounts, and consider operational and organizational changes to align with these strategies.

 AWS has seen many challenges for customers because they have grown organically without employing these recommendations, or by implementing before these recommendations were available. These challenges include the following:
+ Operational inefficiencies and difficulties, such as unintentionally encountering account quotas when operating many workloads in a small number of accounts due to lack of visibility of the shared quotas
+ Use of service roles by humans, and exhaustion in the number of users due to the number of these roles needed to operate many workloads in a small number of accounts
+ Unnecessary complexity due to the large number of accounts managed to operate one workload. This complexity can be part of root causes in incidents within security, availability, and other areas
+ Lack of automation in the provisioning of accounts, causing large delays in implementing new workloads
+ Challenges in managing the email contacts required for notifications about each account (due to lack of automation of account ownership attribution to the workload operators)
+ Challenges in ensuring data governance and residency of data where customers have chosen to use a central account and region for storage, and use of this data in an effort to minimize the number of accounts they are operating

### Embrace infrastructure as code
<a name="embrace-infrastructure-as-code"></a>

 One of the foundational operational capabilities that will enable your ability to manage change effectively is to use infrastructure as code technologies and automation to build and deploy your workloads in AWS. This basic capability might be perceived as being part of your [Infrastructure OU](foundational-ous.md#infrastructure-ou), but these are foundational capabilities for all OUs.

### Examine your operational model
<a name="examine-your-operational-model"></a>

 Amazon has "commitment to operational excellence" as one of its four guiding principles of who we are. We have an operational model that enables rapid decisions and autonomy. The way you operate your business is a primary consideration in how you organize your environment. In many companies, this doesn't change regularly, and changes should always be made with careful consideration of the business impact of the change. Your [Operating Model](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operating-model.html) could be aligned by business unit, regulatory restrictions, area of expertise, and/or organic growth. You might have a need for multiple operational models, for different businesses or business units. The ability for you to meet your goals using AWS is fundamentally affected by your ability to run your operational model.

### Implement identity management and access controls and other security capabilities
<a name="implement-identity-management-and-access-controls-and-other-security-capabilities"></a>

 The [Security OU](foundational-ous.md#security-ou) is a foundational OU. Using a central [identity provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) enables you to centrally manage both the identities of the people and services that will need to access resources in your environment, and the permissions associated with that access. To prevent a single source of compromise, consider having more than one identity provider. If you do not currently have an identity provider, consider [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html). This also provides a central place to enforce multi-factor authentication and provide [federated](https://aws.amazon.com/identity/federation/) access into your environment. Evaluate your capabilities and operational model between your [identity management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/identity-management.html) and [Amazon S3](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/permissions-management.html) permissions management (also known as access controls).

 Next, set up the security capabilities (for example: , encryption and [key management](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html), [secrets management](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), and [incident response](https://docs.aws.amazon.com/wellarchitected/latest/framework/a-incident-response.html) capabilities) in the appropriate environment. You can then use these operational capabilities as you reorganize other parts of your operations. Decide if you want to have a security "rea[centralized log storage](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-logging-and-multiple-account-security-guardrails.html)d only" account to manage and use cross-account access in your environment, or use federated roles directly to access individual accounts in your environment.

 The following capabilities can be built as you scale and deploy workloads, or in preparation for their use as you move workloads:
+ The additional security capabilities of vulnerability and threat management (as part of security tooling)
+ Data de-identification and data isolation (which is normally part of the individual workloads in your [Workloads OU](application-ous.md#workloads-ou).)
+ Patching (which might use your [Deployments OU](advanced-ous.md#deployments-ou) to patch golden machine and container images)
+ Forensics

### Separate the production workload environment from non-production environment(s)
<a name="separate-the-production-workload-environment-from-non-production-environments"></a>

 Next, consider implementing hard isolation between your production environment and your non- production environments by implementing them as separate accounts. This reduces your risk of exposing production data in non-production environments, but might increase the complexity of how you perform deployments. As a result, this change could affect many of your operational capabilities, including:
+ [Network connectivity](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-lens/networkconnectivity.html), in your Infrastructure OU and accounts, and Workloads OU.
+ [Network security](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html), in your Workloads and Security OUs
+ [Application security](https://wa.aws.amazon.com/serv.question.SEC_3.en.html), in your Workloads, Deployments, and Security OUs
+ [Tagging,](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in all OUs
+ Service onboarding and [cloud financial management](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/practice-cloud-financial-management.html), in all OUs
+ [Rollout/rollback](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/) and [change management capabilities](https://docs.aws.amazon.com/wellarchitected/latest/framework/a-change-management.html), in your Deployments and Workloads OUs
+ Developer experience and tools, in your [Sandbox OU](experimental-ous.md#sandbox-ou), as well as in your Deployments and Workload OUs

 It is not uncommon to have basic connectivity to and from your local networks and the internet shared between your production and non-production workloads. If you have deployment tooling that is tightly integrated with your current environment, you can integrate the existing implementation as you move the workload, or you can implement the Deployments OU to also deploy to your existing environment while you move them to your new environment.

### Networking considerations in a multi-account environment
<a name="networking-considerations-in-a-multi-account-environment"></a>

 The number of VPCs a customer operates is usually related to the number of accounts, regulatory requirements (such as the payment card industry (PCI), and compliant/non-PCI compliant), and staged environments (such as prod, dev, and test). With an increasing number of VPCs (account isolated or not), give careful consideration to cross-VPC connectivity management. This is an essential part of the customer's network operation. Additionally, IP address management becomes a key contributing factor to enabling scalability and future growth. You might consider designs that are built around IPv6 adoption that can be driven by the need to scale your network, or by a strategic initiative. Current recommendations for three specific areas in cross-VPC and hybrid connectivity can be grouped by:
+ **Network connectivity** — Interconnecting VPCs, on-premises networks at scale, and choosing the right tool for the use case. For intra-AWS connectivity, [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html), [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html), and [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-services-overview.html) are just a [few options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/welcome.html) which help with different use cases.
+ **Network security** — Building [centralized](foundational-ous.md#infrastructure-ou) or distributed inspection points for accessing the internet and VPC-to-VPC traffic needs to account for the different options, such as [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html), [AWS Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html), and [AWS Web Application Firewall](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html).
+ **DNS management** — Resolving DNS within the AWS and hybrid environments at scale involves both right-sizing and choosing the deployment model that best suits the organization's scaling and growth goals. Inbound and outbound Route 53 Resolver endpoints can be centralized or distributed, depending on the operations and management models, and involve different needs across the AWS network environment.

### Separate the workload environments to align with the operational organization units
<a name="separate-the-workload-environments-to-align-with-the-operational-organization-units"></a>

 To achieve agility and autonomy, your environment will separate into organizational boundaries. Align your workload environments (both production and non-production) with these organizational boundaries to ensure you enable further agility and autonomy. As you grow and expand, it is common to create new boundaries and move workloads to ensure you continue to have these business capabilities. This could further affect your operational capabilities, such as [backups and disaster recovery](https://docs.aws.amazon.com/wellarchitected/latest/framework/a-failure-management.html), [support](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operate.html), template management, records management, and sorting and searching via metadata in your workloads OU. Consider centralizing the management of these capabilities to simplify the realignment. You can use tag policies as a means to classify the workloads. You can use [tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) as a means to classify the workloads. You can [use AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-cross-account-backup.html) to [back up to a designated location](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html) in your environment and allow you to [centralize protection and monitoring](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-backup.html) of your backups.

### Create the additional organizational units to enable other capabilities
<a name="create-the-additional-organizational-units-to-enable-other-capabilities"></a>

 You should consider creating an [Exceptions OU](procedural-ous.md#exceptions-ou). Also, consider creating a [Policy Staging OU](procedural-ous.md#policy-staging-ou). As your business might either acquire or divest parts of your business, consider having a [Transitional OU](procedural-ous.md#transitional-ou) to enable an area to change the policies to align with new requirements. As you deprecate accounts, you will want a [Suspended OU](procedural-ous.md#suspended-ou) to contain these accounts until you are comfortable having them permanently removed. You should consider creating a [Individual Business Users OU](advanced-ous.md#individual-business-users-ou) to enable business users and teams who need access to manage AWS resources directly, rather than management by the Workload OU.

### Other considerations for implementing these changes
<a name="other-considerations-for-implementing-these-changes"></a>

 The reorganization will require movement of accounts, or migrations of workloads between accounts if you have deployed workloads in accounts that don't align with your desired operational model. There are mechanisms to [move accounts between organizations and organizational units](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html#move_account_to_ou), but if your new approach indicates some workloads in an account should belong to one organizational unit and other workloads belong to another organizational unit, you will have misalignment. To align the accounts with the operational model, you will have to migrate workloads between existing accounts, or to new accounts. The methods and capabilities to migrate between accounts are similar to [accomplish these migrations.](https://aws.amazon.com/prescriptive-guidance/)

## Available services
<a name="available-services"></a>

### AWS Organizations
<a name="aws-organizations-1"></a>

 AWS Organizations provides the underlying infrastructure and capabilities for customers to build and manage their multi-account environments. Using AWS Organizations, customers can automate AWS account creation and management; govern access within the organization to AWS services, resources, and Region using preventative controls; centrally manage policies across multiple AWS accounts (SCPs, Tag Policies, AWS Backup, ML opt-out); configure multi-account capabilities for AWS services (such as AWS Config, AWS CloudTrail, AWS CloudFormation, GuardDuty, Amazon Macie, and IAM Identity Center); share resources across accounts; and consolidate their bill.

 AWS has the following resources available for help you establish your multi-account environment using AWS Organizations:
+  [AWS Organizations features](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html#features)
+  [Organizations supported multi-account services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list)
+  [Organization Quotas](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits)

### AWS Control Tower
<a name="aws-control-tower"></a>

 AWS Control Tower provides a simplified way to set up and govern a secure, multi-account AWS environment based on the guidance in this paper. AWS Control Tower automates the creation of your multi-account environment using AWS Organizations, instantiating a set of initial accounts and with some default controls and configurations for the environment. Although AWS Control Tower reduces flexibility, it also provides automations to manage your cloud environment efficiently.

**Note**
 The OU structure that AWS Control Tower initially deploys is slightly different from the guidance in this paper, review [AWS multi-account environment with Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/aws-multi-account-landing-zone.html) for a detailed implementation and mapping between the AWS Control Tower implementation and the guidance offered in this paper.

 AWS has the following resources available for help you establish your multi-account environment using AWS Control Tower:
+  [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower)
+  [AWS Control Tower Quotas](https://docs.aws.amazon.com/controltower/latest/userguide/limits)

### AWS Managed Services
<a name="aws-managed-services"></a>

 AWS Managed Services (AMS) uses AWS services and a growing library of automations, configurations, and run books, to provide an end-to-end operational solution for both new and existing AWS environments. AMS covers the people element of operating the technology that AWS services provide.

 For additional information, refer to [AWS Managed Services features.](https://aws.amazon.com/managed-services/features/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
