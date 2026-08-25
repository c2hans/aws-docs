---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-raw-aes-keyring.html
---

# Raw AES keyrings
<a name="use-raw-aes-keyring"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

The AWS Database Encryption SDK lets you use an AES symmetric key that you provide as a wrapping key that protects your data key. You need to generate, store, and protect the key material, preferably in a hardware security module (HSM) or key management system. Use a Raw AES keyring when you need to provide the wrapping key and encrypt the data keys locally or offline.

The Raw AES keyring encrypts data by using the AES-GCM algorithm and a wrapping key that you specify as a byte array. You can specify only one wrapping key in each Raw AES keyring, but you can include multiple Raw AES keyrings, alone or with other keyrings, in a [multi-keyring](use-multi-keyring.md).

**Key namespaces and names**

To identify the AES key in a keyring, the Raw AES keyring uses a *key namespace* and *key name* that you provide. These values are not secret. They appear in plain text in the [material description](concepts.md#material-description) that the AWS Database Encryption SDK adds to the record. We recommend using a key namespace your HSM or key management system and a key name that identifies the AES key in that system.

**Note**
The key namespace and key name are equivalent to the *Provider ID* (or *Provider*) and *Key ID* fields in the `JceMasterKey`.

If you construct different keyrings to encrypt and decrypt a given field, the namespace and name values are critical. If the key namespace and key name in the decryption keyring isn't an exact, case-sensitive match for the key namespace and key name in the encryption keyring, the decryption keyring isn't used, even if the key material bytes are identical.

For example, you might define a Raw AES keyring with key namespace `HSM_01` and key name `AES_256_012`. Then, you use that keyring to encrypt some data. To decrypt that data, construct a Raw AES keyring with the same key namespace, key name, and key material.

The following examples show how to create a Raw AES keyring. The `AESWrappingKey` variable represents the key material you provide.

------
#### [ Java ]

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
#### [ C\# / .NET ]

```
var keyNamespace = "{{HSM_01}}";
var keyName = "{{AES_256_012}}";

// This example uses the key generator in Bouncy Castle to generate the key material.
// In production, use key material from a secure source.
var aesWrappingKey = new MemoryStream(GeneratorUtilities.GetKeyGenerator("AES256").GenerateKey());

// Create the keyring
var keyringInput = new CreateRawAesKeyringInput
{
    KeyNamespace = keyNamespace,
    KeyName = keyName,
    WrappingKey = {{AESWrappingKey}},
    WrappingAlg = AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16
};

var matProv = new MaterialProviders(new MaterialProvidersConfig());
IKeyring rawAesKeyring = matProv.CreateRawAesKeyring(keyringInput);
```

------
#### [ Rust ]

```
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;
let raw_aes_keyring = mpl
    .create_raw_aes_keyring()
    .key_name("{{AES_256_012}}")
    .key_namespace("{{HSM_01}}")
    .wrapping_key({{aes_key_bytes}})
    .wrapping_alg(AesWrappingAlg::AlgAes256GcmIv12Tag16)
    .send()
    .await?;
```

------
