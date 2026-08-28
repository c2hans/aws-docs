---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-mfa-cloudhsm-cli.html
---

# Quorum authentication and MFA in AWS CloudHSM clusters using CloudHSM CLI
<a name="quorum-mfa-cloudhsm-cli"></a>

The AWS CloudHSM cluster uses the same key for quorum authentication and for multi-factor authentication (MFA). This means a user with MFA enabled is effectively registered for MofN or quorum access control. To successfully use MFA and quorum authentication for the same HSM user, consider the following points:
+ If you are using quorum authentication for a user today, you should use the same key pair you created for the quorum user to enable MFA for the user.
+ If you add the MFA requirement for a non-MFA user who is not a quorum authentication user, then you register that user as a quorum (MofN) registered user with MFA authentication.
+ If you remove the MFA requirement or change the password for an MFA user who is also a registered quorum authentication user, you will also remove the user's registration as a quorum (MofN) user.
+ If you remove the MFA requirement or change the password for an MFA user who is also a quorum authentication user, *but you still want that user to participate in quorum authentication*, then you must register that user again as a Quorum (MofN) user.

For more information about quorum authentication, see [Manage quorum authentication (M of N)](quorum-auth-chsm-cli.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
