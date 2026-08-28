---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-kms-ecdh-keyring.html
---

# AWS KMS ECDH keyrings
<a name="use-kms-ecdh-keyring"></a>

An AWS KMS ECDH keyring uses asymmetric key agreement [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-types.html) to derive a shared symmetric wrapping key between two parties. First, the keyring uses the Elliptic Curve Diffie-Hellman (ECDH) key agreement algorithm to derive a shared secret from the private key in the sender's KMS key pair and the recipient's public key. Then, the keyring uses the shared secret to derive the shared wrapping key that protects your data encryption keys. The key derivation function that the AWS Encryption SDK uses (`KDF_CTR_HMAC_SHA384`) to derive the shared wrapping key conforms to [NIST recommendations for key derivation](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-108r1-upd1.pdf).

The key derivation function returns 64 bytes of keying material. To ensure that both parties use the correct keying material, the AWS Encryption SDK uses the first 32 bytes as a commitment key and the last 32 bytes as the shared wrapping key. On decrypt, if the keyring cannot reproduce the same commitment key and shared wrapping key that is stored on the message header ciphertext, the operation fails. For example, if you encrypt data with a keyring configured with **Alice's** private key and **Bob's** public key, a keyring configured with **Bob's** private key and **Alice's** public key will reproduce the same commitment key and shared wrapping key and be able to decrypt the data. If Bob's public key is not from a KMS key pair, then Bob can create a [Raw ECDH keyring](use-raw-ecdh-keyring.md) to decrypt the data.

The AWS KMS ECDH keyring encrypts data with a symmetric key using AES-GCM. The data key is then envelope encrypted with the derived shared wrapping key using AES-GCM. Each AWS KMS ECDH keyring can have only one shared wrapping key, but you can include multiple AWS KMS ECDH keyrings, alone or with other keyrings, in a [multi-keyring](use-multi-keyring.md).

