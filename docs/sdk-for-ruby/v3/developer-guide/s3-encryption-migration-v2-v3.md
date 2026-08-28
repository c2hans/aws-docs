---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/s3-encryption-migration-v2-v3.html
---

# Amazon S3 Encryption Client Migration (V2 to V3)
<a name="s3-encryption-migration-v2-v3"></a>

**Note**
If you are using V1 of the S3 encryption client, you must first migrate to V2 before migrating to V3. See [Amazon S3 Encryption Client Migration (V1 to V2)](s3-encryption-migration-v1-v2.md) for instructions on migrating from V1 to V2.

This topic shows how to migrate your applications from Version 2 (V2) of the Amazon Simple Storage Service (Amazon S3) encryption client to Version 3 (V3), and ensure application availability throughout the migration process. V3 introduces AES GCM with Key Commitment and Commitment Policies to enhance security and protect against data key tampering.

## Migration Overview
<a name="s3-encryption-migration-v2-v3-overview"></a>

Version 3 of the Amazon S3 encryption client introduces AES GCM with Key Commitment for enhanced security. This new encryption algorithm provides protection against data key tampering and ensures the integrity of encrypted data. The migration to V3 requires careful planning to maintain application availability and data accessibility throughout the process.

This migration happens in two phases:

1. **Update existing clients to read new formats.** First, deploy an updated version of the AWS SDK for Ruby to your application. This will allow existing V2 encryption clients to decrypt objects written by the new V3 clients. If your application uses multiple AWS SDKs, you must upgrade each SDK separately.

2. **Migrate encryption and decryption clients to V3.** Once all of your V2 encryption clients can read new formats, you can migrate your existing encryption and decryption clients to their respective V3 versions. This includes configuring Commitment Policies and updating your code to use the new client configuration options.

If you have not yet migrated from V1 to V2, you must complete that migration first. See [Amazon S3 Encryption Client Migration (V1 to V2)](s3-encryption-migration-v1-v2.md) for detailed instructions on migrating from V1 to V2.

## Understanding V3 Features
<a name="s3-encryption-migration-v2-v3-understanding"></a>

Version 3 of the Amazon S3 encryption client introduces two key security features: Commitment Policies and AES GCM with Key Commitment. Understanding these features is essential for planning your migration strategy and ensuring the security of your encrypted data.

### Commitment Policies
<a name="s3-encryption-migration-v2-v3-commitment-policies"></a>

Commitment Policies control how the encryption client handles key commitment during encryption and decryption operations. Key commitment ensures that encrypted data can only be decrypted with the exact key that was used to encrypt it, protecting against certain types of cryptographic attacks.

The V3 encryption client supports three Commitment Policy options:

 **`FORBID_ENCRYPT_ALLOW_DECRYPT`**

This policy encrypts objects without key commitment and allows decryption of both objects with and without key commitment.
+  **Encryption behavior:** Objects are encrypted without key commitment, using the same algorithm suite as V2.
+  **Decryption behavior:** Can decrypt objects encrypted with or without key commitment.
+  **Security implications:** This policy does not enforce key commitment and may allow tampering. Objects encrypted with this policy do not benefit from the enhanced security protections of key commitment. Use this policy only during migration when you need to maintain compatibility with V2 encryption behavior.
+  **Version compatibility:** Objects encrypted with this policy can be read by all V2 and V3 implementations of the S3 encryption client.

 **`REQUIRE_ENCRYPT_ALLOW_DECRYPT`**

This policy encrypts objects with key commitment and allows decryption of both objects with and without key commitment.
+  **Encryption behavior:** Objects are encrypted with key commitment using AES GCM with Key Commitment.
+  **Decryption behavior:** Can decrypt objects encrypted with or without key commitment, providing backward compatibility.
+  **Security implications:** New objects benefit from key commitment protection, while existing objects without key commitment can still be read. This provides a balance between security and backward compatibility during migration.
+  **Version compatibility:** Objects encrypted with this policy can only be read by the V3 and the latest V2 implementations of the S3 encryption client.

 **`REQUIRE_ENCRYPT_REQUIRE_DECRYPT`**

