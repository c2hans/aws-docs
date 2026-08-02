---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-kms-ecdh-keyring.html
---

# AWS KMS ECDH keyrings
<a name="use-kms-ecdh-keyring"></a>

****

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

**Important**
The AWS KMS ECDH keyring is only available with version 1.5.0 or later of the Material Providers Library.

An AWS KMS ECDH keyring uses asymmetric key agreement [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-types.html) to derive a shared symmetric wrapping key between two parties. First, the keyring uses the Elliptic Curve Diffie-Hellman (ECDH) key agreement algorithm to derive a shared secret from the private key in the sender's KMS key pair and the recipient's public key. Then, the keyring uses the shared secret to derive the shared wrapping key that protects your data encryption keys. The key derivation function that the AWS Database Encryption SDK uses (`KDF_CTR_HMAC_SHA384`) to derive the shared wrapping key conforms to [NIST recommendations for key derivation](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-108r1-upd1.pdf).

The key derivation function returns 64 bytes of keying material. To ensure that both parties use the correct keying material, the AWS Database Encryption SDK uses the first 32 bytes as a commitment key and the last 32 bytes as the shared wrapping key. On decrypt, if the keyring cannot reproduce the same commitment key and shared wrapping key that is stored in the material description field of the encrypted record, the operation fails. For example, if you encrypt a record with a keyring configured with **Alice's** private key and **Bob's** public key, a keyring configured with **Bob's** private key and **Alice's** public key will reproduce the same commitment key and shared wrapping key and be able to decrypt the record. If Bob's public key is not from a KMS key pair, then Bob can create a [Raw ECDH keyring](use-raw-ecdh-keyring.md) to decrypt the record.

The AWS KMS ECDH keyring encrypts records with a symmetric key using AES-GCM. The data key is then envelope encrypted with the derived shared wrapping key using AES-GCM. Each AWS KMS ECDH keyring can have only one shared wrapping key, but you can include multiple AWS KMS ECDH keyrings, alone or with other keyrings, in a [multi-keyring](use-multi-keyring.md).

**Topics**
+ [Required permissions for AWS KMS ECDH keyrings](#kms-ecdh-permissions)
+ [Creating an AWS KMS ECDH keyring](#kms-ecdh-create)
+ [Creating an AWS KMS ECDH discovery keyring](#kms-ecdh-discovery)

## Required permissions for AWS KMS ECDH keyrings
<a name="kms-ecdh-permissions"></a>

The AWS Database Encryption SDK doesn't require an AWS account and it doesn't depend on any AWS service. However, to use an AWS KMS ECDH keyring, you need an AWS account and the following minimum permissions on the AWS KMS keys in your keyring. The permissions vary based on which key agreement schema you use.
+ To encrypt and decrypt records using the `KmsPrivateKeyToStaticPublicKey` key agreement schema, you need [kms:GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) and [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) on the *sender's* asymmetric KMS key pair. If you directly provide the sender's DER-encoded public key when you instantiate your keyring, you only need [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) permission on the sender's asymmetric KMS key pair.
+ To decrypt records using the `KmsPublicKeyDiscovery` key agreement schema, you need [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) and [kms:GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) permissions on the specified asymmetric KMS key pair.

## Creating an AWS KMS ECDH keyring
<a name="kms-ecdh-create"></a>

To create an AWS KMS ECDH keyring that encrypts and decrypts data, you must use the `KmsPrivateKeyToStaticPublicKey` key agreement schema. To initialize an AWS KMS ECDH keyring with the `KmsPrivateKeyToStaticPublicKey` key agreement schema, provide the following values:
+ **Sender's AWS KMS key ID**

  Must identify an asymmetric NIST-recommended elliptic curve (ECC)KMS key pair with a `KeyUsage` value of `KEY_AGREEMENT`. The sender's private key is used to derive the shared secret.
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

The following example creates an AWS KMS ECDH keyring with the with the sender's KMS key, the sender's public key, and the recipient's public key. This example uses the optional `senderPublicKey` parameter to provide the sender's public key. If you do not provide the sender's public key, the keyring calls AWS KMS to retrieve the sender's public key. Both the sender and recipient's key pairs are on the `ECC_NIST_P256` curve.

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
#### [ Rust ]

The following example creates an AWS KMS ECDH keyring with the with the sender's KMS key, the sender's public key, and the recipient's public key. This example uses the optional `sender_public_key` parameter to provide the sender's public key. If you do not provide the sender's public key, the keyring calls AWS KMS to retrieve the sender's public key.

```
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

## Creating an AWS KMS ECDH discovery keyring
<a name="kms-ecdh-discovery"></a>

When decrypting, it's a best practice to specify the keys that the AWS Database Encryption SDK can use. To follow this best practice, use an AWS KMS ECDH keyring with the `KmsPrivateKeyToStaticPublicKey` key agreement schema. However, you can also create an AWS KMS ECDH discovery keyring, that is, an AWS KMS ECDH keyring that can decrypt any record where the public key of the specified KMS key pair matches the *recipient's* public key stored in the material description field of the encrypted record.

**Important**
When you decrypt records using the `KmsPublicKeyDiscovery` key agreement schema, you accept all public keys, regardless of who owns it.

To initialize an AWS KMS ECDH keyring with the `KmsPublicKeyDiscovery` key agreement schema, provide the following values:
+ **Recipient's AWS KMS key ID**

  Must identify an asymmetric NIST-recommended elliptic curve (ECC)KMS key pair with a `KeyUsage` value of `KEY_AGREEMENT`.
+ **Curve specification**

  Identifies the elliptic curve specification in the recipient's KMS key pair.

  Valid values: `ECC_NIST_P256`, `ECC_NIS_P384`, `ECC_NIST_P512`
+ **(Optional) A list of Grant Tokens**

  If you control access to the KMS key in your AWS KMS ECDH keyring with [grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html), you must provide all necessary grant tokens when you initialize the keyring.

------
#### [ C\# / .NET ]

The following example creates an AWS KMS ECDH discovery keyring with a KMS key pair on the `ECC_NIST_P256` curve. You must have [kms:GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) and [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) permissions on the specified KMS key pair. This keyring can decrypt any record where the public key of the specified KMS key pair matches the recipient's public key stored in the material description field of the encrypted record.

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

The following example creates an AWS KMS ECDH discovery keyring with a KMS key pair on the `ECC_NIST_P256` curve. You must have [kms:GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) and [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) permissions on the specified KMS key pair. This keyring can decrypt any record where the public key of the specified KMS key pair matches the recipient's public key stored in the material description field of the encrypted record.

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
#### [ Rust ]

```
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
