---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-2fa.html
---

# Quorum authentication and 2FA in AWS CloudHSM clusters using AWS CloudHSM Management Utility
<a name="quorum-2fa"></a>

The cluster uses the same key for quorum authentication and for two-factor authentication 2FA). This means a user with 2FA enabled is effectively registered for M-of-N-access-control (MofN). To successfully use 2FA and quorum authentication for the same HSM user, consider the following points:
+ If you are using quorum authentication for a user today, you should use the same key pair you created for the quorum user to enable 2FA for the user.
+ If you add the 2FA requirement for a non-2FA user that is not a quorum authentication user, then you register that user as an MofN user with 2FA authentication.
+ If you remove the 2FA requirement or change the password for a 2FA user that is also a quorum authentication user, you will also remove the registration of the quorum user as an MofN user.
+ If you remove the 2FA requirement or change the password for a 2FA user that is also a quorum authentication user, but you *still want that user to participate in quorum authentication*, then you must register that user again as an MofN user.

For more information about quorum authentication, see [Using CMU to manage quorum authentication](quorum-authentication.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
