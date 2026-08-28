---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DataProcessingDetails.html
---

# DataProcessingDetails
<a name="API_DataProcessingDetails"></a>

For a Distillation job, the status details for the data processing sub-task of the job.

## Contents
<a name="API_DataProcessingDetails_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-DataProcessingDetails-creationTime"></a>
The start time of the data processing sub-task of the job.
Type: Timestamp
Required: No

 ** lastModifiedTime **   <a name="bedrock-Type-DataProcessingDetails-lastModifiedTime"></a>
The latest update to the data processing sub-task of the job.
Type: Timestamp
Required: No

 ** status **   <a name="bedrock-Type-DataProcessingDetails-status"></a>
The status of the data processing sub-task of the job.
Type: String
Valid Values: `InProgress | Completed | Stopping | Stopped | Failed | NotStarted`
Required: No

## See Also
<a name="API_DataProcessingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DataProcessingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DataProcessingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DataProcessingDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
