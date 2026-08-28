---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ConnectedHomeSettingsForUpdate.html
---

# ConnectedHomeSettingsForUpdate
<a name="API_ConnectedHomeSettingsForUpdate"></a>

 The label detection settings you want to use in your stream processor. This includes the labels you want the stream processor to detect and the minimum confidence level allowed to label objects.

## Contents
<a name="API_ConnectedHomeSettingsForUpdate_Contents"></a>

 ** Labels **   <a name="rekognition-Type-ConnectedHomeSettingsForUpdate-Labels"></a>
 Specifies what you want to detect in the video, such as people, packages, or pets. The current valid labels you can include in this list are: "PERSON", "PET", "PACKAGE", and "ALL".
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 128 items.
Required: No

 ** MinConfidence **   <a name="rekognition-Type-ConnectedHomeSettingsForUpdate-MinConfidence"></a>
 The minimum confidence required to label an object in the video.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_ConnectedHomeSettingsForUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ConnectedHomeSettingsForUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ConnectedHomeSettingsForUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ConnectedHomeSettingsForUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
