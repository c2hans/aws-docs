---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/hierarchical-keyring-details.html
---

# AWS KMS Hierarchical keyring technical details
<a name="hierarchical-keyring-details"></a>

The [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md) uses a unqiue data key to encrypt each message and encrypts each data key with a unique wrapping key derived from an active branch key. It uses a [key derivation](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-108r1.pdf) in counter mode with a pseudorandom function with HMAC SHA-256 to derive the 32 byte wrapping key with the following inputs.
+ A 16 byte random salt
+ The active branch key
+ The [UTF-8 encoded](https://en.wikipedia.org/wiki/UTF-8) value for the key provider identifier "aws-kms-hierarchy"

The Hierarchical keyring uses the derived wrapping key to encrypt a copy of the plaintext data key using AES-GCM-256 with a 16 byte authentication tag and the following inputs.
+ The derived wrapping key is used as the AES-GCM cipher key
+ The data key is used as the AES-GCM message
+ A 12 byte random initialization vector (IV) is used as the AES-GCM IV
+ Additional authenticated data (AAD) containing the following serialized values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/hierarchical-keyring-details.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
