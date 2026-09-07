---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/progress-tracking.html
---

# Progress tracking
<a name="progress-tracking"></a>

S3 Transfer Manager provides built-in progress tracking capabilities.

## Tracking all operations
<a name="track-all-operations"></a>

You can enable tracking for all operations (file and directory) by setting `track_progress` to `true` on the `S3TransferManager` instance.

```
<?php

use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(
    null,
    [
        'track_progress' => true,
    ]
);
```

With this setting, the SDK uses the built-in `SingleProgressTracker`{{<add link>}} for file operations and uses the `MultiProgressTracker`<add link> for directory operations.

## Tracking a single file operation
<a name="file-op-progress-tracking"></a>

If you didn't enable progress tracking on the transfer manager, you can enable tracking on an individual method in two ways.
Set `track_progress` to `true` in the `$config` array for a specific file operation.

```
<?php

use Aws\S3\S3Transfer\Models\UploadDirectoryRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(
    null, []
);

$uploadDirPromise = $transferManager->uploadDirectory(
    new UploadDirectoryRequest(
        '/path/to/directory',
        'amzn-s3-demo-bucket',
        [],
        [   // $config array
            'track_progress' => true,
        ],
        []
    )
);
```

Create a new `SingleProgressTracker` instance or provide a custom implementation of `AbstractTransferListener`. Pass your tracker to the file operations as the `$progressTracker` parameter.

```
<?php

use Aws\S3\S3Transfer\Models\UploadRequest;
use Aws\S3\S3Transfer\Progress\SingleProgressTracker;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(
    null, []
);

$uploadPromise = $transferManager->upload(
    new UploadRequest(
        '/path/to/Myfile.txt',  // Or an instance of StreamInterface.
        [
            'Bucket' => 'amzn-s3-demo-bucket',
            'Key' => 'file.txt',
        ],
        [],
        [],
        new SingleProgressTracker()  // Or custom implementation of the TransferLister interface.
    )
);
```

The following example shows sample console output from the built-in `SingleProgressTracker` for the upload progress of a file named `MyFile.txt`:

![Console output showing a progress bar for uploading MyFile.txt with percentage complete and transfer speed](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/images/s3_TM_console_output_single_progress_tracker.png)

## Tracking a single directory operation
<a name="directory-op-progress-tracking"></a>

If you didn't enable progress tracking on the transfer manager, you can enable it for directory operations in two ways.

Set 'track\_progress' to `true` in the method's `$config` array argument.

```
<?php

use Aws\S3\S3Transfer\Models\UploadDirectoryRequest;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(
    null, []
);

$uploadDirPromise = $transferManager->uploadDirectory(
    new UploadDirectoryRequest(
        '/path/to/directory',
        'amzn-s3-demo-bucket',
        [],
        [   // $config array
            'track_progress' => true,
        ],
        []
    )
);
```

Create a new `MultiProgressTracker` instance and pass it to the directory operations as the `$progressTracker` parameter.

```
<?php

use Aws\S3\S3Transfer\Models\UploadDirectoryRequest;
use Aws\S3\S3Transfer\Progress\MultiProgressTracker;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$transferManager = new S3TransferManager(
    null, []
);

$uploadDirPromise = $transferManager->uploadDirectory(
    new UploadDirectoryRequest(
        '/path/to/directory',
        'amzn-s3-demo-bucket',
        [],
        [],
        [],
        new MultiProgressTracker()
    )
);
```

The following example shows sample console output from the built-in `MultiProgressTracker` for the upload progress of a directory:

![Console output showing multiple progress bars for uploading multiple files with a summary progress bar at the bottom](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/images/s3_TM_console_output_multi_progress_tracker.png)

The progress of each file is listed along with the summary progress in the last line.

## Custom progress tracking
<a name="custom-progress-tracking"></a>

You can implement your own progress tracking for file operations. Create a class that extends the `AbstractTransferListener` interface and pass it to the method on the request.

The following implementation displays progress information in text format for a single file operation:

