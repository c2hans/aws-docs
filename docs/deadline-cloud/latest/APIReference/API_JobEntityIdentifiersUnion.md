---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_JobEntityIdentifiersUnion.html
---

# JobEntityIdentifiersUnion
<a name="API_JobEntityIdentifiersUnion"></a>

The details of a job entity identifier.

## Contents
<a name="API_JobEntityIdentifiersUnion_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** environmentDetails **   <a name="deadlinecloud-Type-JobEntityIdentifiersUnion-environmentDetails"></a>
The environment details.
Type: [EnvironmentDetailsIdentifiers](API_EnvironmentDetailsIdentifiers.md) object
Required: No

 ** jobAttachmentDetails **   <a name="deadlinecloud-Type-JobEntityIdentifiersUnion-jobAttachmentDetails"></a>
The job attachment details.
Type: [JobAttachmentDetailsIdentifiers](API_JobAttachmentDetailsIdentifiers.md) object
Required: No

 ** jobDetails **   <a name="deadlinecloud-Type-JobEntityIdentifiersUnion-jobDetails"></a>
The job details.
Type: [JobDetailsIdentifiers](API_JobDetailsIdentifiers.md) object
Required: No

 ** stepDetails **   <a name="deadlinecloud-Type-JobEntityIdentifiersUnion-stepDetails"></a>
The step details.
Type: [StepDetailsIdentifiers](API_StepDetailsIdentifiers.md) object
Required: No

## See Also
<a name="API_JobEntityIdentifiersUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobEntityIdentifiersUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobEntityIdentifiersUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobEntityIdentifiersUnion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
