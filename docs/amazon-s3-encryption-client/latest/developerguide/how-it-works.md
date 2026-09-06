---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/how-it-works.html
---

# How the Amazon S3 Encryption Client works
<a name="how-it-works"></a>

**Note**
This documentation describes the Amazon S3 Encryption Client version 3.*x* and newer, which is an independent library. For information about previous versions of the Amazon S3 Encryption Client, see the AWS SDK Developer Guide for your programming language.

The Amazon S3 Encryption Client is designed specifically to protect the data that you store in Amazon S3. The workflows in this section explain how the Amazon S3 Encryption Client encrypts and decrypts your objects.

The Amazon S3 Encryption Client uses envelope encryption to protect your objects. It encrypts each Amazon S3 object under a unique data encryption key. Then it encrypts the data encryption key with a wrapping key that you specify.

Need help with the terminology we use in the Amazon S3 Encryption Client? See [Amazon S3 Encryption Client concepts](concepts.md).

## Encrypt and decrypt with the Amazon S3 Encryption Client
<a name="how-it-works-walkthrough"></a>

The Amazon S3 Encryption Client works as an intermediary between you and Amazon S3 by encrypting your object as you upload it, and decrypting your object as you download it. The following walkthrough specifies an RSA key pair as the wrapping key. For detailed code examples, see the *Examples* topic of your preferred [programming language](programming-languages.md).

1. Specify your wrapping key and create a [keyring](concepts.md#keyring) when you instantiate your client.

1. Encrypt your plaintext object by calling [`PutObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html).

   1. The Amazon S3 Encryption Client provides the encryption materials: one plaintext data key and one copy of that data key encrypted by your wrapping key.

   1. The Amazon S3 Encryption Client uses the plaintext data key to encrypt your object, and then discards the plaintext data key.

   1. The Amazon S3 Encryption Client uploads the encrypted data key and the encrypted object to Amazon S3 as part of the `PutObject` call.

1. Decrypt your encrypted object by calling [`GetObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html).

   1. The Amazon S3 Encryption Client uses your wrapping key to decrypt the encrypted data key.

   1. The Amazon S3 Encryption Client uses the plaintext data key to decrypt the object, discards the plaintext data key, and returns the plaintext object as part of the `GetObject` call.
