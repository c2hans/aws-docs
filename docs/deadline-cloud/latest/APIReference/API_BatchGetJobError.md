---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetJobError.html
---

# BatchGetJobError
<a name="API_BatchGetJobError"></a>

The error details for a job that could not be retrieved in a batch get operation.

## Contents
<a name="API_BatchGetJobError_Contents"></a>

 ** code **   <a name="deadlinecloud-Type-BatchGetJobError-code"></a>
The error code.
Type: String
Valid Values: `InternalServerErrorException | ResourceNotFoundException | ValidationException | AccessDeniedException | ThrottlingException`
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-BatchGetJobError-farmId"></a>
The farm ID of the job that could not be retrieved.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetJobError-jobId"></a>
The job ID of the job that could not be retrieved.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** message **   <a name="deadlinecloud-Type-BatchGetJobError-message"></a>
The error message.
Type: String
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetJobError-queueId"></a>
The queue ID of the job that could not be retrieved.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_BatchGetJobError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetJobError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetJobError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetJobError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
