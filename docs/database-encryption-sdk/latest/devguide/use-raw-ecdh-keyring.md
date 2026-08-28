---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-raw-ecdh-keyring.html
---

# Raw ECDH keyrings
<a name="use-raw-ecdh-keyring"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

**Important**
The Raw ECDH keyring is only available with version 1.5.0 of the Material Providers Library.

The Raw ECDH keyring uses the elliptic curve public-private key pairs that you provide to derive a shared wrapping key between two parties. First, the keyring derives a shared secret using the sender's private key, the recipient's public key, and the Elliptic Curve Diffie-Hellman (ECDH) key agreement algorithm. Then, the keyring uses the shared secret to derive the shared wrapping key that protects your data encryption keys. The key derivation function that the AWS Database Encryption SDK uses (`KDF_CTR_HMAC_SHA384`) to derive the shared wrapping key conforms to [NIST recommendations for key derivation](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-108r1-upd1.pdf).

The key derivation function returns 64 bytes of keying material. To ensure that both parties use the correct keying material, the AWS Database Encryption SDK uses the first 32 bytes as a commitment key and the last 32 bytes as the shared wrapping key. On decrypt, if the keyring cannot reproduce the same commitment key and shared wrapping key that is stored in the material description field of the encrypted record, the operation fails. For example, if you encrypt a record with a keyring configured with **Alice's** private key and **Bob's** public key, a keyring configured with **Bob's** private key and **Alice's** public key will reproduce the same commitment key and shared wrapping key and be able to decrypt the record. If Bob's public key is from an AWS KMS key pair, then Bob can create an [AWS KMS ECDH keyring](use-kms-ecdh-keyring.md) to decrypt the record.

The Raw ECDH keyring encrypts records with a symmetric key using AES-GCM. The data key is then envelope encrypted with the derived shared wrapping key using AES-GCM. Each Raw ECDH keyring can have only one shared wrapping key, but you can include multiple Raw ECDH keyrings, alone or with other keyrings, in a [multi-keyring](use-multi-keyring.md).

You are responsible for generating, storing, and protecting your private keys, preferably in a hardware security module (HSM) or key management system. The sender and recipient's key pairs much be on the same elliptic curve. The AWS Database Encryption SDK supports the following elliptic cuve specifications:
+ `ECC_NIST_P256`
+ `ECC_NIST_P384`
+ `ECC_NIST_P512`

## Creating a Raw ECDH keyring
<a name="raw-ecdh-create"></a>

The Raw ECDH keyring supports three key agreement schemas: `RawPrivateKeyToStaticPublicKey`, `EphemeralPrivateKeyToStaticPublicKey`, and `PublicKeyDiscovery`. The key agreement schema that you select determines which cryptographic operations you can perform and how the keying materials are assembled.

**Topics**
+ [RawPrivateKeyToStaticPublicKey](#raw-ecdh-RawPrivateKeyToStaticPublicKey)
+ [EphemeralPrivateKeyToStaticPublicKey](#raw-ecdh-EphemeralPrivateKeyToStaticPublicKey)
+ [PublicKeyDiscovery](#raw-ecdh-PublicKeyDiscovery)

### RawPrivateKeyToStaticPublicKey
<a name="raw-ecdh-RawPrivateKeyToStaticPublicKey"></a>

Use the `RawPrivateKeyToStaticPublicKey` key agreement schema to statically configure the sender's private key and the recipient's public key in the keyring. This key agreement schema can encrypt and decrypt records.

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
#### [ Rust ]

The following Python example uses the `raw_ecdh_static_configuration` key agreement schema to statically configure the sender's private key and the recipient's public key. Both key pairs must be on the same curve.

```
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

### EphemeralPrivateKeyToStaticPublicKey
<a name="raw-ecdh-EphemeralPrivateKeyToStaticPublicKey"></a>

Keyrings configured with the `EphemeralPrivateKeyToStaticPublicKey` key agreement schema create a new key pair locally and derive a unique shared wrapping key for each encrypt call.

This key agreement schema can only encrypt records. To decrypt records encrypted with the `EphemeralPrivateKeyToStaticPublicKey` key agreement schema, you must use a discovery key agreement schema configured with the same recipient's public key. To decrypt, you can use a Raw ECDH keyring with the [`PublicKeyDiscovery`](#raw-ecdh-PublicKeyDiscovery) key agreement algorithm, or, if the recipient's public key is from an asymmetric key agreement KMS key pair, you can use an AWS KMS ECDH keyring with the [KmsPublicKeyDiscovery](use-kms-ecdh-keyring.md#kms-ecdh-discovery) key agreement schema.

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
#### [ Rust ]

The following example creates a Raw ECDH keyring with the `ephemeral_raw_ecdh_static_configuration` key agreement schema. On encrypt, the keyring will create a new key pair locally on the specified curve.

```
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

### PublicKeyDiscovery
<a name="raw-ecdh-PublicKeyDiscovery"></a>

When decrypting, it's a best practice to specify the wrapping keys that the AWS Database Encryption SDK can use. To follow this best practice, use an ECDH keyring that specifies both a sender's private key and recipient's public key. However, you can also create a Raw ECDH discovery keyring, that is, a Raw ECDH keyring that can decrypt any record where the specified key's public key matches the recipient's public key stored in the material description field of the encrypted record. This key agreement schema can only decrypt records.

**Important**
When you decrypt records using the `PublicKeyDiscovery` key agreement schema, you accept all public keys, regardless of who owns it.

To initialize a Raw ECDH keyring with the `PublicKeyDiscovery` key agreement schema, provide the following values:
+ **Recipient's static private key**

  You must provide the recipient's PEM-encoded private key (PKCS \#8 PrivateKeyInfo structures), as defined in [RFC 5958](https://tools.ietf.org/html/rfc5958#section-2).
+ **Curve specification**

  Identifies the elliptic curve specification in the specified private key. Both the sender and recipient's key pairs must have the same curve specification.

  Valid values: `ECC_NIST_P256`, `ECC_NIS_P384`, `ECC_NIST_P512`

------
#### [ C\# / .NET ]

The following example creates a Raw ECDH keyring with the `PublicKeyDiscovery` key agreement schema. This keyring can decrypt any record where the public key of the specified private key matches the recipient's public key stored in the material description field of the encrypted record.

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

The following example creates a Raw ECDH keyring with the `PublicKeyDiscovery` key agreement schema. This keyring can decrypt any record where the public key of the specified private key matches the recipient's public key stored in the material description field of the encrypted record.

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
#### [ Rust ]

The following example creates a Raw ECDH keyring with the `discovery_raw_ecdh_static_configuration` key agreement schema. This keyring can decrypt any message where the public key of the specified private key matches the recipient's public key stored on the message ciphertext.

```
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
