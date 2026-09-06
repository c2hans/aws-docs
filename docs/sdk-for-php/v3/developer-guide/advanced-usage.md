---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/advanced-usage.html
---

# Advanced usage
<a name="advanced-usage"></a>

This section covers advanced usage patterns and techniques for the S3 Transfer Manager.

## Multipart uploads
<a name="multipart-uploads"></a>

S3 Transfer Manager automatically uses multipart uploads for large files. You can customize this behavior with configuration options.

```
<?php

use Aws\S3\S3Transfer\Models\UploadRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(null, []);

$uploadPromise = $transferManager->upload(
    new UploadRequest(
        '/path/to/large/file.mp4',
        [
            'Bucket' => 'amzn-s3-demo-bucket',
            'Key'    => 'videos/large-file.mp4',
        ],
        [
            // Use multipart upload for files larger than 100MB.
            'multipart_upload_threshold_bytes' => 100 * 1024 * 1024,

            // Use 25MB parts for multipart uploads.
            'target_part_size_bytes'           => 25 * 1024 * 1024,
        ]
    )
);
$uploadPromise->wait();
```

## Multipart downloads
<a name="multipart-downloads"></a>

You can customize multipart download behavior.

```
<?php

use Aws\S3\S3Transfer\AbstractMultipartDownloader;
use Aws\S3\S3Transfer\Models\DownloadRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(null, []);

$downloadPromise = $transferManager->download(
    new DownloadRequest(
        's3://amzn-s3-demo-bucket/large-file.mp4',
        [],
        [
            // Use 25MB parts for multipart downloads.
            'target_part_size_bytes'  => 25 * 1024 * 1024,

            // Use ranged-based download instead of part-based.
            'multipart_download_type' => AbstractMultipartDownloader::RANGED_GET_MULTIPART_DOWNLOADER,
        ]
    )
);
$downloadPromise->wait();
```

For more information about other members of the `AbstractMultipartDownloader` class, see the API documentation{{<add link>}}.

## Custom filters
<a name="custom-filters"></a>

You can use filter functions to selectively upload or download files for directory operations.

### Upload directory filter
<a name="custom-filter-upload-dir"></a>

For more information about parameter information, see the [filter callable option](directory-operations.md#upload-directory-config-callables) of the `uploadDirectory` method.

```
<?php

use Aws\S3\S3Transfer\Models\UploadDirectoryRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(null, []);

// Upload files modified in the last 24 hours.
$uploadDirPromise = $transferManager->uploadDirectory(
    new UploadDirectoryRequest(
        '/path/to/directory',
        'amzn-s3-demo-bucket',
        [],
        [
            'filter' => function ($file) {
                $modTime = filemtime($file);
                return (time() - $modTime) < 86400; // 24 hours
            },
        ]
    )
);
$uploadDirPromise->wait();
```

### Download directory filter
<a name="custom-filter-download-dir"></a>

For more information about parameter information, see the [filter callable option](directory-operations.md#download-dir-callable-options) of the `downloadDirectory` method.

```
<?php

use Aws\S3\S3Transfer\Models\DownloadDirectoryRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(null, []);

// Download files with a specific prefix.
$downloadDirPromise = $transferManager->downloadDirectory(
    new DownloadDirectoryRequest(
        'amzn-s3-demo-bucket',
        '/path/to/directory',
        [],
        [
            'filter' => function ($key) {
                return strpos($key, 'reports/2023/') === 0;
            },
        ]
    )
);
$downloadDirPromise->wait();
```

## Pre-request callbacks
<a name="pre-request-callbacks"></a>

You can modify request parameters for each file using pre-request callbacks. For more information about parameters, see the following:
+ [put\_object\_request\_callaback callable option](directory-operations.md#upload-directory-config-callables) of the `uploadDirectory` method
+ [download\_object\_request\_modifier callable option](directory-operations.md#download-dir-callable-options) of the `downloadDirectory` method

**Example of a pre-request callback for the `uploadDirectory` method**

```
<?php

use Aws\S3\S3Transfer\Models\UploadDirectoryRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(null, []);

// Set custom metadata for each uploaded file.
$uploadDirPromise = $transferManager->uploadDirectory(
    new UploadDirectoryRequest(
        '/path/to/directory',
        'amzn-s3-demo-bucket',
        [],
        [
            'upload_object_request_modifier' => function ($args) {
                $extension = pathinfo($args['Key'], PATHINFO_EXTENSION);

                switch ($extension) {
                    case 'jpg':
                    case 'jpeg':
                        $args['ContentType'] = 'image/jpeg';
                        break;
                    case 'png':
                        $args['ContentType'] = 'image/png';
                        break;
                    case 'pdf':
                        $args['ContentType'] = 'application/pdf';
                        break;
                }

                $args['Metadata'] = [
                    'uploaded_at' => date('Y-m-d H:i:s'),
                ];
            },
        ]
    )
);
$uploadDirPromise->wait();
```
