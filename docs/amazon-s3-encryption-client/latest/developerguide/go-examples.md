---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/go-examples.html
---

# Amazon S3 Encryption Client for Go examples
<a name="go-examples"></a>

The following examples show you how to use the Amazon S3 Encryption Client for Go to encrypt and decrypt Amazon S3 objects. These examples show how to use version 4.*x* of the Amazon S3 Encryption Client for Go.

**Note**
The Amazon S3 Encryption Client for Go does not support [asynchronous programming](using-s3ec-async.md), [multipart uploads](java-examples.md#multipart-upload), or [ranged GET requests](java-examples.md#ranged-gets). To use these features of the Amazon S3 Encryption Client, you must use the Amazon S3 Encryption Client for Java or another Amazon S3 Encryption Client implementation that supports the feature or features in question.

**Topics**
+ [Instantiating the Amazon S3 Encryption Client](#go-instantiate-client)
+ [Encrypting and decrypting Amazon S3 objects](#go-encrypt-example)

## Instantiating the Amazon S3 Encryption Client
<a name="go-instantiate-client"></a>

After [installing the Amazon S3 Encryption Client for Go](go.md#go-installation), you are ready to instantiate your client and begin encrypting and decrypting your Amazon S3 objects. If you have encrypted objects under a previous version of the Amazon S3 Encryption Client, you may need to enable legacy decryption modes or configure a commmitment policy when you instantiate the updated client. For more information, see [Migrating to version 4.*x* of the Amazon S3 Encryption Client for Go](go-v4-migration.md).

The Amazon S3 Encryption Client for Go supports [keyrings](concepts.md#keyring) that use symmetric encryption KMS keys as the wrapping key. The Amazon S3 Encryption Client for Go does not support keyrings that use Raw AES-GCM or Raw RSA wrapping keys. To use Raw AES-GCM or Raw RSA wrapping keys, you must use the Amazon S3 Encryption Client for Java or another Amazon S3 Encryption Client implementation that supports these wrapping key types. For more information, see [Instantiating the Amazon S3 Encryption Client for Java](java-examples.md#java-instantiate-client).

To use a KMS key as your wrapping key, you need [kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) and [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) permissions on the KMS key. To specify a KMS key, use any valid KMS key identifier. For details, see [Key identifiers](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *AWS Key Management Service Developer Guide*.

The following example instantiates the Amazon S3 Encryption Client with the default decryption mode. This means that all objects will be decrypted using the fully supported buffered decryption mode. For more information, see [Decryption modes (Version 3.*x* and later)](encryption-algorithms.md#decryption-modes).

```
import (
   ...
   // Import the materials and client package
   "github.com/aws/amazon-s3-encryption-client-go/client/v4"
   "github.com/aws/amazon-s3-encryption-client-go/materials/v4"
   ...
)
s3EncryptionClient, err := client.New(s3Client, cmm)

// Create the keyring and cryptographic materials manager (CMM)
cmm, err := materials.NewCryptographicMaterialsManager(materials.NewKmsKeyring(kmsClient, {{kmsKeyArn}}, func(options *materials.KeyringOptions) {
		options.EnableLegacyWrappingAlgorithms = false
}))
if err != nil {
	t.Fatalf("error while creating new CMM")
}

s3EncryptionClient, err := client.New(s3Client, cmm)
```

## Encrypting and decrypting Amazon S3 objects
<a name="go-encrypt-example"></a>

The following example shows you how to use the Amazon S3 Encryption Client for Go to encrypt and decrypt Amazon S3 objects.

1. Create a [keyring](concepts.md#keyring) with a KMS key as your wrapping key when you [instantiate your client](#go-instantiate-client).

   ```
   s3Client = s3.NewFromConfig(cfg)
   kmsClient := kms.NewFromConfig(cfg)
   cmm, err := materials.NewCryptographicMaterialsManager(materials.NewKmsKeyring(kmsClient, {{kmsKeyArn}}, func(options *materials.KeyringOptions) {
       options.EnableLegacyWrappingAlgorithms = false
   }))
   if err != nil {
       t.Fatalf("error while creating new CMM")
   }
   ```

1. Encrypt your plaintext object by calling [`PutObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html). To include an optional material description, add an `EncryptionContext` value to the `context` and supply this value to the `PutObject` request.

   1. The Amazon S3 Encryption Client provides the encryption materials: one plaintext data key and one copy of that data key encrypted by your wrapping key.

   1. The Amazon S3 Encryption Client uses the plaintext data key to encrypt your object, and then discards the plaintext data key.

   1. The Amazon S3 Encryption Client uploads the encrypted data key and the encrypted object to Amazon S3 as part of the `PutObject` call.

   ```
   ctx := context.Background()
   ...
   encryptionContext := context.WithValue(ctx, "EncryptionContext", map[string]string{"ec-key": "ec-value"})

   s3EncryptionClient, err := client.New(s3Client, cmm)
   _, err = s3EncryptionClient.PutObject(encryptionContext, &s3.PutObjectInput{
       Bucket: aws.String({{bucket}}),
       Key:    aws.String({{objectKey}}),
       Body:   bytes.NewReader([]byte({{plaintext}})),
   })

   if err != nil {
       t.Fatalf("error while encrypting: %v", err)
   }
   ```

1. Decrypt your encrypted object by calling [`GetObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html).

   1. The Amazon S3 Encryption Client uses your wrapping key to decrypt the encrypted data key.

   1. The Amazon S3 Encryption Client uses the plaintext data key to decrypt the object, discards the plaintext data key, and returns the plaintext object as part of the `GetObject` call.

   ```
   result, err := s3EncryptionClient.GetObject(ctx, &s3.GetObjectInput{
   		Bucket: aws.String({{bucket}}),
   		Key:    aws.String({{objectKey}}),
   	})
   	if err != nil {
   		return fmt.Errorf("error while decrypting: %v", err)
   	}

   	decryptedPlaintext, err := io.ReadAll(result.Body)
   	if err != nil {
   		return fmt.Errorf("failed to read decrypted plaintext into byte array")
   	}
   ```

1. Optional: verify that the decrypted object matches the original plaintext object that you uploaded.

   ```
   if e, a := []byte(plaintext), decryptedPlaintext; !bytes.Equal(e, a) {
   		return fmt.Errorf("expect %v text, got %v", e, a)
   	}
   ```
