---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/encryption-algorithms.html
---

# Supported encryption algorithms
<a name="encryption-algorithms"></a>

**Note**
This documentation describes the Amazon S3 Encryption Client version 3.*x* and newer, which is an independent library. For information about previous versions of the Amazon S3 Encryption Client, see the AWS SDK Developer Guide for your programming language.

The Amazon S3 Encryption Client supports industry-standard algorithms for encrypting objects and data keys. As our knowledge evolves, we adjust our support for encryption algorithms to ensure that your sensitive data is protected. The following topic provides context on which encryption algorithms are fully supported and the different decryption modes supported in version 3.*x* and later of the Amazon S3 Encryption Client.

**Topics**
+ [Encryption algorithms (Version 3.*x* and later)](#v3-algorithms)
+ [Decryption modes (version 3.*x* and later)](#decryption-modes)
+ [Encryption algorithms (Version 2.*x* and earlier)](#supported-algorithms-older)

## Encryption algorithms (Version 3.*x* and later)
<a name="v3-algorithms"></a>

In versions 3.*x* and later, the Amazon S3 Encryption Client will use fully supported algorithms to encrypt and decrypt objects and data keys. You can enable the Amazon S3 Encryption Client to decrypt objects and data keys with a legacy encryption algorithm, but it will not encrypt with a legacy encryption algorithm. It encrypts only with a fully supported encryption algorithm.

The following tables list the object encryption algorithms and wrapping algorithms that are supported in version 3.*x* of the Amazon S3 Encryption Client. Use these tables to determine if any of your objects or data keys were encrypted with an algorithm that is no longer supported. If you need to decrypt objects or data keys that were encrypted with a legacy algorithm, see [Enable Legacy Decryption Modes](java-v3-migration.md#enable-legacy-v2-v3).

**Encrypting objects** — The following table lists the fully supported (Full) and previously supported (Legacy) encryption algorithms that are used to encrypt objects.

| Algorithm | Algorithm Suite | Support |
| --- | --- | --- |
| AES-GCM | ALG\_AES\_256\_GCM\_IV12\_TAG16\_NO\_KDF | Full |
| AES-GCM with key commitment | ALG\_AES\_256\_GCM\_HKDF\_SHA512\_COMMIT\_KEY | Full |
| AES-CBC | ALG\_AES\_256\_CBC\_IV16\_NO\_KDF | Legacy |

AES-GCM with key commitment is an enhanced version of the standard AES-GCM algorithm that provides additional security through [Key commitment](concepts.md#key-commitment). This algorithm ensures that each encrypted object can only be decrypted to a single plaintext, protecting against attacks where an adversary attempts to decrypt data under multiple keys. The key commitment algorithm adds a cryptographic commitment to the data key in the object's encryption metadata, which is verified during decryption. This provides robustness guarantees that prevent key substitution attacks when reading instruction files. Note that encryption using AES-GCM with key commitment is only available in version V4 and later of the Amazon S3 Encryption Client, and objects encrypted with this algorithm can only be decrypted by V4 and the latest 3.*x* clients.

**Encrypting data keys** — The following table lists the fully supported (Full) and previously supported (Legacy) wrapping algorithms that are used to encrypt the data keys that encrypt your objects. Version 3.*x* of the Amazon S3 Encryption Client uses one of the fully supported wrapping algorithms and the wrapping key you specify to encrypt and decrypt the data keys.

| Algorithm | Support |
| --- | --- |
| AES-GCM | Full |
| AWS KMS (with an encryption context) | Full |
| RSA-OAEP-MGF1 and SHA-1 | Full |
| AES | Legacy |
| AESWrap | Legacy |
| AWS KMS (without an encryption context) | Legacy |
| RSA-OAEP-MGF-1 and SHA-256 | Legacy |
| RSA | Legacy |

**Commitment policy encryption support** — The following table shows which algorithm suites support encryption operations based on commitment policy settings. The commitment policy determines whether encryption operations require key commitment.

| Algorithm Suite | FORBID\_ENCRYPT\_ALLOW\_DECRYPT | REQUIRE\_ENCRYPT\_ALLOW\_DECRYPT | REQUIRE\_ENCRYPT\_REQUIRE\_DECRYPT |
| --- | --- | --- | --- |
| AES-GCM | Yes | No | No |
| AES-GCM with key commitment | No | Yes | Yes |

## Decryption modes (version 3.*x* and later)
<a name="decryption-modes"></a>

Version 3.*x* of the Amazon S3 Encryption Client defines four modes of support for decryption that you can use to enable the client to decrypt objects and data keys with either fully supported or legacy algorithms.

### Fully supported
<a name="fully-supported-decryption-modes"></a>

By default, version 3.*x* of the Amazon S3 Encryption Client encrypts and decrypts your objects using the AES-GCM algorithm suite. AES-GCM is an authenticated scheme. This means that an authentication tag is appended to the encrypted object. The default behavior for versions 1.*x* and 2.*x* allowed streaming decryption of AES-GCM encrypted objects. Because authentication happens at the end of the decryption process, the entire object must be read before the cipher can validate the integrity of it. This allows plaintext objects to be released and used before the authentication tag is validated.

Version 3.*x* of the Amazon S3 Encryption Client supports streaming decryption of AES-GCM encrypted objects, but we recommend using the default decryption mode to prevent the release of unauthenticated plaintext objects.

**Buffered (default)**
By default, version 3.*x* of the Amazon S3 Encryption Client automatically buffers the stream contents into memory as the decrypted object is read to prevent the release of unauthenticated objects. If the client reaches the end of the stream, and the authentication fails, your [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) request will throw an exception and the unauthenticated object will not be returned.
When you use the buffered decryption mode with the Amazon S3 Encryption Client for Java, the default maximum object size that can be decrypted is 64 MB. However, you can use the optional `setBufferSize` parameter to customize the maximum object size that the mode will buffer. You can use the `setBufferSize` parameter to specify any integer between 16 bytes and 64 GB as the maxiumum object size.
The following Java example instantiates the client with a raw AES wrapping key and a maximum object size of 32 MiB.

```
S3Client s3Client = S3EncryptionClient.builderV4()
        .aesKey(aesKey)
        .setBufferSize({{32 * 1024 * 1024}}) // OPTIONAL
        .build();
```
When you use the buffered decryption mode with the Amazon S3 Encryption Client for Go, the default maximum object size that can be decrypted is 63 GiB. You cannot set a custom buffer size with the Amazon S3 Encryption Client for Go. As a result, the buffered decryption mode does not require any additional configuration when you instatiate your client with the Amazon S3 Encryption Client for Go.
The Amazon S3 Encryption Client for Python always buffers the entire object into memory during decryption. As a result, the buffered decryption mode does not require any additional configuration when you instantiate your client with the Amazon S3 Encryption Client for Python.
We recommend that you use the buffered decryption mode whenever possible. Since this is the default mode, you do not need to specify the buffered decryption mode when you instantiate your client.

**Delayed authentication**
The Amazon S3 Encryption Client for Go does not support the delayed authentication mode. To decrypt objects under the delayed authentication mode, you must use the Amazon S3 Encryption Client for Java or Amazon S3 Encryption Client for Python.
The delayed authentication mode also supports streaming decryption of AES-GCM encrypted objects, but it does not buffer or interrupt the stream to prevent unauthenticated objects from being returned. We recommend using the Buffered (default) decryption mode whenever possible. However, you might want to use the delayed authentication mode if you established your own method of buffering the stream while using versions 1.*x* and 2.*x* of the client.
If you use the delayed authentication mode and are processing the plaintext data from the stream before reading to the end, you must account for the *delayed* authentication. Read the entire object to the end before you start using the decrypted object. When using this decryption mode, the Amazon S3 Encryption Client will not authenticate any object until it reaches the end of the stream. You will need to manually roll back any data from the stream if an exception is thrown at the end of the stream.
To enable the delayed authentication mode, specify the `enableDelayedAuthenticationMode` parameter when you instantiate the client.
The following Java example specifies a raw AES key as the wrapping key. This client only encrypts with fully supported algorithms and decrypts using the delayed authentication mode.

```
S3Client s3Client = S3EncryptionClient.builderV4()
        .aesKey(aesKey)
        .commitmentPolicy(CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT)
        .enableDelayedAuthenticationMode({{true}})
        .build();
```
The following Python example enables delayed authentication with a KMS key as the wrapping key.

```
config = S3EncryptionClientConfig(
    keyring=keyring,
    enable_delayed_authentication=True,
)
s3ec = S3EncryptionClient(wrapped_s3_client=s3_client, config=config)
```

### Legacy
<a name="legacy-decryption-mode"></a>

**Legacy wrapping algorithms**
By default, the Amazon S3 Encryption Client uses the wrapping key you specify and one of the fully supported wrapping algorithms to encrypt and decrypt the data keys that encrypt your objects. If you need to decrypt data keys that were encrypted with a legacy wrapping algorithm, you must specify the `enableLegacyWrappingAlgorithms` parameter when you instantiate your client.
The following example specifies a raw AES key as the wrapping key. This client only encrypts with fully supported wrapping algorithms. However, it can decrypt data keys encrypted with fully supported or legacy wrapping algorithms.

```
S3Client s3Client = S3EncryptionClient.builderV4()
        .aesKey(aesKey)
        .commitmentPolicy(CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT)
        .enableLegacyWrappingAlgorithms({{true}})
        .build();
```
The following example creates a keyring that uses a KMS key as the wrapping key and only encrypts with fully supported wrapping algorithms. However, it can decrypt data keys encrypted with fully supported or legacy wrapping algorithms.

```
cmm, err := materials.NewCryptographicMaterialsManager(materials.NewKmsKeyring(kmsClient, {{kmsKeyArn}}, func(options *materials.KeyringOptions) {
    options.EnableLegacyWrappingAlgorithms = {{true}}
})
```
The following example creates a keyring that uses a KMS key as the wrapping key and only encrypts with fully supported wrapping algorithms. However, it can decrypt data keys encrypted with fully supported or legacy wrapping algorithms.

```
keyring = KmsKeyring(kms_client, {{kms_key_id}}, enable_legacy_wrapping_algorithms={{True}})
```

**Unauthenticated legacy object encryption algorithms**
If you need to decrypt objects that were encrypted with a legacy algorithm, or you need to partially decrypt an AES-GCM encrypted object by performing a [ranged request](java-examples.md#ranged-gets), you need to use the unauthenticated legacy mode. The Amazon S3 Encryption Client will decrypt objects with a legacy encryption algorithm, but will use the fully supported AES-GCM algorithm to encrypt any objects that you upload to Amazon S3. The decryption of AES-CBC encrypted objects and ranged requests are considered *unauthenticated* because the algorithms do not provide any form of authentication to ensure the integrity of the object.
To enable the unauthenticated legacy mode, specify the `enableLegacyUnauthenticatedModes` parameter when you instantiate the client.
The following example specifies an AES key as the wrapping key. This client only encrypts with fully supported algorithms. However, it can decrypt objects encrypted with fully supported or legacy algorithms.

```
S3Client s3Client = S3EncryptionClient.builderV4()
        .aesKey(aesKey)
        .commitmentPolicy(CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT)
        .enableLegacyUnauthenticatedModes({{true}})
        .build();
```
The following example creates a cryptographic materials manager that only encrypts with fully supported wrapping algorithms. However, it can decrypt objects encrypted with fully supported or legacy algorithms.

```
client, err := NewS3EncryptionClientV3(s3Client, cmm, func(clientOptions *client.EncryptionClientOptions) {
		clientOptions.EnableLegacyUnauthenticatedModes = {{true}}
	})
	if err != nil {
		// handle error
	}
```
The following example creates a client that only encrypts with fully supported algorithms. However, it can decrypt objects encrypted with fully supported or legacy algorithms.

```
config = S3EncryptionClientConfig(
    keyring,
    commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT,
    enable_legacy_unauthenticated_modes={{True}},
)
s3ec = S3EncryptionClient(s3_client, config)
```
The `enableLegacyUnauthenticatedModes` parameter is designed to be a temporary fix. After you've re-encrypted all of your objects with fully supported algorithms, you can remove it from your code.

### Commitment policy decryption support
<a name="commitment-policy-decryption-support"></a>

The following tables show which algorithm suites support decryption operations based on commitment policy settings and the `enableLegacyUnauthenticatedModes` parameter. The commitment policy determines whether decryption operations require key commitment.

**Decryption support with enableLegacyUnauthenticatedModes=false** — The following table shows decryption support when legacy unauthenticated modes are disabled (default behavior).

| Algorithm Suite | FORBID\_ENCRYPT\_ALLOW\_DECRYPT | REQUIRE\_ENCRYPT\_ALLOW\_DECRYPT | REQUIRE\_ENCRYPT\_REQUIRE\_DECRYPT |
| --- | --- | --- | --- |
| AES-CBC | No | No | No |
| AES-CTR | No | No | No |
| Committing AES-CTR | No | No | No |
| AES-GCM | Yes | Yes | No |
| Committing AES-GCM | Yes | Yes | Yes |

**Decryption support with enableLegacyUnauthenticatedModes=true** — The following table shows decryption support when legacy unauthenticated modes are enabled.

| Algorithm Suite | FORBID\_ENCRYPT\_ALLOW\_DECRYPT | REQUIRE\_ENCRYPT\_ALLOW\_DECRYPT | REQUIRE\_ENCRYPT\_REQUIRE\_DECRYPT |
| --- | --- | --- | --- |
| AES-CBC | Yes | Yes | No |
| AES-CTR | Yes | Yes | No |
| AES-CTR with key commitment | Yes | Yes | Yes |
| AES-GCM | Yes | Yes | No |
| AES-GCM with key commitment | Yes | Yes | Yes |

## Encryption algorithms (Version 2.*x* and earlier)
<a name="supported-algorithms-older"></a>

The following tables list the object encryption and wrapping algorithms that are supported in versions 2.*x* and earlier of the Amazon S3 Encryption Client. Versions 1.x and 2.x of the Amazon S3 Encryption Client are included in the following AWS SDKs.

**Encrypting objects** — The following table lists encryption algorithms that are used to encrypt objects.

| Algorithm | C\+\+ | Go | Java | .NET | PHP v3 | Ruby v2 |
| --- | --- | --- | --- | --- | --- | --- |
| AES-GCM | Full | Full | Full | Full | Full | Full |
| AES-CBC | Legacy | Legacy | Legacy | No | No | Legacy |

**Encrypting data keys** — The following table lists encryption algorithms that are used to encrypt the data keys that were used to encrypt objects.

| Algorithm | C\+\+ | Go | Java | .NET | PHP v3 | Ruby v2 |
| --- | --- | --- | --- | --- | --- | --- |
| AES-ECB  | No | No | Legacy | Legacy | No | Legacy |
| AES-GCM | Full | No | Full | Full | No | Full |
| AESWrap | Legacy | No | Legacy | Legacy | No | Legacy |
| KMS | Legacy | Legacy | Legacy | Legacy | Legacy | Legacy |
| KMS\+context | Full | Full | Full | Full | Full | Full |
| RSA | No | No | Legacy | No | No | Legacy |
| RSA-OAEP-SHA1 | No | No | Full | Full | No | Full |
