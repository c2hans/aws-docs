---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-multi-region-access-points.html
---

# Use Amazon S3 Multi-Region Access Points with the AWS SDK for PHP Version 3
<a name="s3-multi-region-access-points"></a>

[Amazon Simple Storage Service (S3) Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html) provide a global endpoint for routing Amazon S3 request traffic between AWS Regions.

You can create Multi-Region Access Points [using the SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3control-2018-08-20.html#createmultiregionaccesspoint), another AWS SDK, the [S3 console, or AWS CLI](https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-create-examples.html),

**Important**
To use Multi-Region Access Points with the SDK for PHP, your PHP environment must have the [AWS Common Runtime (AWS CRT) extension](guide_crt.md) installed.

When you create a Multi-Region Access Point, Amazon S3 generates an Amazon Resource Name (ARN) that has the following format:

`arn:aws:s3::{{account-id}}:accesspoint/{{MultiRegionAccessPoint_alias}}`

You can use the generated ARN in place of a bucket name for `[getObject()](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#getobject)` and `[putObject()](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#putobject)` methods.

```
<?php
require './vendor/autoload.php';

use Aws\S3\S3Client;

// Assign the Multi-Region Access Point to a variable and use it place of a bucket name.
$mrap = 'arn:aws:s3::123456789012:accesspoint/mfzwi23gnjvgw.mrap';
$key = 'my-key';

$s3Client = new S3Client([
    'region' => 'us-east-1'
]);

$s3Client->putObject([
    'Bucket' => $mrap,
    'Key' => $key,
    'Body' => 'Hello World!'
]);

$result = $s3Client->getObject([
    'Bucket' => $mrap,
    'Key' => $key
]);

echo $result['Body'] . "\n";

// Clean up.
$result = $s3Client->deleteObject([
    'Bucket' => $mrap,
    'Key' => $key
]);

$s3Client->waitUntil('ObjectNotExists', ['Bucket' => $mrap, 'Key' => $key]);

echo "Object deleted\n";
```
