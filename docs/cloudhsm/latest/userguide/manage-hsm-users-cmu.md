---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-hsm-users-cmu.html
---

# HSM user management with CloudHSM Management Utility (CMU)
<a name="manage-hsm-users-cmu"></a>

 To manage hardware security module (HSM) users in AWS CloudHSM, you must log in to the HSM with the user name and password of a [cryptographic officer](understanding-users-cmu.md#crypto-officer) (CO). Only COs can manage users. The HSM contains a default CO named admin. You set the password for admin when you [activated the cluster](activate-cluster.md).

This topic provides step-by-step instruction on and detail about managing HSM users with AWS CloudHSM Management Utility (CMU).

**Topics**
+ [Prerequisites](understand-users.md)
+ [User types](understanding-users-cmu.md)
+ [Permissions table](user-permissions-table-cmu.md)
+ [Create users](create-users-cmu.md)
+ [List all users](list-users.md)
+ [Change passwords](change-user-password-cmu.md)
+ [Delete users](delete-user.md)
+ [Manage user 2FA](manage-2fa.md)
+ [Using CMU to manage quorum authentication](quorum-authentication.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
