---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-raw-aes-keyring.html
---

# Raw AES keyrings
<a name="use-raw-aes-keyring"></a>

The AWS Encryption SDK lets you use an AES symmetric key that you provide as a wrapping key that protects your data key. You need to generate, store, and protect the key material, preferably in a hardware security module (HSM) or key management system. Use a Raw AES keyring when you need to provide the wrapping key and encrypt the data keys locally or offline.

The Raw AES keyring encrypts data by using the AES-GCM algorithm and a wrapping key that you specify as a byte array. You can specify only one wrapping key in each Raw AES keyring, but you can include multiple Raw AES keyrings, alone or with other keyrings, in a [multi-keyring](use-multi-keyring.md).

The Raw AES keyring is equivalent to and interoperates with the [JceMasterKey](https://aws.github.io/aws-encryption-sdk-java/com/amazonaws/encryptionsdk/jce/JceMasterKey.html) class in the AWS Encryption SDK for Java and the [RawMasterKey](https://aws-encryption-sdk-python.readthedocs.io/en/latest/generated/aws_encryption_sdk.key_providers.raw.html#aws_encryption_sdk.key_providers.raw.RawMasterKey) class in the AWS Encryption SDK for Python when they are used with an AES encryption keys. You can encrypt data with one implementation and decrypt the data with any other implementation using the same wrapping key. For details, see [Keyring compatibility](choose-keyring.md#keyring-compatibility).

**Key namespaces and names**

To identify the AES key in a keyring, the Raw AES keyring uses a *key namespace* and *key name* that you provide. These values are not secret. They appear in plain text in the header of the [encrypted message](concepts.md#message) that the encrypt operation returns. We recommend using a key namespace your HSM or key management system and a key name that identifies the AES key in that system.

**Note**
The key namespace and key name are equivalent to the *Provider ID* (or *Provider*) and *Key ID* fields in the `JceMasterKey` and `RawMasterKey`.
The AWS Encryption SDK for C and AWS Encryption SDK for .NET reserve the `aws-kms` key namespace value for KMS keys. Do not use this namespace value in a Raw AES keyring or Raw RSA keyring with these libraries.

If you construct different keyrings to encrypt and decrypt a given message, the namespace and name values are critical. If the key namespace and key name in the decryption keyring isn't an exact, case-sensitive match for the key namespace and key name in the encryption keyring, the decryption keyring isn't used, even if the key material bytes are identical.

For example, you might define a Raw AES keyring with key namespace `HSM_01` and key name `AES_256_012`. Then, you use that keyring to encrypt some data. To decrypt that data, construct a Raw AES keyring with the same key namespace, key name, and key material.

The following examples show how to create a Raw AES keyring. The `AESWrappingKey` variable represents the key material you provide.

------
#### [ C ]

To instantiate a Raw AES keyring in the AWS Encryption SDK for C, use `aws_cryptosdk_raw_aes_keyring_new()`. For a complete example, see [raw\_aes\_keyring.c](https://github.com/aws/aws-encryption-sdk-c/blob/master/examples/raw_aes_keyring.c).

```
struct aws_allocator *alloc = aws_default_allocator();

AWS_STATIC_STRING_FROM_LITERAL(wrapping_key_namespace, "HSM_01");
AWS_STATIC_STRING_FROM_LITERAL(wrapping_key_name, "AES_256_012");

struct aws_cryptosdk_keyring *raw_aes_keyring = aws_cryptosdk_raw_aes_keyring_new(
        alloc, wrapping_key_namespace, wrapping_key_name, {{aes_wrapping_key}}, wrapping_key_len);
```

------
#### [ C\# / .NET ]

To create a Raw AES keyring in AWS Encryption SDK for .NET, use the `materialProviders.CreateRawAesKeyring()` method. For a complete example, see [RawAESKeyringExample.cs](https://github.com/aws/aws-encryption-sdk/tree/mainline/AwsEncryptionSDK/runtimes/net/Examples/Keyring/RawAESKeyringExample.cs).

The following example uses version 4.*x* and later of the AWS Encryption SDK for .NET.

```
// Instantiate the AWS Encryption SDK and material providers
var esdk =  new ESDK(new AwsEncryptionSdkConfig());
var mpl = new MaterialProviders(new MaterialProvidersConfig());

var keyNamespace = "HSM_01";
var keyName = "AES_256_012";

// This example uses the key generator in Bouncy Castle to generate the key material.
// In production, use key material from a secure source.
var aesWrappingKey = new MemoryStream(GeneratorUtilities.GetKeyGenerator("AES256").GenerateKey());

// Create the keyring that determines how your data keys are protected.
var createKeyringInput = new CreateRawAesKeyringInput
{
    KeyNamespace = keyNamespace,
    KeyName = keyName,
    WrappingKey = {{aesWrappingKey}},
    WrappingAlg = AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16
};

var keyring = materialProviders.CreateRawAesKeyring(createKeyringInput);
```

------
#### [ JavaScript Browser ]

The AWS Encryption SDK for JavaScript in the browser gets its cryptographic primitives from the [WebCrypto](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API) API. Before you construct the keyring, you must use `RawAesKeyringWebCrypto.importCryptoKey()` to import the raw key material into the WebCrypto backend. This assures that the keyring is complete even though all calls to WebCrypto are asynchronous.

Then, to instantiate a Raw AES keyring, use the `RawAesKeyringWebCrypto()` method. You must specify the AES wrapping algorithm ("wrapping suite) based on the length of your key material. For a complete example, see [aes\_simple.ts (JavaScript Browser)](https://github.com/aws/aws-encryption-sdk-javascript/blob/master/modules/example-browser/src/aes_simple.ts).

The following example uses the `buildClient` function to specify the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. You can also use the `buildClient` to limit the number of encrypted data keys in an encrypted message. For more information, see [Limiting encrypted data keys](configure.md#config-limit-keys).

```
import {
  RawAesWrappingSuiteIdentifier,
  RawAesKeyringWebCrypto,
  synchronousRandomValues,
  buildClient,
  CommitmentPolicy,
} from '@aws-crypto/client-browser'

const { encrypt, decrypt } = buildClient(
  CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

const keyNamespace = '{{HSM_01}}'
const keyName = '{{AES_256_012}}'

const wrappingSuite =
  RawAesWrappingSuiteIdentifier.{{AES256_GCM_IV12_TAG16_NO_PADDING}}

/* Import the plaintext AES key into the WebCrypto backend. */
const aesWrappingKey = await RawAesKeyringWebCrypto.importCryptoKey(
  rawAesKey,
  wrappingSuite
)

const rawAesKeyring = new RawAesKeyringWebCrypto({
  keyName,
  keyNamespace,
  wrappingSuite,
  {{aesWrappingKey}}
})
```

------
#### [ JavaScript Node.js ]

To instantiate a Raw AES keyring in the AWS Encryption SDK for JavaScript for Node.js, create an instance of the ` RawAesKeyringNode` class. You must specify the AES wrapping algorithm ("wrapping suite") based on the length of your key material. For a complete example, see [aes\_simple.ts](https://github.com/aws/aws-encryption-sdk-javascript//blob/master/modules/example-node/src/aes_simple.ts) (JavaScript Node.js).

The following example uses the `buildClient` function to specify the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. You can also use the `buildClient` to limit the number of encrypted data keys in an encrypted message. For more information, see [Limiting encrypted data keys](configure.md#config-limit-keys).

```
import {
  RawAesKeyringNode,
  buildClient,
  CommitmentPolicy,
  RawAesWrappingSuiteIdentifier,
} from '@aws-crypto/client-node'

const { encrypt, decrypt } = buildClient(
  CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

const keyName = '{{AES_256_012}}'
const keyNamespace = '{{HSM_01}}'

const wrappingSuite =
  RawAesWrappingSuiteIdentifier.{{AES256_GCM_IV12_TAG16_NO_PADDING}}

const rawAesKeyring = new RawAesKeyringNode({
  keyName,
  keyNamespace,
  {{aesWrappingKey}},
  wrappingSuite,
})
```

------
#### [ Java ]

To instantiate a Raw AES keyring in the AWS Encryption SDK for Java, use `matProv.CreateRawAesKeyring()`.

```
final CreateRawAesKeyringInput keyringInput = CreateRawAesKeyringInput.builder()
        .keyName("{{AES_256_012}}")
        .keyNamespace("{{HSM_01}}")
        .wrappingKey({{AESWrappingKey}})
        .wrappingAlg(AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16)
        .build();
final MaterialProviders matProv = MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();
IKeyring rawAesKeyring = matProv.CreateRawAesKeyring(keyringInput);
```

------
#### [ Python ]

The following example instantiates the AWS Encryption SDK client with the [default commitment policy](migrate-commitment-policy.md), `REQUIRE_ENCRYPT_REQUIRE_DECRYPT`. For a complete example, see [raw\_aes\_keyring\_example.py](https://github.com/aws/aws-encryption-sdk-python/tree/master/examples/src/raw_aes_keyring_example.py) in the AWS Encryption SDK for Python repository in GitHub.

```
# Instantiate the AWS Encryption SDK client
client = aws_encryption_sdk.EncryptionSDKClient(
    commitment_policy=CommitmentPolicy.{{REQUIRE_ENCRYPT_REQUIRE_DECRYPT}}
)

# Define the key namespace and key name
key_name_space = "{{HSM_01}}"
key_name = "{{AES_256_012}}"

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

# Create Raw AES keyring
keyring_input: CreateRawAesKeyringInput = CreateRawAesKeyringInput(
    key_namespace=key_name_space,
    key_name=key_name,
    wrapping_key={{AESWrappingKey}},
    wrapping_alg=AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16
)

raw_aes_keyring: IKeyring = mat_prov.create_raw_aes_keyring(
    input=keyring_input
)
```

------
#### [ Rust ]

```
// Instantiate the AWS Encryption SDK client
let esdk_config = AwsEncryptionSdkConfig::builder().build()?;
let esdk_client = esdk_client::Client::from_conf(esdk_config)?;

// Define the key namespace and key name
let key_namespace: &str = "{{HSM_01}}";
let key_name: &str = "{{AES_256_012}}";

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

// Create Raw AES keyring
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
    mpl "aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygenerated"
	mpltypes "aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
    client "github.com/aws/aws-encryption-sdk/awscryptographyencryptionsdksmithygenerated"
    esdktypes "github.com/aws/aws-encryption-sdk/awscryptographyencryptionsdksmithygeneratedtypes"
)
//Instantiate the AWS Encryption SDK client.
encryptionClient, err := client.NewClient(esdktypes.AwsEncryptionSdkConfig{})
if err != nil {
    panic(err)
}
// Define the key namespace and key name
var keyNamespace = "A managed aes keys"
var keyName = "My 256-bit AES wrapping key"

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
// Create Raw AES keyring
aesKeyRingInput := mpltypes.CreateRawAesKeyringInput{
    KeyName:      keyName,
    KeyNamespace: keyNamespace,
    WrappingKey:  {{aesWrappingKey}},
    WrappingAlg:  mpltypes.AesWrappingAlgAlgAes256GcmIv12Tag16,
}
aesKeyring, err := matProv.CreateRawAesKeyring(context.Background(), aesKeyRingInput)
if err != nil {
    panic(err)
}
```

------
