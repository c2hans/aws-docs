---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/known-issues-keytool-jarsigner_5.html
---

# Known issues for AWS CloudHSM integration Java Keytool and Jarsigner using Client SDK 5
<a name="known-issues-keytool-jarsigner_5"></a>

The following list provides the current list of known issues for integrations with AWS CloudHSM and Java Keytool and Jarsigner using Client SDK 5.

1. We do not support non-Ed25519 EC keys with Keytool and Jarsigner.

1. We do not support ML-DSA key generation through keytool. Use `KeyPairGenerator` or the CloudHSM CLI to generate ML-DSA key pairs.

1. ML-DSA signature algorithms with jarsigner require JDK 26 or later.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
