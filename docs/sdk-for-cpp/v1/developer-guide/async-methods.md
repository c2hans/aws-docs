---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/async-methods.html
---

# Asynchronous programming using the AWS SDK for C\+\+
<a name="async-methods"></a>

## Asynchronous SDK methods
<a name="asynchronous-sdk-methods"></a>

For many methods, the SDK for C\+\+ provides both synchronous and asynchronous versions. A method is asynchronous if it includes the `Async` suffix in its name. For example, the Amazon S3 method `PutObject` is synchronous, while `PutObjectAsync` is asynchronous.

Like all asynchronous operations, an asynchronous SDK method returns before its main task is finished. For example, the `PutObjectAsync` method returns before it finishes uploading the file to the Amazon S3 bucket. While the upload operation continues, the application can perform other operations, including calling other asynchronous methods. The application is notified that an asynchronous operation has finished when an associated callback function is invoked.

The following sections describe a code example that demonstrates calling the `PutObjectAsync` asynchronous method. Each section focuses on individual portions from the example’s [entire source file](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/put_object_async.cpp).

## Calling SDK asynchronous methods
<a name="calling-sdk-asynchronous-methods"></a>

In general, the asynchronous version of an SDK method accepts the following arguments.
+ A reference to the same Request-type object as its synchronous counterpart.
+ A reference to a response handler callback function. This callback function is invoked when the asynchronous operation finishes. One of the arguments contains the operation’s outcome.
+ An optional `shared_ptr` to an `AsyncCallerContext` object. The object is passed to the response handler callback. It includes a UUID property that can be used to pass text information to the callback.

The `uploadFileAsync` method shown below sets up and calls the SDK's Amazon S3 `PutObjectAsync` method to asynchronously upload a file to an Amazon S3 bucket.

The function receives references to an `S3Client` object and a `PutObjectRequest` object. It receives them from the main function because we need to ensure that these objects exist throughout the duration of the asynchronous calls.

A `shared_ptr` to an `AsyncCallerContext` object is allocated. Its `UUID` property is set to the Amazon S3 object name. For demonstration purposes, the response handler callback accesses the property and outputs its value.

The call to `PutObjectAsync` includes a reference argument to the response handler callback function `uploadFileAsyncFinished`. This callback function is examined in more detail in the next section.

```
bool AwsDoc::S3::uploadFileAsync(const Aws::S3::S3Client &s3Client,
                                Aws::S3::Model::PutObjectRequest &request,
                                const Aws::String &bucketName,
                                const Aws::String &fileName) {
    request.SetBucket(bucketName);
    request.SetKey(fileName);

    const std::shared_ptr<Aws::IOStream> input_data =
            Aws::MakeShared<Aws::FStream>("SampleAllocationTag",
                                          fileName.c_str(),
                                          std::ios_base::in | std::ios_base::binary);

    if (!*input_data) {
        std::cerr << "Error: unable to open file " << fileName << std::endl;
        return false;
    }

    request.SetBody(input_data);

    // Create and configure the context for the asynchronous put object request.
    std::shared_ptr<Aws::Client::AsyncCallerContext> context =
            Aws::MakeShared<Aws::Client::AsyncCallerContext>("PutObjectAllocationTag");
    context->SetUUID(fileName);

    // Make the asynchronous put object call. Queue the request into a
    // thread executor and call the uploadFileAsyncFinished function when the
    // operation has finished.
    s3Client.PutObjectAsync(request, uploadFileAsyncFinished, context);

    return true;
}
```

The resources for an asynchronous operation must exist until the operation finishes. For example, the client and request objects must exist until the application receives notification that the operation completed. The application itself cannot terminate until the asynchronous operation completes.

For this reason, the `uploadFileAsync` method accepts a references to `S3Client` and `PutObjectRequest` objects instead of creating them in the `uploadFileAsync` method and storing them in a local variable.

In the example, the `PutObjectAsync` method returns to the caller immediately after beginning the asynchronous operation, enabling the calling chain to perform additional tasks while the upload operation is in progress.

If the client were stored in a local variable in the `uploadFileAsync` method, it would go out of scope when the method returned. However, the client object must continue to exist until the asynchronous operation finishes.

