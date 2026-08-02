---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_S3DestinationConfig.html
---

# S3DestinationConfig
<a name="API_S3DestinationConfig"></a>

Configuration parameters for where in an S3 bucket to place the harvested content.

## Contents
<a name="API_S3DestinationConfig_Contents"></a>

 ** BucketName **   <a name="mediapackage-Type-S3DestinationConfig-BucketName"></a>
The name of an S3 bucket within which harvested content will be exported.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** DestinationPath **   <a name="mediapackage-Type-S3DestinationConfig-DestinationPath"></a>
The path within the specified S3 bucket where the harvested content will be placed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S]+`
Required: Yes

## See Also
<a name="API_S3DestinationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/S3DestinationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/S3DestinationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/S3DestinationConfig)
