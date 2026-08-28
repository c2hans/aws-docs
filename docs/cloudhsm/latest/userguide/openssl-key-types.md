---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-key-types.html
---

# Supported key types for OpenSSL Dynamic Engine for AWS CloudHSM Client SDK 5
<a name="openssl-key-types"></a>

The AWS CloudHSM OpenSSL Dynamic Engine supports the following key types with Client SDK 5.

| Key Type | Description |
| --- | --- |
| EC | ECDSA sign/verify for P-256, P-384, and secp256k1 key types. To generate EC keys that are interoperable with the OpenSSL engine, see [Export an asymmetric key with CloudHSM CLI](cloudhsm_cli-key-generate-file.md). |
| RSA | RSA key generation for 2048, 3072, and 4096-bit keys.RSA sign/verify. Verification is offloaded to OpenSSL software. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
