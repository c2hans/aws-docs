---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_ClinicalNoteGenerationResult.html
---

# ClinicalNoteGenerationResult
<a name="API_streaming_ClinicalNoteGenerationResult"></a>

The details for clinical note generation, including status, and output locations for clinical note and aggregated transcript if the analytics completed, or failure reason if the analytics failed.

## Contents
<a name="API_streaming_ClinicalNoteGenerationResult_Contents"></a>

 ** ClinicalNoteOutputLocation **   <a name="transcribe-Type-streaming_ClinicalNoteGenerationResult-ClinicalNoteOutputLocation"></a>
Holds the Amazon S3 URI for the output Clinical Note.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(s3://|http(s*)://).+`
Required: No

 ** FailureReason **   <a name="transcribe-Type-streaming_ClinicalNoteGenerationResult-FailureReason"></a>
If `ClinicalNoteGenerationResult` is `FAILED`, information about why it failed.
Type: String
Required: No

 ** Status **   <a name="transcribe-Type-streaming_ClinicalNoteGenerationResult-Status"></a>
The status of the clinical note generation.
Possible Values:
+  `IN_PROGRESS`
+  `FAILED`
+  `COMPLETED`
 After audio streaming finishes, and you send a `MedicalScribeSessionControlEvent` event (with END\_OF\_SESSION as the Type), the status is set to `IN_PROGRESS`. If the status is `COMPLETED`, the analytics completed successfully, and you can find the results at the locations specified in `ClinicalNoteOutputLocation` and `TranscriptOutputLocation`. If the status is `FAILED`, `FailureReason` provides details about the failure.
Type: String
Valid Values: `IN_PROGRESS | FAILED | COMPLETED`
Required: No

 ** TranscriptOutputLocation **   <a name="transcribe-Type-streaming_ClinicalNoteGenerationResult-TranscriptOutputLocation"></a>
Holds the Amazon S3 URI for the output Transcript.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(s3://|http(s*)://).+`
Required: No

## See Also
<a name="API_streaming_ClinicalNoteGenerationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/ClinicalNoteGenerationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/ClinicalNoteGenerationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/ClinicalNoteGenerationResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
