---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-encryption-migration-v2-v3.html
---

# Amazon S3 Encryption Client Migration (V2 to V3) in the AWS SDK for PHP Version 3
<a name="s3-encryption-migration-v2-v3"></a>

**Note**
If you are using Version 1 (V1) of the Amazon S3 encryption client, you must first migrate to Version 2 (V2) before migrating to Version 3 (V3). See [Amazon S3 Encryption Client Migration (V1 to V2) in the AWS SDK for PHP Version 3](s3-encryption-migration-v1-v2.md).

This topic shows how to migrate your applications from Version 2 (V2) of the Amazon Simple Storage Service (Amazon S3) encryption client to Version 3 (V3), and ensure application availability throughout the migration process. Version 3 introduces AES GCM with Key Commitment and Commitment Policies to enhance security and protect against data key tampering.

## Migration overview
<a name="s3-encryption-migration-v2-v3-overview"></a>

This migration happens in two phases:

1. **Update existing clients to read new formats.** First, deploy an updated version of the AWS SDK for PHP to your application. This allows existing V2 encryption clients to decrypt objects written by the new V3 clients. If your application uses multiple AWS SDKs, you must upgrade each SDK separately.

2. **Migrate encryption and decryption clients to V3.** Once all of your V2 encryption clients can read new formats, you can migrate your existing encryption and decryption clients to their respective V3 versions.

## Understanding V3 concepts
<a name="s3-encryption-migration-v2-v3-concepts"></a>

Version 3 of the Amazon S3 encryption client introduces two key security enhancements: Commitment Policies and the AES GCM with Key Commitment algorithm. Understanding these concepts is essential for a successful migration.

### Commitment Policy
<a name="s3-encryption-migration-v2-v3-concepts-commitment-policy"></a>

A Commitment Policy controls how the encryption client handles key commitment during encryption and decryption operations. Version 3 provides three policy options:

`FORBID_ENCRYPT_ALLOW_DECRYPT`
**Encryption behavior:** Encrypts objects without key commitment.
**Decryption behavior:** Allows decryption of objects encrypted with or without key commitment.
**Security implications:** This policy does not enforce key commitment on newly encrypted objects, which may allow data key tampering. Use this policy only during the initial migration phase when you need to maintain compatibility with V2 clients.
**Version compatibility:** Objects encrypted with this policy can be read by all V2 and V3 implementations.

`REQUIRE_ENCRYPT_ALLOW_DECRYPT`
**Encryption behavior:** Encrypts objects with key commitment using the `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` algorithm.
**Decryption behavior:** Allows decryption of objects encrypted with or without key commitment.
**Security implications:** This policy provides enhanced security for newly encrypted objects while maintaining the ability to read existing objects. This is the recommended policy for most migration scenarios.
**Version compatibility:** Objects encrypted with this policy can only be read by V3 and the latest V2 implementations.
**Migration considerations:** Before using this policy, ensure all clients that need to read the encrypted objects have been upgraded to V3 or the latest V2.

`REQUIRE_ENCRYPT_REQUIRE_DECRYPT`
**Encryption behavior:** Encrypts objects with key commitment using the `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` algorithm.
**Decryption behavior:** Only allows decryption of objects encrypted with key commitment. Objects encrypted without key commitment will fail to decrypt.
**Security implications:** This policy provides the highest level of security by enforcing key commitment for both encryption and decryption. Use this policy only after all objects have been migrated to use key commitment.
**Version compatibility:** Only V3 implementations can use this policy. Attempting to decrypt V1 or V2 encrypted objects with this policy will fail.
**Migration considerations:** This policy should only be used after completing the full migration and re-encrypting all existing objects with key commitment.

### AES GCM with Key Commitment
<a name="s3-encryption-migration-v2-v3-concepts-aes-gcm-kc"></a>

The AES GCM with Key Commitment (`ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY`) algorithm is a new encryption algorithm introduced in V3 that provides protection against data key tampering attacks.

**Security enhancement:** `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` protects against data key tampering by cryptographically binding the data key to the encrypted content. This prevents attackers from substituting a different data key during decryption, which could lead to the decryption of unintended data.

**Version compatibility:** Objects encrypted with `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` can only be decrypted by V3 and the lastest V2 implementations of the Amazon S3 encryption client. V1 clients cannot decrypt objects encrypted with this algorithm.

**Important**
**Upgrade requirement:** Before enabling encryption with `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` (by using REQUIRE\_ENCRYPT\_ALLOW\_DECRYPT or REQUIRE\_ENCRYPT\_REQUIRE\_DECRYPT policies), you must ensure that all clients that need to read the encrypted objects have been upgraded to V3. Failure to upgrade all readers will result in decryption failures for objects encrypted with key commitment.

## Update existing clients to read new formats
<a name="s3-encryption-migration-v2-v3-update-clients"></a>

