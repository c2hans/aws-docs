---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/using-waiters.html
---

# Using waiters with the AWS SDK for Swift
<a name="using-waiters"></a>

A waiter is a client-side abstraction that automatically polls a resource until a desired state is reached, or until it's determined that the resource won't enter that state. This kind of polling is commonly used when working with services that typically reach a consistent state, such as Amazon Simple Storage Service (Amazon S3), or services that create resources asynchronously, like Amazon Elastic Compute Cloud (Amazon EC2).

Instead of writing logic to continuously poll an AWS resource, which can be cumbersome and error-prone, you can use a waiter to poll the resource. When the waiter returns, your code knows whether or not the desired state was reached and can act accordingly.

## How to use waiters
<a name="waiters-using"></a>

Many service client classes in the AWS SDK for Swift provide waiters for common "poll and wait" situations that occur while using AWS services. These situations can include both waiting until a resource is available and waiting until the resource becomes unavailable. For example:

**`[S3Client.waitUntilBucketExists(options:input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/waituntilbucketexists(options:input:))``[S3Client.waitUntilBucketNotExists(options:input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/waituntilbucketnotexists(options:input:))`**
Wait until an Amazon S3 bucket exists (or no longer exists).

**`[DynamoDBClient.waitUntilTableExists(options:input:)](https://sdk.amazonaws.com/swift/api/awsdynamodb/latest/documentation/awsdynamodb/dynamodbclient/waituntiltableexists(options:input:))``[DynamoDBClient.waitUntilTableNotExists(options:input:)](https://sdk.amazonaws.com/swift/api/awsdynamodb/latest/documentation/awsdynamodb/dynamodbclient/waituntiltablenotexists(options:input:))`**
Wait until a specific Amazon DynamoDB table exists (or no longer exists).

Waiter functions in the AWS SDK for Swift take two parameters, `options` and `input`.

### Waiter options
<a name="waiters-options"></a>

The first parameter for any waiter function, `options`, is a structure of type `WaiterOptions` (part of the `ClientRuntime` package) that describes the waiter's polling behavior. These options specify the maximum number of seconds to wait before polling times out, and let you optionally set the minimum and maximum delays between retries.

The following example shows how to configure a waiter to wait between a tenth of a second and a half second between retries. The maximum polling time is two seconds.

```
let options = WaiterOptions(maxWaitTime: 2, minDelay: 0.1, maxDelay: 0.5)
```

### Waiter parameters
<a name="waiters-input"></a>

A waiter function's inputs are specified using its `input` parameter. The input's data type corresponds to that of the SDK for Swift function used internally by the waiter to poll the AWS service. For example, the type is `[HeadBucketInput](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/headbucketinput)` for Amazon S3 waiters like `S3Client.waitUntilBucketExists(options:input:)` because this waiter uses the `[S3Client.headBucket(input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/headbucket(input:))` function to poll the bucket. The DynamoDB waiter `DynamoDBClient.waitUntilTableExists(options:input:)` takes as its input a structure of type `[DescribeTableInput](https://sdk.amazonaws.com/swift/api/awsdynamodb/latest/documentation/awsdynamodb/describetableinput)` because it calls `[DynamoDBClient.describeTable(input:)](https://sdk.amazonaws.com/swift/api/awsdynamodb/latest/documentation/awsdynamodb/dynamodbclient/describetable(input:))` internally.

## Example: Waiting for an S3 bucket to exist
<a name="waiters-waituntilbucketexists"></a>

The AWS SDK for Swift offers several waiters for Amazon S3. One of them is `waitUntilBucketExists(options:input:)`, which polls the server until the specified bucket exists.

```
    /// Wait until a bucket with the specified name exists, then return
    /// to the caller. Times out after 60 seconds. Throws an error if the
    /// wait fails.
    ///
    /// - Parameter bucketName: A string giving the name of the bucket
    ///   to wait for.
    ///
    /// - Returns: `true` if the bucket was found or `false` if not.
    ///
    public func waitForBucket(name bucketName: String) async throws -> Bool {
        // Because `waitUntilBucketExists()` internally uses the Amazon S3
        // action `HeadBucket` to look for the bucket, the input is specified
        // with a `HeadBucketInput` structure.

        let output = try await client.waitUntilBucketExists(
            options: WaiterOptions(maxWaitTime: 60.0),
            input: HeadBucketInput(bucket: bucketName)
        )

        switch output.result {
            case .success:
                return true
            case .failure:
                return false
        }
    }
```

This example creates a function that waits until the specified bucket exists, then returns `true`. It returns `false` if polling fails, and might throw an exception if an error occurs. It works by calling the waiter function `[S3Client.waitUntilBucketExists(options:input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/waituntilbucketexists(options:input:))` to poll the server. The `options` specify that polling should time out after 60 seconds.

Because this polling is done using the Amazon S3 action `HeadBucket`, a `HeadBucketInput` object is created with the input parameters for that operation, including the name of the bucket to poll for. This is used as the `input` parameter's value.

`S3Client.waitUntilBucketExists(options:input:)` returns a `result` property whose value is either `.success` if the polling successfully found the bucket, or `.failure` if polling failed. The function returns the corresponding Boolean value to the caller.
