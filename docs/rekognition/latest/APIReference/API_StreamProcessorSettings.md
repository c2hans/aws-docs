---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorSettings.html
---

# StreamProcessorSettings
<a name="API_StreamProcessorSettings"></a>

Input parameters used in a streaming video analyzed by a Amazon Rekognition stream processor. You can use `FaceSearch` to recognize faces in a streaming video, or you can use `ConnectedHome` to detect labels.

## Contents
<a name="API_StreamProcessorSettings_Contents"></a>

 ** ConnectedHome **   <a name="rekognition-Type-StreamProcessorSettings-ConnectedHome"></a>
 Label detection settings to use on a streaming video. Defining the settings is required in the request parameter for [CreateStreamProcessor](API_CreateStreamProcessor.md). Including this setting in the `CreateStreamProcessor` request enables you to use the stream processor for label detection. You can then select what you want the stream processor to detect, such as people or pets. When the stream processor has started, one notification is sent for each object class specified. For example, if packages and pets are selected, one SNS notification is published the first time a package is detected and one SNS notification is published the first time a pet is detected, as well as an end-of-session summary.
Type: [ConnectedHomeSettings](API_ConnectedHomeSettings.md) object
Required: No

 ** FaceSearch **   <a name="rekognition-Type-StreamProcessorSettings-FaceSearch"></a>
Face search settings to use on a streaming video.
Type: [FaceSearchSettings](API_FaceSearchSettings.md) object
Required: No

## See Also
<a name="API_StreamProcessorSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StreamProcessorSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StreamProcessorSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StreamProcessorSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