```
<?php

use Aws\S3\S3Transfer\Models\UploadRequest;
use Aws\S3\S3Transfer\Progress\AbstractTransferListener;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

class MyProgressTracker extends AbstractTransferListener
{
    public function transferInitiated(array $context): void
    {
        $key = $context['request_args']['Key'] ?? 'unknown';
        echo "Starting transfer of {$key}...\n";
    }

    public function bytesTransferred(array $context): bool
    {
        $snapshot = $context['progress_snapshot'];
        $percent = round($snapshot->ratioTransferred() * 100, 2);
        $transferred = round($snapshot->getTransferredBytes() / 1024 / 1024, 2);
        $total = round($snapshot->getTotalBytes() / 1024 / 1024, 2);

        echo "Progress: {$percent}% ({$transferred}MB of {$total}MB)\n";
    }

    public function transferComplete(array $context): void
    {
        $key = $context['request_args']['Key'] ?? 'unknown';
        echo "Transfer complete for {$key}!\n";
    }

    public function transferFail(array $context): void
    {
        $key = $context['request_args']['Key'] ?? 'unknown';
        $reason = $context['reason']->getMessage();
        echo "Transfer failed for {$key}: {$reason}\n";
    }
}

$transferManager = new S3TransferManager(
    null, []
);

// Use your custom tracker.
$uploadPromise = $transferManager->upload(
    new UploadRequest(
        '/path/to/file.txt', // Or an instance of StreamInterface.
        [
            'Bucket' => 'amzn-s3-demo-bucket',
            'Key'    => 'file.txt',
        ],
        [],
        [],
        new MyProgressTracker()
    )
);
```

The following example shows sample output to the console for file upload in progress:

```
Starting transfer of file.txt...
Progress: 42% (16.8MB of 40MB)
```

## Customize a built-in progress tracker
<a name="customize-built-in-progress-tracker"></a>

You can customize progress tracking in a few ways:
+ Create a custom implementation by extending `AbstractTransferListener` and implementing `ProgressTrackerInterface`{{<add link>}}.
+ Customize the existing implementations by configuring the `ConsoleProgressBar`{{<add link>}} that is passed to the built-in trackers.
+ Implement a custom `ProgressBar`{{<add link>}} and pass it to the built-in trackers.

The following examples show how to customize progress tracking. Refer to the [class diagram](class-diagram-tracking.md) to see the relationship between the progress tracking components in the SDK.

### Customize a `ConsoleProgressBar`
<a name="customize-consoleprogressbar"></a>

#### Customize the default bar format
<a name="customize-consoleprogressbar-default-format"></a>

The following example customizes the default progress bar format, which is `ColoredTransferProgressBarFormat`{{<add link>}}. This format shows progress with different colors depending on the transfer state.

The example changes:
+ the character from the default "\#" to "="
+ bar width from the default of 50 to 100

```
<?php

use Aws\S3\S3Client;
use Aws\S3\S3Transfer\Models\UploadRequest;
use Aws\S3\S3Transfer\Progress\ConsoleProgressBar;
use Aws\S3\S3Transfer\Progress\SingleProgressTracker;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$progressBar = new ConsoleProgressBar(
    progressBarChar: '=',
    progressBarWidth: 100,
// Default `ColoredTransferProgressBarFormat` is used.
);
$progressTracker = new SingleProgressTracker(
    progressBar: $progressBar,
);
$s3Client = new S3Client([
    'region' => 'us-east-2',
]);
$s3TransferManager = new S3TransferManager($s3Client);
$source = "/path/file.txt";

$result = $s3TransferManager->upload(
    new UploadRequest(
        source: $source,
        uploadRequestArgs: [
            'Bucket' => 'amzn-s3-demo-bucket',
            'Key'    => 'key',
        ],
        progressTracker: $progressTracker,
    )
)->wait();
print_r($result);
```

The following image shows console output for a customized built-in `ConsoleProgressBar` with a width of 100 and character of "=":

![Console output showing a customized progress bar using equals signs with width of 100 characters](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/images/s3_TM_console_output_custom_progress_tracker.png)

#### Customize by using the plain progress bar format
<a name="customize-consoleprogressbar-plain-format"></a>

The following example customizes the default progress bar by using the built-in `PlainProgressBarFormat`{{<add link>}} with a custom character and width. The `PlainProgressBarFormat` displays in black only. The color doesn't change based on the transfer state.

The example changes:
+ the character from the default "\#" to "\*"
+ bar width from the default of 50 to 25
+ the default `progressBarFormat` instance from `ColoredTransferProgressBarFormat` to `PlainProgressBarFormat`

