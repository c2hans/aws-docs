---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_FaceSearchSettings.html
---

# FaceSearchSettings
<a name="API_FaceSearchSettings"></a>

Input face recognition parameters for an Amazon Rekognition stream processor. Includes the collection to use for face recognition and the face attributes to detect. Defining the settings is required in the request parameter for [CreateStreamProcessor](API_CreateStreamProcessor.md).

## Contents
<a name="API_FaceSearchSettings_Contents"></a>

 ** CollectionId **   <a name="rekognition-Type-FaceSearchSettings-CollectionId"></a>
The ID of a collection that contains faces that you want to search for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: No

 ** FaceMatchThreshold **   <a name="rekognition-Type-FaceSearchSettings-FaceMatchThreshold"></a>
Minimum face match confidence score that must be met to return a result for a recognized face. The default is 80. 0 is the lowest confidence. 100 is the highest confidence. Values between 0 and 100 are accepted, and values lower than 80 are set to 80.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_FaceSearchSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/FaceSearchSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/FaceSearchSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/FaceSearchSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
