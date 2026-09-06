---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/configuration.html
---

# Configuration
<a name="configuration"></a>

S3 Transfer Manager accepts configuration options to customize its behavior. Provide these options when you create an instance of the transfer manager. The configuration parameter can be either an array or an instance of `S3TransferManagerConfig` {{<add link>}}.

The following example configures an S3 Transfer Manager instance:

```
<?php

use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(
    null,
    [
        // 10MB parts for multipart operations.
        'target_part_size_bytes' => 10 * 1024 * 1024,

        // Use multipart upload for files larger than 20MB.
        'multipart_upload_threshold_bytes' => 20 * 1024 * 1024,

        // Enable checksum calculation for data integrity.
        'request_checksum_calculation' => 'when_supported',

        // Enable checksum validation when getting objects.
        'response_checksum_validation' => 'when_supported',

        // Use part-based multipart downloads.
        'multipart_download_type' => 'part',

        // Allow up to 10 concurrent operations.
        'concurrency' => 10,

        // Enable progress tracking.
        'track_progress' => true,

        // Set default region for default S3 client construction.
        'default_region' => 'us-west-2',
    ]
);
```

**Note**
When you provide configuration as an array to `S3TransferManager`, the SDK internally calls `S3TransferManagerConfig::fromArray` to convert it to the proper type.

## Configuration options
<a name="configuration-options"></a>

All configuration options are optional and use default values when not specified.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `target_part_size_bytes` | int | 8MB | The minimum part size for multipart uploads/downloads. |
| `multipart_upload_threshold_bytes` | int | 16MB | File size threshold to use multipart upload. |
| `request_checksum_calculation` | string | 'when\_supported' | Enables checksum calculation. Valid values are 'when\_supported', 'when\_required'. |
| `response_checksum_validation` | string | 'when\_supported' | Enables checksum validation when getting objects. Valid values are 'when\_supported', 'when\_required'. |
| `multipart_download_type` | string | 'part' | Download strategy for large files. Valid values are 'part' (multipart download), 'ranged' (range requests).  |
| `concurrency` | int | 5 | Maximum number of concurrent operations. |
| `track_progress` | bool | FALSE | Whether to track transfer progress. |
| `default_region` | string | 'us-east-1' | AWS Region to use if no S3 client is provided. |