This policy encrypts objects with key commitment and only allows decryption of objects that were encrypted with key commitment.
+  **Encryption behavior:** Objects are encrypted with key commitment using AES GCM with Key Commitment.
+  **Decryption behavior:** Can only decrypt objects that were encrypted with key commitment. Attempts to decrypt objects without key commitment will fail.
+  **Security implications:** This policy provides the highest level of security by enforcing key commitment for all operations. Use this policy only after all objects have been re-encrypted with key commitment and all clients have been upgraded to V3.
+  **Version compatibility:** Objects encrypted with this policy can only be read by the V3 and the latest V2 implementations of the S3 encryption client. This policy also prevents reading objects encrypted by V2 or V1 clients.

**Note**
When planning your migration, start with `REQUIRE_ENCRYPT_ALLOW_DECRYPT` to maintain backward compatibility while gaining the security benefits of key commitment for new objects. Only move to `REQUIRE_ENCRYPT_REQUIRE_DECRYPT` after all objects have been re-encrypted and all clients have been upgraded to V3.

### AES GCM with Key Commitment
<a name="s3-encryption-migration-v2-v3-aes-gcm-kc"></a>

AES GCM with Key Commitment (`ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY`) is a new encryption algorithm introduced in V3 that provides enhanced security by protecting against data key tampering. Understanding how this algorithm works and when it applies is important for planning your migration.

 **How `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` Differs from Previous Algorithms**

Previous versions of the S3 encryption client used AES CBC or AES GCM without key commitment to encrypt the data key in Instruction Files. `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` adds a cryptographic commitment to the encryption process, which binds the encrypted data to a specific key. This prevents an attacker from tampering with the encrypted data key in the Instruction File and causing the client to decrypt data with an incorrect key.

Without key commitment, it may be possible for an attacker to modify the encrypted data key in an Instruction File such that it decrypts to a different key, potentially allowing unauthorized access or data corruption. `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` prevents this attack by ensuring that the encrypted data key can only decrypt to the original key that was used during encryption.

 **Version Compatibility**

Objects encrypted with `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` can only be decrypted by V3 implementations of the S3 encryption client and certain transition versions of V2 that include support for reading V3 formats. V2 clients without this transition support cannot decrypt Instruction Files encrypted with `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY`.

**Warning**
Before enabling encryption with `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` (by using `REQUIRE_ENCRYPT_ALLOW_DECRYPT` or `REQUIRE_ENCRYPT_REQUIRE_DECRYPT` commitment policies), ensure that all clients that need to read your encrypted objects have been upgraded to V3 or a transition version that supports V3 formats. If any V2 clients without transition support attempt to read objects encrypted with `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY`, decryption will fail.

During migration, you can use the `FORBID_ENCRYPT_ALLOW_DECRYPT` commitment policy to continue encrypting without `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` while still allowing your V3 clients to read objects encrypted with key commitment. This provides a safe migration path where you first upgrade all readers, then switch to encrypting with key commitment.

## Update Existing Clients to Read New Formats
<a name="s3-encryption-migration-v2-v3-update-clients"></a>

The V3 encryption client uses encryption algorithms and key commitment features that V2 clients don't support by default. The first step in the migration is to update your V2 decryption clients to a version of the AWS SDK for Ruby that can read V3 encrypted objects. After completing this step, your application's V2 clients will be able to decrypt objects encrypted by V3 encryption clients.

To read objects encrypted by V3 clients (those using `REQUIRE_ENCRYPT_ALLOW_DECRYPT` or `REQUIRE_ENCRYPT_REQUIRE_DECRYPT` commitment policies), you need to use version 1.93.0 or later of the `aws-sdk-s3` gem. This version includes support for decrypting objects encrypted with AES GCM with Key Commitment.

 **Installing from the Command Line**

