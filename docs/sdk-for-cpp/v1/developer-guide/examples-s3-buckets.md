---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-s3-buckets.html
---

# Creating, listing, and deleting buckets
<a name="examples-s3-buckets"></a>

Every *object* or file in Amazon Simple Storage Service (Amazon S3) is contained in a *bucket*, which represents a folder of objects. Each bucket has a name that is globally unique within AWS. For more information, see [Working with Amazon S3 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html) in the Amazon Simple Storage Service User Guide.

## Prerequisites
<a name="codeExamplePrereq"></a>

Before you begin, we recommend you read [Getting started using the AWS SDK for C\+\+](getting-started.md).

Download the example code and build the solution as described in [Getting started on code examples](getting-started-code-examples.md).

To run the examples, the user profile your code uses to make the requests must have proper permissions in AWS (for the service and the action). For more information, see [Providing AWS credentials](credentials.md).

## List buckets
<a name="list-buckets"></a>

To run the `list_buckets` example, at a command prompt, navigate to the folder where your build system creates your build executables. Run the executable like `run_list_buckets` (your full executable filename will differ based on your operating system). The output lists your account's buckets if you have any, or it displays an empty list if you don't have any buckets.

In `list_buckets.cpp`, there are two methods.
+ `main()` calls `ListBuckets()`.
+ `ListBuckets()` uses the SDK to query your buckets.

The `S3Client` object calls the SDK's `ListBuckets()` method. If successful, the method returns a `ListBucketOutcome` object, which contains a `ListBucketResult` object. The `ListBucketResult` object calls the `GetBuckets()` method to get a list of `Bucket` objects that contain information about each Amazon S3 bucket in your account.

 **Code**

```
bool AwsDoc::S3::listBuckets(const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client client(clientConfig);

    auto outcome = client.ListBuckets();

    bool result = true;
    if (!outcome.IsSuccess()) {
        std::cerr << "Failed with error: " << outcome.GetError() << std::endl;
        result = false;
    } else {
        std::cout << "Found " << outcome.GetResult().GetBuckets().size() << " buckets\n";
        for (auto &&b: outcome.GetResult().GetBuckets()) {
            std::cout << b.GetName() << std::endl;
        }
    }

    return result;
}
```

See the complete [list\_buckets example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/list_buckets.cpp) on Github.

## Create a bucket
<a name="create-bucket"></a>

To run the `create_bucket` example, at a command prompt, navigate to the folder where your build system creates your build executables. Run the executable like `run_create_bucket` (your full executable filename will differ based on your operating system). The code creates an empty bucket under your account and then displays the success or failure of the request.

In `create_bucket.cpp`, there are two methods.
+ `main()` calls `CreateBucket()`. In `main()`, you need to change the AWS Region to the Region of your account by using the `enum`. You can view the Region of your account by logging into the [AWS Management Console](https://console.aws.amazon.com/), and locating the Region in the upper right-hand corner.
+ `CreateBucket()` uses the SDK to create a bucket.

The `S3Client` object calls the SDK's `CreateBucket()` method, passing in a `CreateBucketRequest` with the bucket’s name. By default, buckets are created in the *us-east-1* (N. Virginia) Region. If your Region is not *us-east-1* then the code sets up a bucket constraint to ensure the bucket is created in your Region.

 **Code**

```
bool AwsDoc::S3::createBucket(const Aws::String &bucketName,
                              const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client client(clientConfig);
    Aws::S3::Model::CreateBucketRequest request;
    request.SetBucket(bucketName);

    if (clientConfig.region != "us-east-1") {
        Aws::S3::Model::CreateBucketConfiguration createBucketConfig;
        createBucketConfig.SetLocationConstraint(
                Aws::S3::Model::BucketLocationConstraintMapper::GetBucketLocationConstraintForName(
                        clientConfig.region));
        request.SetCreateBucketConfiguration(createBucketConfig);
    }

    Aws::S3::Model::CreateBucketOutcome outcome = client.CreateBucket(request);
    if (!outcome.IsSuccess()) {
        auto err = outcome.GetError();
        std::cerr << "Error: createBucket: " <<
                  err.GetExceptionName() << ": " << err.GetMessage() << std::endl;
    } else {
        std::cout << "Created bucket " << bucketName <<
                  " in the specified AWS Region." << std::endl;
    }

    return outcome.IsSuccess();
}
```

See the complete [create\_buckets example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/create_bucket.cpp) on Github.

## Delete a bucket
<a name="delete-bucket"></a>

To run the `delete_bucket` example, at a command prompt, navigate to the folder where your build system creates your build executables. Run the executable like `run_delete_bucket` (your full executable filename will differ based on your operating system). The code deletes the specified bucket in your account and then displays the success or failure of the request.

In `delete_bucket.cpp` there are two methods.
+ `main()` calls `DeleteBucket()`. In `main()`, you need to change the AWS Region to the Region of your account by using the `enum`. You also need to change the `bucket_name` to the name of the bucket to delete.
+ `DeleteBucket()` uses the SDK to delete the bucket.

The `S3Client` object uses the SDK's `DeleteBucket()` method, passing in a `DeleteBucketRequest` object with the name of the bucket to delete. The bucket must be empty to be successful.

 **Code**

```
bool AwsDoc::S3::deleteBucket(const Aws::String &bucketName,
                              const Aws::S3::S3ClientConfiguration &clientConfig) {

    Aws::S3::S3Client client(clientConfig);

    Aws::S3::Model::DeleteBucketRequest request;
    request.SetBucket(bucketName);

    Aws::S3::Model::DeleteBucketOutcome outcome =
            client.DeleteBucket(request);

    if (!outcome.IsSuccess()) {
        const Aws::S3::S3Error &err = outcome.GetError();
        std::cerr << "Error: deleteBucket: " <<
                  err.GetExceptionName() << ": " << err.GetMessage() << std::endl;
    } else {
        std::cout << "The bucket was deleted" << std::endl;
    }

    return outcome.IsSuccess();
}
```

See the complete [delete\_bucket example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/delete_bucket.cpp) on Github.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
