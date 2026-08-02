---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-02.html
---

# ACCT.02 Restrict use of the root user
<a name="acct-02"></a>

The AWS account root user is created when you sign up for an AWS account, and this user has full ownership privileges and permissions over the account that cannot be changed. Use the root user exclusively for tasks that require root user credentials. For more information, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-tasks.html) in the IAM documentation. Perform all other actions in your account by using other types of IAM identities, such as federated users with IAM roles. For more information, see [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) in the IAM documentation.

**To restrict use of the root user**

1. Require multi-factor authentication (MFA) for the root user. For more information, see [ACCT.05 Require multi-factor authentication (MFA) to log in](acct-05.md).

1. Create an administrative user so that you don't use the root user for everyday tasks. For more information about configuring user access, see [ACCT.03 Configure console access for each user](acct-03.md).
