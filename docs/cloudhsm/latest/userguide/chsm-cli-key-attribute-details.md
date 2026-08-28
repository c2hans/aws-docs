---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/chsm-cli-key-attribute-details.html
---

# Check value in CloudHSM CLI
<a name="chsm-cli-key-attribute-details"></a>

The *check value* in CloudHSM CLI is a 3-byte hash or checksum of a key that is generated when the HSM imports or generates a key. You can also calculate a check value outside of the HSM, such as after you export a key. You can then compare the check value values to confirm the identity and integrity of the key. To get the check value of a key, use [key list](cloudhsm_cli-key-list.md) with the verbose flag.

AWS CloudHSM uses the following standard methods to generate a check value:
+ **Symmetric keys**: First 3 bytes of the result of encrypting a zero-block with the key.
+ **Asymmetric key pairs**: First 3 bytes of the SHA-1 hash of the public key.
+ **HMAC keys**: KCV for HMAC keys is not supported at this time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
