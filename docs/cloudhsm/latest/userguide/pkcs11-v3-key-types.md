---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-v3-key-types.html
---

# Supported key types for PKCS \#11 library for AWS CloudHSM Client SDK 3
<a name="pkcs11-v3-key-types"></a>

The PKCS \#11 library supports the following key types with AWS CloudHSM Client SDK 3.

| Key Type | Description |
| --- | --- |
| RSA | Generate 2048-bit to 4096-bit RSA keys, in increments of 256 bits. |
| EC | Generate keys with the secp224r1 (P-224), secp256r1 (P-256), secp256k1 (Blockchain), secp384r1 (P-384), and secp521r1 (P-521) curves. |
| AES | Generate 128, 192, and 256-bit AES keys.  |
| DES3 (Triple DES) | Generate 192-bit DES3 keys. See note [1](#pkcs11-v3-key-note) below for an upcoming change. |
| GENERIC\_SECRET | Generate 1 to 64 bytes generic secrets. |
+ [1] In accordance with NIST guidance, this is disallowed for clusters in FIPS mode after 2023. For clusters in non-FIPS mode, it is still allowed after 2023. See [FIPS 140 Compliance: 2024 Mechanism Deprecation](compliance-dep-notif.md#compliance-dep-notif-1) for details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
