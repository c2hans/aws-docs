---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-hsm-users-chsm-cli.html
---

# HSM user management with CloudHSM CLI
<a name="manage-hsm-users-chsm-cli"></a>

 To manage hardware security module (HSM) users in AWS CloudHSM, you must log in to the HSM with the user name and password of an [admin](understanding-users.md#admin). Only admins can manage users. The HSM contains a default admin named admin. You set the password for admin when you [activated the cluster](activate-cluster.md).

This topic provides step-by-step instruction on and detail about managing HSM users with CloudHSM CLI.

**Topics**
+ [Prerequisites](manage-hsm-users-chsm-cli-prereq.md)
+ [User types](understanding-users.md)
+ [Permissions table](user-permissions-table-chsm-cli.md)
+ [Create admin](create-admin-cloudhsm-cli.md)
+ [Create CUs](create-user-cloudhsm-cli.md)
+ [List all users](list-users-cloudhsm-cli.md)
+ [Change passwords](change-user-password-cloudhsm-cli.md)
+ [Delete users](delete-user-cloudhsm-cli.md)
+ [Manage user MFA](login-mfa-token-sign.md)
+ [Manage quorum authentication (M of N)](quorum-auth-chsm-cli.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
