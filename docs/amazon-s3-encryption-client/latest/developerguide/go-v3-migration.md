---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/go-v3-migration.html
---

# S3 Encryption Client Migration (2.*x* to 3.*x*)
<a name="go-v3-migration"></a>

**Note:** If you're using version 3.*x* of the Amazon S3 Encryption Client for Go and want to migrate to version 4.*x*, see [S3 Encryption Client Migration (3.*x* to 4.*x*)](go-v4-migration.md).

With version 3.*x* of the Amazon S3 Encryption Client for Go, you create one client for both encryption and decryption. Version 3.*x* replaces the cipher data generators with the cryptographic materials manager (CMM), and replaces the KMS key providers, `NewKMSContextKeyGenerator`, with the `NewKmsKeyring`.

When updating from earlier versions of the Amazon S3 Encryption Client to version 3.*x*, you need to update your client builder code to use the new, simpler client. If you're decrypting ciphertext that was encrypted by earlier versions of the Amazon S3 Encryption Client, you might also need to allow the Amazon S3 Encryption Client to [decrypt legacy encryption algorithms](#enable-legacy-go-v3).

The following examples show the equivalent code required to specify a KMS key provider with a KMS key ID in versions 1.*x*, 2.*x*, and 3.*x* of the Amazon S3 Encryption Client.

------
#### [ Version 1.*x* ]

In version 1.*x*, you use the `NewKMSKeyGeneratorWith` function to construct the `cipherDataGenerator`.

```
sess := session.Must(session.NewSession())
kmsClient := kms.New(sess)
cmkID := "1234abcd-12ab-34cd-56ef-1234567890ab"

cipherDataGenerator := s3crypto.NewKMSKeyGenerator(kmsClient, {{kmsKeyID}})
```

------
#### [ Version 2.*x* ]

In version 2.*x*, you use the `NewKMSContextKeyGenerator` function to construct the `cipherDataGenerator`.

```
sess := session.Must(session.NewSession())
kmsClient := kms.New(sess)
cmkID := "1234abcd-12ab-34cd-56ef-1234567890ab"
var matDesc s3crypto.MaterialDescription

// changed NewKMSKeyGenerator to NewKMSContextKeyGenerator
cipherDataGenerator := s3crypto.NewKMSContextKeyGenerator(kmsClient, {{kmsKeyID}}, matDesc)
```

------
#### [ Version 3.*x* ]

In version 3.*x*, you use the `NewKmsKeyring` function to construct your cryptographic materials manager (CMM).

```
s3Client := s3.NewFromConfig(cfg)
kmsClient := kms.NewFromConfig(cfg)
cmm, err := materials.NewCryptographicMaterialsManager(materials.NewKmsKeyring(kmsClient, {{kmsKeyID}}))
	if err != nil {
		return fmt.Errorf("error while creating new CMM")
	}
```

------

## Migrating from version 2.*x*
<a name="migrate-v2-to-v3"></a>

The following example demonstrates how to migrate a version 2.*x* application that uses the `NewKMSContextKeyGenerator` KMS key provider with a material description and `AESGCMContentCipherBuilderV2` content cipher to version 3.*x* of the Amazon S3 Encryption Client for Go.