## Notification of the Completion of an Asynchronous Operation
<a name="notification-of-the-completion-of-an-asynchronous-operation"></a>

When an asynchronous operation finishes, an application response handler callback function is invoked. This notification includes the outcome of the operation. The outcome is contained in the same Outcome-type class returned by the method’s synchronous counterpart. In the code example, the outcome is in a `PutObjectOutcome` object.

The example’s response handler callback function `uploadFileAsyncFinished` is shown below. It checks whether the asynchronous operation succeeded or failed. It uses a `std::condition_variable` to notify the application thread that the async operation has finished.

```
// A mutex is a synchronization primitive that can be used to protect shared
// data from being simultaneously accessed by multiple threads.
std::mutex AwsDoc::S3::upload_mutex;

// A condition_variable is a synchronization primitive that can be used to
// block a thread, or to block multiple threads at the same time.
// The thread is blocked until another thread both modifies a shared
// variable (the condition) and notifies the condition_variable.
std::condition_variable AwsDoc::S3::upload_variable;
```

```
void uploadFileAsyncFinished(const Aws::S3::S3Client *s3Client,
                            const Aws::S3::Model::PutObjectRequest &request,
                            const Aws::S3::Model::PutObjectOutcome &outcome,
                            const std::shared_ptr<const Aws::Client::AsyncCallerContext> &context) {
    if (outcome.IsSuccess()) {
        std::cout << "Success: uploadFileAsyncFinished: Finished uploading '"
                  << context->GetUUID() << "'." << std::endl;
    } else {
        std::cerr << "Error: uploadFileAsyncFinished: " <<
                  outcome.GetError().GetMessage() << std::endl;
    }

    // Unblock the thread that is waiting for this function to complete.
    AwsDoc::S3::upload_variable.notify_one();
}
```

With the asynchronous operation finished, the resources associated with it can be released. The application can also terminate if it wishes.

The following code demonstrates how the `uploadFileAsync` and `uploadFileAsyncFinished` methods are used by an application.

The application allocates the `S3Client` and `PutObjectRequest` objects so that they continue to exist until the asynchronous operation finishes. After calling `uploadFileAsync`, the application can perform whatever operations it wishes. For simplicity, the example uses a `std::mutex` and `std::condition_variable` to wait until the response handler callback notifies it that the upload operation has finished.

```
int main(int argc, char* argv[])
{
    if (argc != 3)
    {
        std::cout << R"(
Usage:
    run_put_object_async <file_name> <bucket_name>
Where:
    file_name - The name of the file to upload.
    bucket_name - The name of the bucket to upload the object to.
)" << std::endl;
        return 1;
    }

    const Aws::SDKOptions options;
    Aws::InitAPI(options);
    {
        const Aws::String fileName = argv[1];
        const Aws::String bucketName = argv[2];

        // A unique_lock is a general-purpose mutex ownership wrapper allowing
        // deferred locking, time-constrained attempts at locking, recursive
        // locking, transfer of lock ownership, and use with
        // condition variables.
        std::unique_lock<std::mutex> lock(AwsDoc::S3::upload_mutex);

        // Create and configure the Amazon S3 client.
        // This client must be declared here, as this client must exist
        // until the put object operation finishes.
        const Aws::S3::S3ClientConfiguration config;
        // Optional: Set to the AWS Region in which the bucket was created (overrides config file).
        // config.region = "us-east-1";

        const Aws::S3::S3Client s3Client(config);

        // Create the request object.
        // This request object must be declared here, because the object must exist
        // until the put object operation finishes.
        Aws::S3::Model::PutObjectRequest request;

        AwsDoc::S3::uploadFileAsync(s3Client, request, bucketName, fileName);

        std::cout << "main: Waiting for file upload attempt..." <<
                  std::endl << std::endl;

        // While the put object operation attempt is in progress,
        // you can perform other tasks.
        // This example simply blocks until the put object operation
        // attempt finishes.
        AwsDoc::S3::upload_variable.wait(lock);

        std::cout << std::endl << "main: File upload attempt completed."
                  << std::endl;
    }
    Aws::ShutdownAPI(options);

    return 0;
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/put_object_async.cpp) on Github.
