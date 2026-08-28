---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeInputStream.html
---

# MedicalScribeInputStream
<a name="API_streaming_MedicalScribeInputStream"></a>

An encoded stream of events. The stream is encoded as HTTP/2 data frames.

An input stream consists of the following types of events. The first element of the input stream must be the `MedicalScribeConfigurationEvent` event type.
+  `MedicalScribeConfigurationEvent`
+  `MedicalScribeAudioEvent`
+  `MedicalScribeSessionControlEvent`

## Contents
<a name="API_streaming_MedicalScribeInputStream_Contents"></a>

 ** AudioEvent **   <a name="transcribe-Type-streaming_MedicalScribeInputStream-AudioEvent"></a>
A wrapper for your audio chunks
For more information, see [Event stream encoding](https://docs.aws.amazon.com/transcribe/latest/dg/event-stream.html).
Type: [MedicalScribeAudioEvent](API_streaming_MedicalScribeAudioEvent.md) object
Required: No

 ** ConfigurationEvent **   <a name="transcribe-Type-streaming_MedicalScribeInputStream-ConfigurationEvent"></a>
Specify additional streaming session configurations beyond those provided in your initial start request headers. For example, specify channel definitions, encryption settings, and post-stream analytics settings.
Whether you are starting a new session or resuming an existing session, your first event must be a `MedicalScribeConfigurationEvent`.
Type: [MedicalScribeConfigurationEvent](API_streaming_MedicalScribeConfigurationEvent.md) object
Required: No

 ** SessionControlEvent **   <a name="transcribe-Type-streaming_MedicalScribeInputStream-SessionControlEvent"></a>
Specify the lifecycle of your streaming session, such as ending the session.
Type: [MedicalScribeSessionControlEvent](API_streaming_MedicalScribeSessionControlEvent.md) object
Required: No

## See Also
<a name="API_streaming_MedicalScribeInputStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalScribeInputStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalScribeInputStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalScribeInputStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
