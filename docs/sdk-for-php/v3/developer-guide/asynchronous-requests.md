---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/asynchronous-requests.html
---

# Asynchronous programming using the AWS SDK for PHP Version 3
<a name="asynchronous-requests"></a>

You can send commands concurrently using the asynchronous features of the SDK. You can send requests asynchronously by suffixing an operation name with `Async`. This initiates the request and returns a promise.

The promise is fulfilled with the result object on success or rejected with an exception on failure. This enables you to create multiple promises and have them send HTTP requests concurrently when the underlying HTTP handler transfers the requests.

 **Imports**

```
require 'vendor/autoload.php';
use Aws\S3\S3Client;
use Aws\Exception\AwsException;
```

 **Sample Code**

```
// Create an SDK class used to share configuration across clients.
$sdk = new Aws\Sdk([
    'region'   => 'us-west-2'
]);
// Use an Aws\Sdk class to create the S3Client object.
$s3Client = $sdk->createS3();
//Listing all S3 Bucket
$CompleteSynchronously = $s3Client->listBucketsAsync();
// Block until the result is ready.
$CompleteSynchronously = $CompleteSynchronously->wait();
```

You can force a promise to complete synchronously by using the `wait` method of the promise. Forcing the promise to complete also “unwraps” the state of the promise by default, meaning it will either return the result of the promise or throw the exception that was encountered. When calling `wait()` on a promise, the process blocks until the HTTP request is completed and the result is populated or an exception is thrown.

When using the SDK with an event loop library, don’t block on results. Instead, use the `then()` method of a result to access a promise that is resolved or rejected when the operation completes.

 **Imports**

```
require 'vendor/autoload.php';
use Aws\S3\S3Client;
use Aws\Exception\AwsException;
```

 **Sample Code**

```
// Create an SDK class used to share configuration across clients.
$sdk = new Aws\Sdk([
    'region'   => 'us-west-2'
]);
// Use an Aws\Sdk class to create the S3Client object.
$s3Client = $sdk->createS3();
```

```
$promise = $s3Client->listBucketsAsync();
$promise
    ->then(function ($result) {
        echo 'Got a result: ' . var_export($result, true);
    })
    ->otherwise(function ($reason) {
        echo 'Encountered an error: ' . $reason->getMessage();
    });
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
