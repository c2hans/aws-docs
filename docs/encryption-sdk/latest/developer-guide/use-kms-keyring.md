---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-kms-keyring.html
---

# AWS KMS keyrings
<a name="use-kms-keyring"></a>

An AWS KMS keyring uses [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) to generate, encrypt, and decrypt data keys. AWS Key Management Service (AWS KMS) protects your KMS keys and performs cryptographic operations within the FIPS boundary. We recommend that you use a AWS KMS keyring, or a keyring with similar security properties, whenever possible.

All programming language implementations that support keyrings, support AWS KMS keyrings that use symmetric encryption KMS keys. The following programming language implementations also support AWS KMS keyrings that use asymmetric RSA KMS keys:
+ Version 3.*x* of the AWS Encryption SDK for Java
+ Version 4.*x* and later of the AWS Encryption SDK for .NET
+ Version 4.*x* of the AWS Encryption SDK for Python, when used with the optional [Cryptographic Material Providers Library](https://github.com/aws/aws-cryptographic-material-providers-library) (MPL) dependency.
+ Version 1.*x* of the AWS Encryption SDK for Rust
+ Version 0.1.*x* or later of the AWS Encryption SDK for Go

If you try to include an asymmetric KMS key in an encryption keyring in any other language implementation, the encrypt call fails. If you include it in a decryption keyring, it is ignored.

You can use an AWS KMS multi-Region key in an AWS KMS keyring or master key provider beginning in [version 2.3.*x*](about-versions.md#version2.3) of the AWS Encryption SDK and version 3.0.*x* of the AWS Encryption CLI. For details and examples of using the multi-Region-aware symbol, see [Using multi-Region AWS KMS keys](configure.md#config-mrks). For information about multi-Region keys, see [Using multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *AWS Key Management Service Developer Guide*.

**Note**
All mentions of *KMS keyrings* in the AWS Encryption SDK refer to AWS KMS keyrings.

AWS KMS keyrings can include two types of wrapping keys:
+ **Generator key**: Generates a plaintext data key and encrypts it. A keyring that encrypts data must have one generator key.
+ **Additional keys**: Encrypts the plaintext data key that the generator key generated. AWS KMS keyrings can have zero or more additional keys.

You use must have a generator key to encrypt messages. When an AWS KMS keyring has just one KMS key, that key is used to generate and encrypt the data key. When decrypting, the generator key is optional, and the distinction between generator keys and additional keys is ignored.

Like all keyrings, AWS KMS keyrings can be used independently or in a [multi-keyring](use-multi-keyring.md) with other keyrings of the same or a different type.

**Topics**
+ [Required permissions for AWS KMS keyrings](#kms-keyring-permissions)
+ [Identifying AWS KMS keys in an AWS KMS keyring](#kms-keyring-id)
+ [Creating an AWS KMS keyring](#kms-keyring-encrypt)
+ [Using an AWS KMS discovery keyring](#kms-keyring-discovery)
+ [Using an AWS KMS regional discovery keyring](#kms-keyring-regional)

## Required permissions for AWS KMS keyrings
<a name="kms-keyring-permissions"></a>

The AWS Encryption SDK doesn't require an AWS account and it doesn't depend on any AWS service. However, to use an AWS KMS keyring, you need an AWS account and the following minimum permissions on the AWS KMS keys in your keyring.
+ To encrypt with an AWS KMS keyring, you need [kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) permission on the generator key. You need [kms:Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) permission on all additional keys in the AWS KMS keyring.
+ To decrypt with an AWS KMS keyring, you need [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) permission on at least one key in the AWS KMS keyring.
+ To encrypt with a multi-keyring comprised of AWS KMS keyrings, you need [kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) permission on the generator key in the generator keyring. You need [kms:Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) permission on all other keys in all other AWS KMS keyrings.
+ To encrypt with an asymmetric RSA AWS KMS keyring, you do not need [kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) or [kms:Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) because you must specify the public key material that you want to use for encryption when you create the keyring. No AWS KMS calls are made when encrypting with this keyring. To decrypt with an asymmetric RSA AWS KMS keyring, you need [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) permission.

For detailed information about permissions for AWS KMS keys, see [KMS key access and permissions](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html) in the *AWS Key Management Service Developer Guide*.

## Identifying AWS KMS keys in an AWS KMS keyring
<a name="kms-keyring-id"></a>

An AWS KMS keyring can include one or more AWS KMS keys. To specify an AWS KMS key in an AWS KMS keyring, use a supported AWS KMS key identifier. The key identifiers you can use to identify an AWS KMS key in a keyring vary with the operation and the language implementation. For details about the key identifiers for an AWS KMS key, see [Key Identifiers](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *AWS Key Management Service Developer Guide*.

As a best practice, use the most specific key identifier that is practical for your task.
+ In an encryption keyring for the AWS Encryption SDK for C, you can use a [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-ARN) to identify KMS keys. In all other language implementations, you can use a [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id), [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN), [alias name](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-name), or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-ARN) to encrypt data.
+ In a decryption keyring, you must use a key ARN to identify AWS KMS keys. This requirement applies to all language implementations of the AWS Encryption SDK. For details, see [Selecting wrapping keys](configure.md#config-keys).
+ In a keyring used for encryption and decryption, you must use a key ARN to identify AWS KMS keys. This requirement applies to all language implementations of the AWS Encryption SDK.

If you specify an alias name or alias ARN for a KMS key in an encryption keyring, the encrypt operation saves the key ARN currently associated with the alias in the metadata of the encrypted data key. It does not save the alias. Changes to the alias don't affect the KMS key used to decrypt your encrypted data keys.

## Creating an AWS KMS keyring
<a name="kms-keyring-encrypt"></a>

You can configure each AWS KMS keyring with a single AWS KMS key or multiple AWS KMS keys in the same or different AWS accounts and AWS Regions. The AWS KMS keys must be a symmetric encryption KMS keys (SYMMETRIC\_DEFAULT) or an asymmetric RSA KMS key. You can also use a symmetric encryption [multi-Region KMS key](configure.md#config-mrks). You can use one or more AWS KMS keyrings in a [multi-keyring](use-multi-keyring.md).

You can create an AWS KMS keyring that encrypts and decrypts data, or you can create AWS KMS keyrings specifically for encrypting or decrypting. When you create an AWS KMS keyring to encrypt data, you must specify a *generator key*, which is an AWS KMS key that is used to generate a plaintext data key and encrypt it. The data key is mathematically unrelated to the KMS key. Then, if you choose, you can specify additional AWS KMS keys that encrypt the same plaintext data key. To decrypt an encrypted field protected by this keyring, the decryption keyring that you use must include at least one of the AWS KMS keys defined in the keyring, or no AWS KMS keys. (An AWS KMS keyring with no AWS KMS keys is known as an [AWS KMS discovery keyring](#kms-keyring-discovery).)

In AWS Encryption SDK language implementations other than the AWS Encryption SDK for C, all wrapping keys in an encryption keyring or multi-keyring must be able to encrypt the data key. If any wrapping key fails to encrypt, the encrypt method fails. As a result, the caller must have the [required permissions](#kms-keyring-permissions) for all keys in the keyring. If you use a discovery keyring to encrypt data, alone or in a multi-keyring, the encrypt operation fails. The exception is the AWS Encryption SDK for C, where the encrypt operation ignores a standard discovery keyring, but fails if you specify a multi-Region discovery keyring, alone or in a multi-keyring.

The following examples create an AWS KMS keyring with a generator key and one additional key. Both the generator key and additional key are symmetric encryption KMS keys. These examples use [key ARNs](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) to identify the KMS keys. This is a best practice for AWS KMS keyrings used for encryption, and a requirement for AWS KMS keyrings used for decryption. For details, see [Identifying AWS KMS keys in an AWS KMS keyring](#kms-keyring-id).

------
#### [ C ]

To identify an AWS KMS key in an encryption keyring in the AWS Encryption SDK for C, specify a [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-arn). In a decryption keyring, you must use a key ARN. For details, see [Identifying AWS KMS keys in an AWS KMS keyring](#kms-keyring-id).

For a complete example, see [string.cpp](https://github.com/aws/aws-encryption-sdk-c/blob/master/examples/string.cpp).

```
const char * generator_key = "{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}"

const char * additional_key = "{{arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321}}"

struct aws_cryptosdk_keyring *kms_encrypt_keyring =
       Aws::Cryptosdk::KmsKeyring::Builder().Build(generator_key,{additional_key});
```

------
#### [ C\# / .NET ]

To create a keyring with one or more KMS keys in the AWS Encryption SDK for .NET, use the `CreateAwsKmsMultiKeyring()` method. This example uses two AWS KMS keys. To specify one KMS key, use only the `Generator` parameter. The `KmsKeyIds` parameter that specifies additional KMS keys is optional.

The input for this keyring doesn't take an AWS KMS client. Instead, the AWS Encryption SDK uses the default AWS KMS client for each Region represented by a KMS key in the keyring. For example, if the KMS key identified by the value of the `Generator` parameter is in the US West (Oregon) Region (`us-west-2`), the AWS Encryption SDK creates a default AWS KMS client for the `us-west-2` Region. If you need to customize the AWS KMS client, use the `CreateAwsKmsKeyring()` method.

When you specify an AWS KMS key for an encryption keyring in the AWS Encryption SDK for .NET, you can use any valid key identifier: a [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id), [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN), [alias name](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-name), or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-arn). For help identifying the AWS KMS keys in an AWS KMS keyring, see [Identifying AWS KMS keys in an AWS KMS keyring](#kms-keyring-id).

The following example uses version 4.*x* of the AWS Encryption SDK for .NET and the `CreateAwsKmsKeyring()` method to customize the AWS KMS client.

```
// Instantiate the AWS Encryption SDK and material providers
var esdk =  new ESDK(new AwsEncryptionSdkConfig());
var mpl = new MaterialProviders(new MaterialProvidersConfig());

string generatorKey = "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab";
List<string> additionalKeys = new List<string> { "arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321" };

// Instantiate the keyring input object
var createEncryptKeyringInput = new CreateAwsKmsMultiKeyringInput
{
    Generator = generatorKey,
    KmsKeyIds = additionalKeys
};

var kmsEncryptKeyring = mpl.CreateAwsKmsMultiKeyring(createEncryptKeyringInput);
```

------
#### [ JavaScript Browser ]

When you specify an AWS KMS key for an encryption keyring in the AWS Encryption SDK for JavaScript, you can use any valid key identifier: a [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id), [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN), [alias name](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-name), or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-arn). For help identifying the AWS KMS keys in an AWS KMS keyring, see [Identifying AWS KMS keys in an AWS KMS keyring](#kms-keyring-id).

The following example uses the `buildClient` function to specify the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. You can also use the `buildClient` to limit the number of encrypted data keys in an encrypted message. For more information, see [Limiting encrypted data keys](configure.md#config-limit-keys).

For a complete example, see [kms\_simple.ts](https://github.com/aws/aws-encryption-sdk-javascript/blob/master/modules/example-browser/src/kms_simple.ts) in the AWS Encryption SDK for JavaScript repository in GitHub.

```
import {
  KmsKeyringNode,
  buildClient,
  CommitmentPolicy,
} from '@aws-crypto/client-node'

const { encrypt, decrypt } = buildClient(
  CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

const clientProvider = getClient(KMS, { credentials })
const generatorKeyId = '{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}'
const additionalKey = '{{alias/exampleAlias}}'

const keyring = new KmsKeyringBrowser({
  clientProvider,
  generatorKeyId,
  keyIds: [additionalKey]
})
```

------
#### [ JavaScript Node.js ]

When you specify an AWS KMS key for an encryption keyring in the AWS Encryption SDK for JavaScript, you can use any valid key identifier: a [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id), [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN), [alias name](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-name), or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-arn). For help identifying the AWS KMS keys in an AWS KMS keyring, see [Identifying AWS KMS keys in an AWS KMS keyring](#kms-keyring-id).

The following example uses the `buildClient` function to specify the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. You can also use the `buildClient` to limit the number of encrypted data keys in an encrypted message. For more information, see [Limiting encrypted data keys](configure.md#config-limit-keys).

For a complete example, see [kms\_simple.ts](https://github.com/aws/aws-encryption-sdk-javascript/blob/master/modules/example-node/src/kms_simple.ts) in the AWS Encryption SDK for JavaScript repository in GitHub.

```
import {
  KmsKeyringNode,
  buildClient,
  CommitmentPolicy,
} from '@aws-crypto/client-node'

const { encrypt, decrypt } = buildClient(
  CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

const generatorKeyId = '{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}'

const additionalKey = '{{alias/exampleAlias}}'

const keyring = new KmsKeyringNode({
  generatorKeyId,
  keyIds: [additionalKey]
})
```

------
#### [ Java ]

To create a keyring with one or more AWS KMS keys, use the `CreateAwsKmsMultiKeyring()` method. This example uses two KMS keys. To specify one KMS key, use only the `generator` parameter. The `kmsKeyIds` parameter that specifies additional KMS keys is optional.

The input for this keyring doesn't take an AWS KMS client. Instead, the AWS Encryption SDK uses the default AWS KMS client for each Region represented by a KMS key in the keyring. For example, if the KMS key identified by the value of the `Generator` parameter is in the US West (Oregon) Region (`us-west-2`), the AWS Encryption SDK creates a default AWS KMS client for the `us-west-2` Region. If you need to customize the AWS KMS client, use the `CreateAwsKmsKeyring()` method.

When you specify an AWS KMS key for an encryption keyring in the AWS Encryption SDK for Java, you can use any valid key identifier: a [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id), [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN), [alias name](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-name), or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-arn). For help identifying the AWS KMS keys in an AWS KMS keyring, see [Identifying AWS KMS keys in an AWS KMS keyring](#kms-keyring-id).

For a complete example, see [BasicEncryptionKeyringExample.java](https://github.com/aws/aws-encryption-sdk-java/blob/master/src/examples/java/com/amazonaws/crypto/examples/keyrings/BasicEncryptionKeyringExample.java) in the AWS Encryption SDK for Java repository in GitHub.

```
// Instantiate the AWS Encryption SDK and material providers
final AwsCrypto crypto = AwsCrypto.builder().build();
final MaterialProviders materialProviders = MaterialProviders.builder()
            .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
            .build();

String generatorKey = "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab";
List<String> additionalKey = Collections.singletonList("arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321");
// Create the keyring
final CreateAwsKmsMultiKeyringInput keyringInput = CreateAwsKmsMultiKeyringInput.builder()
        .generator(generatorKey)
        .kmsKeyIds(additionalKey)
        .build();
final IKeyring kmsKeyring = materialProviders.CreateAwsKmsMultiKeyring(keyringInput);
```

------
#### [ Python ]

To create a keyring with one or more AWS KMS keys, use the `create_aws_kms_multi_keyring()` method. This example uses two KMS keys. To specify one KMS key, use only the `generator` parameter. The `kms_key_ids` parameter that specifies additional KMS keys is optional.

The input for this keyring doesn't take an AWS KMS client. Instead, the AWS Encryption SDK uses the default AWS KMS client for each Region represented by a KMS key in the keyring. For example, if the KMS key identified by the value of the `generator` parameter is in the US West (Oregon) Region (`us-west-2`), the AWS Encryption SDK creates a default AWS KMS client for the `us-west-2` Region. If you need to customize the AWS KMS client, use the `create_aws_kms_keyring()` method.

When you specify an AWS KMS key for an encryption keyring in the AWS Encryption SDK for Python, you can use any valid key identifier: a [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id), [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN), [alias name](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-name), or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-arn). For help identifying the AWS KMS keys in an AWS KMS keyring, see [Identifying AWS KMS keys in an AWS KMS keyring](#kms-keyring-id).

The following example instantiates the AWS Encryption SDK client with the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. For a complete example, see [aws\_kms\_multi\_keyring\_example.py](https://github.com/aws/aws-encryption-sdk-python/tree/master/examples/src/aws_kms_multi_keyring_example.py) in the AWS Encryption SDK for Python repository in GitHub.

```
# Instantiate the AWS Encryption SDK client
client = aws_encryption_sdk.EncryptionSDKClient(
    commitment_policy=CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

# Optional: Create an encryption context
encryption_context: Dict[str, str] = {
    "encryption": "context",
    "is not": "secret",
    "but adds": "useful metadata",
    "that can help you": "be confident that",
    "the data you are handling": "is what you think it is",
}

# Instantiate the material providers library
mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
    config=MaterialProvidersConfig()
)

# Create the AWS KMS keyring
kms_multi_keyring_input: CreateAwsKmsMultiKeyringInput = CreateAwsKmsMultiKeyringInput(
    generator="{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}",
    kms_key_ids="{{arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321}}"
)

kms_multi_keyring: IKeyring = mat_prov.create_aws_kms_multi_keyring(
    input=kms_multi_keyring_input
)
```

------
#### [ Rust ]

To create a keyring with one or more AWS KMS keys, use the `create_aws_kms_multi_keyring()` method. This example uses two KMS keys. To specify one KMS key, use only the `generator` parameter. The `kms_key_ids` parameter that specifies additional KMS keys is optional.

The input for this keyring doesn't take an AWS KMS client. Instead, the AWS Encryption SDK uses the default AWS KMS client for each Region represented by a KMS key in the keyring. For example, if the KMS key identified by the value of the `generator` parameter is in the US West (Oregon) Region (`us-west-2`), the AWS Encryption SDK creates a default AWS KMS client for the `us-west-2` Region. If you need to customize the AWS KMS client, use the `create_aws_kms_keyring()` method.

When you specify an AWS KMS key for an encryption keyring in the AWS Encryption SDK for Rust, you can use any valid key identifier: a [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id), [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN), [alias name](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-name), or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-arn). For help identifying the AWS KMS keys in an AWS KMS keyring, see [Identifying AWS KMS keys in an AWS KMS keyring](#kms-keyring-id).

The following example instantiates the AWS Encryption SDK client with the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. For a complete example, see [aws\_kms\_keyring\_example.rs](https://github.com/aws/aws-encryption-sdk-dafny/tree/mainline/AwsEncryptionSDK/runtimes/rust/examples/keyring/aws_kms_keyring_example.rs) in the Rust directory of the aws-encryption-sdk repository on GitHub.

```
// Instantiate the AWS Encryption SDK client
let esdk_config = AwsEncryptionSdkConfig::builder().build()?;
let esdk_client = esdk_client::Client::from_conf(esdk_config)?;

// Create an AWS KMS client
let sdk_config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
let kms_client = aws_sdk_kms::Client::new(&sdk_config);

// Optional: Create an encryption context
let encryption_context = HashMap::from([
    ("encryption".to_string(), "context".to_string()),
    ("is not".to_string(), "secret".to_string()),
    ("but adds".to_string(), "useful metadata".to_string()),
    ("that can help you".to_string(), "be confident that".to_string()),
    ("the data you are handling".to_string(), "is what you think it is".to_string()),
]);

// Instantiate the material providers library
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

// Create the AWS KMS keyring
let kms_keyring = mpl
    .create_aws_kms_keyring()
    .kms_key_id(kms_key_id)
    .kms_client(kms_client)
    .send()
    .await?;

kms_multi_keyring: IKeyring = mpl.create_aws_kms_multi_keyring(
    input=kms_multi_keyring_input
)
```

------
#### [ Go ]

To create a keyring with one or more AWS KMS keys, use the `create_aws_kms_multi_keyring()` method. This example uses two KMS keys. To specify one KMS key, use only the `generator` parameter. The `kms_key_ids` parameter that specifies additional KMS keys is optional.

The input for this keyring doesn't take an AWS KMS client. Instead, the AWS Encryption SDK uses the default AWS KMS client for each Region represented by a KMS key in the keyring. For example, if the KMS key identified by the value of the `generator` parameter is in the US West (Oregon) Region (`us-west-2`), the AWS Encryption SDK creates a default AWS KMS client for the `us-west-2` Region. If you need to customize the AWS KMS client, use the `create_aws_kms_keyring()` method.

When you specify an AWS KMS key for an encryption keyring in the AWS Encryption SDK for Go, you can use any valid key identifier: a [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id), [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN), [alias name](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-name), or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-arn). For help identifying the AWS KMS keys in an AWS KMS keyring, see [Identifying AWS KMS keys in an AWS KMS keyring](#kms-keyring-id).

The following example instantiates the AWS Encryption SDK client with the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`.

```
import (
    "context"

	mpl "aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygenerated"
	mpltypes "aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
	client "github.com/aws/aws-encryption-sdk/awscryptographyencryptionsdksmithygenerated"
	esdktypes "github.com/aws/aws-encryption-sdk/awscryptographyencryptionsdksmithygeneratedtypes"
)

// Instantiate the AWS Encryption SDK client
encryptionClient, err := client.NewClient(esdktypes.AwsEncryptionSdkConfig{})
if err != nil {
    panic(err)
}

// Optional: Create an encryption context
encryptionContext := map[string]string{
    "encryption":                "context",
    "is not":                    "secret",
    "but adds":                  "useful metadata",
    "that can help you":         "be confident that",
    "the data you are handling": "is what you think it is",
}

// Instantiate the material providers library
matProv, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
if err != nil {
    panic(err)
}

// Create the AWS KMS keyring
awsKmsMultiKeyringInput := mpltypes.CreateAwsKmsMultiKeyringInput{
    Generator: "&arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    KmsKeyIds: []string{"arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321"},
}
awsKmsMultiKeyring, err := matProv.CreateAwsKmsMultiKeyring(context.Background(), awsKmsMultiKeyringInput)
```

------

The AWS Encryption SDK also supports AWS KMS keyrings that use asymmetric RSA KMS keys. Asymmetric RSA AWS KMS keyrings can only contain one key pair.

To encrypt with an asymmetric RSA AWS KMS keyring, you do not need [kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) or [kms:Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) because you must specify the public key material that you want to use for encryption when you create the keyring. No AWS KMS calls are made when encrypting with this keyring. To decrypt with an asymmetric RSA AWS KMS keyring, you need [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) permission.

**Note**
To create an AWS KMS keyring that uses asymmetric RSA KMS keys, you must use one of the following programming language implementations:
Version 3.*x* of the AWS Encryption SDK for Java
Version 4.*x* and later of the AWS Encryption SDK for .NET
Version 4.*x* of the AWS Encryption SDK for Python, when used with the optional [Cryptographic Material Providers Library](https://github.com/aws/aws-cryptographic-material-providers-library) (MPL) dependency.
Version 1.*x* of the AWS Encryption SDK for Rust
Version 0.1.*x* or later of the AWS Encryption SDK for Go

The following examples use the `CreateAwsKmsRsaKeyring` method to create an AWS KMS keyring with an asymmetric RSA KMS key. To create an asymmetric RSA AWS KMS keyring, provide the following values.
+ `kmsClient`: create a new AWS KMS client
+ `kmsKeyID`: the key ARN that identifies your asymmetric RSA KMS key
+ `publicKey`: a ByteBuffer of a UTF-8 encoded PEM file that represents the public key of the key you passed to `kmsKeyID`
+ `encryptionAlgorithm`: the encryption algorithm must be `RSAES_OAEP_SHA_256` or `RSAES_OAEP_SHA_1`

------
#### [ C\# / .NET ]

To create an asymmetric RSA AWS KMS keyring, you must provide the public key and private key ARN from your asymmetric RSA KMS key. The public key must be PEM encoded. The following example creates an AWS KMS keyring with an asymmetric RSA key pair.

```
// Instantiate the AWS Encryption SDK and material providers
var esdk =  new ESDK(new AwsEncryptionSdkConfig());
var mpl = new MaterialProviders(new MaterialProvidersConfig());

var publicKey = new MemoryStream(Encoding.UTF8.GetBytes({{AWS KMS RSA public key}}));

// Instantiate the keyring input object
var createKeyringInput = new CreateAwsKmsRsaKeyringInput
{
    KmsClient = new AmazonKeyManagementServiceClient(),
    KmsKeyId = {{AWS KMS RSA private key ARN}},
    PublicKey = publicKey,
    EncryptionAlgorithm = EncryptionAlgorithmSpec.RSAES_OAEP_SHA_256
};

// Create the keyring
var kmsRsaKeyring = mpl.CreateAwsKmsRsaKeyring(createKeyringInput);
```

------
#### [ Java ]

To create an asymmetric RSA AWS KMS keyring, you must provide the public key and private key ARN from your asymmetric RSA KMS key. The public key must be PEM encoded. The following example creates an AWS KMS keyring with an asymmetric RSA key pair.

```
// Instantiate the AWS Encryption SDK and material providers
final AwsCrypto crypto = AwsCrypto.builder()
        // Specify algorithmSuite without asymmetric signing here
        //
        // ALG_AES_128_GCM_IV12_TAG16_NO_KDF("0x0014"),
        // ALG_AES_192_GCM_IV12_TAG16_NO_KDF("0x0046"),
        // ALG_AES_256_GCM_IV12_TAG16_NO_KDF("0x0078"),
        // ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256("0x0114"),
        // ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA256("0x0146"),
        // ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256("0x0178")
        .withEncryptionAlgorithm(CryptoAlgorithm.{{ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256}})
        .build();

final MaterialProviders matProv = MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();

// Create a KMS RSA keyring.
//    This keyring takes in:
//     - kmsClient
//     - kmsKeyId: Must be an ARN representing an asymmetric RSA KMS key
//     - publicKey: A ByteBuffer of a UTF-8 encoded PEM file representing the public
//                  key for the key passed into kmsKeyId
//     - encryptionAlgorithm: Must be either RSAES_OAEP_SHA_256 or RSAES_OAEP_SHA_1
final CreateAwsKmsRsaKeyringInput createAwsKmsRsaKeyringInput =
        CreateAwsKmsRsaKeyringInput.builder()
                .kmsClient(KmsClient.create())
                .kmsKeyId({{rsaKeyArn}})
                .publicKey({{publicKey}})
                .encryptionAlgorithm(EncryptionAlgorithmSpec.{{RSAES_OAEP_SHA_256}})
                .build();
IKeyring awsKmsRsaKeyring = matProv.CreateAwsKmsRsaKeyring(createAwsKmsRsaKeyringInput);
```

------
#### [ Python ]

To create an asymmetric RSA AWS KMS keyring, you must provide the public key and private key ARN from your asymmetric RSA KMS key. The public key must be PEM encoded. The following example creates an AWS KMS keyring with an asymmetric RSA key pair.

```
# Instantiate the AWS Encryption SDK client
client = aws_encryption_sdk.EncryptionSDKClient(
    commitment_policy=CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

# Optional: Create an encryption context
encryption_context: Dict[str, str] = {
    "encryption": "context",
    "is not": "secret",
    "but adds": "useful metadata",
    "that can help you": "be confident that",
    "the data you are handling": "is what you think it is",
}

# Instantiate the material providers library
mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
    config=MaterialProvidersConfig()
)

# Create the AWS KMS keyring
keyring_input: CreateAwsKmsRsaKeyringInput = CreateAwsKmsRsaKeyringInput(
    public_key="{{public_key}}",
    kms_key_id="{{kms_key_id}}",
    encryption_algorithm="{{RSAES_OAEP_SHA_256}}",
    kms_client=kms_client
)

kms_rsa_keyring: IKeyring = mat_prov.create_aws_kms_rsa_keyring(
    input=keyring_input
)
```

------
#### [ Rust ]

To create an asymmetric RSA AWS KMS keyring, you must provide the public key and private key ARN from your asymmetric RSA KMS key. The public key must be PEM encoded. The following example creates an AWS KMS keyring with an asymmetric RSA key pair.

```
// Instantiate the AWS Encryption SDK client
let esdk_config = AwsEncryptionSdkConfig::builder().build()?;
let esdk_client = esdk_client::Client::from_conf(esdk_config)?;

// Create an AWS KMS client
let sdk_config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
let kms_client = aws_sdk_kms::Client::new(&sdk_config);

// Optional: Create an encryption context
let encryption_context = HashMap::from([
    ("encryption".to_string(), "context".to_string()),
    ("is not".to_string(), "secret".to_string()),
    ("but adds".to_string(), "useful metadata".to_string()),
    ("that can help you".to_string(), "be confident that".to_string()),
    ("the data you are handling".to_string(), "is what you think it is".to_string()),
]);

// Instantiate the material providers library
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

// Create the AWS KMS keyring
let kms_rsa_keyring = mpl
    .create_aws_kms_rsa_keyring()
    .kms_key_id({{kms_key_id}})
    .public_key(aws_smithy_types::Blob::new({{public_key}}))
    .encryption_algorithm(aws_sdk_kms::types::EncryptionAlgorithmSpec::{{RsaesOaepSha256}})
    .kms_client(kms_client)
    .send()
    .await?;
```

------
#### [ Go ]

```
import (
    "context"

	mpl "aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygenerated"
	mpltypes "aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
	client "github.com/aws/aws-encryption-sdk/awscryptographyencryptionsdksmithygenerated"
	esdktypes "github.com/aws/aws-encryption-sdk/awscryptographyencryptionsdksmithygeneratedtypes"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/kms"
)

// Instantiate the AWS Encryption SDK client
encryptionClient, err := client.NewClient(esdktypes.AwsEncryptionSdkConfig{})
if err != nil {
    panic(err)
}

// Create an AWS KMS client
cfg, err := config.LoadDefaultConfig(context.TODO())
if err != nil {
    panic(err)
}
kmsClient := kms.NewFromConfig(cfg, func(o *kms.Options) {
    o.Region = KmsKeyRegion
})

// Optional: Create an encryption context
encryptionContext := map[string]string{
    "encryption":                "context",
    "is not":                    "secret",
    "but adds":                  "useful metadata",
    "that can help you":         "be confident that",
    "the data you are handling": "is what you think it is",
}

// Instantiate the material providers library
matProv, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
if err != nil {
    panic(err)
}

// Create the AWS KMS keyring
awsKmsRSAKeyringInput := mpltypes.CreateAwsKmsRsaKeyringInput{
    KmsClient:           kmsClient,
    KmsKeyId:            {{kmsKeyID}},
    PublicKey:           {{kmsPublicKey}},
    EncryptionAlgorithm: kmstypes.{{EncryptionAlgorithmSpecRsaesOaepSha256}},
}
awsKmsRSAKeyring, err := matProv.CreateAwsKmsRsaKeyring(context.Background(), awsKmsRSAKeyringInput)
if err != nil {
    panic(err)
}
```

------

## Using an AWS KMS discovery keyring
<a name="kms-keyring-discovery"></a>

When decrypting, it's a [best practice](best-practices.md) to specify the wrapping keys that the AWS Encryption SDK can use. To follow this best practice, use an AWS KMS decryption keyring that limits the AWS KMS wrapping keys to those that you specify. However, you can also create an *AWS KMS discovery keyring*, that is, an AWS KMS keyring that doesn't specify any wrapping keys.

The AWS Encryption SDK provides a standard AWS KMS discovery keyring and a discovery keyring for AWS KMS multi-Region keys. For information about using multi-Region keys with the AWS Encryption SDK, see [Using multi-Region AWS KMS keys](configure.md#config-mrks).

Because it doesn't specify any wrapping keys, a discovery keyring can't encrypt data. If you use a discovery keyring to encrypt data, alone or in a multi-keyring, the encrypt operation fails. The exception is the AWS Encryption SDK for C, where the encrypt operation ignores a standard discovery keyring, but fails if you specify a multi-Region discovery keyring, alone or in a multi-keyring.

When decrypting, a discovery keyring allows the AWS Encryption SDK to ask AWS KMS to decrypt any encrypted data key by using the AWS KMS key that encrypted it, regardless of who owns or has access to that AWS KMS key. The call succeeds only when the caller has `kms:Decrypt` permission on the AWS KMS key.

**Important**
If you include an AWS KMS discovery keyring in a decryption [multi-keyring](use-multi-keyring.md), the discovery keyring overrides all KMS key restrictions specified by other keyrings in the multi-keyring. The multi-keyring behaves like its least restrictive keyring. An AWS KMS discovery keyring has no effect on encryption when used by itself or in a multi-keyring.

The AWS Encryption SDK provides an AWS KMS discovery keyring for convenience. However, we recommend that you use a more limited keyring whenever possible for the following reasons.
+ **Authenticity** – An AWS KMS discovery keyring can use any AWS KMS key that was used to encrypt a data key in the encrypted message, just so the caller has permission to use that AWS KMS key to decrypt. This might not be the AWS KMS key that the caller intends to use. For example, one of the encrypted data keys might have been encrypted under a less secure AWS KMS key that anyone can use.
+ **Latency and performance** – An AWS KMS discovery keyring might be perceptibly slower than other keyrings because the AWS Encryption SDK tries to decrypt all of the encrypted data keys, including those encrypted by AWS KMS keys in other AWS accounts and Regions, and AWS KMS keys that the caller doesn't have permission to use for decryption.

If you use a discovery keyring, we recommend that you use a [*discovery filter*](configure.md#config-discovery) to limit the KMS keys that can be used to those in specified AWS accounts and [partitions](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html). Discovery filters are supported in versions 1.7.*x* and later of the AWS Encryption SDK. For help finding your account ID and partition, see [Your AWS account identifiers](https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html) and [ARN format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arns-syntax) in the *AWS General Reference*.

The following code instantiates an AWS KMS discovery keyring with a discovery filter that limits the KMS keys the AWS Encryption SDK can use to those in the `aws` partition and 111122223333 example account.

Before using this code, replace the example AWS account and partition values with valid values for your AWS account and partition. If your KMS keys are in China Regions, use the `aws-cn` partition value. If your KMS keys are in AWS GovCloud (US) Regions, use the `aws-us-gov` partition value. For all other AWS Regions, use the `aws` partition value.

------
#### [ C ]

For a complete example, see: [ kms\_discovery.cpp](https://github.com/aws/aws-encryption-sdk-c/blob/master/examples/kms_discovery.cpp).

```
std::shared_ptr<KmsKeyring::> discovery_filter(
    KmsKeyring::DiscoveryFilter::Builder("{{aws}}")
        .AddAccount("{{111122223333}}")
        .Build());

struct aws_cryptosdk_keyring *kms_discovery_keyring = Aws::Cryptosdk::KmsKeyring::Builder()
       .BuildDiscovery(discovery_filter));
```

------
#### [ C\# / .NET ]

The following example uses version 4.*x* of the AWS Encryption SDK for .NET.

```
// Instantiate the AWS Encryption SDK and material providers
var esdk =  new ESDK(new AwsEncryptionSdkConfig());
var mpl = new MaterialProviders(new MaterialProvidersConfig());

List<string> account = new List<string> { "{{111122223333}}" };

// In a discovery keyring, you specify an AWS KMS client and a discovery filter,
// but not a AWS KMS key
var kmsDiscoveryKeyringInput = new CreateAwsKmsDiscoveryKeyringInput
{
    KmsClient = new AmazonKeyManagementServiceClient(),
    DiscoveryFilter = new DiscoveryFilter()
    {
        AccountIds = account,
        Partition = "aws"
    }
};

var kmsDiscoveryKeyring = mpl.CreateAwsKmsDiscoveryKeyring(kmsDiscoveryKeyringInput);
```

------
#### [ JavaScript Browser ]

In JavaScript, you must explicitly specify the discovery property.

The following example uses the `buildClient` function to specify the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. You can also use the `buildClient` to limit the number of encrypted data keys in an encrypted message. For more information, see [Limiting encrypted data keys](configure.md#config-limit-keys).

```
import {
  KmsKeyringBrowser,
  buildClient,
  CommitmentPolicy,
} from '@aws-crypto/client-browser'

const { encrypt, decrypt } = buildClient(
  CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

const clientProvider = getClient(KMS, { credentials })

const discovery = true
const keyring = new KmsKeyringBrowser(clientProvider, {
    discovery,
    discoveryFilter: { accountIDs: [{{111122223333}}], partition: '{{aws}}' }
})
```

------
#### [ JavaScript Node.js ]

In JavaScript, you must explicitly specify the discovery property.

The following example uses the `buildClient` function to specify the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. You can also use the `buildClient` to limit the number of encrypted data keys in an encrypted message. For more information, see [Limiting encrypted data keys](configure.md#config-limit-keys).

```
import {
  KmsKeyringNode,
  buildClient,
  CommitmentPolicy,
} from '@aws-crypto/client-node'

const { encrypt, decrypt } = buildClient(
  CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

const discovery = true

const keyring = new KmsKeyringNode({
    discovery,
    discoveryFilter: { accountIDs: ['{{111122223333}}'], partition: '{{aws}}' }
})
```

------
#### [ Java ]

```
// Create discovery filter
DiscoveryFilter discoveryFilter = DiscoveryFilter.builder()
        .partition("{{aws}}")
        .accountIds({{111122223333}})
        .build();
// Create the discovery keyring
CreateAwsKmsMrkDiscoveryMultiKeyringInput createAwsKmsMrkDiscoveryMultiKeyringInput = CreateAwsKmsMrkDiscoveryMultiKeyringInput.builder()
        .discoveryFilter(discoveryFilter)
        .build();
IKeyring decryptKeyring = matProv.CreateAwsKmsMrkDiscoveryMultiKeyring(createAwsKmsMrkDiscoveryMultiKeyringInput);
```

------
#### [ Python ]

```
# Instantiate the AWS Encryption SDK
client = aws_encryption_sdk.EncryptionSDKClient(
    commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT
)

# Create a boto3 client for AWS KMS
kms_client = boto3.client('kms', region_name=aws_region)

# Optional: Create an encryption context
encryption_context: Dict[str, str] = {
    "encryption": "context",
    "is not": "secret",
    "but adds": "useful metadata",
    "that can help you": "be confident that",
    "the data you are handling": "is what you think it is",
}

# Instantiate the material providers
mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
    config=MaterialProvidersConfig()
)

# Create the AWS KMS discovery keyring
discovery_keyring_input: CreateAwsKmsDiscoveryKeyringInput = CreateAwsKmsDiscoveryKeyringInput(
    kms_client=kms_client,
    discovery_filter=DiscoveryFilter(
        account_ids=[{{aws_account_id}}],
        partition="aws"
    )
)

discovery_keyring: IKeyring = mat_prov.create_aws_kms_discovery_keyring(
    input=discovery_keyring_input
)
```

------
#### [ Rust ]

```
// Instantiate the AWS Encryption SDK
let esdk_config = AwsEncryptionSdkConfig::builder().build()?;
let esdk_client = esdk_client::Client::from_conf(esdk_config)?;

// Create a AWS KMS client.
let sdk_config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
let kms_client = aws_sdk_kms::Client::new(&sdk_config);

// Instantiate the material providers library
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

// Create discovery filter
let discovery_filter = DiscoveryFilter::builder()
    .account_ids(vec![aws_account_id.to_string()])
    .partition("aws".to_string())
    .build()?;

// Create the AWS KMS discovery keyring
let discovery_keyring = mpl
    .create_aws_kms_discovery_keyring()
    .kms_client(kms_client.clone())
    .discovery_filter(discovery_filter)
    .send()
    .await?;
```

------
#### [ Go ]

```
import (
    "context"

	mpl "aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygenerated"
	mpltypes "aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
	client "github.com/aws/aws-encryption-sdk/awscryptographyencryptionsdksmithygenerated"
	esdktypes "github.com/aws/aws-encryption-sdk/awscryptographyencryptionsdksmithygeneratedtypes"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/kms"
)

// Instantiate the AWS Encryption SDK client
encryptionClient, err := client.NewClient(esdktypes.AwsEncryptionSdkConfig{})
if err != nil {
    panic(err)
}

// Create an AWS KMS client
cfg, err := config.LoadDefaultConfig(context.TODO())
if err != nil {
    panic(err)
}
kmsClient := kms.NewFromConfig(cfg, func(o *kms.Options) {
    o.Region = KmsKeyRegion
})

// Optional: Create an encryption context
encryptionContext := map[string]string{
    "encryption":                "context",
    "is not":                    "secret",
    "but adds":                  "useful metadata",
    "that can help you":         "be confident that",
    "the data you are handling": "is what you think it is",
}

// Instantiate the material providers library
matProv, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
if err != nil {
    panic(err)
}

// Create discovery filter
discoveryFilter := mpltypes.DiscoveryFilter{
    AccountIds: []string{kmsKeyAccountID},
    Partition:  "aws",
}
awsKmsDiscoveryKeyringInput := mpltypes.CreateAwsKmsDiscoveryKeyringInput{
    KmsClient:       kmsClient,
    DiscoveryFilter: &discoveryFilter,
}
awsKmsDiscoveryKeyring, err := matProv.CreateAwsKmsDiscoveryKeyring(context.Background(), awsKmsDiscoveryKeyringInput)
if err != nil {
    panic(err)
}
```

------

## Using an AWS KMS regional discovery keyring
<a name="kms-keyring-regional"></a>

An *AWS KMS regional discovery keyring* is a keyring that doesn't specify the ARNs of KMS keys. Instead, it allows the AWS Encryption SDK to decrypt using only the KMS keys in particular AWS Regions.

When decrypting with an AWS KMS regional discovery keyring, the AWS Encryption SDK decrypts any encrypted data key that was encrypted under an AWS KMS key in the specified AWS Region. To succeed, the caller must have `kms:Decrypt` permission on at least one of the AWS KMS keys in the specified AWS Region that encrypted a data key.

Like other discovery keyrings, the regional discovery keyring has no effect on encryption. It works only when decrypting encrypted messages. If you use a regional discovery keyring in a multi-keyring that is used for encrypting and decrypting, it is effective only when decrypting. If you use a multi-Region discovery keyring to encrypt data, alone or in a multi-keyring, the encrypt operation fails.

**Important**
If you include an AWS KMS regional discovery keyring in a decryption [multi-keyring](use-multi-keyring.md), the regional discovery keyring overrides all KMS key restrictions specified by other keyrings in the multi-keyring. The multi-keyring behaves like its least restrictive keyring. An AWS KMS discovery keyring has no effect on encryption when used by itself or in a multi-keyring.

The regional discovery keyring in the AWS Encryption SDK for C attempts to decrypt only with KMS keys in the specified Region. When you use a discovery keyring in the AWS Encryption SDK for JavaScript and AWS Encryption SDK for .NET, you configure the Region on the AWS KMS client. These AWS Encryption SDK implementations don't filter KMS keys by Region, but AWS KMS will fail a decrypt request for KMS keys outside of the specified Region.

If you use a discovery keyring, we recommend that you use a *discovery filter* to limit the KMS keys used in decryption to those in specified AWS accounts and partitions. Discovery filters are supported in versions 1.7.*x* and later of the AWS Encryption SDK.

For example, the following code creates an AWS KMS regional discovery keyring with a discovery filter. This keyring limits the AWS Encryption SDK to KMS keys in account 111122223333 in the US West (Oregon) Region (us-west-2).

------
#### [ C ]

To view this keyring, and the `create_kms_client` method, in a working example, see [kms\_discovery.cpp](https://github.com/aws/aws-encryption-sdk-c/blob/master/examples/kms_discovery.cpp).

```
std::shared_ptr<KmsKeyring::DiscoveryFilter> discovery_filter(
    KmsKeyring::DiscoveryFilter::Builder("{{aws}}")
        .AddAccount("{{111122223333}}")
        .Build());

struct aws_cryptosdk_keyring *kms_regional_keyring = Aws::Cryptosdk::KmsKeyring::Builder()
       .WithKmsClient(create_kms_client(Aws::Region::{{US_WEST_2}})).BuildDiscovery(discovery_filter));
```

------
#### [ C\# / .NET ]

The AWS Encryption SDK for .NET does not have a dedicated regional discovery keyring. However, you can use several techniques to limit the KMS keys used when decrypting to a particular Region.

The most efficient way to limit the Regions in a discovery keyring is to use a multi-Region-aware discovery keyring, even if you encrypted the data using only single-Region keys. When it encounters single-Region keys, the multi-Region-aware keyring does not use any multi-Region features.

The keyring returned by the `CreateAwsKmsMrkDiscoveryKeyring()` method filters KMS keys by Region before calling AWS KMS. It sends a decrypt request to AWS KMS only when the encrypted data key was encrypted by a KMS key in the Region specified by the `Region` parameter in the `CreateAwsKmsMrkDiscoveryKeyringInput` object.

The following examples uses version 4.*x* of the AWS Encryption SDK for .NET.

```
// Instantiate the AWS Encryption SDK and material providers
var esdk =  new ESDK(new AwsEncryptionSdkConfig());
var mpl = new MaterialProviders(new MaterialProvidersConfig());

List<string> account = new List<string> { "{{111122223333}}" };

// Create the discovery filter
var filter = DiscoveryFilter = new DiscoveryFilter
{
    AccountIds = account,
    Partition = "aws"
};

var regionalDiscoveryKeyringInput = new CreateAwsKmsMrkDiscoveryKeyringInput
{
    KmsClient = new AmazonKeyManagementServiceClient(RegionEndpoint.{{USWest2}}),
    Region = RegionEndpoint.{{USWest2}},
    DiscoveryFilter = filter
};

var kmsRegionalDiscoveryKeyring = mpl.CreateAwsKmsMrkDiscoveryKeyring(regionalDiscoveryKeyringInput);
```

You can also limit KMS keys to a particular AWS Region by specifying a Region in your instance of the AWS KMS client ([AmazonKeyManagementServiceClient](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/KeyManagementService/TKeyManagementServiceClient.html)). However, this configuration is less efficient and potentially more costly than using a multi-Region-aware discovery keyring. Instead of filtering KMS keys by Region before calling AWS KMS, the AWS Encryption SDK for .NET calls AWS KMS for each encrypted data key (until it decrypts one) and relies on AWS KMS to limit the KMS keys it uses to the specified Region.

The following example uses version 4.*x* of the AWS Encryption SDK for .NET.

```
// Instantiate the AWS Encryption SDK and material providers
var esdk =  new ESDK(new AwsEncryptionSdkConfig());
var mpl = new MaterialProviders(new MaterialProvidersConfig());

List<string> account = new List<string> { "{{111122223333}}" };

// Create the discovery filter,
// but not a AWS KMS key
var createRegionalDiscoveryKeyringInput = new CreateAwsKmsDiscoveryKeyringInput
{
    KmsClient = new AmazonKeyManagementServiceClient(RegionEndpoint.{{USWest2}}),
    DiscoveryFilter = new DiscoveryFilter()
    {
        AccountIds = account,
        Partition = "aws"
    }
};

var kmsRegionalDiscoveryKeyring = mlp.CreateAwsKmsDiscoveryKeyring(createRegionalDiscoveryKeyringInput);
```

------
#### [ JavaScript Browser ]

The following example uses the `buildClient` function to specify the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. You can also use the `buildClient` to limit the number of encrypted data keys in an encrypted message. For more information, see [Limiting encrypted data keys](configure.md#config-limit-keys).

```
import {
  KmsKeyringNode,
  buildClient,
  CommitmentPolicy,
} from '@aws-crypto/client-node'

const { encrypt, decrypt } = buildClient(
  CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

const clientProvider = getClient(KMS, { credentials })

const discovery = true
const clientProvider = limitRegions(['{{us-west-2}}'], getKmsClient)
const keyring = new KmsKeyringBrowser(clientProvider, {
    discovery,
    discoveryFilter: { accountIDs: ['{{111122223333}}'], partition: '{{aws}}' }
})
```

------
#### [ JavaScript Node.js ]

The following example uses the `buildClient` function to specify the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. You can also use the `buildClient` to limit the number of encrypted data keys in an encrypted message. For more information, see [Limiting encrypted data keys](configure.md#config-limit-keys).

To view this keyring, and the `limitRegions` function, in a working example, see [kms\_regional\_discovery.ts](https://github.com/aws/aws-encryption-sdk-javascript/blob/master/modules/example-node/src/kms_regional_discovery.ts).

```
import {
  KmsKeyringNode,
  buildClient,
  CommitmentPolicy,
} from '@aws-crypto/client-node'

const { encrypt, decrypt } = buildClient(
  CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

const discovery = true
const clientProvider = limitRegions(['{{us-west-2}}'], getKmsClient)
const keyring = new KmsKeyringNode({
    clientProvider,
    discovery,
    discoveryFilter: { accountIDs: ['{{111122223333}}'], partition: '{{aws}}' }
})
```

------
#### [ Java ]

```
// Create the discovery filter
DiscoveryFilter discoveryFilter = DiscoveryFilter.builder()
        .partition("{{aws}}")
        .accountIds({{111122223333}})
        .build();
// Create the discovery keyring
CreateAwsKmsMrkDiscoveryMultiKeyringInput createAwsKmsMrkDiscoveryMultiKeyringInput = CreateAwsKmsMrkDiscoveryMultiKeyringInput.builder()
        .discoveryFilter(discoveryFilter)
        .regions("{{us-west-2}}")
        .build();
IKeyring decryptKeyring = matProv.CreateAwsKmsMrkDiscoveryMultiKeyring(createAwsKmsMrkDiscoveryMultiKeyringInput);
```

------
#### [ Python ]

```
# Instantiate the AWS Encryption SDK
client = aws_encryption_sdk.EncryptionSDKClient(
    commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT
)

# Create a boto3 client for AWS KMS
kms_client = boto3.client('kms', region_name=aws_region)

# Optional: Create an encryption context
encryption_context: Dict[str, str] = {
    "encryption": "context",
    "is not": "secret",
    "but adds": "useful metadata",
    "that can help you": "be confident that",
    "the data you are handling": "is what you think it is",
}

# Instantiate the material providers
mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
    config=MaterialProvidersConfig()
)

# Create the AWS KMS regional discovery keyring
regional_discovery_keyring_input: CreateAwsKmsMrkDiscoveryKeyringInput = \
    CreateAwsKmsMrkDiscoveryKeyringInput(
        kms_client=kms_client,
        region=mrk_replica_decrypt_region,
        discovery_filter=DiscoveryFilter(
            account_ids=[{{111122223333}}],
            partition="aws"
        )
)

    regional_discovery_keyring: IKeyring = mat_prov.create_aws_kms_mrk_discovery_keyring(
        input=regional_discovery_keyring_input
    )
```

------
#### [ Rust ]

```
// Instantiate the AWS Encryption SDK
let esdk_config = AwsEncryptionSdkConfig::builder().build()?;
let esdk_client = esdk_client::Client::from_conf(esdk_config)?;

// Optional: Create an encryption context
let encryption_context = HashMap::from([
    ("encryption".to_string(), "context".to_string()),
    ("is not".to_string(), "secret".to_string()),
    ("but adds".to_string(), "useful metadata".to_string()),
    ("that can help you".to_string(), "be confident that".to_string()),
    ("the data you are handling".to_string(), "is what you think it is".to_string()),
]);

// Instantiate the material providers library
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

// Create an AWS KMS client
let decrypt_kms_config = aws_sdk_kms::config::Builder::from(&sdk_config)
    .region(Region::new(mrk_replica_decrypt_region.clone()))
    .build();
let decrypt_kms_client = aws_sdk_kms::Client::from_conf(decrypt_kms_config);

// Create discovery filter
let discovery_filter = DiscoveryFilter::builder()
    .account_ids(vec![aws_account_id.to_string()])
    .partition("aws".to_string())
    .build()?;

// Create the regional discovery keyring
let discovery_keyring = mpl
    .create_aws_kms_mrk_discovery_keyring()
    .kms_client(decrypt_kms_client)
    .region(mrk_replica_decrypt_region)
    .discovery_filter(discovery_filter)
    .send()
    .await?;
```

------
#### [ Go ]

```
import (
    "context"

	mpl "aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygenerated"
	mpltypes "aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
	client "github.com/aws/aws-encryption-sdk/awscryptographyencryptionsdksmithygenerated"
	esdktypes "github.com/aws/aws-encryption-sdk/awscryptographyencryptionsdksmithygeneratedtypes"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/kms"
)

// Instantiate the AWS Encryption SDK client
encryptionClient, err := client.NewClient(esdktypes.AwsEncryptionSdkConfig{})
if err != nil {
    panic(err)
}

// Create an AWS KMS client
cfg, err := config.LoadDefaultConfig(context.TODO())
if err != nil {
    panic(err)
}
kmsClient := kms.NewFromConfig(cfg, func(o *kms.Options) {
    o.Region = KmsKeyRegion
})

// Optional: Create an encryption context
encryptionContext := map[string]string{
    "encryption":                "context",
    "is not":                    "secret",
    "but adds":                  "useful metadata",
    "that can help you":         "be confident that",
    "the data you are handling": "is what you think it is",
}

// Create discovery filter
discoveryFilter := mpltypes.DiscoveryFilter{
    AccountIds: []string{awsAccountID},
    Partition:  "aws",
}

// Create the regional discovery keyring
awsKmsMrkDiscoveryInput := mpltypes.CreateAwsKmsMrkDiscoveryKeyringInput{
    KmsClient:       kmsClient,
    Region:          alternateRegionMrkKeyRegion,
    DiscoveryFilter: &discoveryFilter,
}
awsKmsMrkDiscoveryKeyring, err := matProv.CreateAwsKmsMrkDiscoveryKeyring(context.Background(), awsKmsMrkDiscoveryInput)
if err != nil {
    panic(err)
}
```

------

The AWS Encryption SDK for JavaScript also exports an `excludeRegions` function for Node.js and the browser. This function creates an AWS KMS regional discovery keyring that omits AWS KMS keys in particular regions. The following example creates an AWS KMS regional discovery keyring that can use AWS KMS keys in account 111122223333 in every AWS Region except for US East (N. Virginia) (us-east-1).

The AWS Encryption SDK for C does not have an analogous method, but you can implement one by creating a custom [ClientSupplier](https://github.com/aws/aws-encryption-sdk-c/blob/master/aws-encryption-sdk-cpp/include/aws/cryptosdk/cpp/kms_keyring.h#L157).

This example shows the code for Node.js.

```
const discovery = true
const clientProvider = excludeRegions(['us-east-1'], getKmsClient)
const keyring = new KmsKeyringNode({
    clientProvider,
    discovery,
    discoveryFilter: { accountIDs: [{{111122223333}}], partition: '{{aws}}' }
})
```
