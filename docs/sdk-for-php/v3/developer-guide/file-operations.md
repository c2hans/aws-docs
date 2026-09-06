---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/file-operations.html
---

# File operations
<a name="file-operations"></a>

S3 Transfer Manager provides methods for uploading and downloading individual files.

## Upload local files
<a name="upload-files"></a>

To upload a file to Amazon S3, use the `upload` {{<add link>}} method.

```
<?php

use Aws\S3\S3Transfer\Models\UploadRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(null, [
    'default_region' => 'us-west-2'
]);

// Source can be from a local path to a file.
$source = '/path/to/local/file.txt';
// Or the source can be an instance of StreamInterface.
$source = GuzzleHttp\Psr7\Utils::streamFor('Hello World!');

$uploadPromise = $transferManager->upload(
    new UploadRequest(
        $source,
        [
            'Bucket' => 'amzn-s3-demo-bucket',
            'Key'    => 'path/to/s3/file.txt',
            // Additional `putObject` parameters as needed.
        ],
        [
            // Optional configuration overrides.
            'multipart_upload_threshold_bytes' => 100 * 1024 * 1024, // 100MB
            'target_part_size_bytes'           => 10 * 1024 * 1024, // 10MB
            'track_progress'                   => true,
            'request_checksum_calculation'     => 'when_required',
        ]
    )
);

// The upload is asynchronous, you can wait for it to complete.
$result = $uploadPromise->wait();

// Or you can use the promise for more complex workflows.
$result = $uploadPromise->then(
    function ($result) {
        echo "Upload succeeded!";
    },
    function ($error) {
        echo "Upload failed: " . $error->getMessage();
    }
)->wait();
```

### `upload` method parameters
<a name="upload-parameters"></a>

The `upload` method accepts an instance of `UploadRequest` {{<add link>}} as an argument.

