---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-multi-keyring.html
---

# Multi-keyrings
<a name="use-multi-keyring"></a>

You can combine keyrings into a multi-keyring. A *multi-keyring* is a keyring that consists of one or more individual keyrings of the same or a different type. The effect is like using several keyrings in a series. When you use a multi-keyring to encrypt data, any of the wrapping keys in any of its keyrings can decrypt that data.

When you create a multi-keyring to encrypt data, you designate one of the keyrings as the *generator keyring*. All other keyrings are known as *child keyrings*. The generator keyring generates and encrypts the plaintext data key. Then, all of the wrapping keys in all of the child keyrings encrypt the same plaintext data key. The multi-keyring returns the plaintext key and one encrypted data key for each wrapping key in the multi-keyring. If the generator keyring is a [KMS keyring](use-kms-keyring.md), the generator key in the AWS KMS keyring generates and encrypts the plaintext key. Then, all additional AWS KMS keys in the AWS KMS keyring, and all wrapping keys in all child keyrings in the multi-keyring, encrypt the same plaintext key.

If you create a multi-keyring with no generator keyring, you can use it by itself to decrypt data, but not to encrypt. Or, to use a multi-keyring with no generator keyring in encrypt operations, you can specify it as a child keyring in another multi-keyring. A multi-keyring with no generator keyring cannot be designated as the generator keyring in another multi-keyring.

When decrypting, the AWS Encryption SDK uses the keyrings to try to decrypt one of the encrypted data keys. The keyrings are called in the order that they are specified in the multi-keyring. Processing stops as soon as any key in any keyring can decrypt an encrypted data key.

