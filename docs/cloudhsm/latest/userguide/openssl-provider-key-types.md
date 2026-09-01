---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-provider-key-types.html
---

# Supported key types for OpenSSL Provider for AWS CloudHSM Client SDK 5
<a name="openssl-provider-key-types"></a>

The AWS CloudHSM OpenSSL Provider supports the following key types with Client SDK 5.

| Key Type | Description |
| --- | --- |
| RSA | RSA sign/verify and asymmetric encryption operations. Verification is offloaded to OpenSSL software. To generate RSA keys that are interoperable with the OpenSSL Provider, see [Export an asymmetric key with CloudHSM CLI](cloudhsm_cli-key-generate-file.md). |
| EC | ECDSA sign/verify for P-256, P-384, and P-521 curves. Verification is offloaded to OpenSSL software. To generate EC keys that are interoperable with the OpenSSL Provider, see [Export an asymmetric key with CloudHSM CLI](cloudhsm_cli-key-generate-file.md). |
| Ed25519 | EdDSA sign/verify operations using Curve25519 (RFC 8032). Verification is offloaded to OpenSSL software. Ed25519 is only available on non-FIPS clusters. To generate Ed25519 keys that are interoperable with the OpenSSL Provider, see [Export an asymmetric key with CloudHSM CLI](cloudhsm_cli-key-generate-file.md). |
| ML-DSA-44, ML-DSA-65, ML-DSA-87 | Post-quantum digital signature sign/verify operations as defined in FIPS 204. Verification is offloaded to OpenSSL software. ML-DSA requires OpenSSL 3.5 or later. To generate ML-DSA keys that are interoperable with the OpenSSL Provider, see [Export an asymmetric key with CloudHSM CLI](cloudhsm_cli-key-generate-file.md). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
