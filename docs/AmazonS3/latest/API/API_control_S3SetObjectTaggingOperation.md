---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3SetObjectTaggingOperation.html
---

# S3SetObjectTaggingOperation
<a name="API_control_S3SetObjectTaggingOperation"></a>

Contains the configuration parameters for a PUT Object Tagging operation. S3 Batch Operations passes every object to the underlying `PutObjectTagging` API operation. For more information about the parameters for this operation, see [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPUTtagging.html).

## Contents
<a name="API_control_S3SetObjectTaggingOperation_Contents"></a>

 ** TagSet **   <a name="AmazonS3-Type-control_S3SetObjectTaggingOperation-TagSet"></a>

Type: Array of [S3Tag](API_control_S3Tag.md) data types
Required: No

## See Also
<a name="API_control_S3SetObjectTaggingOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3SetObjectTaggingOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3SetObjectTaggingOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3SetObjectTaggingOperation)
