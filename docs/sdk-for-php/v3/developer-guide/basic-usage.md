---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/basic-usage.html
---

# Basic usage
<a name="basic-usage"></a>

The following example shows how to use the S3 Transfer Manager:

```
<?php

use Aws\S3\S3Client;
use Aws\S3\S3Transfer\Models\UploadRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

// Create an S3 client.
$s3Client = new S3Client([
    'version' => 'latest',
    'region'  => 'us-west-2',
]);

// Create a transfer manager with default configuration.
$transferManager = new S3TransferManager($s3Client);

// Alternative: Create transfer manager with null client. S3 Transfer Manager uses a default S3 client.
$transferManager = new S3TransferManager(null, [
    'default_region' => 'us-west-2'
]);

// Example: Upload a file.
$uploadPromise = $transferManager->upload(
    new UploadRequest(
        '/path/to/local/file.txt',
        [
            'Bucket' => 'amzn-s3-demo-bucket',
            'Key'    => 'path/to/s3/file.txt',
        ]
    )
);

// Wait for the upload to complete.
$result = $uploadPromise->wait();

echo "Upload complete!\n";
```

**Important**
When using S3 Transfer Manager to create a default Amazon S3 client customers may pass a default Region for the client using the `default_region` parameter in the Transfer Manager `config` options, otherwise the Amazon S3 client tries to resolve a Region using the default behavior for resolving configurations, and if the Region is not resolved then an exception is thrown.

## Creating a transfer manager
<a name="creating-transfer-manager"></a>

You can create a transfer manager in two ways:

With an existing S3 client
Pass an existing [https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html) instance to the `S3TransferManager` {{<add link>}} constructor.

```
<?php

use Aws\S3\S3Client;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

// Create an S3 client.
$s3Client = new S3Client([
    'version' => 'latest',
    'region'  => 'us-west-2',
]);

$transferManager = new S3TransferManager($s3Client);
```

With default S3 client creation
Pass `null` as the client and specify configuration options.

```
<?php

use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(null, [
    'default_region' => 'us-west-2'
]);
```
