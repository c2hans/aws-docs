---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/disable-2fa.html
---

# Disable 2FA for HSM users using AWS CloudHSM Management Utility
<a name="disable-2fa"></a>

Use the AWS CloudHSM Management Utility (CMU) to disable two-factor authentication (2FA) for hardware security module HSM) users in AWS CloudHSM.

**To disable 2FA for CO users with 2FA enabled**

1. Use CMU to log in to the HSM as a CO with 2FA enabled.

1.  Use **changePswd** to remove 2FA from CO users with 2FA enabled.

   ```
   aws-cloudhsm > changePswd CO example-user <new password>
   ```

   CMU prompts you to confirm the change password operation.
**Note**
If you remove the 2FA requirement or change the password for a 2FA user that is also a quorum authentication user, you will also remove the registration of the quorum user as an MofN user. For more information about quorum users and 2FA, see [Quorum authentication and 2FA in AWS CloudHSM clusters using AWS CloudHSM Management Utility](quorum-2fa.md).

1. Type **y**.

   CMU confirms the change password operation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
