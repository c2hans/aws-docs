---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/handling-errors.html
---

# Handling errors in the AWS SDK for PHP Version 3
<a name="handling-errors"></a>

## Synchronous Error Handling
<a name="synchronous-error-handling"></a>

If an error occurs while performing an operation, an exception is thrown. For this reason, if you need to handle errors in your code, use `try`/`catch` blocks around your operations. The SDK throws service-specific exceptions when an error occurs.

The following example uses the `Aws\S3\S3Client`. If there is an error, the exception thrown will be of the type `Aws\S3\Exception\S3Exception`. All service-specific exceptions that the SDK throws extend from the `Aws\Exception\AwsException` class. This class contains useful information about the failure, including the request-id, error code, and error type. Note for some services which support it, response data is coerced into an associative array structure (similar to `Aws\Result` objects), which can be accessed like a normal PHP associative array. The `toArray()` method will return any such data, if it exists.

 **Imports**

```
require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\Exception\AwsException;
use Aws\S3\Exception\S3Exception;
```

 **Sample Code**

```
// Create an SDK class used to share configuration across clients.
$sdk = new Aws\Sdk([
    'region'   => 'us-west-2'
]);

// Use an Aws\Sdk class to create the S3Client object.
$s3Client = $sdk->createS3();

try {
    $s3Client->createBucket(['Bucket' => 'amzn-s3-demo-bucket']);
} catch (S3Exception $e) {
    // Catch an S3 specific exception.
    echo $e->getMessage();
} catch (AwsException $e) {
    // This catches the more generic AwsException. You can grab information
    // from the exception using methods of the exception object.
    echo $e->getAwsRequestId() . "\n";
    echo $e->getAwsErrorType() . "\n";
    echo $e->getAwsErrorCode() . "\n";

    // This dumps any modeled response data, if supported by the service
    // Specific members can be accessed directly (e.g. $e['MemberName'])
    var_dump($e->toArray());
}
```

## Asynchronous error handling
<a name="asynchronous-error-handling"></a>

Exceptions are not thrown when sending asynchronous requests. Instead, you must use the `then()` or `otherwise()` method of the returned promise to receive the result or error.

 **Imports**

```
require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\Exception\AwsException;
use Aws\S3\Exception\S3Exception;
```

 **Sample Code**

```
//Asynchronous Error Handling
$promise = $s3Client->createBucketAsync(['Bucket' => 'amzn-s3-demo-bucket']);
$promise->otherwise(function ($reason) {
    var_dump($reason);
});

// This does the same thing as the "otherwise" function.
$promise->then(null, function ($reason) {
    var_dump($reason);
});
```

You can “unwrap” the promise and cause the exception to be thrown instead.

 **Imports**

```
require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\Exception\AwsException;
use Aws\S3\Exception\S3Exception;
```

 **Sample Code**

```
$promise = $s3Client->createBucketAsync(['Bucket' => 'amzn-s3-demo-bucket']);
```

```
//throw exception
try {
    $result = $promise->wait();
} catch (S3Exception $e) {
    echo $e->getMessage();
}
```