For projects that install the `aws-sdk-s3` gem from the command line, use the version option to verify that the minimum version of 1.208.0 is installed.

```
gem install aws-sdk-s3 -v '>= 1.208.0'
```

 **Using Gemfiles**

For projects that use a Gemfile to manage dependencies, set the minimum version of the `aws-sdk-s3` gem to 1.208.0. For example:

```
gem 'aws-sdk-s3', '>= 1.208.0'
```

1. Modify your Gemfile to specify the minimum version.

1. Run `bundle update aws-sdk-s3` to update the gem.

1. To verify your version, run `bundle info aws-sdk-s3`.

**Note**
After updating to the latest version, your existing V2 encryption clients will be able to decrypt objects encrypted by V3 clients. However, they will continue to encrypt new objects using V2 algorithms until you migrate them to V3 as described in the next section.

## Migrate Encryption and Decryption Clients to V3
<a name="s3-encryption-migration-v2-v3-migrate"></a>

After updating your clients to read the new encryption formats, you can update your applications to the V3 encryption and decryption clients. The following steps show you how to successfully migrate your code from V2 to V3.

Before updating your code to use the V3 encryption client, ensure that you have followed the preceding steps and are using the `aws-sdk-s3` gem version 1.93.0 or later.

**Note**
When decrypting with AES-GCM, read the entire object to the end before you start using the decrypted data. This is to verify that the object has not been modified since it was encrypted.

### Configuring V3 Clients
<a name="s3-encryption-migration-v2-v3-configure"></a>

The V3 encryption client introduces new configuration options that control key commitment behavior and backward compatibility. Understanding these options is essential for a successful migration.

 **commitment\_policy**

The `commitment_policy` parameter controls how the encryption client handles key commitment during encryption and decryption operations. This is the most important configuration option for V3 clients.
+  `:require_encrypt_allow_decrypt` - Encrypts new objects with key commitment and allows decryption of objects with or without key commitment. This is the recommended setting for migration, as it provides enhanced security for new objects while maintaining backward compatibility with existing V2 objects.
+  `:forbid_encrypt_allow_decrypt` - Encrypts new objects without key commitment (using V2 algorithms) and allows decryption of objects with or without key commitment. Use this setting only if you need to maintain V2 encryption behavior during migration, such as when some clients cannot yet read V3 encrypted objects.
+  `:require_encrypt_require_decrypt` - Encrypts new objects with key commitment and only allows decryption of objects that were encrypted with key commitment. Use this setting only after all objects have been re-encrypted with key commitment and all clients have been upgraded to V3.

 **security\_profile**

The `security_profile` parameter determines support for reading objects written by older encryption client versions. This parameter is essential for maintaining backward compatibility during migration.
+  `:v3_and_legacy` - Allows the V3 client to decrypt objects encrypted by V1 and V2 encryption clients. Use this setting during migration to ensure your V3 clients can read all existing encrypted objects.
+  `:v3` - Allows the V3 client to decrypt objects encrypted by V2 encryption clients only. Use this setting if you have already migrated all V1 objects to V2 format.
+ If not specified, the client will only decrypt objects encrypted by V3 clients. Use this only for new application development where no legacy objects exist.

 **envelope\_location**

The `envelope_location` parameter determines where encryption metadata (including the encrypted data key) is stored. This parameter affects which objects are protected by AES GCM with Key Commitment.
+  `:metadata` (Default) - Stores encryption metadata in the S3 object's metadata headers. This is the default behavior and is recommended for most use cases. When using metadata storage, AES GCM with Key Commitment does not apply.
+  `:instruction_file` - Stores encryption metadata in a separate S3 object (Instruction File) with a configurable suffix. When using Instruction Files, AES GCM with Key Commitment protects the encrypted data key from tampering. Use this setting if you require the additional security provided by key commitment for the data key itself.

