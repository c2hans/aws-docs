---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-operations.html
---

# Data operations
<a name="data-operations"></a>

After you have established an AWS Payment Cryptography key, it can be used to perform cryptographic operations. Different operations perform different types of activity ranging from encryption, hashing as well as domain specific algorithms such as CVV2 generation.

Encrypted data cannot be decrypted without the matching decryption key (the symmetric key or private key depending on the encryption type). Hashing and domain specific algorithms similarly cannot be verified without the symmetric key or public key.

For information on valid key types for specific operations please see [Valid keys for cryptographic operations](crypto-ops-validkeys-ops.md)

**Note**
We recommend using test data when in a non-production environment. Using production keys and data (PAN, BDK ID, etc.) in a non-production environment may impact your compliance scope such as for PCI DSS and PCI P2PE.

**Topics**
+ [Encrypt, Decrypt and Re-encrypt data](crypto-ops.encryptdecrypt.md)
+ [Generate and verify card data](crypto-ops-carddata.md)
+ [Generate, translate and verify PIN data](data-operations.pindata.md)
+ [Generate and verify ARQC](data-operations.arqc.md)
+ [Generate and verify MAC](crypto-ops-mac.md)
+ [Valid keys for cryptographic operations](crypto-ops-validkeys-ops.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
