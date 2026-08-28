---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/AES_DECRYPT.html
---

# AES\_DECRYPT function
<a name="AES_DECRYPT"></a>

The AES\_DECRYPT function is used for decrypting data using the Advanced Encryption Standard (AES) algorithm.

## Syntax
<a name="AES_DECRYPT-syntax"></a>

```
aes_decrypt(expr, key[, mode[, padding[, aad]]])
```

## Arguments
<a name="AES_DECRYPT-arguments"></a>

 *expr*
The binary value to decrypt.

 *key*
The passphrase to use to decrypt the data.
The passphrase must match the key originally used to produce the encrypted value and be 16, 24, or 32 bytes long.

 *mode*
Specifies which block cipher mode should be used to decrypt messages.
Valid modes: ECB, GCM, CBC.

 *padding*
Specifies how to pad messages whose length isn't a multiple of the block size.
Valid values: PKCS, NONE, DEFAULT.
The DEFAULT padding means PKCS for ECB, NONE for GCM and PKCS for CBC.

 *aad*
Optional additional authenticated data (AAD). Only supported for GCM mode. This can be any free-form input and must be provided for both encryption and decryption.

## Return type
<a name="AES_DECRYPT-return-type"></a>

Returns a decrypted value of *expr* using AES in mode with padding.

## Examples
<a name="AES_DECRYPT-examples"></a>

The following example demonstrates how to use the Spark SQL AES\_ENCRYPT function to securely encrypt a string of data (in this case, the word "Spark") using a specified encryption key. The resulting ciphertext is then Base64-encoded to make it easier to store or transmit.

```
SELECT base64(aes_encrypt('Spark', 'abcdefghijklmnop'));
  4A5jOAh9FNGwoMeuJukfllrLdHEZxA2DyuSQAWz77dfn
```

The following example demonstrates how to use the Spark SQL AES\_DECRYPT function to decrypt data that has been previously encrypted and Base64-encoded. The decryption process requires the correct encryption key and parameters (encryption mode and padding mode) to successfully recover the original plaintext data.

```
SELECT aes_decrypt(unbase64('3lmwu+Mw0H3fi5NDvcu9lg=='), '1234567890abcdef', 'ECB', 'PKCS');
 Spark SQL
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
