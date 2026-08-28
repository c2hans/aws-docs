---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ConnectedHomeSettings.html
---

# ConnectedHomeSettings
<a name="API_ConnectedHomeSettings"></a>

 Label detection settings to use on a streaming video. Defining the settings is required in the request parameter for [CreateStreamProcessor](API_CreateStreamProcessor.md). Including this setting in the `CreateStreamProcessor` request enables you to use the stream processor for label detection. You can then select what you want the stream processor to detect, such as people or pets. When the stream processor has started, one notification is sent for each object class specified. For example, if packages and pets are selected, one SNS notification is published the first time a package is detected and one SNS notification is published the first time a pet is detected, as well as an end-of-session summary.

## Contents
<a name="API_ConnectedHomeSettings_Contents"></a>

 ** Labels **   <a name="rekognition-Type-ConnectedHomeSettings-Labels"></a>
 Specifies what you want to detect in the video, such as people, packages, or pets. The current valid labels you can include in this list are: "PERSON", "PET", "PACKAGE", and "ALL".
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 128 items.
Required: Yes

 ** MinConfidence **   <a name="rekognition-Type-ConnectedHomeSettings-MinConfidence"></a>
 The minimum confidence required to label an object in the video.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_ConnectedHomeSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ConnectedHomeSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ConnectedHomeSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ConnectedHomeSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
