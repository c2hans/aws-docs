---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/directory-operations.html
---

# Directory operations
<a name="directory-operations"></a>

S3 Transfer Manager can handle entire directory transfers.

## Upload directory
<a name="upload-directory"></a>

S3 Transfer Manager can upload an entire directory to an S3 bucket. {{<Are the key values the filenames when uploaded?>}}

```
<?php

use Aws\S3\S3Transfer\Models\UploadDirectoryRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(null, [
    'default_region' => 'us-west-2'
]);

$uploadDirPromise = $transferManager->uploadDirectory(
    new UploadDirectoryRequest(
        '/path/to/local/directory',
        'amzn-s3-demo-bucket',
        [
            // Additional `putObject` parameters that apply to all files.
            'ACL'          => 'public-read',
            'CacheControl' => 'max-age=3600',
        ],
        [
            // Configuration options.
            'recursive'                      => true,
            'follow_symbolic_links'          => false,
            's3_prefix'                      => 'uploads/2023/',
            's3_delimiter'                   => '/',
            'track_progress'                 => true,
            'filter'                         => function ($file) {
                // Upload only .jpg files.
                return pathinfo($file, PATHINFO_EXTENSION) === 'jpg';
            },
            'upload_object_request_modifier' => function ($args) {
                // Customize request arguments for each file.
                $args['ContentType'] = 'image/jpeg';
            },
        ]
    )
);

// Wait for the upload process to complete.
$result = $uploadDirPromise->wait();

$uploaded = $result->getObjectsUploaded();
$failed = $result->getObjectsFailed();
echo "Uploaded {$uploaded} files. Failed: {$failed}\n";
```

### `uploadDirectory` method parameters
<a name="upload-directory-parameters"></a>

The `uploadDirectory` method accepts an instance of `UploadDirectoryRequest`{{<add link>}} as an argument.

