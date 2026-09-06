---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-s3-website-configuration.html
---

# Configuring an Amazon S3 Bucket as a Website
<a name="examples-s3-website-configuration"></a>

You can configure an Amazon S3 bucket to behave as a website. To do this, you need to set its website configuration.

## Prerequisites
<a name="codeExamplePrereq"></a>

Before you begin, we recommend you read [Getting started using the AWS SDK for C\+\+](getting-started.md).

Download the example code and build the solution as described in [Getting started on code examples](getting-started-code-examples.md).

To run the examples, the user profile your code uses to make the requests must have proper permissions in AWS (for the service and the action). For more information, see [Providing AWS credentials](credentials.md).

## Set a Bucket’s Website Configuration
<a name="set-a-bucket-s-website-configuration"></a>

To set an Amazon S3 bucket’s website configuration, call the `S3Client`’s `PutBucketWebsite` function with a [PutBucketWebsiteRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/class_aws_1_1_s3_1_1_model_1_1_put_bucket_website_request.html) object containing the bucket name and its website configuration, provided in a [WebsiteConfiguration](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/class_aws_1_1_s3_1_1_model_1_1_website_configuration.html) object.

Setting an index document is *required*; all other parameters are optional.

 **Code**

```
bool AwsDoc::S3::putWebsiteConfig(const Aws::String &bucketName,
                                  const Aws::String &indexPage, const Aws::String &errorPage,
                                  const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client client(clientConfig);

    Aws::S3::Model::IndexDocument indexDocument;
    indexDocument.SetSuffix(indexPage);

    Aws::S3::Model::ErrorDocument errorDocument;
    errorDocument.SetKey(errorPage);

    Aws::S3::Model::WebsiteConfiguration websiteConfiguration;
    websiteConfiguration.SetIndexDocument(indexDocument);
    websiteConfiguration.SetErrorDocument(errorDocument);

    Aws::S3::Model::PutBucketWebsiteRequest request;
    request.SetBucket(bucketName);
    request.SetWebsiteConfiguration(websiteConfiguration);

    Aws::S3::Model::PutBucketWebsiteOutcome outcome =
            client.PutBucketWebsite(request);

    if (!outcome.IsSuccess()) {
        std::cerr << "Error: PutBucketWebsite: "
                  << outcome.GetError().GetMessage() << std::endl;
    } else {
        std::cout << "Success: Set website configuration for bucket '"
                  << bucketName << "'." << std::endl;
    }

    return outcome.IsSuccess();
}
```

**Note**
Setting a website configuration does not modify the access permissions for your bucket. To make your files visible on the web, you will also need to set a *bucket policy* that allows public read access to the files in the bucket. For more information, see [Managing Access to Amazon S3 Buckets Using Bucket Policies](examples-s3-bucket-policies.md).

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/put_website_config.cpp) on Github.

## Get a Bucket’s Website Configuration
<a name="get-a-bucket-s-website-configuration"></a>

To get an Amazon S3 bucket’s website configuration, call the `S3Client`’s `GetBucketWebsite` function with a [GetBucketWebsiteRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/class_aws_1_1_s3_1_1_model_1_1_get_bucket_website_request.html) containing the name of the bucket to retrieve the configuration for.

The configuration will be returned as a [GetBucketWebsiteResult](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/class_aws_1_1_s3_1_1_model_1_1_get_bucket_website_result.html) object within the outcome object. If there is no website configuration for the bucket, then `null` will be returned.

 **Code**

```
bool AwsDoc::S3::getWebsiteConfig(const Aws::String &bucketName,
                                  const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client s3Client(clientConfig);

    Aws::S3::Model::GetBucketWebsiteRequest request;
    request.SetBucket(bucketName);

    Aws::S3::Model::GetBucketWebsiteOutcome outcome =
            s3Client.GetBucketWebsite(request);

    if (!outcome.IsSuccess()) {
        const Aws::S3::S3Error &err = outcome.GetError();

        std::cerr << "Error: GetBucketWebsite: "
                  << err.GetMessage() << std::endl;
    } else {
        Aws::S3::Model::GetBucketWebsiteResult websiteResult = outcome.GetResult();

        std::cout << "Success: GetBucketWebsite: "
                  << std::endl << std::endl
                  << "For bucket '" << bucketName << "':"
                  << std::endl
                  << "Index page : "
                  << websiteResult.GetIndexDocument().GetSuffix()
                  << std::endl
                  << "Error page: "
                  << websiteResult.GetErrorDocument().GetKey()
                  << std::endl;
    }

    return outcome.IsSuccess();
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/get_website_config.cpp) on Github.

## Delete a Bucket’s Website Configuration
<a name="delete-a-bucket-s-website-configuration"></a>

To delete an Amazon S3 bucket’s website configuration, call the `S3Client`’s `DeleteBucketWebsite` function with a [DeleteBucketWebsiteRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-s3/html/class_aws_1_1_s3_1_1_model_1_1_delete_bucket_website_request.html): containing the name of the bucket to delete the configuration from.

 **Code**

```
bool AwsDoc::S3::deleteBucketWebsite(const Aws::String &bucketName,
                                     const Aws::S3::S3ClientConfiguration &clientConfig) {
    Aws::S3::S3Client client(clientConfig);
    Aws::S3::Model::DeleteBucketWebsiteRequest request;
    request.SetBucket(bucketName);

    Aws::S3::Model::DeleteBucketWebsiteOutcome outcome =
            client.DeleteBucketWebsite(request);

    if (!outcome.IsSuccess()) {
        auto err = outcome.GetError();
        std::cerr << "Error: deleteBucketWebsite: " <<
                  err.GetExceptionName() << ": " << err.GetMessage() << std::endl;
    } else {
        std::cout << "Website configuration was removed." << std::endl;
    }

    return outcome.IsSuccess();
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/delete_website_config.cpp) on Github.

## More Information
<a name="more-information"></a>
+  [PUT Bucket website](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTwebsite.html) in the Amazon Simple Storage Service API Reference
+  [GET Bucket website](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETwebsite.html) in the Amazon Simple Storage Service API Reference
+  [DELETE Bucket website](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketDELETEwebsite.html) in the Amazon Simple Storage Service API Reference
