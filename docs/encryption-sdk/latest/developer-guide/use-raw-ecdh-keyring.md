---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-raw-ecdh-keyring.html
---

# Raw ECDH keyrings
<a name="use-raw-ecdh-keyring"></a>

The Raw ECDH keyring uses the elliptic curve public-private key pairs that you provide to derive a shared wrapping key between two parties. First, the keyring derives a shared secret using the sender's private key, the recipient's public key, and the Elliptic Curve Diffie-Hellman (ECDH) key agreement algorithm. Then, the keyring uses the shared secret to derive the shared wrapping key that protects your data encryption keys. The key derivation function that the AWS Encryption SDK uses (`KDF_CTR_HMAC_SHA384`) to derive the shared wrapping key conforms to [NIST recommendations for key derivation](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-108r1-upd1.pdf).

The key derivation function returns 64 bytes of key material. To ensure that both parties use the correct key material, the AWS Encryption SDK uses the first 32 bytes as a commitment key and the last 32 bytes as the shared wrapping key. On decrypt, if the keyring cannot reproduce the same commitment key and shared wrapping key that is stored on the message header ciphertext, the operation fails. For example, if you encrypt data with a keyring configured with **Alice's** private key and **Bob's** public key, a keyring configured with **Bob's** private key and **Alice's** public key will reproduce the same commitment key and shared wrapping key and be able to decrypt the data. If Bob's public key is from an AWS KMS key pair, then Bob can create an [AWS KMS ECDH keyring](use-kms-ecdh-keyring.md) to decrypt the data.

The Raw ECDH keyring encrypts data with a symmetric key using AES-GCM. The data key is then envelope encrypted with the derived shared wrapping key using AES-GCM. Each Raw ECDH keyring can have only one shared wrapping key, but you can include multiple Raw ECDH keyrings, alone or with other keyrings, in a [multi-keyring](use-multi-keyring.md).

You are responsible for generating, storing, and protecting your private keys, preferably in a hardware security module (HSM) or key management system. The sender and recipient's key pairs much be on the same elliptic curve. The AWS Encryption SDK supports the following elliptic curve specifications:
+ `ECC_NIST_P256`
+ `ECC_NIST_P384`
+ `ECC_NIST_P512`

