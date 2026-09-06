---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/set-up-organization.html
---

# Set up an organization
<a name="set-up-organization"></a>

When you have multiple AWS accounts, you can logically manage those accounts through an organization in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html). An *account* in AWS Organizations is a standard AWS account that contains your AWS resources and the identities that can access those resources. An *organization* is an entity that consolidates your AWS accounts so that you can administer them as a single unit.

When you use an account to create an organization, that account becomes the *management account* (also known as a *payer account* or *root account*) for the organization. An organization can only have one management account. When you add additional AWS accounts to the organization, they become *member accounts*.

|
|
| Note: Each AWS account also has a single identity called the *root user*. You can sign in as the root user by using the email address and password you used to create the account. However, we strongly recommend that you don't use the root user for everyday tasks, even the administrative ones. For more information, see [AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html).We also recommend [centralizing root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html) and removing the root user credentials from member accounts in your organization. |
| --- |

You organize accounts in a hierarchical tree-like structure that consists of the organization root, organizational units (OUs), and member accounts. The *root* is the parent container for all of the accounts in your organization. An *organizational unit* (OU) is a container for [accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) within the [root](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#root). An OU can contain other OUs or member accounts. An OU can have only one parent, and each account can be a member of only one OU. For more information, see [Terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) (AWS Organizations documentation).

A [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) specifies the services and actions that users and roles can use. SCPs are similar to AWS Identity and Access Management (IAM) permissions policies except that they don't grant permissions. Instead, SCPs define the maximum permissions. When you attach a policy to one of the nodes in the hierarchy, it applies to all the OUs and accounts within that node. For example, if you apply a policy to the root, it applies to all [OUs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organizationalunit) and [accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) in the organization, and if you apply a policy to an OU, it applies to only the OUs and accounts in the target OU.

A [resource control policy (RCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) offers central control over the maximum available permissions for resources in your organization. RCPs help you make sure that resources in your account stay within your organization's access control guidelines.

You can use the AWS Organizations console to centrally view and manage all of your accounts within an organization. One of the benefits of using an organization is that you can receive a consolidated bill that shows all charges associated with the management and member accounts. For more information, see [Consolidated billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) (AWS Organizations documentation).

## Best practices
<a name="organization-best-practices"></a>
+ Don't use an existing AWS account to create an organization. Start with a new account, which becomes your management account for the organization. Privileged operations can be performed within an organization's management account, and SCPs and RCPs do not apply to the management account. That's why you should limit the cloud resources and data contained in the management account to only those that must be managed in the management account.
+ Limit access to the management account to only those individuals who need to provision new AWS accounts and to administer the organization.
+ Use SCPs to define the maximum permissions for the root, organizational units, and member accounts. SCPs can't be directly applied to the management account.
+ Use RCPs to define the maximum permissions for resources in member accounts. RCPs can't be directly applied to the management account.
+ Adhere to the [Best practices for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html) (AWS Organizations documentation).
