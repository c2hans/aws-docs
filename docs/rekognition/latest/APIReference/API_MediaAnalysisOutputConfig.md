---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_MediaAnalysisOutputConfig.html
---

# MediaAnalysisOutputConfig
<a name="API_MediaAnalysisOutputConfig"></a>

Output configuration provided in the job creation request.

## Contents
<a name="API_MediaAnalysisOutputConfig_Contents"></a>

 ** S3Bucket **   <a name="rekognition-Type-MediaAnalysisOutputConfig-S3Bucket"></a>
Specifies the Amazon S3 bucket to contain the output of the media analysis job.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[0-9A-Za-z\.\-_]*`
Required: Yes

 ** S3KeyPrefix **   <a name="rekognition-Type-MediaAnalysisOutputConfig-S3KeyPrefix"></a>
Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for storage.
Type: String
Length Constraints: Maximum length of 800.
Pattern: `\S*`
Required: No

## See Also
<a name="API_MediaAnalysisOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/MediaAnalysisOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/MediaAnalysisOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/MediaAnalysisOutputConfig)
