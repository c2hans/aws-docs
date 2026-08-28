---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetdelegation.html
---

# Delegate permission set administration
<a name="permissionsetdelegation"></a>

IAM Identity Center enables you to delegate management of permission sets and assignments in accounts by creating [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) that reference the [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of IAM Identity Center resources. For example, you can create policies that enable different administrators to manage assignments in specified accounts for permission sets with specific tags.

**Note**
To use permission sets, you'll need to use an Organization instance of IAM Identity Center. For more information, see [Organization and account instances of IAM Identity Center](identity-center-instances.md).

You can use either of the following methods to create these types of policies.
+ (Recommended) Create [permission sets](permissionsets.md) in IAM Identity Center, each with a different policy, and assign the permission sets to different users or groups. This enables you to manage administrative permissions for users who sign in using your chosen [IAM Identity Center identity source](manage-your-identity-source.md).
+ Create custom policies in IAM, and then attach them to IAM roles that your administrators assume. For information about roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) to get their assigned IAM Identity Center administrative permissions.

**Important**
IAM Identity Center resource ARNs are case sensitive.

The following shows the proper case for referencing the IAM Identity Center permission set and account resource types.

| Resource Types | ARN | Context Keys |
| --- | --- | --- |
| PermissionSet | arn:${Partition}:sso:::permissionSet/${InstanceId}/${PermissionSetId} | aws:ResourceTag/${TagKey} |
| Account | arn:${Partition}:sso:::account/${AccountId} | Not Applicable |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
