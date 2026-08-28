---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/using-s3ec-async.html
---

# Asynchronous programming in the Amazon S3 Encryption Client for Java
<a name="using-s3ec-async"></a>

Version 3.*x* and later of the Amazon S3 Encryption Client provides a nonblocking asynchronous client that implements high concurrency across a few threads. The asynchronous client enables you to perform requests sequentially without waiting to view results between each request.

The default Amazon S3 Encryption Client uses synchronous methods that block your thread’s execution until the client receives a response from Amazon S3. The asynchronous client returns immediately, giving control back to the calling thread without waiting for a response. Because an asynchronous method returns before a response is available, you need a way to get the response when it’s ready. The methods in version 4.*x* of the Amazon S3 Encryption Client return *CompletableFuture objects* that allow you to access the response when it’s ready.

**Topics**
+ [Instantiating the asynchronous client](#instantiate-async-client)
+ [Encrypt and decrypt with the asynchronous client](#async-example)

## Instantiating the asynchronous client
<a name="instantiate-async-client"></a>

To use the asynchronous client, you must specify the `S3AsyncEncryptionClient` builder and the builder parameter that identifies your [wrapping key](concepts.md#wrapping-key) when you instantiate your client. The Amazon S3 Encryption Client supports the following wrapping keys: symmetric [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys), raw AES-GCM keys, and raw RSA keys.

**Note**
If you use Raw RSA or Raw AES-GCM wrapping keys, you are responsible for generating, storing, and protecting the key material, preferably in a hardware security module (HSM) or key management system.

The following examples instantiate the asynchronous Amazon S3 Encryption Client with the default decryption mode. This means that all objects will be decrypted using the fully supported buffered decryption mode. For more information, see [Decryption modes (Version 3.*x* and later)](encryption-algorithms.md#decryption-modes).

------
#### [ KMS key ]

To specify a KMS key as your wrapping key, instantiate your client with the `kmsKeyId` builder parameter. The value of the `kmsKeyId` parameter can be any valid KMS key identifier. For details, see [Key identifiers](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *AWS Key Management Service Developer Guide*.

```
// v4

class v4KMSKeyExample {
    public static void main(String[] args) {
        S3AsyncClient v4Client = S3AsyncEncryptionClient.builderV4()
                .kmsKeyId({{kmsKeyId}})
                .build();
    }
}
```

------
#### [ Raw AES key ]

To specify a raw AES key (`javax.crypto.SecretKey`) as your wrapping key, instantiate your client with the `aesKey` builder parameter.

```
// v4

class v4AESKeyExample {
    public static void main(String[] args) {
        S3AsyncClient v4Client = S3AsyncEncryptionClient.builderV4()
                .aesKey({{aesKey}})
                .build();
    }
}
```

------
#### [ Raw RSA key ]

To specify a raw RSA key (`java.security.KeyPair`) as your wrapping key, instantiate your client with the `rsaKeyPair` builder parameter. You can specify an entire RSA key pair or a partial RSA key pair. The value of the `rsaKeyPair` parameter must include both the public and private keys in the key pair to perform both encrypt and decrypt operations. You can specify the public key to enable the Amazon S3 Encryption Client to perform encrypt operations, or the private key to enable decrypt operations as needed. By specifying a partial key pair you can limit the exposure of your keys. For examples using a partial key pair, see the [amazon-s3-encryption-client-java](https://github.com/aws/amazon-s3-encryption-client-java/tree/main/src/examples/java/software/amazon/encryption/s3/examples/PartialKeyPairExample.java) GitHub repository.

To instantiate version 4.*x* of the client to perform both encrypt and decrypt operations, specify both the public and private keys of your key pair.

```
// v4

class v4RSAKeyPairExample {
    public static void main(String[] args) {
        S3AsyncClient v4Client = S3AsyncEncryptionClient.builderV4()
                .rsaKeyPair({{rsaKeyPair}})
                .build();
    }
}
```

To instantiate the client to encrypt only, specify the **public key**. If you specify the public key alone, all `GetObject` calls will fail because the private key is required to decrypt.

```
// v4

class v4RSAKeyPairExample {
    public static void main(String[] args) {
        S3AsyncClient v4Client = S3AsyncEncryptionClient.builderV4()
                .rsaKeyPair(new PartialRsaKeyPair(null, {{rsaKeyPair}}.getPublic()))
                .build();
    }
}
```

To instantiate the client to decrypt only, specify the **private key**. If you specify the private key alone, all `PutObject` calls will fail because the public key is required to encrypt.

```
// v4

class v4RSAKeyPairExample {
    public static void main(String[] args) {
        S3AsyncClient v4Client = S3AsyncEncryptionClient.builderV4()
                .rsaKeyPair(new PartialRsaKeyPair({{rsaKeyPair}}.getPrivate(), null))
                .build();
    }
}
```

------

You can customize your asynchronous client by specifying different builder parameters to enable the features you need. By default, version 4.*x* of the Amazon S3 Encryption Client does not support [legacy decryption](encryption-algorithms.md#legacy-decryption-mode), [ranged 'GET' requests](java-examples.md#ranged-gets), or [multipart uploads](java-examples.md#multipart-upload) (via the high-level API).

For example, if you need to decrypt data keys that were encrypted with a legacy wrapping algorithm, specify the [`enableLegacyWrappingAlgorithms`](java-v3-migration.md#enable-legacy-v2-v3) parameter when you instantiate your client. The following example specifies a raw AES key as the wrapping key.

```
// v4

class v4EnableLegacyModesAsyncClientExample {
    public static void main(String[] args) {
        S3AsyncClient v4Client = S3AsyncEncryptionClient.builderV4()
                .aesKey(AES_KEY)
                .enableLegacyWrappingAlgorithms({{true}})
                .build();
    }
}
```

## Encrypt and decrypt with the asynchronous client
<a name="async-example"></a>

The following walkthrough demonstrates how encrypt and decrypt asynchronously with version 4.*x* of the Amazon S3 Encryption Client.

1. Instantiate your asynchronous client with the `S3AsyncEncryptionClient` builder.

   The following example specifies a raw AES key as the wrapping key.

   ```
   // v4

   class v4EnableAsyncClientExample {
       public static void main(String[] args) {
           S3AsyncClient v4Client = S3AsyncEncryptionClient.builderV4()
                   .aesKey(AES_KEY)
                   .build();
       }
   }
   ```

1. Call [`PutObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) to encrypt a plaintext object and upload it to Amazon S3.

   The asynchronous client stores the response to confirm that the `PutObject` request completed when you call `GetObject` in the future.

   ```
   // v4

   class v4PutObjectAsyncClientExample {
       public static void main(String[] args) {
           CompletableFuture<PutObjectResponse> futurePut = v4AsyncClient.putObject(builder -> builder
                   .bucket({{bucket}})
                   .key({{objectKey}})
                   .build(), AsyncRequestBody.fromString({{objectContent}}));
           // Block on completion of the futurePut
           futurePut.join();
       }
   }
   ```

1. Call [`GetObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) to download and decrypt the encrypted object.

   ```
   // v4

   class v4GetObjectAsyncClientExample {
       public static void main(String[] args) {
            CompletableFuture<ResponseBytes<GetObjectResponse>> futureGet = v4AsyncClient.getObject(builder -> builder
                   .bucket({{bucket}})
                   .key({{objectKey}})
                   .build(), AsyncResponseTransformer.toBytes());
           // Wait for the future to complete
           ResponseBytes<GetObjectResponse> getResponse = futureGet.join();
       }
   }
   ```

1. Optional: verify that the decrypted object matches the original plaintext object that you uploaded.

   ```
   assert output.equals({{objectContent}});
   ```

1. The Amazon S3 Encryption Client implements the `AutoClosable` interface, which automatically calls `close()` when you exit a `try-with-resources` block for which the object has been declared in the resource specification header. As a best practice, you should either use `try-with-resources` or explicitly call the `close()` method.

   ```
   s3Client.close();
   ```

**Note**
The default decryption mode cannot decrypt objects larger than 64 MB. This decryption mode automatically buffers stream contents into memory to prevent the release of unauthenticated objects. If you attempt to decrypt an object larger than 64 MB, you will receive an exception directing you to enable the delayed authentication decryption mode. For more information, see [Decryption modes](encryption-algorithms.md#decryption-modes).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon S3 Encryption Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-s3-encryption-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
