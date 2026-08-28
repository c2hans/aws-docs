---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetJobEntityError.html
---

# GetJobEntityError
<a name="API_GetJobEntityError"></a>

The error for the job entity.

## Contents
<a name="API_GetJobEntityError_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** environmentDetails **   <a name="deadlinecloud-Type-GetJobEntityError-environmentDetails"></a>
The environment details for the failed job entity.
Type: [EnvironmentDetailsError](API_EnvironmentDetailsError.md) object
Required: No

 ** jobAttachmentDetails **   <a name="deadlinecloud-Type-GetJobEntityError-jobAttachmentDetails"></a>
The job attachment details for the failed job entity.
Type: [JobAttachmentDetailsError](API_JobAttachmentDetailsError.md) object
Required: No

 ** jobDetails **   <a name="deadlinecloud-Type-GetJobEntityError-jobDetails"></a>
The job details for the failed job entity.
Type: [JobDetailsError](API_JobDetailsError.md) object
Required: No

 ** stepDetails **   <a name="deadlinecloud-Type-GetJobEntityError-stepDetails"></a>
The step details for the failed job entity.
Type: [StepDetailsError](API_StepDetailsError.md) object
Required: No

## See Also
<a name="API_GetJobEntityError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetJobEntityError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetJobEntityError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetJobEntityError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
