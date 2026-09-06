---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_EnrichmentSourceS3Configuration.html
---

# EnrichmentSourceS3Configuration
<a name="API_EnrichmentSourceS3Configuration"></a>

S3 configuration for the source import file to be enriched.

## Contents
<a name="API_EnrichmentSourceS3Configuration_Contents"></a>

 ** s3Bucket **   <a name="mgn-Type-EnrichmentSourceS3Configuration-s3Bucket"></a>
The name of the S3 bucket containing the source import file.
Type: String
Pattern: `[a-zA-Z0-9.\-_]{1,255}`
Required: Yes

 ** s3BucketOwner **   <a name="mgn-Type-EnrichmentSourceS3Configuration-s3BucketOwner"></a>
The AWS account ID of the S3 bucket owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: Yes

 ** s3Key **   <a name="mgn-Type-EnrichmentSourceS3Configuration-s3Key"></a>
The S3 key (path) for the source import file.
Type: String
Pattern: `[^\x00]{1,1024}`
Required: Yes

## See Also
<a name="API_EnrichmentSourceS3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/EnrichmentSourceS3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/EnrichmentSourceS3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/EnrichmentSourceS3Configuration)
