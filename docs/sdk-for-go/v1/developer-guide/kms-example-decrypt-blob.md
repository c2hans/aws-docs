---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/kms-example-decrypt-blob.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Decrypting a Data Blob in AWS Key Management Service
<a name="kms-example-decrypt-blob"></a>

The following example uses the AWS SDK for Go[Decrypt](https://docs.aws.amazon.com/sdk-for-go/api/service/kms/#KMS.Decrypt) method, which implements the [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) operation, to decrypt the provided string and emits the result.

```
import (
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/kms"

    "fmt"
    "os"
)

func main() {
    // Initialize a session that the SDK uses to load
    // credentials from the shared credentials file ~/.aws/credentials
    // and configuration from the shared configuration file ~/.aws/config.
    sess := session.Must(session.NewSessionWithOptions(session.Options{
        SharedConfigState: session.SharedConfigEnable,
    }))

    // Create KMS service client
    svc := kms.New(sess)

    // Encrypted data
    blob := []byte("1234567890")

    // Decrypt the data
    result, err := svc.Decrypt(&kms.DecryptInput{CiphertextBlob: blob})

    if err != nil {
        fmt.Println("Got error decrypting data: ", err)
        os.Exit(1)
    }

    blob_string := string(result.Plaintext)

    fmt.Println(blob_string)
```

Choose `Copy` to save the code locally. See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/go/example_code/kms/kms_decrypt_data.go) on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
