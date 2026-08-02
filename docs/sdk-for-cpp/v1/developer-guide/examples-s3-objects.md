---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-s3-objects.html
---

# Operations on objects
<a name="examples-s3-objects"></a>

An Amazon S3 object represents a *file*, which is a collection of data. Every object must reside within a [bucket](examples-s3-buckets.md).

## Prerequisites
<a name="codeExamplePrereq"></a>

Before you begin, we recommend you read [Getting started using the AWS SDK for C\+\+](getting-started.md).

Download the example code and build the solution as described in [Getting started on code examples](getting-started-code-examples.md).

To run the examples, the user profile your code uses to make the requests must have proper permissions in AWS (for the service and the action). For more information, see [Providing AWS credentials](credentials.md).

## Upload a file to a bucket
<a name="upload-object"></a>

Use the `S3Client` object `PutObject` function, supplying it with a bucket name, key name, and file to upload. `Aws::FStream` is used to upload the contents of the local file to the bucket. The bucket must exist or an error will result.

For an example on uploading objects asynchronously, see [Asynchronous programming using the AWS SDK for C\+\+](async-methods.md)

 **Code**

```
bool AwsDoc::S3::putObject(const Aws::String &bucketName,
                           const Aws::String &fileName,
                           const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client s3Client(clientConfig);

    Aws::S3::Model::PutObjectRequest request;
    request.SetBucket(bucketName);
    //We are using the name of the file as the key for the object in the bucket.
    //However, this is just a string and can be set according to your retrieval needs.
    request.SetKey(fileName);

    std::shared_ptr<Aws::IOStream> inputData =
            Aws::MakeShared<Aws::FStream>("SampleAllocationTag",
                                          fileName.c_str(),
                                          std::ios_base::in | std::ios_base::binary);

    if (!*inputData) {
        std::cerr << "Error unable to read file " << fileName << std::endl;
        return false;
    }

    request.SetBody(inputData);

    Aws::S3::Model::PutObjectOutcome outcome =
            s3Client.PutObject(request);

    if (!outcome.IsSuccess()) {
        std::cerr << "Error: putObject: " <<
                  outcome.GetError().GetMessage() << std::endl;
    } else {
        std::cout << "Added object '" << fileName << "' to bucket '"
                  << bucketName << "'.";
    }

    return outcome.IsSuccess();
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/put_object.cpp) on Github.

## Upload a string to a bucket
<a name="upload-object-string"></a>

Use the `S3Client` object `PutObject` function, supplying it with a bucket name, key name, and file to upload. The bucket must exist or an error will result. This example differs from the previous one by using `Aws::StringStream` to upload an in-memory string data object directly to a bucket.

For an example on uploading objects asynchronously, see [Asynchronous programming using the AWS SDK for C\+\+](async-methods.md)

 **Code**

```
bool AwsDoc::S3::putObjectBuffer(const Aws::String &bucketName,
                                 const Aws::String &objectName,
                                 const std::string &objectContent,
                                 const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client s3Client(clientConfig);

    Aws::S3::Model::PutObjectRequest request;
    request.SetBucket(bucketName);
    request.SetKey(objectName);

    const std::shared_ptr<Aws::IOStream> inputData =
            Aws::MakeShared<Aws::StringStream>("");
    *inputData << objectContent.c_str();

    request.SetBody(inputData);

    Aws::S3::Model::PutObjectOutcome outcome = s3Client.PutObject(request);

    if (!outcome.IsSuccess()) {
        std::cerr << "Error: putObjectBuffer: " <<
                  outcome.GetError().GetMessage() << std::endl;
    } else {
        std::cout << "Success: Object '" << objectName << "' with content '"
                  << objectContent << "' uploaded to bucket '" << bucketName << "'.";
    }

    return outcome.IsSuccess();
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/put_object_buffer.cpp) on Github.

## List objects
<a name="list-objects"></a>

To get a list of objects within a bucket, use the `S3Client` object `ListObjects` function. Supply it with a `ListObjectsRequest` that you set with the name of a bucket to list the contents of.

The `ListObjects` function returns a `ListObjectsOutcome` object that you can use to get a list of objects in the form of `Object` instances.

 **Code**