#### `UploadRequest` parameters
<a name="upload-request-parameters"></a>

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `$source` | string\|`StreamInterface` | Yes | Path of local file path or stream containing data to upload. |
| `$uploadRequestArgs` | array | Yes | Upload request arguments (must include Bucket and Key). |
| `$config` | array | No | Configuration overrides specific to this upload. For more information about configuration options, see the[ following section](#upload-request-config-parameters). |
| `$listeners` | array | No | Array of `TransferListener` objects for monitoring this upload. |
| `$progressTracker` | TransferListener | No | A progress tracker for this upload. |

##### `$config` options for `UploadRequest`
<a name="upload-request-config-parameters"></a>

The SDK resolves default `$config` value from the [configuration](configuration.md#configuration-options) of the S3 Transfer Manager.

| Option | Type | Required | Description |
| --- | --- | --- | --- |
| `multipart_upload_threshold_bytes` | int | No | Overrides the default threshold for when a multipart upload is triggered. |
| `target_part_size_bytes` | int | No | Overrides the default target part size in bytes. |
| `track_progress` | bool | No | Overrides the default option to enable progress tracking. If this option is true and you don't provide a progressTracker parameter, the SDK uses a default implementation. |
| `concurrency` | int | No | Overrides the default value for concurrency. |
| `request_checksum_calculation` | string | No | Overrides the default value for whether a request checksum calculation must be performed. |

When the `upload` method runs successfully, it returns an `UploadResult` {{<add link>}}.

## Download S3 objects
<a name="download-files"></a>

To download an object from Amazon S3, use the `download` {{<add link>}} method.

```
<?php

use Aws\S3\S3Transfer\Models\DownloadRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(null, [
    'default_region' => 'us-west-2'
]);

// Download using an S3 URI.
$downloadPromise = $transferManager->download(
    new DownloadRequest(
        's3://amzn-s3-demo-bucket/path/to/s3/file.txt',
        [
            // Additional `getObject` parameters as needed.
        ],
        [
            // Optional configuration overrides.
            'response_checksum_validation' => 'when_required',
            'track_progress'               => true,
            'target_part_size_bytes'       => 10 * 1024 * 1024, // 10MB
        ]
    )
);

// Wait for the download to complete.
$result = $downloadPromise->wait();

// The SDK uses a stream-based download handler by default.
$stream = $result->getDownloadDataResult();

// You can either get the content.
$content = $stream->getContents();

// Or write the stream to a file.
file_put_contents('/path/to/local/file.txt', $stream);

// Don't forget to close the stream.
$stream->close();
```

### `download` method parameters
<a name="download-parameters"></a>

The `download` method accepts an instance of `DownloadRequest` {{<add link>}} as an argument.

#### DownloadRequest parameters
<a name="download-request-parameters"></a>

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `$source` | string\|array\|`null` | No | The object to download from S3. You can provide this parameter as an S3 URI string ("s3://amzn-s3-demo-bucket/key"), an array with Bucket and Key keys, or `null`. When this value is `null`, pass the Bucket and Key values in the `$downloadRequestArgs` parameter. |
| `$downloadRequestArgs` | array | No | Additional download object request arguments. If `$source` is `null`, provide the Bucket and Key values here.  |
| `$config` | array | No | Configuration overrides specific to this download. For more information about configuration options, see the [following section](#download-request-config-parameters). |
| $downloadHandler | `AbstractDownloadHandler`{{<add link>}}\|`null` | No | The handler that receives each object chunk and manages its download. <br />The default handler for the `download` method uses a stream-based handler. This handler pushes each object chunk into a stream. <br />The default handler for the `downloadFile` method (see [Download an S3 object to a local file](#download-file-to-local)) uses a file-based handler. This handler writes each chunk to a file.<br />You can implement your own `DownloadHandler` to customize where and how the SDK stores downloaded data. For example, you can store data in databases, cloud storage, or custom processing pipelines instead of files or streams. |
| `$progressTracker` | `TransferListener` | No | A progress tracker for this download. |
| `$listeners` | `array` | No | Array of `AbstractTransferListener` objects for monitoring this download. |

##### `$config` options for `DownloadRequest`
<a name="download-request-config-parameters"></a>

The SDK resolves default `$config` value from the [configuration](configuration.md#configuration-options) of the S3 Transfer Manager.

| Option | Type | Required | Description |
| --- | --- | --- | --- |
| `multipart_download_type` | string | No | Overrides the default multipart download type. Valid values are 'part', 'ranged' |
| `response_checksum_validation` | string | No | Overrides the resolved value from transfer manager config for whether checksum validation should be done. The SDK considers this option only if `ChecksumMode` is not present in the `$getObjectRequestArgs` of the `DownloadRequest`. |
| `track_progress` | bool | No | Overrides the default option for enabling progress tracking. If this option is `true` and you don't provide a `progressTracker` parameter with the `DownloadRequest,` the SDK uses a default implementation.<br />Use this option to enable a default progress tracker when the `$progressTracker` parameter is `null`. |
| `target_part_size_bytes` | int | No | The part size in bytes to use in a range multipart download. If you don't provide this parameter, the download uses the `target_part_size_bytes` configured on the transfer manager. |

When the `download` method runs successfully, it returns an `DownloadResult` {{<add link>}}.

## Download an S3 object to a local file
<a name="download-file-to-local"></a>

To download an S3 object directly to a local file, use the `downloadFile` method:

```
<?php

use Aws\S3\S3Transfer\Models\DownloadFileRequest;
use Aws\S3\S3Transfer\Models\DownloadRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(null, [
    'default_region' => 'us-west-2'
]);

$downloadFilePromise = $transferManager->downloadFile(
    new DownloadFileRequest(
        '/path/to/local/file.txt',  // Destination file path.
        false,  // Fail when destination exists.
        new DownloadRequest(
            's3://amzn-s3-demo-bucket/path/to/s3/file.txt',
            [],  // `getObject` request args
            [
                'track_progress'         => true,
                'target_part_size_bytes' => 10 * 1024 * 1024, // 10MB parts
            ]
        )
    )
);

// Wait for download to complete.
$result = $downloadFilePromise->wait();

// `getDownloadDataResult()` returns the string for the file path of the downloaded content because
//  the default `DownloadHandler` used by `downloadFile()` is a file-based handler.
echo "File downloaded successfully at {$result->getDownloadDataResult()}!\n";
```

### `downloadFile` method parameters
<a name="download-file-request"></a>

The `downloadFile` method accepts an instance of `DownloadFileRequest` as an argument.

#### `DownloadFileRequest` parameters
<a name="download-file-request-params"></a>

| Option | Type | Required | Description |
| --- | --- | --- | --- |
| `$destination` | string | Yes | Local path where the file is saved. |
| `$failsWhenDestinationExists` | bool | Yes | Whether to fail if the destination file already exists. If this option is `false` and the destination file exists, the SDK deletes or overrides the existing file. |
| `$downloadRequest` | `DownloadRequest` | Yes | The configured `DownloadRequest` object. For more information, see [`DownloadRequest` object](#download-request-parameters). |

When the `downloadFile` method runs successfully, it returns a `DownloadResult` {{<add link>}}.
