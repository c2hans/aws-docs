---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_JobAttachmentDetailsError.html
---

# JobAttachmentDetailsError
<a name="API_JobAttachmentDetailsError"></a>

The error details for job attachments.

## Contents
<a name="API_JobAttachmentDetailsError_Contents"></a>

 ** code **   <a name="deadlinecloud-Type-JobAttachmentDetailsError-code"></a>
The error code.
Type: String
Valid Values: `AccessDeniedException | InternalServerException | ValidationException | ResourceNotFoundException | MaxPayloadSizeExceeded | ConflictException`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-JobAttachmentDetailsError-jobId"></a>
The job ID.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** message **   <a name="deadlinecloud-Type-JobAttachmentDetailsError-message"></a>
The error message detailing the error's cause.
Type: String
Required: Yes

## See Also
<a name="API_JobAttachmentDetailsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobAttachmentDetailsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobAttachmentDetailsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobAttachmentDetailsError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