**Programming language compatibility**
The Raw ECDH keyring is introduced in version 1.5.0 of the [Cryptographic Material Providers Library](https://github.com/aws/aws-cryptographic-material-providers-library) (MPL) and is supported by the following programming languages and versions:
+ Version 3.*x* of the AWS Encryption SDK for Java
+ Version 4.*x* and later of the AWS Encryption SDK for .NET
+ Version 4.*x* of the AWS Encryption SDK for Python, when used with the optional MPL dependency.
+ Version 1.*x* of the AWS Encryption SDK for Rust
+ Version 0.1.*x* or later of the AWS Encryption SDK for Go

## Creating a Raw ECDH keyring
<a name="raw-ecdh-create"></a>

The Raw ECDH keyring supports three key agreement schemas: `RawPrivateKeyToStaticPublicKey`, `EphemeralPrivateKeyToStaticPublicKey`, and `PublicKeyDiscovery`. The key agreement schema that you select determines which cryptographic operations you can perform and how the keying materials are assembled.

**Topics**
+ [RawPrivateKeyToStaticPublicKey](#raw-ecdh-RawPrivateKeyToStaticPublicKey)
+ [EphemeralPrivateKeyToStaticPublicKey](#raw-ecdh-EphemeralPrivateKeyToStaticPublicKey)
+ [PublicKeyDiscovery](#raw-ecdh-PublicKeyDiscovery)

### RawPrivateKeyToStaticPublicKey
<a name="raw-ecdh-RawPrivateKeyToStaticPublicKey"></a>

Use the `RawPrivateKeyToStaticPublicKey` key agreement schema to statically configure the sender's private key and the recipient's public key in the keyring. This key agreement schema can encrypt and decrypt data.

To initialize a Raw ECDH keyring with the `RawPrivateKeyToStaticPublicKey` key agreement schema, provide the following values:
+ **Sender's private key**

  You must provide the sender's PEM-encoded private key (PKCS \#8 PrivateKeyInfo structures), as defined in [RFC 5958](https://tools.ietf.org/html/rfc5958#section-2).
+ **Recipient's public key**

  You must provide the recipient's DER-encoded X.509 public key, also known as `SubjectPublicKeyInfo` (SPKI), as defined in [RFC 5280](https://tools.ietf.org/html/rfc5280).

  You can specify the public key of an asymmetric key agreement KMS key pair or the public key from a key pair generated outside of AWS.
+ **Curve specification**

  Identifies the elliptic curve specification in the specified key pairs. Both the sender and recipient's key pairs must have the same curve specification.

  Valid values: `ECC_NIST_P256`, `ECC_NIS_P384`, `ECC_NIST_P512`

------
#### [ C\# / .NET ]

```
// Instantiate material providers
var materialProviders = new MaterialProviders(new MaterialProvidersConfig());
	    var BobPrivateKey = new MemoryStream(new byte[] { });
	    var AlicePublicKey = new MemoryStream(new byte[] { });

	    // Create the Raw ECDH static keyring
	    var staticConfiguration = new RawEcdhStaticConfigurations()
	    {
		    RawPrivateKeyToStaticPublicKey = new RawPrivateKeyToStaticPublicKeyInput
		    {
			    SenderStaticPrivateKey = BobPrivateKey,
			    RecipientPublicKey = AlicePublicKey
		    }
	    };

	    var createKeyringInput = new CreateRawEcdhKeyringInput()
	    {
		    CurveSpec = ECDHCurveSpec.{{ECC_NIST_P256}},
		    KeyAgreementScheme = staticConfiguration
	    };

	    var keyring = materialProviders.CreateRawEcdhKeyring(createKeyringInput);
```

------
#### [ Java ]

The following Java example uses the `RawPrivateKeyToStaticPublicKey` key agreement schema to statically configure the sender's private key and the recipient's public key. Both key pairs are on the `ECC_NIST_P256` curve.

```
private static void StaticRawKeyring() {
    // Instantiate material providers
    final MaterialProviders materialProviders =
      MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();

    KeyPair senderKeys = GetRawEccKey();
    KeyPair recipient = GetRawEccKey();

    // Create the Raw ECDH static keyring
    final CreateRawEcdhKeyringInput rawKeyringInput =
      CreateRawEcdhKeyringInput.builder()
        .curveSpec(ECDHCurveSpec.{{ECC_NIST_P256}})
        .KeyAgreementScheme(
          RawEcdhStaticConfigurations.builder()
            .RawPrivateKeyToStaticPublicKey(
                RawPrivateKeyToStaticPublicKeyInput.builder()
                  // Must be a PEM-encoded private key
                  .senderStaticPrivateKey(ByteBuffer.wrap(senderKeys.getPrivate().getEncoded()))
                  // Must be a DER-encoded X.509 public key
                  .recipientPublicKey(ByteBuffer.wrap(recipient.getPublic().getEncoded()))
                  .build()
            )
            .build()
        ).build();

    final IKeyring staticKeyring = materialProviders.CreateRawEcdhKeyring(rawKeyringInput);
}
```

------
#### [ Python ]

The following Python example uses the `RawEcdhStaticConfigurationsRawPrivateKeyToStaticPublicKey` key agreement schema to statically configure the sender's private key and the recipient's public key. Both key pairs are on the `ECC_NIST_P256` curve.

```
import boto3
from aws_cryptographic_materialproviders.mpl.models import (
    CreateRawEcdhKeyringInput,
    RawEcdhStaticConfigurationsRawPrivateKeyToStaticPublicKey,
    RawPrivateKeyToStaticPublicKeyInput,
)
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models import ECDHCurveSpec

# Instantiate the material providers library
mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
    config=MaterialProvidersConfig()
)

# Must be a PEM-encoded private key
bob_private_key = get_private_key_bytes()
# Must be a DER-encoded X.509 public key
alice_public_key = get_public_key_bytes()

# Create the raw ECDH static keyring
raw_keyring_input = CreateRawEcdhKeyringInput(
    curve_spec = ECDHCurveSpec.{{ECC_NIST_P256}},
    key_agreement_scheme = RawEcdhStaticConfigurationsRawPrivateKeyToStaticPublicKey(
        RawPrivateKeyToStaticPublicKeyInput(
            sender_static_private_key = bob_private_key,
            recipient_public_key = alice_public_key,
        )
    )
)

keyring = mat_prov.create_raw_ecdh_keyring(raw_keyring_input)
```

------
#### [ Rust ]

The following Python example uses the `raw_ecdh_static_configuration` key agreement schema to statically configure the sender's private key and the recipient's public key. Both key pairs must be on the same curve.

```
// Instantiate the AWS Encryption SDK client
let esdk_config = AwsEncryptionSdkConfig::builder().build()?;
let esdk_client = esdk_client::Client::from_conf(esdk_config)?;

// Optional: Create your encryption context
let encryption_context = HashMap::from([
    ("encryption".to_string(), "context".to_string()),
    ("is not".to_string(), "secret".to_string()),
    ("but adds".to_string(), "useful metadata".to_string()),
    ("that can help you".to_string(), "be confident that".to_string()),
    ("the data you are handling".to_string(), "is what you think it is".to_string()),
]);

// Create keyring input
let raw_ecdh_static_configuration_input =
    RawPrivateKeyToStaticPublicKeyInput::builder()
        // Must be a UTF8 PEM-encoded private key
        .sender_static_private_key(private_key_sender_utf8_bytes)
        // Must be a UTF8 DER-encoded X.509 public key
        .recipient_public_key(public_key_recipient_utf8_bytes)
        .build()?;

let raw_ecdh_static_configuration = RawEcdhStaticConfigurations::RawPrivateKeyToStaticPublicKey(raw_ecdh_static_configuration_input);

// Instantiate the material providers library
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

// Create raw ECDH static keyring
let raw_ecdh_keyring = mpl
    .create_raw_ecdh_keyring()
    .curve_spec(ecdh_curve_spec)
    .key_agreement_scheme(raw_ecdh_static_configuration)
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
)

// Instantiate the AWS Encryption SDK client
encryptionClient, err := client.NewClient(esdktypes.AwsEncryptionSdkConfig{})
if err != nil {
    panic(err)
}

// Optional: Create your encryption context
encryptionContext := map[string]string{
    "encryption":                "context",
    "is not":                    "secret",
    "but adds":                  "useful metadata",
    "that can help you":         "be confident that",
    "the data you are handling": "is what you think it is",
}

// Create keyring input
rawEcdhStaticConfigurationInput := mpltypes.RawPrivateKeyToStaticPublicKeyInput{
    SenderStaticPrivateKey: privateKeySender,
    RecipientPublicKey:     publicKeyRecipient,
}
rawECDHStaticConfiguration := &mpltypes.RawEcdhStaticConfigurationsMemberRawPrivateKeyToStaticPublicKey{
    Value: rawEcdhStaticConfigurationInput,
}
rawEcdhKeyRingInput := mpltypes.CreateRawEcdhKeyringInput{
    CurveSpec:          ecdhCurveSpec,
    KeyAgreementScheme: rawECDHStaticConfiguration,
}

// Instantiate the material providers library
matProv, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
if err != nil {
    panic(err)
}

// Create raw ECDH static keyring
rawEcdhKeyring, err := matProv.CreateRawEcdhKeyring(context.Background(), rawEcdhKeyRingInput)
if err != nil {
    panic(err)
}
```

------

### EphemeralPrivateKeyToStaticPublicKey
<a name="raw-ecdh-EphemeralPrivateKeyToStaticPublicKey"></a>

Keyrings configured with the `EphemeralPrivateKeyToStaticPublicKey` key agreement schema create a new key pair locally and derive a unique shared wrapping key for each encrypt call.

This key agreement schema can only encrypt messages. To decrypt messages encrypted with the `EphemeralPrivateKeyToStaticPublicKey` key agreement schema, you must use a discovery key agreement schema configured with the same recipient's public key. To decrypt, you can use a Raw ECDH keyring with the [`PublicKeyDiscovery`](#raw-ecdh-PublicKeyDiscovery) key agreement algorithm, or, if the recipient's public key is from an asymmetric key agreement KMS key pair, you can use an AWS KMS ECDH keyring with the [KmsPublicKeyDiscovery](use-kms-ecdh-keyring.md#kms-ecdh-discovery) key agreement schema.

To initialize a Raw ECDH keyring with the `EphemeralPrivateKeyToStaticPublicKey` key agreement schema, provide the following values:
+ **Recipient's public key**

  You must provide the recipient's DER-encoded X.509 public key, also known as `SubjectPublicKeyInfo` (SPKI), as defined in [RFC 5280](https://tools.ietf.org/html/rfc5280).

  You can specify the public key of an asymmetric key agreement KMS key pair or the public key from a key pair generated outside of AWS.
+ **Curve specification**

  Identifies the elliptic curve specification in the specified public key.

  On encrypt, the keyring creates a new key pair on the specified curve and uses the new private key and specified public key to derive a shared wrapping key.

  Valid values: `ECC_NIST_P256`, `ECC_NIS_P384`, `ECC_NIST_P512`

------
#### [ C\# / .NET ]

The following example creates a Raw ECDH keyring with the `EphemeralPrivateKeyToStaticPublicKey` key agreement schema. On encrypt, the keyring will create a new key pair locally on the specified `ECC_NIST_P256` curve.

```
// Instantiate material providers
var materialProviders = new MaterialProviders(new MaterialProvidersConfig());
	    var AlicePublicKey = new MemoryStream(new byte[] { });

	    // Create the Raw ECDH ephemeral keyring
	    var ephemeralConfiguration = new RawEcdhStaticConfigurations()
	    {
		    EphemeralPrivateKeyToStaticPublicKey = new EphemeralPrivateKeyToStaticPublicKeyInput
		    {
			    RecipientPublicKey = AlicePublicKey
		    }
	    };

	    var createKeyringInput = new CreateRawEcdhKeyringInput()
	    {
		    CurveSpec = ECDHCurveSpec.{{ECC_NIST_P256}},
		    KeyAgreementScheme = ephemeralConfiguration
	    };

	    var keyring = materialProviders.CreateRawEcdhKeyring(createKeyringInput);
```

------
#### [ Java ]

The following example creates a Raw ECDH keyring with the `EphemeralPrivateKeyToStaticPublicKey` key agreement schema. On encrypt, the keyring will create a new key pair locally on the specified `ECC_NIST_P256` curve.

```
private static void EphemeralRawEcdhKeyring() {
    // Instantiate material providers
    final MaterialProviders materialProviders =
      MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();

    ByteBuffer recipientPublicKey = getPublicKeyBytes();

    // Create the Raw ECDH ephemeral keyring
    final CreateRawEcdhKeyringInput ephemeralInput =
      CreateRawEcdhKeyringInput.builder()
        .curveSpec(ECDHCurveSpec.{{ECC_NIST_P256}})
        .KeyAgreementScheme(
          RawEcdhStaticConfigurations.builder()
            .EphemeralPrivateKeyToStaticPublicKey(
              EphemeralPrivateKeyToStaticPublicKeyInput.builder()
                .recipientPublicKey(recipientPublicKey)
                .build()
            )
            .build()
        ).build();

    final IKeyring ephemeralKeyring = materialProviders.CreateRawEcdhKeyring(ephemeralInput);
}
```

------
#### [ Python ]

The following example creates a Raw ECDH keyring with the `RawEcdhStaticConfigurationsEphemeralPrivateKeyToStaticPublicKey` key agreement schema. On encrypt, the keyring will create a new key pair locally on the specified `ECC_NIST_P256` curve.

```
import boto3
from aws_cryptographic_materialproviders.mpl.models import (
    CreateRawEcdhKeyringInput,
    RawEcdhStaticConfigurationsEphemeralPrivateKeyToStaticPublicKey,
    EphemeralPrivateKeyToStaticPublicKeyInput,
)
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models import ECDHCurveSpec

# Instantiate the material providers library
mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
    config=MaterialProvidersConfig()
)

# Your get_public_key_bytes must return a DER-encoded X.509 public key
recipient_public_key = get_public_key_bytes()

# Create the raw ECDH ephemeral private key keyring
ephemeral_input = CreateRawEcdhKeyringInput(
    curve_spec = ECDHCurveSpec.{{ECC_NIST_P256}},
    key_agreement_scheme = RawEcdhStaticConfigurationsEphemeralPrivateKeyToStaticPublicKey(
        EphemeralPrivateKeyToStaticPublicKeyInput(
            recipient_public_key = recipient_public_key,
        )
    )
)

keyring = mat_prov.create_raw_ecdh_keyring(ephemeral_input)
```

------
#### [ Rust ]

The following example creates a Raw ECDH keyring with the `ephemeral_raw_ecdh_static_configuration` key agreement schema. On encrypt, the keyring will create a new key pair locally on the specified curve.

```
// Instantiate the AWS Encryption SDK client
let esdk_config = AwsEncryptionSdkConfig::builder().build()?;
let esdk_client = esdk_client::Client::from_conf(esdk_config)?;

// Optional: Create your encryption context
let encryption_context = HashMap::from([
    ("encryption".to_string(), "context".to_string()),
    ("is not".to_string(), "secret".to_string()),
    ("but adds".to_string(), "useful metadata".to_string()),
    ("that can help you".to_string(), "be confident that".to_string()),
    ("the data you are handling".to_string(), "is what you think it is".to_string()),
]);

// Load public key from UTF-8 encoded PEM files into a DER encoded public key.
let public_key_file_content = std::fs::read_to_string(Path::new(EXAMPLE_ECC_PUBLIC_KEY_FILENAME_RECIPIENT))?;
let parsed_public_key_file_content = parse(public_key_file_content)?;
let public_key_recipient_utf8_bytes = parsed_public_key_file_content.contents();

// Create EphemeralPrivateKeyToStaticPublicKeyInput
let ephemeral_raw_ecdh_static_configuration_input =
    EphemeralPrivateKeyToStaticPublicKeyInput::builder()
        // Must be a UTF8 DER-encoded X.509 public key
        .recipient_public_key(public_key_recipient_utf8_bytes)
        .build()?;

let ephemeral_raw_ecdh_static_configuration =
    RawEcdhStaticConfigurations::EphemeralPrivateKeyToStaticPublicKey(ephemeral_raw_ecdh_static_configuration_input);

// Instantiate the material providers library
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

// Create raw ECDH ephemeral private key keyring
let ephemeral_raw_ecdh_keyring = mpl
    .create_raw_ecdh_keyring()
    .curve_spec(ecdh_curve_spec)
    .key_agreement_scheme(ephemeral_raw_ecdh_static_configuration)
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
)

// Instantiate the AWS Encryption SDK client
encryptionClient, err := client.NewClient(esdktypes.AwsEncryptionSdkConfig{})
if err != nil {
    panic(err)
}

// Optional: Create your encryption context
encryptionContext := map[string]string{
    "encryption":                "context",
    "is not":                    "secret",
    "but adds":                  "useful metadata",
    "that can help you":         "be confident that",
    "the data you are handling": "is what you think it is",
}

// Load public key from UTF-8 encoded PEM files into a DER encoded public key
publicKeyRecipient, err := LoadPublicKeyFromPEM(eccPublicKeyFileNameRecipient)
if err != nil {
    panic(err)
}

// Create EphemeralPrivateKeyToStaticPublicKeyInput
ephemeralRawEcdhStaticConfigurationInput := mpltypes.EphemeralPrivateKeyToStaticPublicKeyInput{
    RecipientPublicKey: publicKeyRecipient,
}
ephemeralRawECDHStaticConfiguration :=
    mpltypes.RawEcdhStaticConfigurationsMemberEphemeralPrivateKeyToStaticPublicKey{
        Value: ephemeralRawEcdhStaticConfigurationInput,
    }

// Instantiate the material providers library
matProv, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
if err != nil {
    panic(err)
}

// Create raw ECDH ephemeral private key keyring
rawEcdhKeyRingInput := mpltypes.CreateRawEcdhKeyringInput{
    CurveSpec:          ecdhCurveSpec,
    KeyAgreementScheme: &ephemeralRawECDHStaticConfiguration,
}
ecdhKeyring, err := matProv.CreateRawEcdhKeyring(context.Background(), rawEcdhKeyRingInput)
if err != nil {
    panic(err)
}
```

------

### PublicKeyDiscovery
<a name="raw-ecdh-PublicKeyDiscovery"></a>

When decrypting, it's a best practice to specify the wrapping keys that the AWS Encryption SDK can use. To follow this best practice, use an ECDH keyring that specifies both a sender's private key and recipient's public key. However, you can also create a Raw ECDH discovery keyring, that is, a Raw ECDH keyring that can decrypt any message where the specified key's public key matches the recipient's public key stored on the message ciphertext. This key agreement schema can only decrypt messages.

**Important**
When you decrypt messages using the `PublicKeyDiscovery` key agreement schema, you accept all public keys, regardless of who owns it.

To initialize a Raw ECDH keyring with the `PublicKeyDiscovery` key agreement schema, provide the following values:
+ **Recipient's static private key**

  You must provide the recipient's PEM-encoded private key (PKCS \#8 PrivateKeyInfo structures), as defined in [RFC 5958](https://tools.ietf.org/html/rfc5958#section-2).
+ **Curve specification**

  Identifies the elliptic curve specification in the specified private key. Both the sender and recipient's key pairs must have the same curve specification.

  Valid values: `ECC_NIST_P256`, `ECC_NIS_P384`, `ECC_NIST_P512`

------
#### [ C\# / .NET ]

The following example creates a Raw ECDH keyring with the `PublicKeyDiscovery` key agreement schema. This keyring can decrypt any message where the public key of the specified private key matches the recipient's public key stored on the message ciphertext.

```
// Instantiate material providers
var materialProviders = new MaterialProviders(new MaterialProvidersConfig());
	    var AlicePrivateKey = new MemoryStream(new byte[] { });

	    // Create the Raw ECDH discovery keyring
	    var discoveryConfiguration = new RawEcdhStaticConfigurations()
	    {
		    PublicKeyDiscovery = new PublicKeyDiscoveryInput
		    {
			    RecipientStaticPrivateKey = AlicePrivateKey
		    }
	    };

	    var createKeyringInput = new CreateRawEcdhKeyringInput()
	    {
		    CurveSpec = ECDHCurveSpec.ECC_NIST_P256,
		    KeyAgreementScheme = discoveryConfiguration
	    };

	    var keyring = materialProviders.CreateRawEcdhKeyring(createKeyringInput);
```

------
#### [ Java ]

The following example creates a Raw ECDH keyring with the `PublicKeyDiscovery` key agreement schema. This keyring can decrypt any message where the public key of the specified private key matches the recipient's public key stored on the message ciphertext.

```
private static void RawEcdhDiscovery() {
    // Instantiate material providers
    final MaterialProviders materialProviders =
      MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();

    KeyPair recipient = GetRawEccKey();

    // Create the Raw ECDH discovery keyring
    final CreateRawEcdhKeyringInput rawKeyringInput =
      CreateRawEcdhKeyringInput.builder()
        .curveSpec(ECDHCurveSpec.{{ECC_NIST_P256}})
        .KeyAgreementScheme(
          RawEcdhStaticConfigurations.builder()
            .PublicKeyDiscovery(
              PublicKeyDiscoveryInput.builder()
                // Must be a PEM-encoded private key
                .recipientStaticPrivateKey(ByteBuffer.wrap(sender.getPrivate().getEncoded()))
                .build()
            )
            .build()
        ).build();

    final IKeyring publicKeyDiscovery  = materialProviders.CreateRawEcdhKeyring(rawKeyringInput);
}
```

------
#### [ Python ]

The following example creates a Raw ECDH keyring with the `RawEcdhStaticConfigurationsPublicKeyDiscovery` key agreement schema. This keyring can decrypt any message where the public key of the specified private key matches the recipient's public key stored on the message ciphertext.

```
import boto3
from aws_cryptographic_materialproviders.mpl.models import (
    CreateRawEcdhKeyringInput,
    RawEcdhStaticConfigurationsPublicKeyDiscovery,
    PublicKeyDiscoveryInput,
)
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models import ECDHCurveSpec

# Instantiate the material providers library
mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
    config=MaterialProvidersConfig()
)

# Your get_private_key_bytes must return a PEM-encoded private key
recipient_private_key = get_private_key_bytes()

# Create the raw ECDH discovery keyring
raw_keyring_input = CreateRawEcdhKeyringInput(
    curve_spec = ECDHCurveSpec.{{ECC_NIST_P256}},
    key_agreement_scheme = RawEcdhStaticConfigurationsPublicKeyDiscovery(
        PublicKeyDiscoveryInput(
            recipient_static_private_key = recipient_private_key,
        )
    )
)

keyring = mat_prov.create_raw_ecdh_keyring(raw_keyring_input)
```

------
#### [ Rust ]

The following example creates a Raw ECDH keyring with the `discovery_raw_ecdh_static_configuration` key agreement schema. This keyring can decrypt any message where the public key of the specified private key matches the recipient's public key stored on the message ciphertext.

```
// Instantiate the AWS Encryption SDK client and material providers library
let esdk_config = AwsEncryptionSdkConfig::builder().build()?;
let esdk_client = esdk_client::Client::from_conf(esdk_config)?;

let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

// Optional: Create your encryption context
let encryption_context = HashMap::from([
    ("encryption".to_string(), "context".to_string()),
    ("is not".to_string(), "secret".to_string()),
    ("but adds".to_string(), "useful metadata".to_string()),
    ("that can help you".to_string(), "be confident that".to_string()),
    ("the data you are handling".to_string(), "is what you think it is".to_string()),
]);

// Load keys from UTF-8 encoded PEM files.
let mut file = File::open(Path::new(EXAMPLE_ECC_PRIVATE_KEY_FILENAME_RECIPIENT))?;
let mut private_key_recipient_utf8_bytes = Vec::new();
file.read_to_end(&mut private_key_recipient_utf8_bytes)?;

// Create PublicKeyDiscoveryInput
let discovery_raw_ecdh_static_configuration_input =
    PublicKeyDiscoveryInput::builder()
        // Must be a UTF8 PEM-encoded private key
        .recipient_static_private_key(private_key_recipient_utf8_bytes)
        .build()?;

let discovery_raw_ecdh_static_configuration =
    RawEcdhStaticConfigurations::PublicKeyDiscovery(discovery_raw_ecdh_static_configuration_input);

// Create raw ECDH discovery private key keyring
let discovery_raw_ecdh_keyring = mpl
    .create_raw_ecdh_keyring()
    .curve_spec(ecdh_curve_spec)
    .key_agreement_scheme(discovery_raw_ecdh_static_configuration)
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
)

// Instantiate the AWS Encryption SDK client
encryptionClient, err := client.NewClient(esdktypes.AwsEncryptionSdkConfig{})
if err != nil {
    panic(err)
}

// Optional: Create your encryption context
encryptionContext := map[string]string{
    "encryption":                "context",
    "is not":                    "secret",
    "but adds":                  "useful metadata",
    "that can help you":         "be confident that",
    "the data you are handling": "is what you think it is",
}

// Load keys from UTF-8 encoded PEM files.
privateKeyRecipient, err := os.ReadFile(eccPrivateKeyFileNameRecipient)
if err != nil {
    panic(err)
}

// Instantiate the material providers library
matProv, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
if err != nil {
    panic(err)
}

// Create PublicKeyDiscoveryInput
discoveryRawEcdhStaticConfigurationInput := mpltypes.PublicKeyDiscoveryInput{
    RecipientStaticPrivateKey: privateKeyRecipient,
}

discoveryRawEcdhStaticConfiguration := &mpltypes.RawEcdhStaticConfigurationsMemberPublicKeyDiscovery{
    Value: discoveryRawEcdhStaticConfigurationInput,
}

// Create raw ECDH discovery private key keyring
discoveryRawEcdhKeyringInput := mpltypes.CreateRawEcdhKeyringInput{
    CurveSpec:          ecdhCurveSpec,
    KeyAgreementScheme: discoveryRawEcdhStaticConfiguration,
}

discoveryRawEcdhKeyring, err := matProv.CreateRawEcdhKeyring(context.Background(), discoveryRawEcdhKeyringInput)
if err != nil {
    panic(err)
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
