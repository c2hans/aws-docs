---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_StorageClassConfiguration.html
---

# StorageClassConfiguration
<a name="API_s3Buckets_StorageClassConfiguration"></a>

The configuration details for the storage class of tables or table buckets. This allows you to optimize storage costs by selecting the appropriate storage class based on your access patterns and performance requirements.

## Contents
<a name="API_s3Buckets_StorageClassConfiguration_Contents"></a>

 ** storageClass **   <a name="AmazonS3-Type-s3Buckets_StorageClassConfiguration-storageClass"></a>
The storage class for the table or table bucket. Valid values include storage classes optimized for different access patterns and cost profiles.
Type: String
Valid Values: `STANDARD | INTELLIGENT_TIERING`
Required: Yes

## See Also
<a name="API_s3Buckets_StorageClassConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/StorageClassConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/StorageClassConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/StorageClassConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
