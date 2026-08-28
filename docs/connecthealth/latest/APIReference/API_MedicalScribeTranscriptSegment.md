---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeTranscriptSegment.html
---

# MedicalScribeTranscriptSegment
<a name="API_MedicalScribeTranscriptSegment"></a>

A segment of transcript text with timing and channel information

## Contents
<a name="API_MedicalScribeTranscriptSegment_Contents"></a>

 ** audioBeginOffset **   <a name="connecthealth-Type-MedicalScribeTranscriptSegment-audioBeginOffset"></a>
The offset from audio start when the audio for this segment begins
Type: Double
Required: No

 ** audioEndOffset **   <a name="connecthealth-Type-MedicalScribeTranscriptSegment-audioEndOffset"></a>
The offset from audio start when the audio for this segment ends
Type: Double
Required: No

 ** channelId **   <a name="connecthealth-Type-MedicalScribeTranscriptSegment-channelId"></a>
The channel identifier for this segment
Type: String
Required: No

 ** content **   <a name="connecthealth-Type-MedicalScribeTranscriptSegment-content"></a>
The transcript text content
Type: String
Required: No

 ** isPartial **   <a name="connecthealth-Type-MedicalScribeTranscriptSegment-isPartial"></a>
Indicates whether this is a partial or final transcript
Type: Boolean
Required: No

 ** segmentId **   <a name="connecthealth-Type-MedicalScribeTranscriptSegment-segmentId"></a>
The unique identifier for this segment
Type: String
Required: No

## See Also
<a name="API_MedicalScribeTranscriptSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalScribeTranscriptSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalScribeTranscriptSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalScribeTranscriptSegment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
