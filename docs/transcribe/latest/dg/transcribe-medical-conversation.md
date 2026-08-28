---
source_url: https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-medical-conversation.html
---

# Transcribing a medical conversation
<a name="transcribe-medical-conversation"></a>

You can use Amazon Transcribe Medical to transcribe a medical conversation between a clinician and a patient using either a batch transcription job or a real-time stream. Batch transcription jobs enable you to transcribe audio files. To ensure that Amazon Transcribe Medical produces transcription results with the highest possible accuracy, you must specify the medical specialty of the clinician in your transcription job or stream.

You can transcribe a clinician-patient visit in the following medical specialities:
+ Cardiology – available in streaming transcription only
+ Neurology – available in streaming transcription only
+ Oncology – available in streaming transcription only
+ Primary Care – includes the following types of medical practice:
  + Family medicine
  + Internal medicine
  + Obstetrics and Gynecology (OB-GYN)
  + Pediatrics
+ Urology – available in streaming transcription only

You can improve transcription accuracy by using medical custom vocabularies. For information on how medical custom vocabularies work, see [Improving transcription accuracy with medical custom vocabularies](vocabulary-med.md).

By default, Amazon Transcribe Medical returns the transcription with the highest confidence level. If you'd like to configure it to return alternative transcriptions, see [Generating alternative transcriptions](alternative-med-transcriptions.md).

For information about how numbers and medical measurements appear in the transcription output, see [Transcribing numbers](how-numbers-med.md) and [Transcribing medical terms and measurements](how-measurements-med.md).

**Topics**
+ [Transcribing an audio file of a medical conversation](batch-medical-conversation.md)
+ [Transcribing a medical conversation in a real-time stream](streaming-medical-conversation.md)
+ [Enabling speaker partitioning](conversation-diarization-med.md)
+ [Transcribing multi-channel audio](conversation-channel-id-med.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
