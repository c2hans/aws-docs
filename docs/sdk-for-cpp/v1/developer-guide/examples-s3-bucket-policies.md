---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-s3-bucket-policies.html
---

# Managing Access to Amazon S3 Buckets Using Bucket Policies
<a name="examples-s3-bucket-policies"></a>

You can set, get, or delete a *bucket policy* to manage access to your Amazon S3 buckets.

## Prerequisites
<a name="codeExamplePrereq"></a>

Before you begin, we recommend you read [Getting started using the AWS SDK for C\+\+](getting-started.md).

Download the example code and build the solution as described in [Getting started on code examples](getting-started-code-examples.md).

To run the examples, the user profile your code uses to make the requests must have proper permissions in AWS (for the service and the action). For more information, see [Providing AWS credentials](credentials.md).

## Set a Bucket Policy
<a name="set-s3-bucket-policy"></a>

You can set the bucket policy for a particular S3 bucket by calling the `S3Client`’s `PutBucketPolicy` function and providing it with the bucket name and policy’s JSON representation in a [PutBucketPolicyRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/class_aws_1_1_s3_1_1_model_1_1_put_bucket_policy_request.html).

 **Code**

```
//! Build a policy JSON string.
/*!
  \param userArn: Aws user Amazon Resource Name (ARN).
      For more information, see https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns.
  \param bucketName: Name of a bucket.
  \return String: Policy as JSON string.
*/

Aws::String getPolicyString(const Aws::String &userArn,
                            const Aws::String &bucketName) {
    return
            "{\n"
            "   \"Version\":\"2012-10-17\",\n"
            "   \"Statement\":[\n"
            "       {\n"
            "           \"Sid\": \"1\",\n"
            "           \"Effect\": \"Allow\",\n"
            "           \"Principal\": {\n"
            "               \"AWS\": \""
            + userArn +
            "\"\n""           },\n"
            "           \"Action\": [ \"s3:getObject\" ],\n"
            "           \"Resource\": [ \"arn:aws:s3:::"
            + bucketName +
            "/*\" ]\n"
            "       }\n"
            "   ]\n"
            "}";
}
```

```
bool AwsDoc::S3::putBucketPolicy(const Aws::String &bucketName,
                                 const Aws::String &policyBody,
                                 const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client s3Client(clientConfig);

    std::shared_ptr<Aws::StringStream> request_body =
            Aws::MakeShared<Aws::StringStream>("");
    *request_body << policyBody;

    Aws::S3::Model::PutBucketPolicyRequest request;
    request.SetBucket(bucketName);
    request.SetBody(request_body);

    Aws::S3::Model::PutBucketPolicyOutcome outcome =
            s3Client.PutBucketPolicy(request);

    if (!outcome.IsSuccess()) {
        std::cerr << "Error: putBucketPolicy: "
                  << outcome.GetError().GetMessage() << std::endl;
    } else {
        std::cout << "Set the following policy body for the bucket '" <<
                  bucketName << "':" << std::endl << std::endl;
        std::cout << policyBody << std::endl;
    }

    return outcome.IsSuccess();
}
```

**Note**
The [Aws::Utils::Json::JsonValue](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-core/html/class_aws_1_1_utils_1_1_json_1_1_json_value.html) utility class can be used to help you construct valid JSON objects to pass to `PutBucketPolicy`.

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/put_bucket_policy.cpp) on Github.

## Get a Bucket Policy
<a name="get-s3-bucket-policy"></a>

To retrieve the policy for an Amazon S3 bucket, call the `S3Client`’s `GetBucketPolicy` function, passing it the name of the bucket in a [GetBucketPolicyRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/class_aws_1_1_s3_1_1_model_1_1_get_bucket_policy_request.html).

 **Code**

```
bool AwsDoc::S3::getBucketPolicy(const Aws::String &bucketName,
                                 const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client s3Client(clientConfig);

    Aws::S3::Model::GetBucketPolicyRequest request;
    request.SetBucket(bucketName);

    Aws::S3::Model::GetBucketPolicyOutcome outcome =
            s3Client.GetBucketPolicy(request);

    if (!outcome.IsSuccess()) {
        const Aws::S3::S3Error &err = outcome.GetError();
        std::cerr << "Error: getBucketPolicy: "
                  << err.GetExceptionName() << ": " << err.GetMessage() << std::endl;
    } else {
        Aws::StringStream policy_stream;
        Aws::String line;

        outcome.GetResult().GetPolicy() >> line;
        policy_stream << line;

        std::cout << "Retrieve the policy for bucket '" << bucketName << "':\n\n" <<
                  policy_stream.str() << std::endl;
    }

    return outcome.IsSuccess();
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/get_bucket_policy.cpp) on Github.

## Delete a Bucket Policy
<a name="delete-s3-bucket-policy"></a>

To delete a bucket policy, call the `S3Client`’s `DeleteBucketPolicy` function, providing it with the bucket name in a [DeleteBucketPolicyRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/class_aws_1_1_s3_1_1_model_1_1_delete_bucket_policy_request.html).

 **Code**

```
bool AwsDoc::S3::deleteBucketPolicy(const Aws::String &bucketName,
                                    const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client client(clientConfig);

    Aws::S3::Model::DeleteBucketPolicyRequest request;
    request.SetBucket(bucketName);

    Aws::S3::Model::DeleteBucketPolicyOutcome outcome = client.DeleteBucketPolicy(request);

    if (!outcome.IsSuccess()) {
        const Aws::S3::S3Error &err = outcome.GetError();
        std::cerr << "Error: deleteBucketPolicy: " <<
                  err.GetExceptionName() << ": " << err.GetMessage() << std::endl;
    } else {
        std::cout << "Policy was deleted from the bucket." << std::endl;
    }

    return outcome.IsSuccess();
}
```

This function succeeds even if the bucket doesn’t already have a policy. If you specify a bucket name that doesn’t exist or if you don’t have access to the bucket, an `AmazonServiceException` is thrown.

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/delete_bucket_policy.cpp) on Github.

## More Info
<a name="more-info"></a>
+  [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/PutBucketPolicy.html) in the Amazon Simple Storage Service API Reference
+  [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/GetBucketPolicy.html) in the Amazon Simple Storage Service API Reference
+  [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/DeleteBucketPolicy.html) in the Amazon Simple Storage Service API Reference
+  [Access Policy Language Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html) in the Amazon Simple Storage Service User Guide
+  [Bucket Policy Examples](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) in the Amazon Simple Storage Service User Guide

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
