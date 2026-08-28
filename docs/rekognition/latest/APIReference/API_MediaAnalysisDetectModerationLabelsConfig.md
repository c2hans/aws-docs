---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_MediaAnalysisDetectModerationLabelsConfig.html
---

# MediaAnalysisDetectModerationLabelsConfig
<a name="API_MediaAnalysisDetectModerationLabelsConfig"></a>

Configuration for Moderation Labels Detection.

## Contents
<a name="API_MediaAnalysisDetectModerationLabelsConfig_Contents"></a>

 ** MinConfidence **   <a name="rekognition-Type-MediaAnalysisDetectModerationLabelsConfig-MinConfidence"></a>
Specifies the minimum confidence level for the moderation labels to return. Amazon Rekognition doesn't return any labels with a confidence level lower than this specified value.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** ProjectVersion **   <a name="rekognition-Type-MediaAnalysisDetectModerationLabelsConfig-ProjectVersion"></a>
Specifies the custom moderation model to be used during the label detection job. If not provided the pre-trained model is used.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/version\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: No

## See Also
<a name="API_MediaAnalysisDetectModerationLabelsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/MediaAnalysisDetectModerationLabelsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/MediaAnalysisDetectModerationLabelsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/MediaAnalysisDetectModerationLabelsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
