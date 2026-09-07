---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/aws-organizations.html
---

# AWS Organizations
<a name="aws-organizations"></a>

 [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) helps you centrally govern your environment as you grow and scale your workloads on AWS. Whether you are a growing startup or a large enterprise, Organizations helps you to centrally provision accounts and resources; secure and audit their environment for compliance; share resources; control access to accounts, Regions, and services; as well as optimize costs and simplify billing. Additionally, Organizations supports aggregation of health events, consolidated data on use of access permissions, and centralized management of backups and tagging for multi-account environments.

 This section includes best practices for organizing your AWS accounts, including grouping your accounts into organizational units (OUs) so that you can more effectively secure and manage your overall AWS environment.

## What is an Organization?
<a name="what-is-an-organization"></a>

 An organization is an entity that you create to consolidate a collection of accounts so that you can administer them as a single unit. Within each organization, you can organize the accounts in a hierarchical, tree-like structure with a [root](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#root) at the top and [organizational units (OUs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organizationalunit) nested under the root. Each account can be placed directly in the root, or placed in one of the OUs in the hierarchy.

 Each organization consists of:
+  A management account
+  Zero or more member accounts
+  Zero or more organizational units (OUs)
+  Zero or more policies

## Organizations management account
<a name="organizations-management-account"></a>

 The management account creates the AWS organization's resources, OUs, and policies, to manage the organization's member accounts. Access to the management account must be strictly controlled by a small set of highly-trusted individuals from the organization, following the [Principles of Least Privilege](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_permissions_least_privileges.html) based on the activities they need to perform. This account **should not** be used for business workloads and should not contain business resources.

 Additionally, the organization management account is where automation tooling is installed to automate consistent deployment of controls or other standardized infrastructure constructs across accounts in an organization. A trust relationship, which is used by the automation tooling, exists between child AWS accounts in the organization and the organization management account.

 This relationship is established by default when new AWS accounts are created in the organization, and it enables management account users and roles to assume this cross-account [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) [role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in child accounts.

### Considerations for setting up the management account:
<a name="considerations-for-setting-up-the-management-account"></a>

 Most customers start with one AWS account, where they build some Proof of Concepts (PoCs) before deploying their workloads on AWS. In this situation, we recommend creating a new AWS account to be your management account, and [inviting your existing account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html) into your new AWS organization. This allows you to keep any PoCs or workloads that you might already have in that account intact.

 When you set up the management account, we recommend using an email address that belongs to a shared mailbox, to avoid losing access to this account if only one individual has access to this email address, and for example, they leave your organization or lose access to the account.

## Organizations member accounts
<a name="organizations-member-accounts"></a>

 AWS Organizations member accounts belong to the organization and reside in the overall organization's structure. All billing for member accounts is consolidated to the management account of the organization. Most of your workloads will reside in member accounts, except for some centrally managed processes that must reside in either the management account or in accounts assigned as designated administrators for specific AWS services.

## Organizational units (OUs)
<a name="organizational-units"></a>

 An organizational unit (OU) provides a means to group accounts within a root. An OU can also contain other OUs. When you attach a policy to one of the nodes in the hierarchy, it flows down and affects all the branches (OUs) and leaves (accounts) beneath it. An OU can have exactly one parent, and each account can be a member of exactly one OU.

 OUs are not meant to mirror your own organization's reporting structure. Instead, OUs are intended to group accounts that have common overarching security policies and operational needs. The primary question to ask yourself is: How likely will the group need a set of similar policies?

 The following diagram shows a basic organization that consists of seven accounts that are organized into four OUs under the [root.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#root) The organization also has a few policies that are applied to OUs.

![Diagram showing an example of a basic organization](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/basic-organization-example.png)