```
import (
	"bytes"
	"context"
	"fmt"
	"log"

	// AWS SDK for Go v1 (for V2 S3EC)
	awsV1 "github.com/aws/aws-sdk-go/aws"
	sessionV1 "github.com/aws/aws-sdk-go/aws/session"
	kmsV1 "github.com/aws/aws-sdk-go/service/kms"
	s3V1 "github.com/aws/aws-sdk-go/service/s3"
	s3cryptoV2 "github.com/aws/aws-sdk-go/service/s3/s3crypto"

	// AWS SDK for Go v2 (for V3 S3EC)
	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/kms"
	"github.com/aws/aws-sdk-go-v2/service/s3"

	// V3 S3 Encryption Client imports
	"github.com/aws/amazon-s3-encryption-client-go/v3/client"
	"github.com/aws/amazon-s3-encryption-client-go/v3/materials"
)

func KmsContextV2toV3GCMExample() error {
	bucket := LoadBucket()
	kmsKeyAlias := LoadAwsKmsAlias()

	objectKey := "my-object-key"
	region := "us-west-2"
	plaintext := "This is an example.\n"

	// Create an S3EC Go v2 encryption client
	// using the KMS client from AWS SDK for Go v1
	sessKms, err := sessionV1.NewSession(&awsV1.Config{
		Region: aws.String(region),
	})

	kmsSvc := kmsV1.New(sessKms)
	handler := s3cryptoV2.NewKMSContextKeyGenerator(kmsSvc, kmsKeyAlias, s3cryptoV2.MaterialDescription{})
	builder := s3cryptoV2.AESGCMContentCipherBuilderV2(handler)
	encClient, err := s3cryptoV2.NewEncryptionClientV2(sessKms, builder)
	if err != nil {
		log.Fatalf("error creating new v2 client: %v", err)
	}

	// Encrypt using KMS+Context and AES-GCM content cipher
	_, err = encClient.PutObject(&s3V1.PutObjectInput{
		Bucket: aws.String(bucket),
		Key:    aws.String(objectKey),
		Body:   bytes.NewReader([]byte(plaintext)),
	})
	if err != nil {
		log.Fatalf("error calling putObject: %v", err)
	}
	fmt.Printf("successfully uploaded file to %s/%s\n", bucket, key)

	// Create an S3EC Go v3 client
	// using the KMS client from AWS SDK for Go v2
	ctx := context.Background()
	cfg, err := config.LoadDefaultConfig(ctx,
		config.WithRegion(region),
	)

	kmsV2 := kms.NewFromConfig(cfg)
	cmm, err := materials.NewCryptographicMaterialsManager(materials.NewKmsKeyring(kmsV2, kmsKeyAlias))
	if err != nil {
		t.Fatalf("error while creating new CMM")
	}

	s3V2 := s3.NewFromConfig(cfg)
	s3ecV3, err := client.New(s3V2, cmm)

	result, err := s3ecV3.GetObject(ctx, &s3.GetObjectInput{
		Bucket: aws.String(bucket),
		Key:    aws.String(objectKey),
	})
	if err != nil {
		t.Fatalf("error while decrypting: %v", err)
	}
}
```

## Enable legacy decryption modes
<a name="enable-legacy-go-v3"></a>

If you need to decrypt objects or data keys that were encrypted with a legacy algorithm, or you need to partially decrypt an AES-GCM encrypted object when performing a [ranged request](java-examples.md#ranged-gets), you need to explicitly enable this behavior when you instantiate the client.

Version 3.*x* of the Amazon S3 Encryption Client encrypts only with [fully supported algorithms](encryption-algorithms.md#v3-algorithms). It will never encrypt with a legacy algorithm. By default, it decrypts only with fully supported algorithms, but you can enable it to decrypt with both fully supported and legacy algorithms. For more information, see [Decryption modes (Amazon S3 Encryption Client for Java version 3.*x* and later)](encryption-algorithms.md#decryption-modes).

The `enableLegacyUnauthenticatedModes` flag enables the Amazon S3 Encryption Client to decrypt encrypted objects with a fully supported or legacy encryption algorithm.

Version 3.*x* of the Amazon S3 Encryption Client uses one of the fully supported wrapping algorithms and the wrapping key you specify to encrypt and decrypt the data keys. The `enableLegacyWrappingAlgorithms` flag enables the Amazon S3 Encryption Client to decrypt encrypted data keys with a fully supported or legacy wrapping algorithm.

If your client doesn't include the necessary legacy decryption mode with a value of `true`, and it encounters an object encrypted with a legacy algorithm, it throws `S3EncryptionClientException`.

The following example enables the `enableLegacyUnauthenticatedModes` and `enableLegacyWrappingAlgorithms` flags. This client always encrypts only with fully supported algorithms. However, it can decrypt objects and data keys encrypted with fully supported or legacy algorithms.

```
cmm, err := materials.NewCryptographicMaterialsManager(materials.NewKmsKeyring(kmsClient, , func(options *materials.KeyringOptions) {
    options.EnableLegacyWrappingAlgorithms = true
})

if err != nil {
	t.Fatalf("error while creating new CMM")
}

client, err := client.New(s3Client, cmm, func(clientOptions *client.EncryptionClientOptions) {
		clientOptions.EnableLegacyUnauthenticatedModes = true
})

if err != nil {
	// handle error
}
```

The legacy decryption modes are designed to be a temporary fix. After you've re-encrypted all of your objects with fully supported algorithms, you can eliminate it from your code.