Beginning in [version 1.7.*x*](about-versions.md#version-1.7), when an encrypted data key is encrypted under an AWS Key Management Service (AWS KMS) keyring (or master key provider), the AWS Encryption SDK always passes the key ARN of the AWS KMS key to the `KeyId` parameter of the AWS KMS [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) operation. This is an AWS KMS best practice that assures that you decrypt the encrypted data key with the wrapping key you intend to use.

To see a working example of a multi-keyring, see:
+ C: [multi\_keyring.cpp](https://github.com/aws/aws-encryption-sdk-c/blob/master/examples/multi_keyring.cpp)[]()
+ C\# / .NET: [MultiKeyringExample.cs](https://github.com/aws/aws-encryption-sdk/tree/mainline/AwsEncryptionSDK/runtimes/net/Examples/Keyring/MultiKeyringExample.cs)
+ JavaScript Node.js: [multi\_keyring.ts](https://github.com/aws/aws-encryption-sdk-javascript/blob/master/modules/example-node/src/multi_keyring.ts)
+ JavaScript Browser: [multi\_keyring.ts](https://github.com/aws/aws-encryption-sdk-javascript/blob/master/modules/example-browser/src/multi_keyring.ts)
+ Java: [MultiKeyringExample.java](https://github.com/aws/aws-encryption-sdk-java/blob/master/src/examples/java/com/amazonaws/crypto/examples/keyrings/MultiKeyringExample.java)
+ Python: [multi\_keyring\_example.py](https://github.com/aws/aws-encryption-sdk-python/tree/master/examples/src/multi_keyring_example.py)

To create a multi-keyring, first instantiate the child keyrings. In this example, we use an AWS KMS keyring and a Raw AES keyring, but you can combine any supported keyrings in a multi-keyring.

------
#### [ C ]

```
/* Define an AWS KMS keyring. For details, see [string.cpp](https://github.com/aws/aws-encryption-sdk-c/blob/master/examples/string.cpp) */
struct aws_cryptosdk_keyring *kms_keyring = Aws::Cryptosdk::KmsKeyring::Builder().Build(example_key);

// Define a Raw AES keyring. For details, see [raw\_aes\_keyring.c](https://github.com/aws/aws-encryption-sdk-c/blob/master/examples/raw_aes_keyring.c) */
struct aws_cryptosdk_keyring *aes_keyring = aws_cryptosdk_raw_aes_keyring_new(
        alloc, wrapping_key_namespace, wrapping_key_name, wrapping_key, AWS_CRYPTOSDK_AES256);
```

------
#### [ C\# / .NET ]

```
// Define an AWS KMS keyring. For details, see [AwsKmsKeyringExample.cs](https://github.com/aws/aws-encryption-sdk/tree/mainline/AwsEncryptionSDK/runtimes/net/Examples/Keyring/AwsKmsKeyringExample.cs).
var kmsKeyring = materialProviders.CreateAwsKmsKeyring(createKmsKeyringInput);

// Define a Raw AES keyring. For details, see [RawAESKeyringExample.cs](https://github.com/aws/aws-encryption-sdk/tree/mainline/AwsEncryptionSDK/runtimes/net/Examples/Keyring/RawAESKeyringExample.cs).
var aesKeyring = materialProviders.CreateRawAesKeyring(createAesKeyringInput);
```

------
#### [ JavaScript Browser ]

The following example uses the `buildClient` function to specify the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. You can also use the `buildClient` to limit the number of encrypted data keys in an encrypted message. For more information, see [Limiting encrypted data keys](configure.md#config-limit-keys).

```
import {
  KmsKeyringBrowser,
  KMS,
  getClient,
  RawAesKeyringWebCrypto,
  RawAesWrappingSuiteIdentifier,
  MultiKeyringWebCrypto,
  buildClient,
  CommitmentPolicy,
  synchronousRandomValues,
} from '@aws-crypto/client-browser'

const { encrypt, decrypt } = buildClient(
  CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

const clientProvider = getClient(KMS, { credentials })

// Define an AWS KMS keyring. For details, see [kms\_simple.ts](https://github.com/aws/aws-encryption-sdk-javascript/blob/master/modules/example-browser/src/kms_simple.ts).
const kmsKeyring = new KmsKeyringBrowser({ generatorKeyId: exampleKey })

// Define a Raw AES keyring. For details, see [aes\_simple.ts](https://github.com/aws/aws-encryption-sdk-javascript/blob/master/modules/example-browser/src/aes_simple.ts).
const aesKeyring = new RawAesKeyringWebCrypto({ keyName, keyNamespace, wrappingSuite, masterKey })
```

------
#### [ JavaScript Node.js ]

The following example uses the `buildClient` function to specify the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. You can also use the `buildClient` to limit the number of encrypted data keys in an encrypted message. For more information, see [Limiting encrypted data keys](configure.md#config-limit-keys).

```
import {
  MultiKeyringNode,
  KmsKeyringNode,
  RawAesKeyringNode,
  RawAesWrappingSuiteIdentifier,
  buildClient,
  CommitmentPolicy,
} from '@aws-crypto/client-node'

const { encrypt, decrypt } = buildClient(
  CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

// Define an AWS KMS keyring. For details, see [kms\_simple.ts](https://github.com/aws/aws-encryption-sdk-javascript/blob/master/modules/example-node/src/kms_simple.ts).
const kmsKeyring = new KmsKeyringNode({ generatorKeyId: exampleKey })

// Define a Raw AES keyring. For details, see [raw\_aes\_keyring\_node.ts](https://github.com/aws/aws-encryption-sdk-javascript/blob/master/modules/raw-aes-keyring-node/src/raw_aes_keyring_node.ts).
const aesKeyring = new RawAesKeyringNode({ keyName, keyNamespace, wrappingSuite, unencryptedMasterKey })
```

------
#### [ Java ]

```
// Define the raw AES keyring.
final MaterialProviders matProv = MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();
final CreateRawAesKeyringInput createRawAesKeyringInput = CreateRawAesKeyringInput.builder()
        .keyName("AES_256_012")
        .keyNamespace("HSM_01")
        .wrappingKey(AESWrappingKey)
        .wrappingAlg(AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16)
        .build();
IKeyring rawAesKeyring = matProv.CreateRawAesKeyring(createRawAesKeyringInput);

// Define the AWS KMS keyring.
final CreateAwsKmsMrkMultiKeyringInput createAwsKmsMrkMultiKeyringInput = CreateAwsKmsMrkMultiKeyringInput.builder()
        .generator(kmsKeyArn)
        .build();
IKeyring awsKmsMrkMultiKeyring = matProv.CreateAwsKmsMrkMultiKeyring(createAwsKmsMrkMultiKeyringInput);
```

------
#### [ Python ]

The following example instantiates the AWS Encryption SDK client with the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`.

```
# Create the AWS KMS keyring
kms_client = boto3.client('kms', region_name="us-west-2")

mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
    config=MaterialProvidersConfig()
)

kms_keyring_input: CreateAwsKmsKeyringInput = CreateAwsKmsKeyringInput(
    generator={{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}},
    kms_client=kms_client
)

kms_keyring: IKeyring = mat_prov.create_aws_kms_keyring(
    input=kms_keyring_input
)

# Create Raw AES keyring
key_name_space = "{{HSM_01}}"
key_name = "{{AES_256_012}}"

raw_aes_keyring_input: CreateRawAesKeyringInput = CreateRawAesKeyringInput(
    key_namespace=key_name_space,
    key_name=key_name,
    wrapping_key={{AESWrappingKey}},
    wrapping_alg=AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16
)

raw_aes_keyring: IKeyring = mat_prov.create_raw_aes_keyring(
    input=raw_aes_keyring_input
)
```

------
#### [ Rust ]

```
// Instantiate the AWS Encryption SDK client
let esdk_config = AwsEncryptionSdkConfig::builder().build()?;
let esdk_client = esdk_client::Client::from_conf(esdk_config)?;

// Create the AWS KMS client
let sdk_config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
let kms_client = aws_sdk_kms::Client::new(&sdk_config);

// Instantiate the material providers library
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

// Create an AWS KMS keyring
let kms_keyring = mpl
    .create_aws_kms_keyring()
    .kms_key_id(kms_key_id)
    .kms_client(kms_client)
    .send()
    .await?;

// Create a Raw AES keyring
let key_namespace: &str = "my-key-namespace";
let key_name: &str = "my-aes-key-name";

let raw_aes_keyring = mpl
    .create_raw_aes_keyring()
    .key_name(key_name)
    .key_namespace(key_namespace)
    .wrapping_key(aws_smithy_types::Blob::new({{AESWrappingKey}}))
    .wrapping_alg(AesWrappingAlg::AlgAes256GcmIv12Tag16)
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

// Instantiate the material providers library
matProv, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
if err != nil {
    panic(err)
}

// Create an AWS KMS keyring
awsKmsKeyringInput := mpltypes.CreateAwsKmsKeyringInput{
    KmsClient: kmsClient,
    KmsKeyId:  kmsKeyId,
}
awsKmsKeyring, err := matProv.CreateAwsKmsKeyring(context.Background(), awsKmsKeyringInput)
if err != nil {
    panic(err)
}

// Create a Raw AES keyring
var keyNamespace = "my-key-namespace"
var keyName = "my-aes-key-name"

aesKeyRingInput := mpltypes.CreateRawAesKeyringInput{
    KeyName:      keyName,
    KeyNamespace: keyNamespace,
    WrappingKey:  {{AESWrappingKey}},
    WrappingAlg:  mpltypes.AesWrappingAlgAlgAes256GcmIv12Tag16,
}
aesKeyring, err := matProv.CreateRawAesKeyring(context.Background(), aesKeyRingInput)
```

------

Next, create the multi-keyring and specify its generator keyring, if any. In this example, we create a multi-keyring in which the AWS KMS keyring is the generator keyring and the AES keyring is the child keyring.

------
#### [ C ]

In the multi-keyring constructor in C, you specify only its generator keyring.

```
struct aws_cryptosdk_keyring *multi_keyring = aws_cryptosdk_multi_keyring_new(alloc, kms_keyring);
```

To add a child keyring to your multi-keyring, use the `aws_cryptosdk_multi_keyring_add_child` method. You need to call the method once for each child keyring that you add.

```
// Add the Raw AES keyring (C only)
aws_cryptosdk_multi_keyring_add_child(multi_keyring, aes_keyring);
```

------
#### [ C\# / .NET ]

 The .NET `CreateMultiKeyringInput` constructor lets you define a generator keyring and child keyrings. The resulting `CreateMultiKeyringInput` object is immutable.

```
var createMultiKeyringInput = new CreateMultiKeyringInput
{
    Generator = kmsKeyring,
    ChildKeyrings = new List<IKeyring>() {aesKeyring}
};

var multiKeyring = materialProviders.CreateMultiKeyring(createMultiKeyringInput);
```

------
#### [ JavaScript Browser ]

JavaScript multi-keyrings are immutable. The JavaScript multi-keyring constructor lets you specify the generator keyring and multiple child keyrings.

```
const clientProvider = getClient(KMS, { credentials })

const multiKeyring = new MultiKeyringWebCrypto(generator: kmsKeyring, children: [aesKeyring]);
```

------
#### [ JavaScript Node.js ]

JavaScript multi-keyrings are immutable. The JavaScript multi-keyring constructor lets you specify the generator keyring and multiple child keyrings.

```
const multiKeyring = new MultiKeyringNode(generator: kmsKeyring, children: [aesKeyring]);
```

------
#### [ Java ]

The Java `CreateMultiKeyringInput` constructor lets you define a generator keyring and child keyrings. The resulting `createMultiKeyringInput` object is immutable.

```
final CreateMultiKeyringInput createMultiKeyringInput = CreateMultiKeyringInput.builder()
        .generator(awsKmsMrkMultiKeyring)
        .childKeyrings(Collections.singletonList(rawAesKeyring))
        .build();
IKeyring multiKeyring = matProv.CreateMultiKeyring(createMultiKeyringInput);
```

------
#### [ Python ]

```
multi_keyring_input: CreateMultiKeyringInput = CreateMultiKeyringInput(
    generator=kms_keyring,
    child_keyrings=[raw_aes_keyring]
)

multi_keyring: IKeyring = mat_prov.create_multi_keyring(
    input=multi_keyring_input
)
```

------
#### [ Rust ]

```
let multi_keyring = mpl
    .create_multi_keyring()
    .generator(kms_keyring.clone())
    .child_keyrings(vec![raw_aes_keyring.clone()])
    .send()
    .await?;
```

------
#### [ Go ]

```
createMultiKeyringInput := mpltypes.CreateMultiKeyringInput{
		Generator:     awsKmsKeyring,
		ChildKeyrings: []mpltypes.IKeyring{rawAESKeyring},
	}
	multiKeyring, err := matProv.CreateMultiKeyring(context.Background(), createMultiKeyringInput)
	if err != nil {
		panic(err)
	}
```

------

Now, you can use the multi-keyring to encrypt and decrypt data.
