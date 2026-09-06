---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/examples.html
---

# Ready-to-use examples
<a name="examples"></a>

This section provides a complete helper class with static methods for common S3 Transfer Manager operations. The helper class simplifies usage. It handles initialization and configuration internally.

## S3TransferHelper class
<a name="s3-transfer-helper-class"></a>

```
<?php

use Aws\S3\S3Transfer\Models\DownloadDirectoryRequest;
use Aws\S3\S3Transfer\Models\DownloadFileRequest;
use Aws\S3\S3Transfer\Models\DownloadRequest;
use Aws\S3\S3Transfer\Models\UploadDirectoryRequest;
use Aws\S3\S3Transfer\Models\UploadRequest;
use Aws\S3\S3Transfer\S3TransferManager;
use Psr\Http\Message\StreamInterface;

class S3TransferHelper
{
    /**
     * Upload a file from a local path to S3.
     */
    public static function uploadFile(
        string $filePath,
        string $bucket,
        string $key
    ): array
    {
        $transferManager = new S3TransferManager();

        $uploadRequest = new UploadRequest(
            $filePath,
            [
                'Bucket' => $bucket,
                'Key'    => $key,
            ],
            []
        );

        return $transferManager->upload($uploadRequest)->wait()->getResult();
    }

    /**
     * Upload from a stream to S3
     */
    public static function uploadFromStream(
        StreamInterface $stream,
        string          $bucket,
        string          $key,
        bool            $trackProgress = true,
    ): array
    {
        $transferManager = new S3TransferManager();

        $uploadRequest = new UploadRequest(
            $stream,
            [
                'Bucket' => $bucket,
                'Key'    => $key,
            ],
            ['track_progress' => $trackProgress]
        );

        return $transferManager->upload($uploadRequest)->wait()->getResult();
    }

    /**
     * Download a file from S3 to a local path
     */
    public static function downloadFile(
        string $bucket,
        string $key,
        string $destinationPath,
        bool   $failsWhenDestinationExists = false,
        bool   $trackProgress = true,
    ): void
    {
        $transferManager = new S3TransferManager();
        $downloadRequest = new DownloadRequest(
            [
                'Bucket' => $bucket,
                'Key'    => $key
            ],
            [],
            ['track_progress' => $trackProgress]
        );

        $downloadFileRequest = new DownloadFileRequest(
            $destinationPath,
            $failsWhenDestinationExists,
            $downloadRequest
        );

        $transferManager->downloadFile($downloadFileRequest)->wait();
    }

    /**
     * Upload an entire directory to S3
     */
    public static function uploadDirectory(
        string $sourceDirectory,
        string $bucket,
        string $s3Prefix = '',
        bool   $trackProgress = true,
    ): array
    {
        $transferManager = new S3TransferManager();
        $uploadDirectoryRequest = new UploadDirectoryRequest(
            $sourceDirectory,
            $bucket,
            [],
            [
                's3_prefix'      => $s3Prefix,
                'track_progress' => $trackProgress,
            ]
        );

        $result = $transferManager->uploadDirectory($uploadDirectoryRequest)->wait();

        return [
            'uploaded' => $result->getObjectsUploaded(),
            'failed'   => $result->getObjectsFailed(),
        ];
    }

    /**
     * Download directory from S3
     */
    public static function downloadDirectory(
        string $bucket,
        string $destinationDirectory,
        string $s3Prefix = '',
        bool   $trackProgress = true,
    ): array
    {
        $transferManager = new S3TransferManager();
        $downloadDirectoryRequest = new DownloadDirectoryRequest(
            $bucket,
            $destinationDirectory,
            [],
            [
                's3_prefix'      => $s3Prefix,
                'track_progress' => $trackProgress,
            ]
        );

        $result = $transferManager->downloadDirectory($downloadDirectoryRequest)->wait();

        return [
            'downloaded' => $result->getObjectsDownloaded(),
            'failed'     => $result->getObjectsFailed(),
        ];
    }
}
```

## Helper class usage examples
<a name="helper-usage-examples"></a>

The following examples show how to use the `S3TransferHelper` class.

```
<?php

require __DIR__ . '/../vendor/autoload.php';
require __DIR__ . '/S3TransferHelper.php';

// Upload a local file
$result = S3TransferHelper::uploadFile(
    '/path/to/local/document.pdf',
    'amzn-s3-demo-bucket',
    'documents/document.pdf'
);

echo "File uploaded successfully. ETag: " . $result['ETag'] . "\n";

// Download a file to local path
S3TransferHelper::downloadFile(
    'amzn-s3-demo-bucket',
    'documents/document.pdf',
    '/path/to/local/downloaded-document.pdf',
    false, // Don't fail if destination exists
    true   // Track progress
);

echo "File downloaded successfully!\n";

// Upload entire directory
$result = S3TransferHelper::uploadDirectory(
    '/path/to/local/photos',
    'amzn-s3-demo-bucket',
    'photos/vacation-2023/', // S3 prefix
    true // Track progress
);

echo "Directory upload completed.\n";
echo "Uploaded: {$result['uploaded']} files\n";
echo "Failed: {$result['failed']} files\n";

// Download directory from S3
$result = S3TransferHelper::downloadDirectory(
    'amzn-s3-demo-bucket',
    '/path/to/local/downloads',
    'photos/vacation-2023/', // S3 prefix to download
    true // Track progress
);

echo "Directory download completed.\n";
echo "Downloaded: {$result['downloaded']} files\n";
echo "Failed: {$result['failed']} files\n";
```