#### `UploadDirectoryRequest` parameters
<a name="upload-directory-request-parameters"></a>

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `$sourceDirectory` | string | Yes | Path of the local directory to upload. |
| `$targetBucket` | string | Yes | Destination S3 bucket name. |
| `$uploadRequestArgs` | array | No | Additional upload object request parameters for all files. |
| `$config` | array | No | Configuration options for the directory upload. For more information about configuration options, see the [following section](#upload-directory-config-parameters). |
| `$listeners` | array | No | Array of `TransferListener` objects. The SDK clones each `TransferListener` per file. |
| `$max_depth` | bool | -1 "Runtime default" | To indicate the maximum depth of the recursive file three walk.  |
| `$progressTracker` | `TransferListener` | No | A progress tracker for all uploads. |

##### `$config` options for `UploadDirectoryRequest`
<a name="upload-directory-config-parameters"></a>

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `recursive` | bool | `false` | Whether to recursively upload subdirectories. |
| `follow_symbolic_links` | bool | `false` | Whether to follow symbolic links. |
| `s3_prefix` | string | '' | Prefix to add to all object keys. |
| `s3_delimiter` | string | '/' | The delimiter to use in S3 object keys. |
| track\_progress | bool | false | Whether to track progress. |
| `max_concurrency` | int | 100 | The maximum number of concurrent uploads. |
| `filter` | callable | null | Function to filter which files to upload. |
| `upload_object_request_modifier` | callable | null | Function to customize each upload request. |
| `failure_policy` | callable | null | Function to handle upload failures. |

##### Callable types of `$config` options
<a name="upload-directory-config-callables"></a>

****

| Option name | parameter name | parameter type | parameter info |
| --- | --- | --- | --- |
| filter | $file | SplFileInfo\|string | If cast to string, it is the file path. Otherwise, it is an instance of `SplFileInfo`. |
| upload\_object\_request\_modifier | $requestArgs | array | The request arguments for each individual upload request. For more information about array options, see the parameter syntax section of the [putObject method](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#putobject). |
| failure\_policy | $uploadRequestArgs | array | The request arguments for each individual upload request. For more information about array options, see the parameter syntax section of the [putObject method](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#putobject) for array options. |
|  | $uploadDirectoryArgs | array | An array with the source directory and the target bucket for the upload directory operation. |
|  | $reason | Throwable\|string | The exception holder that contains information about what caused the failure. |
|  | $uploadDirectoryResult | UploadDirectoryResult | The object that contains the number of objects successfully uploaded and the number that failed. |

When the `uploadDirectory` method runs successfully, it returns an `UploadDirectoryResult` {{<add link>}}.

## Download directory
<a name="download-directory"></a>

You can download a directory from an S3 bucket. {{<Are the filenames the key values when downloaded? If there is no extension in the key, is there also no extension on the file?>}}

```
<?php

use Aws\S3\S3Transfer\Models\DownloadDirectoryRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(null, [
    'default_region' => 'us-west-2'
]);

$downloadDirPromise = $transferManager->downloadDirectory(
    new DownloadDirectoryRequest(
        'amzn-s3-demo-bucket',
        '/path/to/local/directory',
        [
            // Additional `getObject` parameters that apply to all files.
        ],
        [
            // Configuration options.
            's3_prefix'                        => 'uploads/2023/',
            's3_delimiter'                     => '/',
            'track_progress'                   => true,
            'filter'                           => function ($key) {
                // Download only .jpg files.
                return pathinfo($key, PATHINFO_EXTENSION) === 'jpg';
            },
            'download_object_request_modifier' => function ($args) {
                // Customize request arguments for each file.
                $args['ResponseContentType'] = 'image/jpeg';
            },
            'list_objects_v2_args'              => [
                'MaxKeys' => 1000,
                'Prefix'  => 'uploads/2023/',
            ],
            'fails_when_destination_exists'    => true,
        ]
    )
);

// Wait for the download process to complete.
$result = $downloadDirPromise->wait();

$downloaded = $result->getObjectsDownloaded();
$failed = $result->getObjectsFailed();
echo "Downloaded {$downloaded} files. Failed: {$failed}\n";
```

### `downloadDirectory` method parameters
<a name="download-directory-parameters"></a>

The `downloadDirectory` method accepts an instance of `DownloadDirectoryRequest`{{<add link>}} as an argument.

#### `DownloadDirectoryRequest` parameters
<a name="download-directory-request-parameters"></a>

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `$sourceBucket` | string | Yes | Source S3 bucket name from which objects are downloaded. |
| `$destinationDirectory` | string | Yes | Local directory to download files into. |
| `$downloadRequestArgs` | array | No | Additional download object request parameters for all files. |
| `$config` | array | No | Configuration options for the directory download. For more information about configuration options, see the [following section](#download-directory-config-parameters). |
| `$listeners` | array | No | Array of `TransferListener` objects. The SDK clones each `TransferListener` per file. |
| `$progressTracker` | `TransferListener` | No | A progress tracker for all downloads. |

##### `$config` options for `DownloadDirectoryRequest`
<a name="download-directory-config-parameters"></a>

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `s3_prefix` | string | '' | Prefix for filtering (if not in `list_objects_v2_args`). |
| `track_progress` | bool | `false` | Whether to track progress. |
| `filter` | callable | `null` | Function to filter which S3 objects to download. |
| `download_object_request_modifier` | callable | `null` | Function to customize each download request. |
| `list_objects_v2_args` | array | [] | Arguments for the [`ListObjectsV2`](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#listobjectsv2) operation. This operation fetches the metadata for the objects to download. |
| `fails_when_destination_exists` | bool | false | Whether to fail when an object destination file path already exists. |
| `failure_policy` | callable | null | Function to handle download failures. |
| `max_concurrency` | int | 100 | The max number of concurrent downloads. |
| `target_part_size_bytes` | int | varies | Part size for multipart downloads when multipart download type is ranged. |

##### Callable types of `$config` options
<a name="download-dir-callable-options"></a>

****

| Option name | parameter name | parameter type | parameter info |
| --- | --- | --- | --- |
| filter | $objectKey | string | The object key name from the bucket. |
| download\_object\_request\_modifier | $requestArgs | array | The request arguments for each individual download request. For more information about array options, see the parameter syntax section of the [getObject method](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#getobject). |
| failure\_policy | $downloadObjectRequestArgs | array | The request arguments for each individual download request. For more information about array options, see the *parameter syntax* section of the [getObject method](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#getobject). |
|  | $downloadDirectoryRequest | array | An array with the source bucket and the target directory for the download directory operation.  |
|  | $reason | Throwable | The exception holder that contains information about what caused the failure. |
|  | $downloadDirectoryResult | DownloadDirectoryResult {{<add link>}} | The object that contains the number of objects successfully downloaded and the number that failed. |

## How directory operations work
<a name="directory-operations-behavior"></a>

This section explains how the S3 Transfer Manager handles file paths and object keys during directory operations.

### Upload path handling
<a name="upload-path-handling"></a>

When you upload a directory, the SDK constructs S3 object keys from file paths:

1. Calculates each file's path relative to the source directory

1. Prepends the `s3_prefix` value if specified (automatically adds trailing slash)

1. Replaces the OS directory separator with the `s3_delimiter` (default `/`)

The `recursive` option controls whether subdirectories are included. When `false` (default), only top-level files are uploaded. When `true`, all files in subdirectories are uploaded, preserving the directory structure in object keys.

**Note**
The key in S3 for each uploaded file will be the provided s3 prefix, by default is null, plus the relative path of the file starting from the specified source directory. Also, we replace the directory separator in the resolved key name with the provided s3 delimiter, which by default it will be /.
**Example 1**

```
$sourceDirectory = "/opt/my-upload-directory";
$s3Prefix = "important/";
$s3Delimiter = "/"; // Default value
```
Directory Structure

```
/opt/my-upload-directory/
-- my-file1.txt
-- my-file-2.txt
-- sub-dir/
---- my-another-file1.txt
---- my-another-file2.txt
```
The keys for each file will be:

```
$s3Prefix + $fileRelativePath;
```

```
- important/my-file1.txt
- important/my-file-2.txt
- important/sub-dir/my-another-file1.txt
- important/sub-dir/my-another-file2.txt
```
**Example 2**

```
$sourceDirectory = "/opt/my-docs";
$s3Prefix = ''; // No provided and it will defaulted to empty string
$s3Delimiter = "/"; // Default value
```
Directory Structure

```
/opt/my-docs/
-- my-file1.txt
-- my-file-2.txt
-- sub-dir/
---- my-another-file1.txt
---- my-another-file2.txt
```
The keys for each file will be:

```
$s3Prefix + $fileRelativePath;
```

```
- my-file1.txt
- my-file-2.txt
- sub-dir/my-another-file1.txt
- sub-dir/my-another-file2.txt
```

**Example Upload directory path handling**

```
<?php
// Source directory: /home/user/photos/
//   fla/beach.jpg
//   fla/sunset.jpg
//   fla/pool/party.jpg
// With s3_prefix: '2023' and recursive: true
// Results:
//   2023/fla/beach.jpg
//   2023/fla/sunset.jpg
//   2023/fla/pool/party.jpg
```

### Download path handling
<a name="download-path-handling"></a>

When you download a directory, the SDK constructs local file paths from S3 object keys:

1. Removes the `s3_prefix` from the object key if specified

1. Replaces the S3 delimiter (`/`) with the OS directory separator

1. Appends the result to the destination directory

Downloads are always recursive. The SDK retrieves all objects under the specified prefix and creates subdirectories as needed. It validates that paths don't resolve outside the destination directory for security.

**Example Download directory path handling**

```
<?php
// S3 objects:
//   2023/fla/beach.jpg
//   2023/fla/sunset.jpg
//   2023/fla/pool/party.jpg
// With s3_prefix: '2023' and destination: /home/user/downloads
// Results:
//   /home/user/downloads/fla/beach.jpg
//   /home/user/downloads/fla/sunset.jpg
//   /home/user/downloads/fla/pool/party.jpg
```

**Note**
The file path for the downloaded objects will be resolved as follow:
The s3 prefix, if provided, will be removed from the object key.
If the s3Delimiter is different than the OS directory separator then, the s3 delimiter will be replaced with the OS directory separator.
**Example 1**

```
$s3Prefix = "my-prefix";
$s3Objects = [
    "my-prefix/file-1.txt",
    "my-prefix/file-2.txt",
    "my-prefix/subdir/file-1.txt"
];
$targetDirectory = "/opt/bucket/downloads/";
```
Once those objects are downloaded will be placed as follow:

```
/opt/bucket/downloads/
-- file-1.txt
-- file-2.txt
-- subdir/
---- file-1.txt
```
As we can see, the prefix was removed from the final file path for the objects.
**Example 2 - without s3 prefix**

```
$s3Prefix = ""; // No provided
$s3Objects = [
    "README.md",
    "my-docs/file-1.txt",
    "my-docs/file-2.txt",
    "my-docs/statements/file-1.txt"
];
$targetDirectory = "/opt/bucket/downloads/";
```
Once those objects are downloaded will be placed as follow:

```
/opt/bucket/downloads/
-- README.md
-- my-docs/
---- file-1.txt
---- file-2.txt
---- statements/
------ file-1.txt
```
