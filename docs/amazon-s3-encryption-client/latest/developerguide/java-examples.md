---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/java-examples.html
---

# Amazon S3 Encryption Client for Java examples
<a name="java-examples"></a>

The following examples show you how to use the Amazon S3 Encryption Client for Java to encrypt and decrypt Amazon S3 objects. These examples show how to use version 4.*x* of the Amazon S3 Encryption Client for Java. For more detailed examples, see the [amazon-s3-encryption-client-java](https://github.com/aws/amazon-s3-encryption-client-java/tree/main/src/examples/java/software/amazon/encryption/s3/examples) GitHub repository.

**Topics**
+ [Instantiating the Amazon S3 Encryption Client](#java-instantiate-client)
+ [Encrypting and decrypting Amazon S3 objects](#java-encrypt-example)
+ [Ranged GET requests](#ranged-gets)
+ [Multipart upload](#multipart-upload)

## Instantiating the Amazon S3 Encryption Client
<a name="java-instantiate-client"></a>

After [installing the Amazon S3 Encryption Client for Java](java.md#java-installation), you are ready to instantiate your client and begin encrypting and decrypting your Amazon S3 objects. If you have encrypted objects under a previous version of the Amazon S3 Encryption Client, you may need to enable legacy decryption modes when you instantiate the updated client. For more information, see [Migrating to version 3.*x* of the Amazon S3 Encryption Client for Java](java-v3-migration.md).

With version 3.*x* or later of the Amazon S3 Encryption Client for Java, you can instantiate your client specifying the builder parameter that identifies your [wrapping key](concepts.md#wrapping-key). The Amazon S3 Encryption Client supports the following wrapping keys: symmetric [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys), Raw AES-GCM keys, and Raw RSA keys. Then, the Amazon S3 Encryption Client automatically configures a keyring based on the wrapping key type with default settings and a default cryptographic materials manager (CMM). If you want to customize your client, you can also [manually configure your keyring](#java-instantiate-client-manually).

**Note**
If you use Raw RSA or Raw AES-GCM wrapping keys, you are responsible for generating, storing, and protecting the key material, preferably in a hardware security module (HSM) or key management system.

The following examples instantiate the Amazon S3 Encryption Client with the default decryption mode. This means that all objects will be decrypted using the fully supported buffered decryption mode. For more information, see [Decryption modes (Version 3.*x* and later)](encryption-algorithms.md#decryption-modes).

**Topics**
+ [AWS KMS wrapping key](#java-instantiate-kms-wrapping-key)
+ [Raw AES wrapping key](#java-instantiate-raw-aes-wrapping-key)
+ [Raw RSA wrapping key](#java-instantiate-raw-rsa-wrapping-key)
+ [Manually instantiate the client](#java-instantiate-client-manually)

### AWS KMS wrapping key
<a name="java-instantiate-kms-wrapping-key"></a>

To specify a KMS key as your wrapping key, instantiate your client with the `kmsKeyId` builder parameter.

To use a KMS key as your wrapping key, you need [kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) and [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) permissions on the KMS key. The value of the `kmsKeyId` parameter can be any valid KMS key identifier. For details, see [Key identifiers](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *AWS Key Management Service Developer Guide*.

```
// v4

class v4KMSKeyExample {
    public static void main(String[] args) {
        S3Client v4Client = S3EncryptionClient.builderV4()
                .kmsKeyId({{kmsKeyId}})
                .build();
    }
}
```

### Raw AES wrapping key
<a name="java-instantiate-raw-aes-wrapping-key"></a>

To specify a Raw AES key (`javax.crypto.SecretKey`) as your wrapping key, instantiate your client with the `aesKey` builder parameter.

```
// v4

class v4AESKeyExample {
    public static void main(String[] args) {
        S3Client v4Client = S3EncryptionClient.builderV4()
                .aesKey({{aesKey}})
                .build();
    }
}
```

### Raw RSA wrapping key
<a name="java-instantiate-raw-rsa-wrapping-key"></a>

To specify a Raw RSA key (`java.security.KeyPair`) as your wrapping key, instantiate your client with the `rsaKeyPair` builder parameter. You can specify an entire RSA key pair or a partial RSA key pair. The value of the `rsaKeyPair` parameter must include both the public and private keys in the key pair to perform both encrypt and decrypt operations. You can specify the public key to enable the Amazon S3 Encryption Client to perform encrypt operations, or the private key to enable decrypt operations as needed. By specifying a partial key pair you can limit the exposure of your keys. For examples using a partial key pair, see the [amazon-s3-encryption-client-java](https://github.com/aws/amazon-s3-encryption-client-java/tree/main/src/examples/java/software/amazon/encryption/s3/examples/PartialKeyPairExample.java) GitHub repository.

------
#### [ RSA key pair ]

To instantiate version 3.*x* of the client to perform both encrypt and decrypt operations, specify both the public and private keys of your key pair.

```
// v4

class v4RSAKeyPairExample {
    public static void main(String[] args) {
        S3Client v4Client = S3EncryptionClient.builderV4()
                .rsaKeyPair({{rsaKeyPair}})
                .build();
    }
}
```

------
#### [ Public key ]

To instantiate the client to encrypt only, specify the **public key**. If you specify the public key alone, all `GetObject` calls will fail because the private key is required to decrypt.

```
// v4

class v4RSAKeyPairExample {
    public static void main(String[] args) {
        S3Client v4Client = S3EncryptionClient.builderV4()
                .rsaKeyPair(new PartialRsaKeyPair(null, {{rsaKeyPair}}.getPublic()))
                .build();
    }
}
```

------
#### [ Private key ]

To instantiate the client to decrypt only, specify the **private key**. If you specify the private key alone, all `PutObject` calls will fail because the public key is required to encrypt.

```
// v4

class v4RSAKeyPairExample {
    public static void main(String[] args) {
        S3Client v4Client = S3EncryptionClient.builderV4()
                .rsaKeyPair(new PartialRsaKeyPair({{rsaKeyPair}}.getPrivate(), null))
                .build();
    }
}
```

------

### Manually instantiate the client
<a name="java-instantiate-client-manually"></a>

If you want to customize your client, you can manually configure your own keyring and cryptographic materials manager (CMM). The following example manually configures an AWS KMS keyring using a symmetric encryption AWS KMS wrapping key and passes the custom AWS KMS client to the Amazon S3 Encryption Client.

```
// v4
class v4CustomKeyringExample {
    public static void main(String[] args) {
        KmsKeyring keyring = KmsKeyring.builder()
            .wrappingKeyId({{KMS_KEY_ID}})
            .kmsClient({{customKmsClient}})
            .build();

        CryptographicMaterialsManager cmm = DefaultCryptoMaterialsManager.builder()
            .keyring(keyring)
            .build();

        S3Client v4Client = S3EncryptionClient.builderV4()
            .cryptoMaterialsManager(cmm)
            .build();
    }
}
```

## Encrypting and decrypting Amazon S3 objects
<a name="java-encrypt-example"></a>

The following example shows you how to use the Amazon S3 Encryption Client for Java to encrypt and decrypt Amazon S3 objects.

This example uses a Raw RSA wrapping key and instantiates the Amazon S3 Encryption Client with the default decryption mode.

1. Specify your wrapping key by passing it to the Amazon S3 Encryption Client when you [instantiate your client](#java-instantiate-client). The Amazon S3 Encryption Client for Java automatically configures a [keyring](concepts.md#keyring) based on the wrapping key you specify.

   ```
   // v4

   class v4RSAKeyPairExample {
       public static void main(String[] args) {
           S3Client v4Client = S3EncryptionClient.builderV4()
                   .rsaKeyPair({{rsaKeyPair}})
                   .build();
       }
   }
   ```

1. Encrypt your plaintext object by calling [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html).

   1. The Amazon S3 Encryption Client provides the encryption materials: one plaintext data key and one copy of that data key encrypted by your wrapping key.

   1. The Amazon S3 Encryption Client uses the plaintext data key to encrypt your object, and then discards the plaintext data key.

   1. The Amazon S3 Encryption Client uploads the encrypted data key and the encrypted object to Amazon S3 as part of the `PutObject` call.

   ```
   // v4

   class v4EncryptExample {
       public static void main(String[] args) {
           s3Client.putObject(PutObjectRequest.builder()
                           .bucket({{bucket}})
                           .key({{objectKey}})
                           .build(), RequestBody.fromString({{objectContent}}));
       }
   }
   ```

1. Decrypt your encrypted object by calling [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html).

   1. The Amazon S3 Encryption Client uses your wrapping key to decrypt the encrypted data key.

   1. The Amazon S3 Encryption Client uses the plaintext data key to decrypt the object, discards the plaintext data key, and returns the plaintext object as part of the `GetObject` call.

   ```
   // v4

   class v4DecryptExample {
       public static void main(String[] args) {
           ResponseBytes<GetObjectResponse> objectResponse = s3Client.getObjectAsBytes(builder -> builder
                   .bucket({{bucket}})
                   .key({{objectKey}}));
           String output = objectResponse.asUtf8String();
       }
   }
   ```
**Note**
The default decryption mode cannot decrypt objects larger than 64 MB. This decryption mode automatically buffers stream contents into memory to prevent the release of unauthenticated objects. If you attempt to decrypt an object larger than 64 MB, you will receive an exception directing you to enable the delayed authentication decryption mode. For more information, see [Decryption modes](encryption-algorithms.md#decryption-modes).

1. Optional: verify that the decrypted object matches the original plaintext object that you uploaded.

   ```
   assert output.equals({{objectContent}});
   ```

1. The Amazon S3 Encryption Client implements the `AutoClosable` interface, which automatically calls `close()` when you exit a `try-with-resources` block for which the object has been declared in the resource specification header. As a best practice, you should either use `try-with-resources` or explicitly call the `close()` method.

   ```
   s3Client.close();
   ```

## Ranged GET requests
<a name="ranged-gets"></a>

With Amazon S3, you can download a specific part of an object by performing a ranged GET request. In version 3.*x* and later of the Amazon S3 Encryption Client, you must explicitly enable the [unauthenticated legacy decryption mode](encryption-algorithms.md#legacy-decryption-mode) to perform ranged requests.

By default, version 4.*x* of the Amazon S3 Encryption Client encrypts and decrypts your objects using the AES-GCM with key commitment algorithm suite. However, you can enable it to use the legacy AES-CTR algorithm to partially decrypt your object during a ranged GET request. The Amazon S3 Encryption Client cannot use AES-GCM for ranged gets because it is an authenticated scheme that appends an authentication tag to the encrypted object. When you request a partial object, the client cannot read the entire object stream to reach the authenticated tag. This means that the partial object is not authenticated.

### Specifying a range
<a name="specify-ranged-request"></a>

You can include the `Range` parameter in your `GetObject` request to download and decrypt a specific byte-range from an object. The start and end indices of the byte range are included in the partial object. The byte-range you specify should reflect to the following format:

```
range("bytes={{startIndex}}–{{endIndex}}")
```

The following list details how the Amazon S3 Encryption Client responds to ranged requests that specify an invalid byte-range. For more detailed examples, see the [amazon-s3-encryption-client-java](https://github.com/aws/amazon-s3-encryption-client-java/tree/main/src/examples/java/software/amazon/encryption/s3/examples) GitHub repository.
+ When the start index is within object range but the end index is greater than the object's total length, the Amazon S3 Encryption Client returns the object from the start index to the end of the original plaintext object.
+ When the start index is greater than the end index, the Amazon S3 Encryption Client returns the entire object.
+ When the range is specified with an invalid format, the Amazon S3 Encryption Client returns the entire object.

  For example, if the range was specified as `range("10-20")`, instead of `range("bytes=10-20")`, then the Amazon S3 Encryption Client will return the entire object.
+ When both the start and end indicies are greater than the original plaintext object's total length, but still within the same cipher block, the Amazon S3 Encryption Client returns an empty object.
+ When both the start and end indicies are greater than the original plaintext object's total length, and are outside of the object's cipher block, the `GetObject` request fails.

#### Performing a ranged request
<a name="ranged-request-example"></a>

The following walkthrough explains how to perform a ranged request when using version 4.*x* of the Amazon S3 Encryption Client.

1. Enable ranged gets by specifying the `enableLegacyUnauthenticatedModes` parameter when you instantiate your client.

   The following example specifies a raw AES key as the wrapping key.

   ```
   // v4

   class v4EnableRangedGetsExample {
       public static void main(String[] args) {
           S3Client v4Client = S3EncryptionClient.builderV4()
                   .aesKey({{aesKey}})
                   .enableLegacyUnauthenticatedModes({{true}})
                   .build();
       }
   }
   ```

1. Partially decrypt your encrypted object by specifying the byte-range in your [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) request.

   The following example specifies a start index at byte 10 and end index at byte 20.

   ```
   // v4

   class v4RangedGetExample {
       public static void main(String[] args) {
           ResponseBytes<GetObjectResponse> objectResponse = v4Client.getObjectAsBytes(builder -> builder
                   .bucket({{bucket}})
                   .range("bytes={{10-20}}")
                   .key({{objectKey}}));
           String output = objectResponse.asUtf8String();
       }
   }
   ```

1. Optional: verify that the decrypted partial object matches the original plaintext object that you uploaded at the same range.

   ```
   assert output.equals({{objectContent}});
   ```

1. The Amazon S3 Encryption Client implements the `AutoClosable` interface, which automatically calls `close()` when you exit a `try-with-resources` block for which the object has been declared in the resource specification header. As a best practice, you should either use `try-with-resources` or explicitly call the `close()` method.

   ```
   s3Client.close();
   ```

## Multipart upload
<a name="multipart-upload"></a>

Amazon S3 allows you to upload a single object as a set of parts using [multipart uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html). Amazon S3 recommends that when your object size reaches 100 MB, you should consider using multipart uploads. In version 3.*x* or later of the Amazon S3 Encryption Client, you can perform multipart uploads with the low-level API or the high-level API. Use the low-level API when you need to vary part sizes during the upload or require more control over the multipart upload process. Use the high-level API to simplify the multipart upload process by enabling the Amazon S3 Encryption Client to automatically perform multipart uploads.

### Multipart Upload (high-level API)
<a name="highlevel-multipart-upload"></a>

When you use the high-level API, the Amazon S3 Encryption Client automatically performs multipart uploads for all objects larger than 5 MB. The Amazon S3 Encryption Client encrypts the object locally and then calls the [AWS CRT-based Amazon S3 client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/crt-based-s3-client.html) to perform the multipart upload to Amazon S3.

**Note**
If your permissions to access required Amazon S3 resources or KMS keys are revoked during a multipart upload using the high-level API, the in-progress request may upload successfully. Subsequent multipart upload requests will fail.

To enable automatic multipart uploads with the high-level API, you must add dependencies for the AWS CRT-based Amazon S3 client to your Maven project file and specify the `enableMultipartPutObject` parameter when you instantiate your client.

------
#### [ Add dependencies ]

To use the AWS CRT-based Amazon S3 client with the Amazon S3 Encryption Client, add the following two dependencies. For more information on creating dependencies and installing the Amazon S3 Encryption Client, see [Installing the Amazon S3 Encryption Client for Java](java.md#java-installation).

```
<dependency>
  <groupId>software.amazon.awssdk</groupId>
  <artifactId>s3</artifactId>
  <version>2.19.3
<dependency>
  <groupId>software.amazon.awssdk.crt</groupId>
  <artifactId>aws-crt</artifactId>
  <version>0.21.5</version>
</dependency>
```

------
#### [ Enable multipart upload ]

To enable the Amazon S3 Encryption Client to automatically perform multipart uploads, specify the `enableMultipartPutObject` parameter when you instantiate your client.

The following example specifies a raw AES key as the wrapping key.

```
// v4

class v4EnableMultipartUploadExample {
    public static void main(String[] args) {
        S3Client v4Client = S3EncryptionClient.builderV4()
                .aesKey({{aesKey}})
                .enableMultipartPutObject({{true}})
                .build();
    }
}
```

------

### Multipart Upload (low-level API)
<a name="lowlevel-multipart-upload"></a>

The Amazon S3 Encryption Client does not require any additional configuration to use the low-level API. Use the following API calls to generate a multipart upload request with version 4.*x* of the Amazon S3 Encryption Client.

1. Start the multipart upload process by calling [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html).

1. Call [https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html) to upload each part of your object. When you upload the final part, you must specify `isLastPart` for the Amazon S3 Encryption Client to be able to call `cipher.doFinal()`

   ```
   // v4

   class v4UploadFinalPartExample {
       public static void main(String[] args) {
            UploadPartRequest uploadPartRequest = UploadPartRequest.builder()
                       .bucket({{bucket}})
                       .key({{objectKey}})
                       .uploadId(initiateResult.uploadId())
                       .partNumber(partsSent)
                       .overrideConfiguration(isLastPart({{true}}))
                       .build();
       }
   }
   ```

1. Call [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html) to finish the process.
