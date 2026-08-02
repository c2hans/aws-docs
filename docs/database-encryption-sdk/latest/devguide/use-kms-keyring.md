---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-kms-keyring.html
---

# AWS KMS keyrings
<a name="use-kms-keyring"></a>

****

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

An AWS KMS keyring uses symmetric encryption or asymmetric RSA [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) to generate, encrypt, and decrypt data keys. AWS Key Management Service (AWS KMS) protects your KMS keys and performs cryptographic operations within the FIPS boundary. We recommend that you use a AWS KMS keyring, or a keyring with similar security properties, whenever possible.

You can also use a symmetric multi-Region KMS key in an AWS KMS keyring. For more details and examples using multi-Region AWS KMS keys, see [Using multi-Region AWS KMS keys](#config-mrks). For information about multi-Region keys, see [Using multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *AWS Key Management Service Developer Guide*.

AWS KMS keyrings can include two types of wrapping keys:
+ **Generator key**: Generates a plaintext data key and encrypts it. A keyring that encrypts data must have one generator key.
+ **Additional keys**: Encrypts the plaintext data key that the generator key generated. AWS KMS keyrings can have zero or more additional keys.

You must have a generator key to encrypt records. When an AWS KMS keyring has just one AWS KMS key, that key is used to generate and encrypt the data key.

Like all keyrings, AWS KMS keyrings can be used independently or in a [multi-keyring](use-multi-keyring.md) with other keyrings of the same or a different type.

**Topics**
+ [Required permissions for AWS KMS keyrings](#kms-keyring-permissions)
+ [Identifying AWS KMS keys in an AWS KMS keyring](#kms-keyring-id)
+ [Creating an AWS KMS keyring](#kms-keyring-create)
+ [Using multi-Region AWS KMS keys](#config-mrks)
+ [Using an AWS KMS discovery keyring](#kms-keyring-discovery)
+ [Using an AWS KMS regional discovery keyring](#kms-keyring-regional)

## Required permissions for AWS KMS keyrings
<a name="kms-keyring-permissions"></a>

The AWS Database Encryption SDK doesn't require an AWS account and it doesn't depend on any AWS service. However, to use an AWS KMS keyring, you need an AWS account and the following minimum permissions on the AWS KMS keys in your keyring.
+ To encrypt with an AWS KMS keyring, you need [kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) permission on the generator key. You need [kms:Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) permission on all additional keys in the AWS KMS keyring.
+ To decrypt with an AWS KMS keyring, you need [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) permission on at least one key in the AWS KMS keyring.
+ To encrypt with a multi-keyring comprised of AWS KMS keyrings, you need [kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) permission on the generator key in the generator keyring. You need [kms:Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) permission on all other keys in all other AWS KMS keyrings.
+ To encrypt with an asymmetric RSA AWS KMS keyring, you do not need [kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) or [kms:Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) because you must specify the public key material that you want to use for encryption when you create the keyring. No AWS KMS calls are made when encrypting with this keyring. To decrypt with an asymmetric RSA AWS KMS keyring, you need [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) permission.

For detailed information about permissions for AWS KMS keys, see [Authentication and access control](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html) in the *AWS Key Management Service Developer Guide*.

## Identifying AWS KMS keys in an AWS KMS keyring
<a name="kms-keyring-id"></a>

An AWS KMS keyring can include one or more AWS KMS keys. To specify an AWS KMS key in an AWS KMS keyring, use a supported AWS KMS key identifier. The key identifiers you can use to identify an AWS KMS key in a keyring vary with the operation and the language implementation. For details about the key identifiers for an AWS KMS key, see [Key Identifiers](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *AWS Key Management Service Developer Guide*.

As a best practice, use the most specific key identifier that is practical for your task.
+ To encrypt with an AWS KMS keyring, you can use a [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id), [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN), [alias name](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-name), or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-ARN) to encrypt data.
**Note**
If you specify an alias name or alias ARN for a KMS key in an encryption keyring, the encrypt operation saves the key ARN currently associated with the alias in the metadata of the encrypted data key. It does not save the alias. Changes to the alias don't affect the KMS key used to decrypt your encrypted data keys.
+ To decrypt with an AWS KMS keyring, you must use a key ARN to identify AWS KMS keys. For details, see [Selecting wrapping keys](configure.md#config-keys).
+ In a keyring used for encryption and decryption, you must use a key ARN to identify AWS KMS keys.

When decrypting, the AWS Database Encryption SDK searches the AWS KMS keyring for an AWS KMS key that can decrypt one of the encrypted data keys. Specifically, the AWS Database Encryption SDK uses the following pattern for each encrypted data key in the material description.
+ The AWS Database Encryption SDK gets the key ARN of the AWS KMS key that encrypted the data key from the metadata of the material description.
+ The AWS Database Encryption SDK searches the decryption keyring for an AWS KMS key with a matching key ARN.
+ If it finds an AWS KMS key with a matching key ARN in the keyring, the AWS Database Encryption SDK asks AWS KMS to use the KMS key to decrypt the encrypted data key.
+ Otherwise, it skips to the next encrypted data key, if any.

## Creating an AWS KMS keyring
<a name="kms-keyring-create"></a>

You can configure each AWS KMS keyring with a single AWS KMS key or multiple AWS KMS keys in the same or different AWS accounts and AWS Regions. The AWS KMS key must be a symmetric encryption key (`SYMMETRIC_DEFAULT`) or an asymmetric RSA KMS key. You can also use a symmetric encryption [multi-Region KMS key](#config-mrks). You can use one or more AWS KMS keyrings in a [multi-keyring](use-multi-keyring.md).

You can create an AWS KMS keyring that encrypts and decrypts data, or you can create AWS KMS keyrings specifically for encrypting or decrypting. When you create an AWS KMS keyring to encrypt data, you must specify a *generator key*, which is an AWS KMS key that is used to generate a plaintext data key and encrypt it. The data key is mathematically unrelated to the KMS key. Then, if you choose, you can specify additional AWS KMS keys that encrypt the same plaintext data key. To decrypt an encrypted field protected by this keyring, the decryption keyring that you use must include at least one of the AWS KMS keys defined in the keyring, or no AWS KMS keys. (An AWS KMS keyring with no AWS KMS keys is known as an [AWS KMS discovery keyring](#kms-keyring-discovery).)

All wrapping keys in an encryption keyring or multi-keyring must be able to encrypt the data key. If any wrapping key fails to encrypt, the encrypt method fails. As a result, the caller must have the [required permissions](#kms-keyring-permissions) for all keys in the keyring. If you use a discovery keyring to encrypt data, alone or in a multi-keyring, the encrypt operation fails.

The following examples use the `CreateAwsKmsMrkMultiKeyring` method to create an AWS KMS keyring with a symmetric encryption KMS key. The `CreateAwsKmsMrkMultiKeyring` method automatically creates the AWS KMS client and ensures that the keyring will correctly handle both single-Region and multi-Region keys. These examples use a [key ARNs](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) to identify the KMS keys. For details, see [Identifying AWS KMS keys in an AWS KMS keyring](#kms-keyring-id)

------
#### [ Java ]

```
final MaterialProviders matProv = MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();
final CreateAwsKmsMrkMultiKeyringInput keyringInput = CreateAwsKmsMrkMultiKeyringInput.builder()
        .generator({{kmsKeyArn}})
        .build();
final IKeyring kmsKeyring = matProv.CreateAwsKmsMrkMultiKeyring(keyringInput);
```

------
#### [ C\# / .NET ]

```
var matProv = new MaterialProviders(new MaterialProvidersConfig());
var createAwsKmsMrkMultiKeyringInput = new CreateAwsKmsMrkMultiKeyringInput
{
    Generator = {{kmsKeyArn}}
};
var awsKmsMrkMultiKeyring = matProv.CreateAwsKmsMrkMultiKeyring(createAwsKmsMrkMultiKeyringInput);
```

------
#### [ Rust ]

```
let provider_config = MaterialProvidersConfig::builder().build()?;
let mat_prov = client::Client::from_conf(provider_config)?;
let kms_keyring = mat_prov
    .create_aws_kms_mrk_multi_keyring()
    .generator({{kms_key_id}})
    .send()
    .await?;
```

------

The following examples use the `CreateAwsKmsRsaKeyring` method to create an AWS KMS keyring with an asymmetric RSA KMS key. To create an asymmetric RSA AWS KMS keyring, provide the following values.
+ `kmsClient`: create a new AWS KMS client
+ `kmsKeyID`: the key ARN that identifies your asymmetric RSA KMS key
+ `publicKey`: a ByteBuffer of a UTF-8 encoded PEM file that represents the public key of the key you passed to `kmsKeyID`
+ `encryptionAlgorithm`: the encryption algorithm must be `RSAES_OAEP_SHA_256` or `RSAES_OAEP_SHA_1`

------
#### [ Java ]

```
 final MaterialProviders matProv = MaterialProviders.builder()
    .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
    .build();
final CreateAwsKmsRsaKeyringInput createAwsKmsRsaKeyringInput =
    CreateAwsKmsRsaKeyringInput.builder()
        .kmsClient(KmsClient.create())
        .kmsKeyId({{rsaKMSKeyArn}})
        .publicKey({{publicKey}})
        .encryptionAlgorithm(EncryptionAlgorithmSpec.{{RSAES_OAEP_SHA_256}})
        .build();
IKeyring awsKmsRsaKeyring = matProv.CreateAwsKmsRsaKeyring(createAwsKmsRsaKeyringInput);
```

------
#### [ C\# / .NET ]

```
var matProv = new MaterialProviders(new MaterialProvidersConfig());
var createAwsKmsRsaKeyringInput = new CreateAwsKmsRsaKeyringInput
{
    KmsClient = new AmazonKeyManagementServiceClient(),
    KmsKeyId = {{rsaKMSKeyArn}},
    PublicKey = {{publicKey}},
    EncryptionAlgorithm = EncryptionAlgorithmSpec.{{RSAES_OAEP_SHA_256}}
};
IKeyring awsKmsRsaKeyring = matProv.CreateAwsKmsRsaKeyring(createAwsKmsRsaKeyringInput);
```

------
#### [ Rust ]

```
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;
let sdk_config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
let kms_rsa_keyring = mpl
    .create_aws_kms_rsa_keyring()
    .kms_key_id({{rsa_kms_key_arn}})
    .public_key({{public_key}})
    .encryption_algorithm(aws_sdk_kms::types::EncryptionAlgorithmSpec::{{RsaesOaepSha256}})
    .kms_client(aws_sdk_kms::Client::new(&sdk_config))
    .send()
    .await?;
```

------

## Using multi-Region AWS KMS keys
<a name="config-mrks"></a>

You can use multi-Region AWS KMS keys as wrapping keys in the AWS Database Encryption SDK. If you encrypt with a multi-Region key in one AWS Region, you can decrypt using a related multi-Region key in a different AWS Region.

Multi-Region KMS keys are a set of AWS KMS keys in different AWS Regions that have the same key material and key ID. You can use these *related* keys as though they were the same key in different Regions. Multi-Region keys support common disaster recovery and backup scenarios that require encrypting in one Region and decrypting in a different Region without making a cross-Region call to AWS KMS. For information about multi-Region keys, see [Using multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *AWS Key Management Service Developer Guide*.

To support multi-Region keys, the AWS Database Encryption SDK includes AWS KMS multi-Region-aware keyrings. The `CreateAwsKmsMrkMultiKeyring` method supports both single-Region and multi-Region keys.
+ For single-Region keys, the multi-Region-aware symbol behaves just like the single-Region AWS KMS keyring. It attempts to decrypt ciphertext only with the single-Region key that encrypted the data. To simplify your AWS KMS keyring experience, we recommend using the `CreateAwsKmsMrkMultiKeyring` method whenever you use a symmetric encryption KMS key.
+ For multi-Region keys, the multi-Region-aware symbol attempts to decrypt ciphertext with the same multi-Region key that encrypted the data or with the related multi-Region key in the Region you specify.

In the multi-Region-aware keyrings that take more than one KMS key, you can specify multiple single-Region and multi-Region keys. However, you can specify only one key from each set of related multi-Region keys. If you specify more than one key identifier with the same key ID, the constructor call fails.

The following examples create an AWS KMS keyring with a multi-Region KMS key. The examples specify a multi-Region key as the generator key and a single-Region key as the child key.

------
#### [ Java ]

```
final MaterialProviders matProv = MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();
final CreateAwsKmsMrkMultiKeyringInput createAwsKmsMrkMultiKeyringInput =
    CreateAwsKmsMrkMultiKeyringInput.builder()
            .generator({{multiRegionKeyArn}})
            .kmsKeyIds(Collections.singletonList({{kmsKeyArn}}))
            .build();
IKeyring awsKmsMrkMultiKeyring = matProv.CreateAwsKmsMrkMultiKeyring(createAwsKmsMrkMultiKeyringInput);
```

------
#### [ C\# / .NET ]

```
var matProv = new MaterialProviders(new MaterialProvidersConfig());
var createAwsKmsMrkMultiKeyringInput = new CreateAwsKmsMrkMultiKeyringInput
{
    Generator = {{multiRegionKeyArn}},
    KmsKeyIds = new List<String> { {{kmsKeyArn}} }
};
var awsKmsMrkMultiKeyring = matProv.CreateAwsKmsMrkMultiKeyring(createAwsKmsMrkMultiKeyringInput);
```

------
#### [ Rust ]

```
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

let aws_kms_mrk_multi_keyring = mpl
    .create_aws_kms_mrk_multi_keyring()
    .generator({{multiRegion_key_arn}})
    .kms_key_ids(vec![{{key_arn}}.to_string()])
    .send()
    .await?;
```

------

When you use multi-Region AWS KMS keyrings, you can decrypt ciphertext in strict mode or discover mode. To decrypt the ciphertext in strict mode, instantiate the multi-Region-aware symbol with the key ARN of the related multi-Region key in the region you are decrypting the ciphertext. If you specify the key ARN of a related multi-Region key in a different Region (for example, the region where the record was encrypted), the multi-Region-aware symbol will make a cross-Region call for that AWS KMS key.

When decrypting in strict mode, the multi-Region-aware symbol requires a key ARN. It accepts only one key ARN from each set of related multi-Region keys.

You can also decrypt in *discovery mode* with AWS KMS multi-Region keys. When decrypting in discovery mode, you don't specify any AWS KMS keys. (For information about single-Region AWS KMS discovery keyrings, see [Using an AWS KMS discovery keyring](#kms-keyring-discovery).)

If you encrypted with a multi-Region key, the multi-Region-aware symbol in discovery mode will try to decrypt by using a related multi-Region key in the local Region. If none exists; the call fails. In discovery mode, the AWS Database Encryption SDK will not attempt a cross-Region call for the multi-Region key used for encryption.

## Using an AWS KMS discovery keyring
<a name="kms-keyring-discovery"></a>

When decrypting, it's a best practice to specify the wrapping keys that the AWS Database Encryption SDK can use. To follow this best practice, use an AWS KMS decryption keyring that limits the AWS KMS wrapping keys to those that you specify. However, you can also create an *AWS KMS discovery keyring*, that is, an AWS KMS keyring that doesn't specify any wrapping keys.

The AWS Database Encryption SDK provides a standard AWS KMS discovery keyring and a discovery keyring for AWS KMS multi-Region keys. For information about using multi-Region keys with the AWS Database Encryption SDK, see [Using multi-Region AWS KMS keys](#config-mrks).

Because it doesn't specify any wrapping keys, a discovery keyring can't encrypt data. If you use a discovery keyring to encrypt data, alone or in a multi-keyring, the encrypt operation fails.

When decrypting, a discovery keyring allows the AWS Database Encryption SDK to ask AWS KMS to decrypt any encrypted data key by using the AWS KMS key that encrypted it, regardless of who owns or has access to that AWS KMS key. The call succeeds only when the caller has `kms:Decrypt` permission on the AWS KMS key.

**Important**
If you include an AWS KMS discovery keyring in a decryption [multi-keyring](use-multi-keyring.md), the discovery keyring overrides all KMS key restrictions specified by other keyrings in the multi-keyring. The multi-keyring behaves like its least restrictive keyring. If you use a discovery keyring to encrypt data, alone or in a multi-keyring, the encrypt operation fails

The AWS Database Encryption SDK provides an AWS KMS discovery keyring for convenience. However, we recommend that you use a more limited keyring whenever possible for the following reasons.
+ **Authenticity** – An AWS KMS discovery keyring can use any AWS KMS key that was used to encrypt a data key in the material description, so long as the caller has permission to use that AWS KMS key to decrypt. This might not be the AWS KMS key that the caller intends to use. For example, one of the encrypted data keys might have been encrypted under a less secure AWS KMS key that anyone can use.
+ **Latency and performance** – An AWS KMS discovery keyring might be perceptibly slower than other keyrings because the AWS Database Encryption SDK tries to decrypt all of the encrypted data keys, including those encrypted by AWS KMS keys in other AWS accounts and Regions, and AWS KMS keys that the caller doesn't have permission to use for decryption.

If you use a discovery keyring, we recommend that you use a [*discovery filter*](configure.md#config-discovery) to limit the KMS keys that can be used to those in specified AWS accounts and [partitions](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html). For help finding your account ID and partition, see [Your AWS account identifiers](https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html) and [ARN format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arns-syntax) in the *AWS General Reference*.

The following code examples instantiate an AWS KMS discovery keyring with a discovery filter that limits the KMS keys that the AWS Database Encryption SDK can use to those in the `aws` partition and `111122223333` example account.

Before using this code, replace the example AWS account and partition values with valid values for your AWS account and partition. If your KMS keys are in China Regions, use the `aws-cn` partition value. If your KMS keys are in AWS GovCloud (US) Regions, use the `aws-us-gov` partition value. For all other AWS Regions, use the `aws` partition value.

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
#### [ C\# / .NET ]

```
// Create discovery filter
var discoveryFilter = new DiscoveryFilter
{
    Partition = "{{aws}}",
    AccountIds = {{111122223333}}
};
// Create the discovery keyring
var createAwsKmsMrkDiscoveryMultiKeyringInput = new CreateAwsKmsMrkDiscoveryMultiKeyringInput
{
    DiscoveryFilter = discoveryFilter
};
var decryptKeyring = matProv.CreateAwsKmsMrkDiscoveryMultiKeyring(createAwsKmsMrkDiscoveryMultiKeyringInput);
```

------
#### [ Rust ]

```
// Create discovery filter
let discovery_filter = DiscoveryFilter::builder()
    .partition("{{aws}}")
    .account_ids({{111122223333}})
    .build()?;

// Create the discovery keyring
let decrypt_keyring = mpl
    .create_aws_kms_mrk_discovery_multi_keyring()
    .discovery_filter(discovery_filter)
    .send()
    .await?;
```

------

## Using an AWS KMS regional discovery keyring
<a name="kms-keyring-regional"></a>

An *AWS KMS regional discovery keyring* is a keyring that doesn't specify the ARNs of KMS keys. Instead, it allows the AWS Database Encryption SDK to decrypt using only the KMS keys in particular AWS Regions.

When decrypting with an AWS KMS regional discovery keyring, the AWS Database Encryption SDK decrypts any encrypted data key that was encrypted under an AWS KMS key in the specified AWS Region. To succeed, the caller must have `kms:Decrypt` permission on at least one of the AWS KMS keys in the specified AWS Region that encrypted a data key.

Like other discovery keyrings, the regional discovery keyring has no effect on encryption. It works only when decrypting encrypted fields. If you use a regional discovery keyring in a multi-keyring that is used for encrypting and decrypting, it is effective only when decrypting. If you use a multi-Region discovery keyring to encrypt data, alone or in a multi-keyring, the encrypt operation fails.

**Important**
If you include an AWS KMS regional discovery keyring in a decryption [multi-keyring](use-multi-keyring.md), the regional discovery keyring overrides all KMS key restrictions specified by other keyrings in the multi-keyring. The multi-keyring behaves like its least restrictive keyring. An AWS KMS discovery keyring has no effect on encryption when used by itself or in a multi-keyring.

The regional discovery keyring in the AWS Database Encryption SDK attempts to decrypt only with KMS keys in the specified Region. When you use a discovery keyring, you configure the Region on the AWS KMS client. These AWS Database Encryption SDK implementations don't filter KMS keys by Region, but AWS KMS will fail a decrypt request for KMS keys outside of the specified Region.

If you use a discovery keyring, we recommend that you use a *discovery filter* to limit the KMS keys used in decryption to those in specified AWS accounts and partitions.

For example, the following code creates an AWS KMS regional discovery keyring with a discovery filter. This keyring limits the AWS Database Encryption SDK to KMS keys in account 111122223333 in the US West (Oregon) Region (us-west-2).

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
#### [ C\# / .NET ]

```
// Create discovery filter
var discoveryFilter = new DiscoveryFilter
{
    Partition = "{{aws}}",
    AccountIds = {{111122223333}}
};
// Create the discovery keyring
var createAwsKmsMrkDiscoveryMultiKeyringInput = new CreateAwsKmsMrkDiscoveryMultiKeyringInput
{
    DiscoveryFilter = discoveryFilter,
    Regions = {{us-west-2}}
};
var decryptKeyring = matProv.CreateAwsKmsMrkDiscoveryMultiKeyring(createAwsKmsMrkDiscoveryMultiKeyringInput);
```

------
#### [ Rust ]

```
// Create discovery filter
let discovery_filter = DiscoveryFilter::builder()
    .partition("{{aws}}")
    .account_ids({{111122223333}})
    .build()?;

// Create the discovery keyring
let decrypt_keyring = mpl
    .create_aws_kms_mrk_discovery_multi_keyring()
    .discovery_filter(discovery_filter)
    .regions({{us-west-2}})
    .send()
    .await?;
```

------
