---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/mfa-key-pair-cloudhsm-cli.html
---

# MFA key pair requirements for AWS CloudHSM using CloudHSM CLI
<a name="mfa-key-pair-cloudhsm-cli"></a>

To enable multi-factor authentication (MFA) for a hardware security module (HSM) user in AWS CloudHSM, you can create a new key pair or use an existing key that meets the following requirements:
+ **Key type:** Asymmetric
+ **Key usage:** Sign and verify
+ **Key spec:** RSA\_2048
+ **Signing algorithm includes:** sha256WithRSAEncryption

**Note**
If you are using quorum authentication or plan to use quorum authentication, see [Quorum authentication and MFA in AWS CloudHSM clusters using CloudHSM CLI](quorum-mfa-cloudhsm-cli.md)

You can use CloudHSM CLI and the key pair to create a new admin user with MFA enabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
