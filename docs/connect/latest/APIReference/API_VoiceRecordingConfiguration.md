---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_VoiceRecordingConfiguration.html
---

# VoiceRecordingConfiguration
<a name="API_VoiceRecordingConfiguration"></a>

Contains information about the recording configuration settings.

## Contents
<a name="API_VoiceRecordingConfiguration_Contents"></a>

 ** IvrRecordingTrack **   <a name="connect-Type-VoiceRecordingConfiguration-IvrRecordingTrack"></a>
Identifies which IVR track is being recorded.
One and only one of the track configurations should be presented in the request.
Type: String
Valid Values: `ALL`
Required: No

 ** VoiceRecordingTrack **   <a name="connect-Type-VoiceRecordingConfiguration-VoiceRecordingTrack"></a>
Identifies which track is being recorded.
Type: String
Valid Values: `FROM_AGENT | TO_AGENT | ALL`
Required: No

## See Also
<a name="API_VoiceRecordingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/VoiceRecordingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/VoiceRecordingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/VoiceRecordingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