```
<?php

use Aws\S3\S3Client;
use Aws\S3\S3Transfer\Models\UploadRequest;
use Aws\S3\S3Transfer\Progress\ConsoleProgressBar;
use Aws\S3\S3Transfer\Progress\PlainProgressBarFormat;
use Aws\S3\S3Transfer\Progress\SingleProgressTracker;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

$progressBar = new ConsoleProgressBar(
    progressBarChar: '*',
    progressBarWidth: 25,
    progressBarFormat: new PlainProgressBarFormat(),
);
$progressTracker = new SingleProgressTracker(
    progressBar: $progressBar,
);
$s3Client = new S3Client([
    'region' => 'us-east-2',
]);
$s3TransferManager = new S3TransferManager($s3Client);
$source = "/path/file.txt";

$result = $s3TransferManager->upload(
    new UploadRequest(
        source: $source,
        uploadRequestArgs: [
            'Bucket' => 'amzn-s3-demo-bucket',
            'Key'    => 'key',
        ],
        progressTracker: $progressTracker,
    )
)->wait();
print_r($result);
```

The following image shows console output for a customized built-in `ConsoleProgressBar` using a plain progress bar format with a width of 25 and character of "\*":

![Console output showing a plain black progress bar using asterisks with width of 25 characters](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/images/s3_TM_console_output_custom-plain_progress_tracker.png)

#### Customize by creating a new bar format
<a name="customize-consoleprogressbar-custom-format"></a>

The following example customizes the default progress bar by using a new bar format (extending `ProgressBarFormat`{{<add link>}}) instead of customizing a built-in format.

```
<?php

use Aws\S3\S3Client;
use Aws\S3\S3Transfer\Models\UploadRequest;
use Aws\S3\S3Transfer\Progress\ConsoleProgressBar;
use Aws\S3\S3Transfer\Progress\ProgressBarFormat;
use Aws\S3\S3Transfer\Progress\SingleProgressTracker;
use Aws\S3\S3Transfer\S3TransferManager;

require __DIR__ . '/../vendor/autoload.php';

// Implement a custom bar format.
class PercentBarFormat extends ProgressBarFormat
{
    public const FORMAT_TEMPLATE = "|object_name| - |percent|% [|transferred| |unit|ytes]";
    public const FORMAT_PARAMETERS = [
        'object_name',       // `uploadRequestArgs` Key parameter.
        'percent',           //  Percent transferred.
        // 'progress_bar',      Optional, if used, default is a `ConsoleProgressBar`.
        // 'to_be_transferred', Optional.
        'transferred',       //  Default is bytes transferred.
        'unit',              //  Default is 'B'.
    ];

    public function getFormatTemplate(): string
    {
        return self::FORMAT_TEMPLATE;
    }

    public function getFormatParameters(): array
    {
        return self::FORMAT_PARAMETERS;
    }

    protected function getFormatDefaultParameterValues(): array
    {
        return [];
    }
}

// Create an instance of the custom implemention
$progressBarFormat = new PercentBarFormat();
$progressBar = new ConsoleProgressBar(
    progressBarFormat: $progressBarFormat,
);
$progressTracker = new SingleProgressTracker(
    progressBar: $progressBar,
);
$s3Client = new S3Client([
    'region' => 'us-east-2',
]);
$s3TransferManager = new S3TransferManager($s3Client);
$source = "/path/file";

$result = $s3TransferManager->upload(
    new UploadRequest(
        source: $source,
        uploadRequestArgs: [
            'Bucket' => 'amzn-s3-demo-bucket',
            'Key'    => 'key',
        ],
        progressTracker: $progressTracker,
    )
)->wait();
print_r($result);
```

The following image shows console output for a customized built-in `ConsoleProgressBar` using a custom progress bar format:

![Console output showing a custom percentage-based progress format displaying object name and bytes transferred](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/images/s3_TM_console_output_custom-percentage_progress_tracker.png)

A custom bar format accepts several parameters:
+ object\_name
+ percent
+ progress\_bar
+ to\_be\_transferred
+ transferred
+ unit

You can combine the delimited (pipe character) parameter names to customize the output. The example uses the following template. The `getFormatTemplate` method of the `PercentBarFormat` class returns this template:

```
"|object_name| - |percent|% [|transferred| |unit|ytes]"
```
