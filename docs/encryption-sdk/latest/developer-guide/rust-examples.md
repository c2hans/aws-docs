---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/rust-examples.html
---

# AWS Encryption SDK for Rust example code
<a name="rust-examples"></a>

The following examples show the basic coding patterns that you use when programming with the AWS Encryption SDK for Rust. Specifically, you instantiate the AWS Encryption SDK and the material providers library. Then, before calling each method, you instantiate the object that defines the input for the method.

For examples showing how to configure options in the AWS Encryption SDK, such as specifying an alternate algorithm suite and limiting encrypted data keys, see the [Rust examples](https://github.com/aws/aws-encryption-sdk-dafny/tree/mainline/AwsEncryptionSDK/runtimes/rust/examples/) in the aws-encryption-sdk repository on GitHub.

## Encrypting and decrypting data in the AWS Encryption SDK for Rust
<a name="rust-example-encrypt"></a>

This example shows the basic pattern for encrypting and decrypting data. It encrypts a small file with data keys that are protected by one AWS KMS wrapping key.

**Step 1: Instantiate the AWS Encryption SDK.**
You'll use the methods in the AWS Encryption SDK to encrypt and decrypt data.

```
let esdk_config = AwsEncryptionSdkConfig::builder().build()?;
let esdk_client = esdk_client::Client::from_conf(esdk_config)?;
```

**Step 2: Create an AWS KMS client.**

```
let sdk_config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
let kms_client = aws_sdk_kms::Client::new(&sdk_config);
```

**Optional: Create your encryption context.**

```
let encryption_context = HashMap::from([
    ("encryption".to_string(), "context".to_string()),
    ("is not".to_string(), "secret".to_string()),
    ("but adds".to_string(), "useful metadata".to_string()),
    ("that can help you".to_string(), "be confident that".to_string()),
    ("the data you are handling".to_string(), "is what you think it is".to_string()),
]);
```

**Step 3: Instantiate the material providers library.**
You'll use the methods in the material providers library to create the keyrings that specify which keys protect your data.

```
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;
```

**Step 4: Create an AWS KMS keyring.**
To create the keyring, call the keyring method with the keyring input object. This example uses the `create_aws_kms_keyring()` method and specifies one KMS key.

```
let kms_keyring = mpl
    .create_aws_kms_keyring()
    .kms_key_id(kms_key_id)
    .kms_client(kms_client)
    .send()
    .await?;
```

**Step 5: Encrypt the plaintext.**

```
let plaintext = example_data.as_bytes();

let encryption_response = esdk_client.encrypt()
    .plaintext(plaintext)
    .keyring(kms_keyring.clone())
    .encryption_context(encryption_context.clone())
    .send()
    .await?;

let ciphertext = encryption_response
                    .ciphertext
                    .expect("Unable to unwrap ciphertext from encryption response");
```

**Step 6: Decrypt your encrypted data using the same keyring you used on encrypt.**

```
let decryption_response = esdk_client.decrypt()
    .ciphertext(ciphertext)
    .keyring(kms_keyring)
    // Provide the encryption context that was supplied to the encrypt method
    .encryption_context(encryption_context)
    .send()
    .await?;

let decrypted_plaintext = decryption_response
                            .plaintext
                            .expect("Unable to unwrap plaintext from decryption response");
```
