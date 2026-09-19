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

<table>
<thead>
  <tr><th>Value</th><th>Length in bytes</th><th>Interpreted as</th></tr>
</thead>
<tbody>
  <tr><td>"aws-kms-hierarchy"</td><td>17</td><td>UTF-8 encoded</td></tr>
  <tr><td>The branch key identifier</td><td>Variable</td><td>UTF-8 encoded</td></tr>
  <tr><td>The branch key version</td><td>16</td><td>UTF-8 encoded</td></tr>
  <tr><td>Encryption context</td><td>Variable</td><td>UTF-8 encoded key value pairs</td></tr>
</tbody>
</table>