**Programming language compatibility**
The AWS KMS ECDH keyring is introduced in version 1.5.0 of the [Cryptographic Material Providers Library](https://github.com/aws/aws-cryptographic-material-providers-library) (MPL) and is supported by the following programming languages and versions:
+ Version 3.*x* of the AWS Encryption SDK for Java
+ Version 4.*x* and later of the AWS Encryption SDK for .NET
+ Version 4.*x* of the AWS Encryption SDK for Python, when used with the optional MPL dependency.
+ Version 1.*x* of the AWS Encryption SDK for Rust
+ Version 0.1.*x* or later of the AWS Encryption SDK for Go

**Topics**
+ [Required permissions for AWS KMS ECDH keyrings](#kms-ecdh-permissions)
+ [Creating an AWS KMS ECDH keyring](#kms-ecdh-create)
+ [Creating an AWS KMS ECDH discovery keyring](#kms-ecdh-discovery)

## Required permissions for AWS KMS ECDH keyrings
<a name="kms-ecdh-permissions"></a>

The AWS Encryption SDK doesn't require an AWS account and it doesn't depend on any AWS service. However, to use an AWS KMS ECDH keyring, you need an AWS account and the following minimum permissions on the AWS KMS keys in your keyring. The permissions vary based on which key agreement schema you use.
+ To encrypt and decrypt data using the `KmsPrivateKeyToStaticPublicKey` key agreement schema, you need [kms:GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) and [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) on the *sender's* asymmetric KMS key pair. If you directly provide the sender's DER-encoded public key when you instantiate your keyring, you only need [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) permission on the sender's asymmetric KMS key pair.
+ To decrypt data using the `KmsPublicKeyDiscovery` key agreement schema, you need [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) and [kms:GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) permissions on the specified asymmetric KMS key pair.

## Creating an AWS KMS ECDH keyring
<a name="kms-ecdh-create"></a>

To create an AWS KMS ECDH keyring that encrypts and decrypts data, you must use the `KmsPrivateKeyToStaticPublicKey` key agreement schema. To initialize an AWS KMS ECDH keyring with the `KmsPrivateKeyToStaticPublicKey` key agreement schema, provide the following values:
+ **Sender's AWS KMS key ID**

  Must identify an asymmetric NIST-recommended elliptic curve (ECC) KMS key pair with a `KeyUsage` value of `KEY_AGREEMENT`. The sender's private key is used to derive the shared secret.
+ **(Optional) Sender's public key**

  Must be a DER-encoded X.509 public key, also known as `SubjectPublicKeyInfo` (SPKI), as defined in [RFC 5280](https://tools.ietf.org/html/rfc5280).

  The AWS KMS [GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) operation returns the public key of an asymmetric KMS key pair in the required DER-encoded format.

  To reduce the number of AWS KMS calls that your keyring makes, you can directly provide the sender's public key. If no value is provided for the sender's public key, the keyring calls AWS KMS to retrieve the sender's public key.
+ **Recipient's public key**

  You must provide the recipient's DER-encoded X.509 public key, also known as `SubjectPublicKeyInfo` (SPKI), as defined in [RFC 5280](https://tools.ietf.org/html/rfc5280).

  The AWS KMS [GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) operation returns the public key of an asymmetric KMS key pair in the required DER-encoded format.
+ **Curve specification**

  Identifies the elliptic curve specification in the specified key pairs. Both the sender and recipient's key pairs must have the same curve specification.

  Valid values: `ECC_NIST_P256`, `ECC_NIS_P384`, `ECC_NIST_P512`
+ **(Optional) A list of Grant Tokens**

  If you control access to the KMS key in your AWS KMS ECDH keyring with [grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html), you must provide all necessary grant tokens when you initialize the keyring.

------
#### [ C\# / .NET ]

The following example creates an AWS KMS ECDH keyring with the with the sender's KMS key, the sender's public key, and the recipient's public key. This example uses the optional `SenderPublicKey` parameter to provide the sender's public key. If you do not provide the sender's public key, the keyring calls AWS KMS to retrieve the sender's public key. Both the sender and recipient's key pairs are on the `ECC_NIST_P256` curve.

```
// Instantiate material providers
var materialProviders = new MaterialProviders(new MaterialProvidersConfig());

// Must be DER-encoded X.509 public keys
var BobPublicKey = new MemoryStream(new byte[] { });
var AlicePublicKey = new MemoryStream(new byte[] { });

// Create the AWS KMS ECDH static keyring
var staticConfiguration = new KmsEcdhStaticConfigurations
{
    KmsPrivateKeyToStaticPublicKey = new KmsPrivateKeyToStaticPublicKeyInput
    {
        SenderKmsIdentifier = "{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}",
        SenderPublicKey = BobPublicKey,
        RecipientPublicKey = AlicePublicKey
    }
};

var createKeyringInput = new CreateAwsKmsEcdhKeyringInput
{
    CurveSpec = ECDHCurveSpec.{{ECC_NIST_P256}},
    KmsClient = new AmazonKeyManagementServiceClient(),
    KeyAgreementScheme = staticConfiguration
};

var keyring = materialProviders.CreateAwsKmsEcdhKeyring(createKeyringInput);
```

------
#### [ Java ]

The following example creates an AWS KMS ECDH keyring with the with the sender's KMS key, the sender's public key, and the recipient's public key. This example uses the optional `senderPublicKey` parameter to provide the sender's public key. If you do not provide the sender's public key, the keyring calls AWS KMS to retrieve the sender's public key. Both the sender and recipient's key pairs are on the `ECC_NIST_P256` curve.

```
// Retrieve public keys
// Must be DER-encoded X.509 public keys
ByteBuffer BobPublicKey = getPublicKeyBytes("{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}");
        ByteBuffer AlicePublicKey = getPublicKeyBytes("{{arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321}}");

// Create the AWS KMS ECDH static keyring
        final CreateAwsKmsEcdhKeyringInput senderKeyringInput =
          CreateAwsKmsEcdhKeyringInput.builder()
            .kmsClient(KmsClient.create())
            .curveSpec(ECDHCurveSpec.{{ECC_NIST_P256}})
            .KeyAgreementScheme(
              KmsEcdhStaticConfigurations.builder()
                .KmsPrivateKeyToStaticPublicKey(
                  KmsPrivateKeyToStaticPublicKeyInput.builder()
                    .senderKmsIdentifier("{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}")
                    .senderPublicKey(BobPublicKey)
                    .recipientPublicKey(AlicePublicKey)
                    .build()).build()).build();
```

------
#### [ Python ]

The following example creates an AWS KMS ECDH keyring with the with the sender's KMS key, the sender's public key, and the recipient's public key. This example uses the optional `senderPublicKey` parameter to provide the sender's public key. If you do not provide the sender's public key, the keyring calls AWS KMS to retrieve the sender's public key. Both the sender and recipient's key pairs are on the `ECC_NIST_P256` curve.

```
import boto3
from aws_cryptographic_materialproviders.mpl.models import (
    CreateAwsKmsEcdhKeyringInput,
    KmsEcdhStaticConfigurationsKmsPrivateKeyToStaticPublicKey,
    KmsPrivateKeyToStaticPublicKeyInput,
)
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models import ECDHCurveSpec

# Instantiate the material providers library
mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
    config=MaterialProvidersConfig()
)

# Retrieve public keys
# Must be DER-encoded X.509 public keys
bob_public_key = get_public_key_bytes("{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}")
alice_public_key = get_public_key_bytes("{{arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321}}")

# Create the AWS KMS ECDH static keyring
sender_keyring_input = CreateAwsKmsEcdhKeyringInput(
    kms_client = boto3.client('kms', region_name="us-west-2"),
    curve_spec = ECDHCurveSpec.{{ECC_NIST_P256}},
    key_agreement_scheme = KmsEcdhStaticConfigurationsKmsPrivateKeyToStaticPublicKey(
        KmsPrivateKeyToStaticPublicKeyInput(
            sender_kms_identifier = "{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}",
            sender_public_key = bob_public_key,
            recipient_public_key = alice_public_key,

        )
    )
)

keyring = mat_prov.create_aws_kms_ecdh_keyring(sender_keyring_input)
```

------
#### [ Rust ]

The following example creates an AWS KMS ECDH keyring with the with the sender's KMS key, the sender's public key, and the recipient's public key. This example uses the optional `sender_public_key` parameter to provide the sender's public key. If you do not provide the sender's public key, the keyring calls AWS KMS to retrieve the sender's public key.

```
// Instantiate the AWS Encryption SDK client
let esdk_config = AwsEncryptionSdkConfig::builder().build()?;
let esdk_client = esdk_client::Client::from_conf(esdk_config)?;

// Create the AWS KMS client
let sdk_config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
let kms_client = aws_sdk_kms::Client::new(&sdk_config);

// Optional: Create your encryption context
let encryption_context = HashMap::from([
    ("encryption".to_string(), "context".to_string()),
    ("is not".to_string(), "secret".to_string()),
    ("but adds".to_string(), "useful metadata".to_string()),
    ("that can help you".to_string(), "be confident that".to_string()),
    ("the data you are handling".to_string(), "is what you think it is".to_string()),
]);

// Retrieve public keys
// Must be DER-encoded X.509 keys
let public_key_file_content_sender = std::fs::read_to_string(Path::new(EXAMPLE_KMS_ECC_PUBLIC_KEY_FILENAME_SENDER))?;
let parsed_public_key_file_content_sender = parse(public_key_file_content_sender)?;
let public_key_sender_utf8_bytes = parsed_public_key_file_content_sender.contents();

let public_key_file_content_recipient = std::fs::read_to_string(Path::new(EXAMPLE_KMS_ECC_PUBLIC_KEY_FILENAME_RECIPIENT))?;
let parsed_public_key_file_content_recipient = parse(public_key_file_content_recipient)?;
let public_key_recipient_utf8_bytes = parsed_public_key_file_content_recipient.contents();

// Create KmsPrivateKeyToStaticPublicKeyInput
let kms_ecdh_static_configuration_input =
    KmsPrivateKeyToStaticPublicKeyInput::builder()
        .sender_kms_identifier({{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}})
        // Must be a UTF8 DER-encoded X.509 public key
        .sender_public_key(public_key_sender_utf8_bytes)
        // Must be a UTF8 DER-encoded X.509 public key
        .recipient_public_key(public_key_recipient_utf8_bytes)
        .build()?;

let kms_ecdh_static_configuration = KmsEcdhStaticConfigurations::KmsPrivateKeyToStaticPublicKey(kms_ecdh_static_configuration_input);

// Instantiate the material providers library
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

// Create AWS KMS ECDH keyring
let kms_ecdh_keyring = mpl
    .create_aws_kms_ecdh_keyring()
    .kms_client(kms_client)
    .curve_spec(ecdh_curve_spec)
    .key_agreement_scheme(kms_ecdh_static_configuration)
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

// Retrieve public keys
// Must be DER-encoded X.509 keys
publicKeySender, err := utils.LoadPublicKeyFromPEM(kmsEccPublicKeyFileNameSender)
if err != nil {
    panic(err)
}
publicKeyRecipient, err := utils.LoadPublicKeyFromPEM(kmsEccPublicKeyFileNameRecipient)
if err != nil {
    panic(err)
}

// Create KmsPrivateKeyToStaticPublicKeyInput
kmsEcdhStaticConfigurationInput := mpltypes.KmsPrivateKeyToStaticPublicKeyInput{
    RecipientPublicKey:  publicKeyRecipient,
    SenderKmsIdentifier: {{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}},
    SenderPublicKey:     publicKeySender,
}
kmsEcdhStaticConfiguration := &mpltypes.KmsEcdhStaticConfigurationsMemberKmsPrivateKeyToStaticPublicKey{
    Value: kmsEcdhStaticConfigurationInput,
}

// Instantiate the material providers library
matProv, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
if err != nil {
    panic(err)
}

// Create AWS KMS ECDH keyring
awsKmsEcdhKeyringInput := mpltypes.CreateAwsKmsEcdhKeyringInput{
    CurveSpec:          ecdhCurveSpec,
    KeyAgreementScheme: kmsEcdhStaticConfiguration,
    KmsClient:          kmsClient,
}
awsKmsEcdhKeyring, err := matProv.CreateAwsKmsEcdhKeyring(context.Background(), awsKmsEcdhKeyringInput)
if err != nil {
    panic(err)
}
```

------

## Creating an AWS KMS ECDH discovery keyring
<a name="kms-ecdh-discovery"></a>

When decrypting, it's a best practice to specify the keys that the AWS Encryption SDK can use. To follow this best practice, use an AWS KMS ECDH keyring with the `KmsPrivateKeyToStaticPublicKey` key agreement schema. However, you can also create an AWS KMS ECDH discovery keyring, that is, an AWS KMS ECDH keyring that can decrypt any message where the public key of the specified KMS key pair matches the *recipient's* public key stored on the message ciphertext.

**Important**
When you decrypt messages using the `KmsPublicKeyDiscovery` key agreement schema, you accept all public keys, regardless of who owns it.

To initialize an AWS KMS ECDH keyring with the `KmsPublicKeyDiscovery` key agreement schema, provide the following values:
+ **Recipient's AWS KMS key ID**

  Must identify an asymmetric NIST-recommended elliptic curve (ECC) KMS key pair with a `KeyUsage` value of `KEY_AGREEMENT`.
+ **Curve specification**

  Identifies the elliptic curve specification in the recipient's KMS key pair.

  Valid values: `ECC_NIST_P256`, `ECC_NIS_P384`, `ECC_NIST_P512`
+ **(Optional) A list of Grant Tokens**

  If you control access to the KMS key in your AWS KMS ECDH keyring with [grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html), you must provide all necessary grant tokens when you initialize the keyring.

------
#### [ C\# / .NET ]

The following example creates an AWS KMS ECDH discovery keyring with a KMS key pair on the `ECC_NIST_P256` curve. You must have [kms:GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) and [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) permissions on the specified KMS key pair. This keyring can decrypt any message where the public key of the specified KMS key pair matches the recipient's public key stored on the message ciphertext.

```
// Instantiate material providers
var materialProviders = new MaterialProviders(new MaterialProvidersConfig());

// Create the AWS KMS ECDH discovery keyring
var discoveryConfiguration = new KmsEcdhStaticConfigurations
{
    KmsPublicKeyDiscovery = new KmsPublicKeyDiscoveryInput
    {
        RecipientKmsIdentifier = "{{arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321}}"
    }

};
var createKeyringInput = new CreateAwsKmsEcdhKeyringInput
{
    CurveSpec = ECDHCurveSpec.{{ECC_NIST_P256}},
    KmsClient = new AmazonKeyManagementServiceClient(),
    KeyAgreementScheme = discoveryConfiguration
};
var keyring = materialProviders.CreateAwsKmsEcdhKeyring(createKeyringInput);
```

------
#### [ Java ]

The following example creates an AWS KMS ECDH discovery keyring with a KMS key pair on the `ECC_NIST_P256` curve. You must have [kms:GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) and [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) permissions on the specified KMS key pair. This keyring can decrypt any message where the public key of the specified KMS key pair matches the recipient's public key stored on the message ciphertext.

```
// Create the AWS KMS ECDH discovery keyring
final CreateAwsKmsEcdhKeyringInput recipientKeyringInput =
  CreateAwsKmsEcdhKeyringInput.builder()
    .kmsClient(KmsClient.create())
    .curveSpec(ECDHCurveSpec.{{ECC_NIST_P256}})
    .KeyAgreementScheme(
      KmsEcdhStaticConfigurations.builder()
        .KmsPublicKeyDiscovery(
          KmsPublicKeyDiscoveryInput.builder()
            .recipientKmsIdentifier("{{arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321}}").build()
        ).build())
    .build();
```

------
#### [ Python ]

The following example creates an AWS KMS ECDH discovery keyring with a KMS key pair on the `ECC_NIST_P256` curve. You must have [kms:GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) and [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) permissions on the specified KMS key pair. This keyring can decrypt any message where the public key of the specified KMS key pair matches the recipient's public key stored on the message ciphertext.

```
import boto3
from aws_cryptographic_materialproviders.mpl.models import (
    CreateAwsKmsEcdhKeyringInput,
    KmsEcdhStaticConfigurationsKmsPublicKeyDiscovery,
    KmsPublicKeyDiscoveryInput,
)
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models import ECDHCurveSpec

# Instantiate the material providers library
mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
    config=MaterialProvidersConfig()
)

# Create the AWS KMS ECDH discovery keyring
create_keyring_input = CreateAwsKmsEcdhKeyringInput(
    kms_client = boto3.client('kms', region_name="us-west-2"),
    curve_spec = ECDHCurveSpec.{{ECC_NIST_P256}},
    key_agreement_scheme = KmsEcdhStaticConfigurationsKmsPublicKeyDiscovery(
        KmsPublicKeyDiscoveryInput(
            recipient_kms_identifier = "{{arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321}}",
        )
    )
)

keyring = mat_prov.create_aws_kms_ecdh_keyring(create_keyring_input)
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

// Optional: Create your encryption context
let encryption_context = HashMap::from([
    ("encryption".to_string(), "context".to_string()),
    ("is not".to_string(), "secret".to_string()),
    ("but adds".to_string(), "useful metadata".to_string()),
    ("that can help you".to_string(), "be confident that".to_string()),
    ("the data you are handling".to_string(), "is what you think it is".to_string()),
]);

// Create KmsPublicKeyDiscoveryInput
let kms_ecdh_discovery_static_configuration_input =
    KmsPublicKeyDiscoveryInput::builder()
        .recipient_kms_identifier(ecc_recipient_key_arn)
        .build()?;

let kms_ecdh_discovery_static_configuration = KmsEcdhStaticConfigurations::KmsPublicKeyDiscovery(kms_ecdh_discovery_static_configuration_input);

// Instantiate the material providers library
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

// Create AWS KMS ECDH discovery keyring
let kms_ecdh_discovery_keyring = mpl
    .create_aws_kms_ecdh_keyring()
    .kms_client(kms_client.clone())
    .curve_spec(ecdh_curve_spec)
    .key_agreement_scheme(kms_ecdh_discovery_static_configuration)
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

// Create KmsPublicKeyDiscoveryInput
kmsEcdhDiscoveryStaticConfigurationInput := mpltypes.KmsPublicKeyDiscoveryInput{
    RecipientKmsIdentifier: eccRecipientKeyArn,
}
kmsEcdhDiscoveryStaticConfiguration := &mpltypes.KmsEcdhStaticConfigurationsMemberKmsPublicKeyDiscovery{
    Value: kmsEcdhDiscoveryStaticConfigurationInput,
}

// Instantiate the material providers library
matProv, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
if err != nil {
    panic(err)
}

// Create AWS KMS ECDH discovery keyring
awsKmsEcdhDiscoveryKeyringInput := mpltypes.CreateAwsKmsEcdhKeyringInput{
    CurveSpec:          ecdhCurveSpec,
    KeyAgreementScheme: kmsEcdhDiscoveryStaticConfiguration,
    KmsClient:          kmsClient,
}
awsKmsEcdhDiscoveryKeyring, err := matProv.CreateAwsKmsEcdhKeyring(context.Background(), awsKmsEcdhDiscoveryKeyringInput)
if err != nil {
    panic(err)
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