When using `:instruction_file`, you can optionally specify the `instruction_file_suffix` parameter to customize the suffix used for Instruction File objects. The default suffix is `.instruction`.

 **When to Use Each Configuration Option**

During migration, follow this recommended configuration strategy:

1.  **Initial Migration:** Set `commitment_policy: :require_encrypt_allow_decrypt` and `security_profile: :v3_and_legacy`. This allows your V3 clients to encrypt new objects with key commitment while still being able to decrypt all existing V1 and V2 objects.

1.  **After All Clients Are Upgraded:** Continue using `commitment_policy: :require_encrypt_allow_decrypt` and `security_profile: :v3_and_legacy` until you have re-encrypted all objects that need key commitment protection.

1.  **Full V3 Enforcement:** Only after all objects have been re-encrypted with key commitment and you no longer need to read V1/V2 objects, you can optionally switch to `commitment_policy: :require_encrypt_require_decrypt` and remove the `security_profile` parameter (or set it to `:v2` if V2 objects still exist).

For `envelope_location`, continue using your existing storage method (`:metadata` or `:instruction_file`) unless you have a specific reason to change it. If you are currently using metadata storage and want the additional security of AES GCM with Key Commitment for the data key, you can switch to `:instruction_file`, but note that this will require updating all clients that read these objects.

### Migrate Encryption and Decryption clients to V3
<a name="s3-encryption-migration-v2-v3-migrate"></a>

After updating your clients to read the new encryption formats, you can update your applications to the V3 encryption and decryption clients. The following examples show you how to successfully migrate your code from V2 to V3.

#### Using V3 Encryption Clients
<a name="s3-encryption-migration-v2-v3-using-v3-clients"></a>

 **Pre-migration (V2)**

```
require 'aws-sdk-s3'

# Create V2 encryption client with KMS
client = Aws::S3::EncryptionV2::Client.new(
  kms_key_id: kms_key_id,
  key_wrap_schema: :kms_context,
  content_encryption_schema: :aes_gcm_no_padding,
  security_profile: :v2_and_legacy,
  commitment_policy: :forbid_encrypt_allow_decrypt
)

# Encrypt and upload object
client.put_object(bucket: 'my-bucket', key: 'my-object', body: 'secret data')

# Download and decrypt object
resp = client.get_object(bucket: 'my-bucket', key: 'my-object')
decrypted_data = resp.body.read
```

 **During migration (V3 with backward compatibility)**

```
require 'aws-sdk-s3'

# Create V3 encryption client with KMS
client = Aws::S3::EncryptionV3::Client.new(
  kms_key_id: kms_key_id,
  key_wrap_schema: :kms_context,
  content_encryption_schema: :aes_gcm_no_padding,
  security_profile: :v3_and_legacy,
  commitment_policy: :require_encrypt_allow_decrypt
)

# Encrypt and upload object
client.put_object(bucket: 'my-bucket', key: 'my-object', body: 'secret data')

# Download and decrypt object
resp = client.get_object(bucket: 'my-bucket', key: 'my-object')
decrypted_data = resp.body.read
```

 **Post-migration (V3)**

```
require 'aws-sdk-s3'

# Create V3 encryption client with KMS
client = Aws::S3::EncryptionV3::Client.new(
  kms_key_id: kms_key_id,
  key_wrap_schema: :kms_context,
  content_encryption_schema: :aes_gcm_no_padding,
  security_profile: :v3,
  # Use the commitment policy (REQUIRE_ENCRYPT_REQUIRE_DECRYPT)
  # This encrypts with key commitment and does not decrypt V2 objects
  commitment_policy: :require_encrypt_require_decrypt
)

# Encrypt and upload object
client.put_object(bucket: 'my-bucket', key: 'my-object', body: 'secret data')

# Download and decrypt object
resp = client.get_object(bucket: 'my-bucket', key: 'my-object')
decrypted_data = resp.body.read
```

The key difference in V3 is the addition of the `commitment_policy` parameter. Setting it to `:require_encrypt_require_decrypt` ensures that new objects are encrypted with key commitment and that the client is only decrypting object encrypted with key commitment, providing enhanced security against data key tampering.

