---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-checksums.html
---

# Data integrity protection with checksums
<a name="s3-checksums"></a>

Amazon Simple Storage Service (Amazon S3) provides the ability to specify a checksum when you upload an object. When you specify a checksum, it is stored with the object and can be validated when the object is downloaded.

Checksums provide an additional layer of data integrity when you transfer files. With checksums, you can verify data consistency by confirming that the received file matches the original file. For more information about checksums with Amazon S3, see the [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) including the [supported algorithms](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#using-additional-checksums).

You have the flexibility to choose the algorithm that best fits your needs and let the SDK calculate the checksum. Alternatively, you can provide a pre-computed checksum value by using one of the supported algorithms.

**Note**
Beginning with version 3.337.0 of the AWS SDK for PHP, the SDK provides default integrity protection by automatically calculating a `CRC32` checksum for uploads. The SDK calculates this checksum if you don't provide a precalculated checksum value or if you don't specify an algorithm that the SDK should use to calculate a checksum.
The SDK also provides global settings for data integrity protections that you can set externally, which you can read about in the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/feature-dataintegrity.html).

**Important**
To work with the `CRC32C` algorithm, your PHP environment requires the[ installation of the AWS Common Runtime (AWS CRT) extension](guide_crt.md).

We discuss checksums in two request phases: uploading an object and downloading an object.

## Upload an object
<a name="use-service-S3-checksum-upload"></a>

You upload objects to Amazon S3 by using the [putObject](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#putobject) method of the `S3Client`. Use the `ChecksumAlgorithm` pair in the parameter array to enable checksum computation and specify the algorithm.

```
$client = new \Aws\S3\S3Client(['region' => 'us-east-2']); // See the note below.
$result = $client->putObject([
        'Bucket' => '{{amzn-s3-demo-bucket}}',
        'Key' => '{{key}}',
        'ChecksumAlgorithm' => 'CRC32',
        'Body' => 'Object contents to test the checksum.'
]);
```

If you don't provide a checksum algorithm with the request, the checksum behavior varies depending on the version of the SDK that you use as shown in the following table.

**Checksum behavior when no checksum algorithm is provided**

| PHP SDK version | Checksum behavior |
| --- | --- |
| earlier than 3.337.0 | The SDK doesn't automatically calculate a CRC-based checksum and provide it in the request. |
| 3.337.0 or later | The SDK uses the `CRC32` algorithm to calculate the checksum and provides it in the request. Amazon S3 validates the integrity of the transfer by computing its own `CRC32` checksum and compares it to the checksum provided by the SDK. If the checksums match, the checksum is saved with the object. |

### Use a pre-calculated checksum value
<a name="use-service-S3-checksum-upload-pre"></a>

A pre-calculated checksum value provided with the request disables automatic computation by the SDK and uses the provided value instead.

The following example shows a request with a pre-calculated SHA256 checksum.

```
use Aws\S3\S3Client;
use GuzzleHttp\Psr7;

$client = new S3Client([
    'region' => 'us-east-1',
]);

// Calculate the SHA256 checksum of the contents to be uploaded.
$contents = 'Object contents to test the checksum.';
$body = Psr7\Utils::streamFor($contents);
$sha256 = base64_encode(Psr7\Utils::hash($body, 'sha256', true));

$result = $client->putObject([
    'Bucket' => '{{amzn-s3-demo-bucket}}',
    'Key' => '{{key'}},
    'Body' => $body,
    'ChecksumSHA256' => $sha256
]);
```

If Amazon S3 determines the checksum value is incorrect for the specified algorithm, the service returns an error response.

### Multipart uploads
<a name="use-service-S3-checksum-upload-multi"></a>

You can also use checksums with multipart uploads.

 As shown in the following example, specify the checksum algorithm as a key-value pair in the `params` array of the [`MultipartUploader` constructor](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.MultipartUploader.html#___construct).

```
$s3Client = new S3Client([
    'region' => 'us-east-1'
]);

$stream = fopen("{{/path/to/large/file}}", "r");

$mpUploader = new MultipartUploader($s3Client, $stream, [
    'bucket' => '{{amzn-s3-demo-bucket}}',
    'key' => '{{key'}},
    'params' => ['ChecksumAlgorithm' => 'CRC32']
]);
```

## Download an object
<a name="use-service-S3-checksum-download"></a>

When you use the [getObject](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#getobject) method to download an object, the SDK automatically validates the checksum when the `ChecksumMode` key's value is `enabled`.

The request in the following snippet directs the SDK to validate the checksum in the response by calculating the checksum and comparing the values.

```
$result = $client->getObject([
        'Bucket' => '{{amzn-s3-demo-bucket}}',
        'Key' => '{{test-checksum-key}}',
        'ChecksumMode' => 'enabled',
]);
```

**Note**
If the object wasn't uploaded with a checksum, no validation takes place.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
