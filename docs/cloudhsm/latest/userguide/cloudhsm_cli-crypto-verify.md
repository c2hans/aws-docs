---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-crypto-verify.html
---

# The crypto verify category in CloudHSM CLI
<a name="cloudhsm_cli-crypto-verify"></a>

In the CloudHSM CLI, **crypto verify** is a parent category for a group of commands that, when combined with the parent category, confirms whether a file has been signed by a given key. **crypto verify** has the following subcommands:
+ [crypto verify ecdsa](cloudhsm_cli-crypto-verify-ecdsa.md)
+ [crypto verify ed25519](cloudhsm_cli-crypto-verify-ed25519.md)
+ [crypto verify ed25519ph](cloudhsm_cli-crypto-verify-ed25519ph.md)
+ [crypto verify ml-dsa](cloudhsm_cli-crypto-verify-mldsa.md)
+ [crypto verify rsa-pkcs](cloudhsm_cli-crypto-verify-rsa-pkcs.md)
+ [crypto verify rsa-pkcs-pss](cloudhsm_cli-crypto-verify-rsa-pkcs-pss.md)

The **crypto verify** command compares a signed file against a source file and analyzes whether they are cryptographically related based on a given public key and signing mechanism.

**Note**
Files can be signed in AWS CloudHSM with the [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md) operation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
