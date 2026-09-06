---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/s3-checksums.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Data integrity protection with Amazon S3 checksums
<a name="s3-checksums"></a>

Amazon Simple Storage Service (Amazon S3) provides the ability to specify a checksum when you upload an object. When you specify a checksum, it is stored with the object and can be validated when the object is downloaded.

Checksums provide an additional layer of data integrity when you transfer files. With checksums, you can verify data consistency by confirming that the received file matches the original file. For more information about checksums with Amazon S3, see the [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html), including the [supported algorithms](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#using-additional-checksums).

You have the flexibility to choose the algorithm that best fits your needs and let the SDK calculate the checksum. Alternatively, you can provide a pre-computed checksum value by using one of the supported algorithms.

**Note**
Beginning with version 3.729.0 of the AWS SDK for JavaScript, the SDK provides default integrity protections by automatically calculating a `CRC32` checksum for uploads. The SDK calculates this checksum if you don't provide a precalculated checksum value or if you don't specify an algorithm that the SDK should use to calculate a checksum.
The SDK also provides global settings for data integrity protections that you can set externally, which you can read about in the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/feature-dataintegrity.html).

## Upload an object
<a name="use-service-S3-checksum-upload"></a>

You upload objects to Amazon S3 by using the [PutObject](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/PutObjectCommand/) command of the `S3Client`. Use the `ChecksumAlgorithm` parameter of the builder for the `PutObjectRequest` to enable checksum computation and specify the algorithm. See [supported checksum algorithms](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#using-additional-checksums) for valid values.

The following code snippet shows a request to upload an object with a CRC-32 checksum. When the SDK sends the request, it calculates the CRC-32 checksum and uploads the object. Amazon S3 stores the checksum with the object.

```
import { ChecksumAlgorithm, S3 } from "@aws-sdk/client-s3";

const client = new S3();
const response = await client.putObject({
  Bucket: "my-bucket",
  Key: "my-key",
  Body: "Hello, world!",
  ChecksumAlgorithm: ChecksumAlgorithm.CRC32,
});
```

If you don't provide a checksum algorithm with the request, the checksum behavior varies depending on the version of the SDK that you use as shown in the following table.

**Checksum behavior when no checksum algorithm is provided**

| SDK for JavaScript version | Checksum behavior |
| --- | --- |
| Earlier than 3.729.0 | The SDK doesn't automatically calculate a CRC-based checksum and provide it in the request. |
| 3.729.0 or later | The SDK uses the CRC32 algorithm to calculate the checksum and provides it in the request. Amazon S3 validates the integrity of the transfer by computing its own CRC32 checksum and compares it to the checksum provided by the SDK. If the checksums match, the checksum is saved with the object. |

If the checksum that the SDK calculates doesn't match the checksum that Amazon S3 calculates when it receives the request, an error is returned.

### Use a pre-calculated checksum value
<a name="use-service-S3-checksum-upload-pre"></a>

A pre-calculated checksum value provided with the request disables automatic computation by the SDK and uses the provided value instead.

The following example shows a request with a pre-calculated SHA-256 checksum.

```
import { S3 } from "@aws-sdk/client-s3";
import { createHash } from "node:crypto";

const client = new S3();

const Body = "Hello, world!";
const ChecksumSHA256 = await createHash("sha256").update(Body).digest("base64");

const response = await client.putObject({
  Bucket: "my-bucket",
  Key: "my-key",
  Body,
  ChecksumSHA256,
});
```

If Amazon S3 determines the checksum value is incorrect for the specified algorithm, the service returns an error response.

### Multipart uploads
<a name="use-service-S3-checksum-upload-multi"></a>

You can also use checksums with multipart uploads. The AWS SDK for JavaScript can use the `Upload` library options to from `@aws-sdk/lib-storage` to use checksums with multipart uploads.

```
import { ChecksumAlgorithm, S3 } from "@aws-sdk/client-s3";
import { Upload } from "@aws-sdk/lib-storage";
import { createReadStream } from "node:fs";

const client = new S3();
const filePath = "/path/to/file";
const Body = createReadStream(filePath);

const upload = new Upload({
  client,
  params: {
    Bucket: "my-bucket",
    Key: "my-key",
    Body,
    ChecksumAlgorithm: ChecksumAlgorithm.CRC32,
  },
});
await upload.done();
```
