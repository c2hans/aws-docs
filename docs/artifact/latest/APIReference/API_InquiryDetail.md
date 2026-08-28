---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_InquiryDetail.html
---

# InquiryDetail
<a name="API_InquiryDetail"></a>

Detailed information about a compliance inquiry.

## Contents
<a name="API_InquiryDetail_Contents"></a>

 ** arn **   <a name="artifact-Type-InquiryDetail-arn"></a>
ARN of the compliance inquiry resource.
Type: String
Required: Yes

 ** createdAt **   <a name="artifact-Type-InquiryDetail-createdAt"></a>
Timestamp indicating when the resource was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="artifact-Type-InquiryDetail-id"></a>
Unique resource ID for the compliance inquiry.
Type: String
Pattern: `compliance-inquiry-[a-zA-Z0-9]{16}`
Required: Yes

 ** inputSource **   <a name="artifact-Type-InquiryDetail-inputSource"></a>
Type of inquiry content (text or file).
Type: String
Valid Values: `TEXT | FILE`
Required: Yes

 ** name **   <a name="artifact-Type-InquiryDetail-name"></a>
Title of the inquiry.
Type: String
Required: Yes

 ** status **   <a name="artifact-Type-InquiryDetail-status"></a>
Current processing status of the inquiry.
Type: String
Valid Values: `PROCESSING | HUMAN_REVIEW | COMPLETED | FAILED`
Required: Yes

 ** statusMessage **   <a name="artifact-Type-InquiryDetail-statusMessage"></a>
Status message providing additional context.
Type: String
Valid Values: `Compliance inquiry processing is complete. | Malware was detected on the file. Provide a new file and try again. | Compliance inquiry processing is in-progress. | An internal error occurred while processing the inquiry. Try again at a later time. | Human review is in progress. | Compliance inquiry processing is complete. One or more queries encountered errors during processing.`
Required: Yes

 ** supportMode **   <a name="artifact-Type-InquiryDetail-supportMode"></a>
Support mode for this inquiry. AI\_ONLY provides AI-generated responses. FULL\_SUPPORT includes human expert review.
Type: String
Valid Values: `AI_ONLY | FULL_SUPPORT`
Required: No

 ** updatedAt **   <a name="artifact-Type-InquiryDetail-updatedAt"></a>
Timestamp indicating when the resource was last modified.
Type: Timestamp
Required: No

## See Also
<a name="API_InquiryDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/InquiryDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/InquiryDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/InquiryDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Artifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query artifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