The `put_object` call itself remains unchanged. All the security enhancements are configured at the client level.

### Additional Examples
<a name="s3-encryption-migration-v2-v3-additional-examples"></a>

This section provides additional examples for specific migration scenarios and configuration options that may be useful during your V2 to V3 migration.

#### Instruction File vs Metadata Storage
<a name="s3-encryption-migration-v2-v3-example-storage"></a>

The S3 encryption client can store encryption metadata (including the encrypted data key) in two different locations: in the S3 object's metadata headers or in a separate Instruction File. The choice of storage method affects which objects benefit from AES GCM with Key Commitment protection.

 **Metadata Storage (Default)**

By default, the encryption client stores encryption metadata in the S3 object's metadata headers. This is the recommended approach for most use cases because it keeps the encryption metadata with the object and doesn't require managing separate Instruction File objects.

```
require 'aws-sdk-s3'

# Create V3 encryption client with metadata storage (default)
client = Aws::S3::EncryptionV3::Client.new(
  kms_key_id: kms_key_id,
  key_wrap_schema: :kms_context,
  content_encryption_schema: :aes_gcm_no_padding,
  security_profile: :v3_and_legacy,
  commitment_policy: :require_encrypt_allow_decrypt,
  envelope_location: :metadata # Explicitly set to metadata (this is the default)
)

# Encrypt and upload object
# Encryption metadata is stored in the object's metadata headers
client.put_object(bucket: 'my-bucket', key: 'my-object',body: 'secret data')
```

When using metadata storage, AES GCM with Key Commitment does not apply to the encrypted data key. However, the content encryption still benefits from key commitment when using `commitment_policy: :require_encrypt_allow_decrypt` or `:require_encrypt_require_decrypt`.

 **Instruction File Storage**

Alternatively, you can configure the encryption client to store encryption metadata in a separate S3 object called an Instruction File. When using Instruction Files with V3, the encrypted data key is protected by AES GCM with Key Commitment, providing additional security against data key tampering.

```
require 'aws-sdk-s3'

# Create V3 encryption client with instruction file storage
client = Aws::S3::EncryptionV3::Client.new(
  kms_key_id: kms_key_id,
  key_wrap_schema: :kms_context,
  content_encryption_schema: :aes_gcm_no_padding,
  security_profile: :v3_and_legacy,
  commitment_policy: :require_encrypt_allow_decrypt,
  envelope_location: :instruction_file, # Store metadata in separate instruction file
  instruction_file_suffix: '.instruction' # Optional: customize the suffix (default is '.instruction')
)

# Encrypt and upload object
# Encryption metadata is stored in a separate object: 'my-object.instruction'
client.put_object(bucket: 'my-bucket', key: 'my-object', body: 'secret data')

# When retrieving the object, the client automatically reads the instruction file
resp = client.get_object(bucket: 'my-bucket', key: 'my-object')
decrypted_data = resp.body.read
```

When using `envelope_location: :instruction_file`, the encryption client creates two S3 objects:

1. The encrypted data object (e.g., `my-object`)

1. The Instruction File containing encryption metadata (e.g., `my-object.instruction`)

The `instruction_file_suffix` parameter allows you to customize the suffix used for Instruction Files. The default value is `.instruction`.

 **When to Use Each Storage Method**
+  **Use Metadata Storage** for most scenarios. It simplifies object management since encryption metadata travels with the object.
+  **Use Instruction File Storage** when object metadata size is a concern or when you need to separate encryption metadata from the encrypted object. Note that using Instruction Files requires managing two S3 objects (the encrypted object and its instruction file) instead of one.

**Warning**
If you change from metadata storage to instruction file storage (or vice versa), existing objects encrypted with the old storage method will not be readable by clients configured with the new storage method. Plan your storage method carefully and maintain consistency across your application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Ruby. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-ruby` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
