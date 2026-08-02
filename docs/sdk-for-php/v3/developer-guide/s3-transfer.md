---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-transfer.html
---

# Transfer directories to and from Amazon S3 using the AWS SDK for PHP Version 3
<a name="s3-transfer"></a>

You use the `Transfer` class in AWS SDK for PHP Version 3 to upload entire directories to an Amazon S3 bucket and download entire buckets to a local directory.

## Uploading a local directory to Amazon S3
<a name="uploading-a-local-directory-to-s3"></a>

The [https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.Transfer.html](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.Transfer.html) object performs the transfers. The following example shows how to recursively upload a local directory of files to an Amazon S3 bucket.

```
// Create an S3 client.
$client = new \Aws\S3\S3Client([
    'region'  => 'us-west-2',
    'version' => '2006-03-01',
]);

// Where the files will be sourced from.
$source = '/path/to/source/files';

// Where the files will be transferred to.
$dest = 's3://bucket';

// Create a transfer object.
$directoryTransfer = new \Aws\S3\Transfer($client, $source, $dest);

// Perform the transfer synchronously.
$directoryTransfer->transfer();
```

In this example, we created an Amazon S3 client, created a `Transfer` object, and performed transfer synchronously.

The previous example demonstrates the minimum amount of code needed to perform a transfer. A `Transfer` object can also perform transfers asynchronously and has various configuration options that you can use to customize the transfers.

You can upload the local files to a “subfolder” of an Amazon S3 bucket by providing a key prefix in the `s3://` URI. The following example uploads the local files on disk to the `bucket` bucket and stores the files under the `foo` key prefix.

```
$source = '/path/to/source/files';
$dest = 's3://bucket/foo';
$directoryTransfer = new \Aws\S3\Transfer($client, $source, $dest);
$directoryTransfer->transfer();
```

## Downloading an Amazon S3 bucket
<a name="downloading-an-s3-bucket"></a>

You can recursively download an Amazon S3 bucket to a local directory on disk by specifying the `$source` argument as an Amazon S3 URI (e.g., `s3://bucket`) and the `$dest` argument as the path to a local directory.

```
// Where the files will be sourced from.
$source = 's3://bucket';

// Where the files will be transferred to.
$dest = '/path/to/destination/dir';

$directoryTransfer = new \Aws\S3\Transfer($client, $source, $dest);
$directoryTransfer->transfer();
```

**Note**
The SDK automatically creates any necessary directories when downloading the objects in the bucket.

You can include a key prefix in the Amazon S3 URI after the bucket to download only objects stored under a “pseudo-folder”. The following example downloads only files stored under the “/foo” key prefix of the given bucket.

```
$source = 's3://bucket/foo';
$dest = '/path/to/destination/dir';
$directoryTransfer = new \Aws\S3\Transfer($client, $source, $dest);
$directoryTransfer->transfer();
```

## Configuration
<a name="configuration"></a>

The `Transfer` object constructor accepts the following arguments.

** `$client` **
The `Aws\ClientInterface` object to use to perform the transfers.

** `$source` (string \| `Iterator`)**
The source data being transferred. This can point to a local path on disk (e.g., `/path/to/files`) or an Amazon S3 bucket (e.g., `s3://bucket`). The `s3://` URI may also contain a key prefix that can be used to only transfer objects under a common prefix.
If the `$source` argument is an Amazon S3 URI, the `$dest` argument must be a local directory (and vice versa).
In addition to providing a string value, you can also provide an `\Iterator` object that yields absolute file names. If you provide an `\Iterator` object, you **must** provide a `base_dir` option in the `$options` associative array.

** `$dest` **
The destination where the files will be transferred. If the `$source` argument is a local path on disk, `$dest` must be an Amazon S3 bucket URI (e.g., `s3://bucket`). If the `$source` argument is an Amazon S3 bucket URI, the `$dest` argument must be a local path on disk.

** `$options` **
An associative array of transfer options. The following transfer options are valid:
**`add_content_md5` (bool)**
Set to `true` to calculate the MD5 checksum for uploads.
** `base_dir` (string)**
Base directory of the source, if `$source` is an iterator. If the `$source` option is not an array, then this option is ignored.
** `before` (callable)**
A callback to invoke before each transfer. The callback should have a function signature like `function (Aws\Command $command) {...}`. The provided command will be a `GetObject`, `PutObject`, `CreateMultipartUpload`, `UploadPart`, or `CompleteMultipartUpload` command.
** `mup_threshold` (int)**
Size in bytes in which a multipart upload should be used instead of `PutObject`. Defaults to `16777216` (16 MB).
** `concurrency` (int, default=5)**
Number of files to upload concurrently. The ideal concurrency value will vary based on the number of files being uploaded and the average size of each file. Generally, smaller files benefit from a higher concurrency while larger files do not.
** `debug` (bool)**
Set to `true` to print out debug information for transfers. Set to an `fopen()` resource to write to a specific stream instead of writing to STDOUT.

## Async transfers
<a name="async-transfers"></a>

The `Transfer` object is an instance of `GuzzleHttp\Promise\PromisorInterface`. This means that the transfer can occur asynchronously and is initiated by calling the `promise` method of the object.

```
$source = '/path/to/source/files';
$dest = 's3://bucket';
$directoryTransfer = new \Aws\S3\Transfer($client, $source, $dest);

// Initiate the transfer and get a promise.
$promise = $directoryTransfer->promise();

// Do something when the transfer is complete using the then() method.
$promise->then(function () {
    echo 'Done!';
});
```

The promise is rejected if any file fails to transfer. You can handle the failed transfer asynchronously using the `otherwise` method of the promise. The `otherwise` function accepts a callback to invoke when an error occurs. The callback accepts the `$reason` for the rejection, which typically is an instance of `Aws\Exception\AwsException` (although a value of **any** type can be delivered to the callback).

```
$promise->otherwise(function ($reason) {
    echo 'Transfer failed: ';
    var_dump($reason);
});
```

Because the `Transfer` object returns a promise, these transfers can occur concurrently with other asynchronous promises.

## Customizing the directory transfer
<a name="customizing-the-transfer-manager-s-commands"></a>

By adding a callback to the constructor, you can customize the options that the `Transfer` executes.

```
$uploader = new Transfer($s3Client, $source, $dest, [
    'before' => function (\Aws\Command $command) {
        // Commands can vary for multipart uploads, so check which command
        // is being processed.
        if (in_array($command->getName(), ['PutObject', 'CreateMultipartUpload'])) {
            // Set custom cache-control metadata.
            $command['CacheControl'] = 'max-age=3600';
            // Apply a canned ACL.
            $command['ACL'] = strpos($command['Key'], 'CONFIDENTIAL') ### false
                ? 'public-read'
                : 'private';
        }
    },
]);
```
