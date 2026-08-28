---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles-create-permissions.html
---

# Allow users and groups to create and modify roles
<a name="emr-iam-roles-create-permissions"></a>

IAM principals (users and groups) who create, modify, and specify roles for a cluster, including default roles, must be allowed to perform the following actions. For details about each action, see [Actions](https://docs.aws.amazon.com/IAM/latest/APIReference/API_Operations.html) in the *IAM API Reference*.
+ `iam:CreateRole`
+ `iam:PutRolePolicy`
+ `iam:CreateInstanceProfile`
+ `iam:AddRoleToInstanceProfile`
+ `iam:ListRoles`
+ `iam:GetPolicy`
+ `iam:GetInstanceProfile`
+ `iam:GetPolicyVersion`
+ `iam:AttachRolePolicy`
+ `iam:PassRole`

The `iam:PassRole` permission allows cluster creation. The remaining permissions allow the creation of the default roles.

For information about assigning permissions to a user, see [Changing permissions for a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
