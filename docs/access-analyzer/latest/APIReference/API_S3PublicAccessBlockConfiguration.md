---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_S3PublicAccessBlockConfiguration.html
---

# S3PublicAccessBlockConfiguration
<a name="API_S3PublicAccessBlockConfiguration"></a>

The `PublicAccessBlock` configuration to apply to this Amazon S3 bucket. If the proposed configuration is for an existing Amazon S3 bucket and the configuration is not specified, the access preview uses the existing setting. If the proposed configuration is for a new bucket and the configuration is not specified, the access preview uses `false`. If the proposed configuration is for a new access point or multi-region access point and the access point BPA configuration is not specified, the access preview uses `true`. For more information, see [PublicAccessBlockConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html).

## Contents
<a name="API_S3PublicAccessBlockConfiguration_Contents"></a>

 ** ignorePublicAcls **   <a name="accessanalyzer-Type-S3PublicAccessBlockConfiguration-ignorePublicAcls"></a>
 Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket.
Type: Boolean
Required: Yes

 ** restrictPublicBuckets **   <a name="accessanalyzer-Type-S3PublicAccessBlockConfiguration-restrictPublicBuckets"></a>
 Specifies whether Amazon S3 should restrict public bucket policies for this bucket.
Type: Boolean
Required: Yes

## See Also
<a name="API_S3PublicAccessBlockConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/S3PublicAccessBlockConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/S3PublicAccessBlockConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/S3PublicAccessBlockConfiguration)
