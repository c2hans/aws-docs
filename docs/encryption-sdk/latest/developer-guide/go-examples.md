---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/go-examples.html
---

# AWS Encryption SDK for Go example code
<a name="go-examples"></a>

The following examples show the basic coding patterns that you use when programming with the AWS Encryption SDK for Go. Specifically, you instantiate the AWS Encryption SDK and the material providers library. Then, before calling each method, you instantiate the object that defines the input for the method.

For examples showing how to configure options in the AWS Encryption SDK, such as specifying an alternate algorithm suite and limiting encrypted data keys, see the [Go examples](https://github.com/aws/aws-encryption-sdk/tree/mainline/releases/go/encryption-sdk/examples) in the aws-encryption-sdk repository on GitHub.

## Encrypting and decrypting data in the AWS Encryption SDK for Go
<a name="go-example-encrypt"></a>

This example shows the basic pattern for encrypting and decrypting data. It encrypts a small amount of data with data keys that are protected by one AWS KMS wrapping key.

**Step 1: Instantiate the AWS Encryption SDK.**
You'll use the methods in the AWS Encryption SDK to encrypt and decrypt data.

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

encryptionClient, err := client.NewClient(esdktypes.AwsEncryptionSdkConfig{})
if err != nil {
    panic(err)
}
```

**Step 2: Create an AWS KMS client.**

```
cfg, err := config.LoadDefaultConfig(context.TODO())
if err != nil {
    panic(err)
}
kmsClient := kms.NewFromConfig(cfg, func(o *kms.Options) {
    o.Region = KmsKeyRegion
})
```

**Optional: Create your encryption context.**

```
encryptionContext := map[string]string{
    "encryption":                "context",
    "is not":                    "secret",
    "but adds":                  "useful metadata",
    "that can help you":         "be confident that",
    "the data you are handling": "is what you think it is",
}
```

**Step 3: Instantiate the material providers library.**
You'll use the methods in the material providers library to create the keyrings that specify which keys protect your data.

```
matProv, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
if err != nil {
    panic(err)
}
```

**Step 4: Create an AWS KMS keyring.**
To create the keyring, call the keyring method with the keyring input object. This example uses the `CreateAwsKmsKeyring` method and specifies one KMS key. The `kmsKeyId` variable represents the key ARN of the KMS key you provide.

```
awsKmsKeyringInput := mpltypes.CreateAwsKmsKeyringInput{
    KmsClient: kmsClient,
    KmsKeyId:  kmsKeyId,
}
awsKmsKeyring, err := matProv.CreateAwsKmsKeyring(context.Background(), awsKmsKeyringInput)
if err != nil {
    panic(err)
}
```

**Step 5: Encrypt the plaintext.**

```
res, err := encryptionClient.Encrypt(context.Background(), esdktypes.EncryptInput{
    Plaintext:         []byte(exampleText),
    EncryptionContext: encryptionContext,
    Keyring:           awsKmsKeyring,
})
if err != nil {
    panic(err)
}

ciphertext := res.Ciphertext
```

**Step 6: Decrypt your encrypted data using the same keyring you used on encrypt.**

```
decryptOutput, err := encryptionClient.Decrypt(context.Background(), esdktypes.DecryptInput{
    Ciphertext:        ciphertext,
    // Provide the encryption context that was supplied to the encrypt method
    EncryptionContext: encryptionContext,
    Keyring:           awsKmsKeyring,
})
if err != nil {
    panic(err)
}

decrypted := decryptOutput.Plaintext
```