The V3 encryption client uses encryption algorithms and key commitment features that older versions of the client don't support. The first step in the migration is to update your V2 decryption clients to the latest SDK release. After completing this step, your application's V2 clients will be able to decrypt objects encrypted by V3 encryption clients. See details below for each installation method of the AWS SDK for PHP.

### Building and installing the latest SDK version
<a name="s3-encryption-migration-v2-v3-update-clients-sdk"></a>

To complete this migration, you must use the latest version of the `aws/aws-sdk-php` package that includes V3 encryption client support.

 **Installing from Composer**

For projects that were installed using Composer, in the Composer file, update the SDK package to the latest version of the SDK and then run the following command.

```
composer update aws/aws-sdk-php
```

 **Installing Using the Phar or Zip File**

Use one of the following methods. Be sure to place the updated SDK file in the location required by your code, which is determined by the require statement.

For projects that were installed using the Phar file, download the updated file: [`aws.phar`](https://docs.aws.amazon.com/aws-sdk-php/v3/download/aws.phar).

```
<?php
  require '/path/to/aws.phar';
?>
```

For projects that were installed using the Zip file, download the updated file: [``](https://docs.aws.amazon.com/aws-sdk-php/v3/download/aws.zip).

```
<?php
  require '/path/to/aws-autoloader.php';
?>
```

### Building, installing, and deploying applications
<a name="s3-encryption-migration-v2-v3-update-clients-deploy"></a>

After updating the SDK, rebuild and redeploy your application to ensure all components are using the updated version. This step is critical to ensure that your V2 clients can read objects encrypted by V3 clients.

Follow your organization's standard deployment procedures to roll out the updated application. Ensure that all instances of your application are updated before proceeding to migrate your encryption and decryption clients to V3.

After deployment, verify that your application can still decrypt existing objects and that no errors occur during normal operations. This confirms that the SDK update was successful and your application is ready for the next phase of migration.

## Migrate Encryption and Decryption clients to V3
<a name="s3-encryption-migration-v2-v3-migrate"></a>

After updating your clients to read the new encryption formats, you can update your applications to the V3 encryption and decryption clients. The following examples show you how to successfully migrate your code from V2 to V3.

### Using V3 Encryption Clients
<a name="s3-encryption-migration-v2-v3-using-v3-clients"></a>

V3 introduces the `S3EncryptionClientV3` class and `KmsMaterialsProviderV3` to replace the V2 equivalents. The key differences in V3 are:
+ V3 uses `KmsMaterialsProviderV3` (same as V2) but verifies encryption context when decrypting objects in `GetObject` calls.
+ V3 introduces Commitment Policies to control encryption and decryption behavior.

 **Example: Migrating from V2 to V3 with KMS Encryption**

 *Pre-migration (V2)*

```
use Aws\S3\Crypto\S3EncryptionClientV2;
use Aws\S3\S3Client;
use Aws\Crypto\KmsMaterialsProviderV2;
use Aws\Kms\KmsClient;

$encryptionClient = new S3EncryptionClientV2(
   new S3Client([
      'profile' => 'default',
      'region' => 'us-east-1',
      'version' => 'latest',
   ])
);

$kmsKeyId = 'kms-key-id';
$materialsProvider = new KmsMaterialsProviderV2(
   new KmsClient([
      'profile' => 'default',
      'region' => 'us-east-1',
      'version' => 'latest',
   ]),
   $kmsKeyId
);

$bucket = 'the-bucket-name';
$key = 'the-file-name';
$cipherOptions = [
   'Cipher' => 'gcm',
   'KeySize' => 256,
];

$encryptionClient->putObject([
   '@MaterialsProvider' => $materialsProvider,
   '@CipherOptions' => $cipherOptions,
   '@KmsEncryptionContext' => ['context-key' => 'context-value'],
   'Bucket' => $bucket,
   'Key' => $key,
   'Body' => fopen('file-to-encrypt.txt', 'r'),
]);

$result = $encryptionClient->getObject([
   '@KmsAllowDecryptWithAnyCmk' => true,
   '@SecurityProfile' => 'V2_AND_LEGACY',
   '@CommitmentPolicy' => 'FORBID_ENCRYPT_ALLOW_DECRYPT',
   '@MaterialsProvider' => $materialsProvider,
   '@CipherOptions' => $cipherOptions,
   'Bucket' => $bucket,
   'Key' => $key,
]);
```

 *During migration (V3 with backward compatibility)*

```
use Aws\S3\Crypto\S3EncryptionClientV3;
use Aws\S3\S3Client;
use Aws\Crypto\KmsMaterialsProviderV3;
use Aws\Kms\KmsClient;

// Create V3 encryption client
$encryptionClient = new S3EncryptionClientV3(
   new S3Client([
      'profile' => 'default',
      'region' => 'us-east-1',
      'version' => 'latest',
   ])
);

// Create encryption materials
$kmsKeyId = 'kms-key-id';
$materialsProvider = new KmsMaterialsProviderV3(
   new KmsClient([
      'profile' => 'default',
      'region' => 'us-east-1',
      'version' => 'latest',
   ]),
   $kmsKeyId
);

$bucket = 'the-bucket-name';
$key = 'the-file-name';
$cipherOptions = [
   'Cipher' => 'gcm',
   'KeySize' => 256,
];

$encryptionClient->putObject([
   '@MaterialsProvider' => $materialsProvider,
   '@CipherOptions' => $cipherOptions,
   '@CommitmentPolicy' => 'REQUIRE_ENCRYPT_ALLOW_DECRYPT',
   '@KmsEncryptionContext' => ['context-key' => 'context-value'],
   'Bucket' => $bucket,
   'Key' => $key,
   'Body' => fopen('file-to-encrypt.txt', 'r'),
]);

$result = $encryptionClient->getObject([
   '@SecurityProfile' => 'V3_AND_LEGACY',
   '@CommitmentPolicy' => 'REQUIRE_ENCRYPT_ALLOW_DECRYPT',
   '@MaterialsProvider' => $materialsProvider,
   '@CipherOptions' => $cipherOptions,
   'Bucket' => $bucket,
   'Key' => $key,
]);
```

 *Post-migration (V3 with key commitment)*

```
use Aws\S3\Crypto\S3EncryptionClientV3;
use Aws\S3\S3Client;
use Aws\Crypto\KmsMaterialsProviderV3;
use Aws\Kms\KmsClient;

// Create V3 encryption client
$encryptionClient = new S3EncryptionClientV3(
   new S3Client([
      'profile' => 'default',
      'region' => 'us-east-1',
      'version' => 'latest',
   ])
);

// Create encryption materials
$kmsKeyId = 'kms-key-id';
$materialsProvider = new KmsMaterialsProviderV3(
   new KmsClient([
      'profile' => 'default',
      'region' => 'us-east-1',
      'version' => 'latest',
   ]),
   $kmsKeyId
);

$bucket = 'the-bucket-name';
$key = 'the-file-name';
$cipherOptions = [
   'Cipher' => 'gcm',
   'KeySize' => 256,
];

$encryptionClient->putObject([
   '@MaterialsProvider' => $materialsProvider,
   '@CipherOptions' => $cipherOptions,
   // Use the commitment policy (REQUIRE_ENCRYPT_REQUIRE_DECRYPT)
   // This encrypts with key commitment and does not decrypt V2 objects
   '@CommitmentPolicy' => 'REQUIRE_ENCRYPT_REQUIRE_DECRYPT',
   '@KmsEncryptionContext' => ['context-key' => 'context-value'],
   'Bucket' => $bucket,
   'Key' => $key,
   'Body' => fopen('file-to-encrypt.txt', 'r'),
]);

$result = $encryptionClient->getObject([
   '@SecurityProfile' => 'V3',
   // Use the commitment policy (REQUIRE_ENCRYPT_REQUIRE_DECRYPT)
   // This encrypts with key commitment and does not decrypt V2 objects
   '@CommitmentPolicy' => 'REQUIRE_ENCRYPT_REQUIRE_DECRYPT',
   '@MaterialsProvider' => $materialsProvider,
   '@CipherOptions' => $cipherOptions,
   'Bucket' => $bucket,
   'Key' => $key,
]);
```

Key differences in V3:
+ Use `KmsMaterialsProviderV3` instead of `KmsMaterialsProviderV2`
+ The `@KmsEncryptionContext` parameter is still required for `putObject` operations
+ The `@KmsEncryptionContext` parameter is optional for `getObject` operations and will verify that the supplied encryption context matches the one in the object.
+ The `@SecurityProfile` parameter controls which encryption versions can be decrypted. Set to `'V3_AND_LEGACY'` to support reading V1 and V2 encrypted objects during migration
+ The `@CommitmentPolicy` parameter controls the commitment policy for this operation. Set to `'FORBID_ENCRYPT_ALLOW_DECRYPT'` to support reading non commitment encrypted objects during migration

## Additional examples
<a name="s3-encryption-migration-v2-v3-examples"></a>

The following examples demonstrate additional configuration options available in V3 that can help you manage the migration process and control encryption behavior.

### Enabling legacy support
<a name="s3-encryption-migration-v2-v3-examples-legacy"></a>

During migration, you may need to decrypt objects that were encrypted with V1 or V2 of the Amazon S3 encryption client. The `@SecurityProfile` parameter controls which encryption versions your V3 client can decrypt.

**When to use this configuration:** Use the `'V3_AND_LEGACY'` security profile when your application needs to read objects encrypted by V1 or V2 clients. This is common during the migration period when you have a mix of old and new encrypted objects in your buckets.

```
use Aws\S3\Crypto\S3EncryptionClientV3;
use Aws\S3\S3Client;
use Aws\Crypto\KmsMaterialsProviderV3;
use Aws\Kms\KmsClient;

$kmsKeyId = 'kms-key-id';
$materialsProvider = new KmsMaterialsProviderV3(
    new KmsClient([
        'profile' => 'default',
        'region' => 'us-east-1',
        'version' => 'latest',
    ]),
    $kmsKeyId
);

$encryptionClient = new S3EncryptionClientV3(
    new S3Client([
        'profile' => 'default',
        'region' => 'us-east-1',
        'version' => 'latest',
    ])
);

$bucket = 'the-bucket-name';
$key = 'the-file-name';
$cipherOptions = [
    'Cipher' => 'gcm',
    'KeySize' => 256,
];

// Decrypt objects encrypted with V1, V2, or V3
$result = $encryptionClient->getObject([
    '@SecurityProfile' => 'V3_AND_LEGACY',
    '@CommitmentPolicy' => 'REQUIRE_ENCRYPT_ALLOW_DECRYPT',
    '@MaterialsProvider' => $materialsProvider,
    '@CipherOptions' => $cipherOptions,
    'Bucket' => $bucket,
    'Key' => $key,
]);
```

The `@SecurityProfile` parameter accepts the following values:
+ `'V3'` (default): Only decrypt objects encrypted with V3 using key commitment
+ `'V3_AND_LEGACY'`: Decrypt objects encrypted with V1, V2, or V3

**Important**
After completing your migration and re-encrypting all objects with V3, you should remove the `@SecurityProfile` parameter or set it to `'V3'` to ensure maximum security.

### Configuring storage method
<a name="s3-encryption-migration-v2-v3-examples-storage"></a>

The Amazon S3 encryption client can store encryption metadata in two ways: in the object's metadata headers or in a separate instruction file. The `@MetadataStrategy` parameter controls which storage method is used.

**When to use this configuration:** Use `'INSTRUCTION_FILE'` when you need to preserve the original object metadata or when working with objects that have metadata size constraints. Use `'METADATA'` (the default) for simpler deployments where encryption metadata can be stored alongside the object.

```
use Aws\S3\Crypto\S3EncryptionClientV3;
use Aws\S3\S3Client;
use Aws\Crypto\KmsMaterialsProviderV3;
use Aws\Kms\KmsClient;

$kmsKeyId = 'kms-key-id';
$materialsProvider = new KmsMaterialsProviderV3(
    new KmsClient([
        'profile' => 'default',
        'region' => 'us-east-1',
        'version' => 'latest',
    ]),
    $kmsKeyId
);

$encryptionClient = new S3EncryptionClientV3(
    new S3Client([
        'profile' => 'default',
        'region' => 'us-east-1',
        'version' => 'latest',
    ])
);

$bucket = 'the-bucket-name';
$key = 'the-file-name';
$cipherOptions = [
    'Cipher' => 'gcm',
    'KeySize' => 256,
];

// Store encryption metadata in a separate instruction file
$encryptionClient->putObject([
    '@MaterialsProvider' => $materialsProvider,
    '@CipherOptions' => $cipherOptions,
    '@CommitmentPolicy' => 'REQUIRE_ENCRYPT_REQUIRE_DECRYPT',
    '@MetadataStrategy' => 'INSTRUCTION_FILE',
    '@KmsEncryptionContext' => ['context-key' => 'context-value'],
    'Bucket' => $bucket,
    'Key' => $key,
    'Body' => fopen('file-to-encrypt.txt', 'r'),
]);

// Store encryption metadata in object headers (default)
$encryptionClient->putObject([
    '@MaterialsProvider' => $materialsProvider,
    '@CipherOptions' => $cipherOptions,
    '@CommitmentPolicy' => 'REQUIRE_ENCRYPT_REQUIRE_DECRYPT',
    '@MetadataStrategy' => 'METADATA',
    '@KmsEncryptionContext' => ['context-key' => 'context-value'],
    'Bucket' => $bucket,
    'Key' => $key,
    'Body' => fopen('file-to-encrypt.txt', 'r'),
]);
```

The `@MetadataStrategy` parameter accepts the following values:
+ `'METADATA'` (default): Store encryption metadata in the object's metadata headers
+ `'INSTRUCTION_FILE'`: Store encryption metadata in a separate instruction file with the suffix `.instruction`

**Note**
When using `'INSTRUCTION_FILE'`, the AES GCM with Key Commitment algorithm provides additional protection against data key tampering. Objects using `'METADATA'` storage do not benefit from this additional protection.
