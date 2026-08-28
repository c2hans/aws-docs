---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_PostCallAnalyticsSettings.html
---

# PostCallAnalyticsSettings
<a name="API_media-pipelines-chime_PostCallAnalyticsSettings"></a>

Allows you to specify additional settings for your Call Analytics post-call request, including output locations for your redacted transcript, which IAM role to use, and which encryption key to use.

 `DataAccessRoleArn` and `OutputLocation` are required fields.

 `PostCallAnalyticsSettings` provides the same insights as a Call Analytics post-call transcription. For more information, refer to [Post-call analytics with real-time transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-post-call.html) in the *Amazon Transcribe Developer Guide*.

## Contents
<a name="API_media-pipelines-chime_PostCallAnalyticsSettings_Contents"></a>

 ** DataAccessRoleArn **   <a name="chimesdk-Type-media-pipelines-chime_PostCallAnalyticsSettings-DataAccessRoleArn"></a>
The ARN of the role used by AWS Transcribe to upload your post call analysis. For more information, see [Post-call analytics with real-time transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-post-call.html) in the *Amazon Transcribe Developer Guide*.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `.*`
Required: Yes

 ** OutputLocation **   <a name="chimesdk-Type-media-pipelines-chime_PostCallAnalyticsSettings-OutputLocation"></a>
The URL of the Amazon S3 bucket that contains the post-call data.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `.*`
Required: Yes

 ** ContentRedactionOutput **   <a name="chimesdk-Type-media-pipelines-chime_PostCallAnalyticsSettings-ContentRedactionOutput"></a>
The content redaction output settings for a post-call analysis task.
Type: String
Valid Values: `redacted | redacted_and_unredacted`
Required: No

 ** OutputEncryptionKMSKeyId **   <a name="chimesdk-Type-media-pipelines-chime_PostCallAnalyticsSettings-OutputEncryptionKMSKeyId"></a>
The ID of the KMS (Key Management Service) key used to encrypt the output.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `.*`
Required: No

## See Also
<a name="API_media-pipelines-chime_PostCallAnalyticsSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/PostCallAnalyticsSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/PostCallAnalyticsSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/PostCallAnalyticsSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
