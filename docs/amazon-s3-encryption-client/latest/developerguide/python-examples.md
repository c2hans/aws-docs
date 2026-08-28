---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/python-examples.html
---

# Amazon S3 Encryption Client for Python examples
<a name="python-examples"></a>

The following examples show you how to use the Amazon S3 Encryption Client for Python to encrypt and decrypt Amazon S3 objects. These examples show how to use version 4.*x* of the Amazon S3 Encryption Client for Python.

**Note**
The Amazon S3 Encryption Client for Python does not support [asynchronous programming](using-s3ec-async.md) or [ranged GET requests](java-examples.md#ranged-gets). To use these features of the Amazon S3 Encryption Client, you must use the Amazon S3 Encryption Client for Java or another Amazon S3 Encryption Client implementation that supports the feature or features in question.

**Note**
The Amazon S3 Encryption Client for Python supports streaming decryption with [delayed authentication](encryption-algorithms.md#decryption-modes). For more information, see [Streaming decryption](#python-streaming-example).

**Topics**
+ [Instantiating the Amazon S3 Encryption Client](#python-instantiate-client)
+ [Encrypting and decrypting Amazon S3 objects](#python-encrypt-example)
+ [Multipart upload](#python-multipart-upload)
+ [Streaming decryption](#python-streaming-example)

## Instantiating the Amazon S3 Encryption Client
<a name="python-instantiate-client"></a>

After [installing the Amazon S3 Encryption Client for Python](python.md#python-installation), you are ready to instantiate your client and begin encrypting and decrypting your Amazon S3 objects.

The Amazon S3 Encryption Client for Python supports [keyrings](concepts.md#keyring) that use symmetric encryption KMS keys as the wrapping key. The Amazon S3 Encryption Client for Python does not support keyrings that use Raw AES-GCM or Raw RSA wrapping keys. To use Raw AES-GCM or Raw RSA wrapping keys, you must use the Amazon S3 Encryption Client for Java or another Amazon S3 Encryption Client implementation that supports these wrapping key types. For more information, see [Instantiating the Amazon S3 Encryption Client for Java](java-examples.md#java-instantiate-client).

To use a KMS key as your wrapping key, you need [kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) and [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) permissions on the KMS key. To specify a KMS key, use any valid KMS key identifier. For details, see [Key identifiers](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *AWS Key Management Service Developer Guide*.

The following example instantiates the Amazon S3 Encryption Client with the default configuration. By default, the Amazon S3 Encryption Client for Python encrypts using the AES-GCM with key commitment algorithm suite and the `REQUIRE_ENCRYPT_REQUIRE_DECRYPT` commitment policy.

```
import boto3
from s3_encryption import S3EncryptionClient, S3EncryptionClientConfig
from s3_encryption.materials.kms_keyring import KmsKeyring

# Create the boto3 clients
s3_client = boto3.client("s3")
kms_client = boto3.client("kms")

# Create the KMS keyring
keyring = KmsKeyring(kms_client, {{kms_key_id}})

# Create the S3 Encryption Client configuration and client
config = S3EncryptionClientConfig(keyring)
s3ec = S3EncryptionClient(s3_client, config)
```

## Encrypting and decrypting Amazon S3 objects
<a name="python-encrypt-example"></a>

The following example shows you how to use the Amazon S3 Encryption Client for Python to encrypt and decrypt Amazon S3 objects.

1. Create a [keyring](concepts.md#keyring) with a KMS key as your wrapping key when you [instantiate your client](#python-instantiate-client).

   ```
   import boto3
   from s3_encryption import S3EncryptionClient, S3EncryptionClientConfig
   from s3_encryption.materials.kms_keyring import KmsKeyring

   s3_client = boto3.client("s3")
   kms_client = boto3.client("kms")

   keyring = KmsKeyring(kms_client, {{kms_key_id}})
   config = S3EncryptionClientConfig(keyring)
   s3ec = S3EncryptionClient(s3_client, config)
   ```

1. Encrypt your plaintext object by calling [`PutObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html). To include an optional [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html), add an `EncryptionContext` parameter to the `put_object` call.

   1. The Amazon S3 Encryption Client provides the encryption materials: one plaintext data key and one copy of that data key encrypted by your wrapping key.

   1. The Amazon S3 Encryption Client uses the plaintext data key to encrypt your object, and then discards the plaintext data key.

   1. The Amazon S3 Encryption Client uploads the encrypted data key and the encrypted object to Amazon S3 as part of the `PutObject` call.

   ```
   plaintext = "Hello, S3 Encryption Client!"

   s3ec.put_object(
       Bucket={{bucket}},
       Key={{object_key}},
       Body=plaintext,
       EncryptionContext={"ec-key": "ec-value"}  # optional
   )
   ```

1. Decrypt your encrypted object by calling [`GetObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html). If you specified an encryption context during encryption, you must provide the same encryption context during decryption.

   1. The Amazon S3 Encryption Client uses your wrapping key to decrypt the encrypted data key.

   1. The Amazon S3 Encryption Client uses the plaintext data key to decrypt the object, discards the plaintext data key, and returns the plaintext object as part of the `GetObject` call.

   ```
   response = s3ec.get_object(
       Bucket={{bucket}},
       Key={{object_key}},
       EncryptionContext={"ec-key": "ec-value"}  # must match encryption context
   )

   decrypted_plaintext = response["Body"].read().decode("utf-8")
   ```

1. Optional: verify that the decrypted object matches the original plaintext object that you uploaded.

   ```
   assert decrypted_plaintext == plaintext
   ```

## Multipart upload
<a name="python-multipart-upload"></a>

Amazon S3 recommends that when your object size reaches 100 MB, you should consider using [multipart uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html). The Amazon S3 Encryption Client for Python provides two high-level methods that automatically handle encrypted multipart uploads: `upload_file` and `upload_fileobj`.

Both methods automatically split large objects into parts, encrypt each part, and upload them to Amazon S3. If the file is smaller than the multipart threshold (default 8 MB), `upload_file` uses `put_object` instead.

### Uploading a file from disk
<a name="python-upload-file"></a>

Use `upload_file` to encrypt and upload a file from the local file system. You can optionally specify a `multipart_threshold` to control when multipart upload is used, and a `multipart_chunksize` to control the size of each part.

```
import boto3
from s3_encryption import S3EncryptionClient, S3EncryptionClientConfig
from s3_encryption.materials.kms_keyring import KmsKeyring

s3_client = boto3.client("s3")
kms_client = boto3.client("kms")

keyring = KmsKeyring(kms_client=kms_client, kms_key_id={{kms_key_id}})
config = S3EncryptionClientConfig(keyring=keyring)
s3ec = S3EncryptionClient(wrapped_s3_client=s3_client, config=config)

# Upload a file (automatically uses multipart for large files)
s3ec.upload_file(
    {{filename}},
    {{bucket}},
    {{object_key}},
    multipart_threshold=8 * 1024 * 1024,   # optional, default 8 MB
    multipart_chunksize=8 * 1024 * 1024,   # optional, default 8 MB
)
```

### Uploading a file-like object
<a name="python-upload-fileobj"></a>

Use `upload_fileobj` to encrypt and upload a file-like object (any object with a `read()` method) to Amazon S3 via multipart upload. The caller retains ownership of the file object — it will not be closed by this method.

```
import io
import boto3
from s3_encryption import S3EncryptionClient, S3EncryptionClientConfig
from s3_encryption.materials.kms_keyring import KmsKeyring

s3_client = boto3.client("s3")
kms_client = boto3.client("kms")

keyring = KmsKeyring(kms_client=kms_client, kms_key_id={{kms_key_id}})
config = S3EncryptionClientConfig(keyring=keyring)
s3ec = S3EncryptionClient(wrapped_s3_client=s3_client, config=config)

# Upload a file-like object via multipart upload
with open({{filename}}, "rb") as f:
    s3ec.upload_fileobj(
        f,
        {{bucket}},
        {{object_key}},
        multipart_chunksize=8 * 1024 * 1024,  # optional, default 8 MB
    )
```

## Streaming decryption
<a name="python-streaming-example"></a>

By default, the Amazon S3 Encryption Client for Python buffers the entire ciphertext and verifies the authentication tag before releasing any plaintext. This is the safest mode, but requires holding the entire object in memory.

With delayed authentication enabled, plaintext is released incrementally as it is decrypted, before the authentication tag has been verified. This allows processing large files without buffering the entire object in memory.

**Important**
With delayed authentication, plaintext is released before it has been authenticated. An attacker could modify the ciphertext and the client would release tampered plaintext before detecting the modification. Only use this mode when you need to process files too large to buffer in memory and you understand the security implications.
Your application should read the stream to completion. If an error is thrown during the final read due to an invalid authentication tag, your application must discard and invalidate any data that was already processed.

The following walkthrough explains how to use streaming decryption with delayed authentication in the Amazon S3 Encryption Client for Python.

1. Enable delayed authentication by specifying the `enable_delayed_authentication` parameter when you configure your client.

   ```
   import boto3
   from s3_encryption import S3EncryptionClient, S3EncryptionClientConfig
   from s3_encryption.materials.kms_keyring import KmsKeyring

   s3_client = boto3.client("s3")
   kms_client = boto3.client("kms")

   keyring = KmsKeyring(kms_client=kms_client, kms_key_id={{kms_key_id}})

   config = S3EncryptionClientConfig(
       keyring=keyring,
       enable_delayed_authentication=True,
   )
   s3ec = S3EncryptionClient(wrapped_s3_client=s3_client, config=config)
   ```

1. Encrypt and upload your object by calling `upload_file`. This method automatically performs a multipart upload for large files.

   ```
   s3ec.upload_file({{filename}}, {{bucket}}, {{object_key}})
   ```

1. Stream the decrypted object back in chunks. With delayed authentication, plaintext is released incrementally without buffering the entire object in memory.

   ```
   from s3_encryption.exceptions import S3EncryptionClientSecurityError

   response = s3ec.get_object(Bucket={{bucket}}, Key={{object_key}})
   body = response["Body"]

   chunks = []
   try:
       while True:
           chunk = body.read(1024 * 1024)  # Read 1 MB at a time
           if not chunk:
               break
           chunks.append(chunk)

       plaintext = b"".join(chunks)

   except S3EncryptionClientSecurityError:
       # Authentication tag verification failed.
       # Discard any plaintext released before the error.
       raise
   ```

1. Optional: verify that the decrypted content matches the original data.

   ```
   assert plaintext == {{large_data}}
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon S3 Encryption Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-s3-encryption-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
