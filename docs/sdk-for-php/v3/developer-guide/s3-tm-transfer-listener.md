---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-tm-transfer-listener.html
---

# Transfer listeners
<a name="s3-tm-transfer-listener"></a>

You can implement your own listener that reacts to different transfer events. The events are:
+ **`transferInitiated`**: When a transfer initiates
+ **`bytesTransferred`**: When a transfer transfers bytes from source to destination
+ **`transferComplete`**: When a transfer completes without errors
+ **`transferFail`**: When a transfer failed before completion

Each `S3TransferManager` operation (for example, `uploadFile` and `downloadDirectory`) has a `listeners` parameter. This parameter is an array that expects each item to be an instance of `AbstractTransferListener`.

`AbstractTransferListener` is an abstract base class that you can extend to monitor transfer operations. It provides empty method implementations for all transfer events. You only need to override the methods for the events you want to handle.

Each `AbstractTransferListener` method receives a `$context` argument. This argument contains key-value information about the operation. The context includes:
+ `request_args` (array) - Request parameters
+ `progress_snapshot` (instance of `TransferProgressSnapshot`{{<add link>}}) - Current request status
+ `reason` (instance of `Throwable`) - provided only for the `transferFail` method

The `progress_snapshot` property also carries the `reason` property for failure events. You can access the exception through `$context['reason']` or through `$context['progress_snapshot']→getReason()`.

The following code shows the `AbstractTransferListener` class structure:

```
<?php

namespace Aws\S3\S3Transfer\Progress;

abstract class AbstractTransferListener
{
    /**
     * @param array $context
     * - request_args: (array) The request arguments that will be provided
     *   as part of the request initialization.
     * - progress_snapshot: (TransferProgressSnapshot) The transfer snapshot holder.
     *
     * @return void
     */
    public function transferInitiated(array $context): void {}

    /**
     * @param array $context
     * - request_args: (array) The request arguments that will be provided
     *   as part of the operation that originated the bytes transferred event.
     * - progress_snapshot: (TransferProgressSnapshot) The transfer snapshot holder.
     *
     * @return void
     */
    public function bytesTransferred(array $context): bool {}

    /**
     * @param array $context
     * - request_args: (array) The request arguments that will be provided
     *   as part of the operation that originated the bytes transferred event.
     * - progress_snapshot: (TransferProgressSnapshot) The transfer snapshot holder.
     *
     * @return void
     */
    public function transferComplete(array $context): void {}

    /**
     * @param array $context
     * - request_args: (array) The request arguments that will be provided
     *    as part of the operation that originated the bytes transferred event.
     * - progress_snapshot: (TransferProgressSnapshot) The transfer snapshot holder.
     * - reason: (Throwable) The exception originated by the transfer failure.
     *
     * @return void
     */
    public function transferFail(array $context): void {}
}
```

The following example shows a `AbstractTransferListener` implementation that overrides only the `transferInitiated` and `transferFail` methods:

```
<?php

namespace MyApp\Listeners;

use Aws\S3\S3Transfer\Progress\AbstractTransferListener;

class MyCustomListener extends AbstractTransferListener
{
    public function transferInitiated(array $context): void
    {
        $progressSnapshot = $context['progress_snapshot'];

        echo "Transfer initiated for object with identifier: "
            . $progressSnapshot->getIdentifier();
    }

    public function transferFail(array $context): void
    {
        $progressSnapshot = $context['progress_snapshot'];
        $reason = $context['reason'];

        echo "Transfer for object with identifier: "
            . $progressSnapshot->getIdentifier() . " has failed.";

        echo "Completion Status: " . $progressSnapshot->getTransferredBytes()
            . "/"
            . $progressSnapshot->getTotalBytes() . " B";

        echo "Reason of failure is: " . $reason;
    }
}
```

```
<?php

use Aws\S3\S3Transfer\Models\UploadRequest;
use Aws\S3\S3Transfer\S3TransferManager;
use MyApp\Listeners\MyCustomListener;

require __DIR__ . '/../vendor/autoload.php';

// The following example uses `MyCustomListener` in an `upload` operation.
$transferManager = new S3TransferManager(
    null,
    ['default_region' => 'us-east-2']
);
$uploadPromise = $transferManager->upload(
    new UploadRequest(
        source: "/tmp/myfile.txt",
        uploadRequestArgs: [
            'Bucket' => 'amzn-s3-demo-bucket',
            'Key' => 'MyKey'
        ],
        listeners: [
            new MyCustomListener()
        ]
    )
);

$result = $uploadPromise->wait();
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