```
bool AwsDoc::S3::listObjects(const Aws::String &bucketName,
                             Aws::Vector<Aws::String> &keysResult,
                             const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client s3Client(clientConfig);

    Aws::S3::Model::ListObjectsV2Request request;
    request.WithBucket(bucketName);

    Aws::String continuationToken; // Used for pagination.
    Aws::Vector<Aws::S3::Model::Object> allObjects;

    do {
        if (!continuationToken.empty()) {
            request.SetContinuationToken(continuationToken);
        }

        auto outcome = s3Client.ListObjectsV2(request);

        if (!outcome.IsSuccess()) {
            std::cerr << "Error: listObjects: " <<
                      outcome.GetError().GetMessage() << std::endl;
            return false;
        } else {
            Aws::Vector<Aws::S3::Model::Object> objects =
                    outcome.GetResult().GetContents();

            allObjects.insert(allObjects.end(), objects.begin(), objects.end());
            continuationToken = outcome.GetResult().GetNextContinuationToken();
        }
    } while (!continuationToken.empty());

    std::cout << allObjects.size() << " object(s) found:" << std::endl;

    for (const auto &object: allObjects) {
        std::cout << "  " << object.GetKey() << std::endl;
        keysResult.push_back(object.GetKey());
    }

    return true;
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/list_objects.cpp) on Github.

## Download an object
<a name="download-object"></a>

Use the `S3Client` object `GetObject` function, passing it a `GetObjectRequest` that you set with the name of a bucket and the object key to download. `GetObject` returns a [https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/namespace_aws_1_1_s3_1_1_model.html#a6e16a7b25e8c7547934968a538a15272](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/namespace_aws_1_1_s3_1_1_model.html#a6e16a7b25e8c7547934968a538a15272) object that consists of a [https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/class_aws_1_1_s3_1_1_model_1_1_get_object_result.html](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/class_aws_1_1_s3_1_1_model_1_1_get_object_result.html) and a [https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/class_aws_1_1_s3_1_1_s3_error.html](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/class_aws_1_1_s3_1_1_s3_error.html). `GetObjectResult` can be used to access the S3 object’s data.

The following example downloads an object from Amazon S3. The object contents are stored in a local variable and the first line of the contents is output to the console.

 **Code**

```
bool AwsDoc::S3::getObject(const Aws::String &objectKey,
                           const Aws::String &fromBucket,
                           const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client client(clientConfig);

    Aws::S3::Model::GetObjectRequest request;
    request.SetBucket(fromBucket);
    request.SetKey(objectKey);

    Aws::S3::Model::GetObjectOutcome outcome =
            client.GetObject(request);

    if (!outcome.IsSuccess()) {
        const Aws::S3::S3Error &err = outcome.GetError();
        std::cerr << "Error: getObject: " <<
                  err.GetExceptionName() << ": " << err.GetMessage() << std::endl;
    } else {
        std::cout << "Successfully retrieved '" << objectKey << "' from '"
                  << fromBucket << "'." << std::endl;
    }

    return outcome.IsSuccess();
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/get_object.cpp) on Github.

## Delete an object
<a name="delete-object"></a>

Use the `S3Client` object’s `DeleteObject` function, passing it a `DeleteObjectRequest` that you set with the name of a bucket and object to download. *The specified bucket and object key must exist or an error will result*.

 **Code**

```
bool AwsDoc::S3::deleteObject(const Aws::String &objectKey,
                              const Aws::String &fromBucket,
                              const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client client(clientConfig);
    Aws::S3::Model::DeleteObjectRequest request;

    request.WithKey(objectKey)
            .WithBucket(fromBucket);

    Aws::S3::Model::DeleteObjectOutcome outcome =
            client.DeleteObject(request);

    if (!outcome.IsSuccess()) {
        auto err = outcome.GetError();
        std::cerr << "Error: deleteObject: " <<
                  err.GetExceptionName() << ": " << err.GetMessage() << std::endl;
    } else {
        std::cout << "Successfully deleted the object." << std::endl;
    }

    return outcome.IsSuccess();
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/delete_object.cpp) on Github.
