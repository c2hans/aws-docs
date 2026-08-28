---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/enable-2fa-kms.html
---

# 2FA key pair requirements for AWS CloudHSM using AWS CloudHSM Management Utility
<a name="enable-2fa-kms"></a>

To enable two-factor authentication (2FA) for an AWS CloudHSM hardware security module (HSM) user, use a key that meets the following requirements.

You can create a new key pair or use an existing key that meets the following requirements.
+ Key type: Asymmetric
+ Key usage: Sign and Verify
+ Key spec: RSA\_2048
+ Signing algorithm includes:
  + `sha256WithRSAEncryption`

**Note**
If you are using quorum authentication or plan to use quorum authentication, see [Quorum authentication and 2FA in AWS CloudHSM clusters using AWS CloudHSM Management Utility](quorum-2fa.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
