---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_InquirySummary.html
---

# InquirySummary
<a name="API_InquirySummary"></a>

Summary information about a compliance inquiry.

## Contents
<a name="API_InquirySummary_Contents"></a>

 ** arn **   <a name="artifact-Type-InquirySummary-arn"></a>
ARN of the compliance inquiry resource.
Type: String
Required: Yes

 ** createdAt **   <a name="artifact-Type-InquirySummary-createdAt"></a>
Timestamp indicating when the resource was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="artifact-Type-InquirySummary-id"></a>
Unique resource ID for the compliance inquiry.
Type: String
Pattern: `compliance-inquiry-[a-zA-Z0-9]{16}`
Required: Yes

 ** inputSource **   <a name="artifact-Type-InquirySummary-inputSource"></a>
Type of inquiry content (text or file).
Type: String
Valid Values: `TEXT | FILE`
Required: Yes

 ** name **   <a name="artifact-Type-InquirySummary-name"></a>
Title of the inquiry.
Type: String
Required: Yes

 ** status **   <a name="artifact-Type-InquirySummary-status"></a>
Current processing status of the inquiry.
Type: String
Valid Values: `PROCESSING | HUMAN_REVIEW | COMPLETED | FAILED`
Required: Yes

 ** statusMessage **   <a name="artifact-Type-InquirySummary-statusMessage"></a>
Status message providing additional context.
Type: String
Valid Values: `Compliance inquiry processing is complete. | Malware was detected on the file. Provide a new file and try again. | Compliance inquiry processing is in-progress. | An internal error occurred while processing the inquiry. Try again at a later time. | Human review is in progress. | Compliance inquiry processing is complete. One or more queries encountered errors during processing.`
Required: Yes

## See Also
<a name="API_InquirySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/InquirySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/InquirySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/InquirySummary)
