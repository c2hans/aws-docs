---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-raw-rsa-keyring.html
---

# Raw RSA keyrings
<a name="use-raw-rsa-keyring"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

The Raw RSA keyring performs asymmetric encryption and decryption of data keys in local memory with an RSA public and private keys that you provide. You need to generate, store, and protect the private key, preferably in a hardware security module (HSM) or key management system. The encryption function encrypts the data key under the RSA public key. The decryption function decrypts the data key using the private key. You can select from among the several RSA padding modes.

A Raw RSA keyring that encrypts and decrypts must include an asymmetric public key and private key pair. However, you can encrypt data with a Raw RSA keyring that has only a public key, and you can decrypt data with a Raw RSA keyring that has only a private key. You can include any Raw RSA keyring in a [multi-keyring](use-multi-keyring.md). If you configure a Raw RSA keyring with a public and private key, be sure that they are part of the same key pair.

 The Raw RSA keyring is equivalent to and interoperates with the [JceMasterKey](https://aws.github.io/aws-encryption-sdk-java/com/amazonaws/encryptionsdk/jce/JceMasterKey.html) in the AWS Encryption SDK for Java when they are used with RSA asymmetric encryption keys.

**Note**
The Raw RSA keyring does not support asymmetric KMS keys. To use asymmetric RSA KMS keys, construct an [AWS KMS keyring](use-kms-keyring.md).

**Namespaces and names**

To identify the RSA key material in a keyring, the Raw RSA keyring uses a *key namespace* and *key name* that you provide. These values are not secret. They appear in plain text in the [material description](concepts.md#material-description) that the AWS Database Encryption SDK adds to the record. We recommend using the key namespace and key name that identifies the RSA key pair (or its private key) in your HSM or key management system.

**Note**
The key namespace and key name are equivalent to the *Provider ID* (or *Provider*) and *Key ID* fields in the `JceMasterKey`.

If you construct different keyrings to encrypt and decrypt a given record, the namespace and name values are critical. If the key namespace and key name in the decryption keyring isn't an exact, case-sensitive match for the key namespace and key name in the encryption keyring, the decryption keyring isn't used, even if the keys are from the same key pair.

The key namespace and key name of the key material in the encryption and decryption keyrings must be same whether the keyring contains the RSA public key, the RSA private key, or both keys in the key pair. For example, suppose you encrypt data with a Raw RSA keyring for an RSA public key with key namespace `HSM_01` and key name `RSA_2048_06`. To decrypt that data, construct a Raw RSA keyring with the private key (or key pair), and the same key namespace and name.

**Padding mode**

You must specify a padding mode for Raw RSA keyrings used for encryption and decryption, or use features of your language implementation that specify it for you.

The AWS Encryption SDK supports the following padding modes, subjects to the constraints of each language. We recommend an [OAEP](https://tools.ietf.org/html/rfc8017#section-7.1) padding mode, particularly OAEP with SHA-256 and MGF1 with SHA-256 Padding. The [PKCS1](https://tools.ietf.org/html/rfc8017#section-7.2) padding mode is supported only for backward compatibility.
+ OAEP with SHA-1 and MGF1 with SHA-1 Padding
+ OAEP with SHA-256 and MGF1 with SHA-256 Padding
+ OAEP with SHA-384 and MGF1 with SHA-384 Padding
+ OAEP with SHA-512 and MGF1 with SHA-512 Padding
+ PKCS1 v1.5 Padding

The following Java example shows how to create a Raw RSA keyring with the public and private key of an RSA key pair and the OAEP with SHA-256 and MGF1 with SHA-256 padding mode. The `RSAPublicKey` and `RSAPrivateKey` variables represent the key material you provide.

------
#### [ Java ]

```
final CreateRawRsaKeyringInput keyringInput = CreateRawRsaKeyringInput.builder()
        .keyName("{{RSA_2048_06}}")
        .keyNamespace("{{HSM_01}}")
        .paddingScheme(PaddingScheme.{{OAEP_SHA256_MGF1}})
        .publicKey({{RSAPublicKey}})
        .privateKey({{RSAPrivateKey}})
        .build();
final MaterialProviders matProv = MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();
IKeyring rawRsaKeyring = matProv.CreateRawRsaKeyring(keyringInput);
```

------
#### [ C\# / .NET ]

```
var keyNamespace = "{{HSM_01}}";
var keyName = "{{RSA_2048_06}}";

// Get public and private keys from PEM files
var publicKey = new MemoryStream(System.IO.File.ReadAllBytes("RSAKeyringExamplePublicKey.pem"));
var privateKey = new MemoryStream(System.IO.File.ReadAllBytes("RSAKeyringExamplePrivateKey.pem"));

// Create the keyring input
var keyringInput = new CreateRawRsaKeyringInput
{
    KeyNamespace = keyNamespace,
    KeyName = keyName,
    PaddingScheme = PaddingScheme.{{OAEP_SHA512_MGF1}},
    PublicKey = publicKey,
    PrivateKey = privateKey
};

// Create the keyring
var matProv = new MaterialProviders(new MaterialProvidersConfig());
var rawRsaKeyring = matProv.CreateRawRsaKeyring(keyringInput);
```

------
#### [ Rust ]

```
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;
let raw_rsa_keyring = mpl
    .create_raw_rsa_keyring()
    .key_name("{{RSA_2048_06}}")
    .key_namespace("{{HSM_01}}")
    .padding_scheme(PaddingScheme::{{OaepSha256Mgf1}})
    .public_key({{RSA_public_key}})
    .private_key({{RSA_private_key}})
    .send()
    .await?;
```

------
