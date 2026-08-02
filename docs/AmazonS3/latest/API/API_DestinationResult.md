---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_DestinationResult.html
---

# DestinationResult
<a name="API_DestinationResult"></a>

 The destination information for the S3 Metadata configuration.

## Contents
<a name="API_DestinationResult_Contents"></a>

 ** TableBucketArn **   <a name="AmazonS3-Type-DestinationResult-TableBucketArn"></a>
 The Amazon Resource Name (ARN) of the table bucket where the metadata configuration is stored.
Type: String
Required: No

 ** TableBucketType **   <a name="AmazonS3-Type-DestinationResult-TableBucketType"></a>
 The type of the table bucket where the metadata configuration is stored. The `aws` value indicates an AWS managed table bucket, and the `customer` value indicates a customer-managed table bucket. V2 metadata configurations are stored in AWS managed table buckets, and V1 metadata configurations are stored in customer-managed table buckets.
Type: String
Valid Values: `aws | customer`
Required: No

 ** TableNamespace **   <a name="AmazonS3-Type-DestinationResult-TableNamespace"></a>
 The namespace in the table bucket where the metadata tables for a metadata configuration are stored.
Type: String
Required: No

## See Also
<a name="API_DestinationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DestinationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DestinationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DestinationResult)
