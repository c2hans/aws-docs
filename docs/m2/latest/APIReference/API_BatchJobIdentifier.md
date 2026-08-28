---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_BatchJobIdentifier.html
---

# BatchJobIdentifier
<a name="API_BatchJobIdentifier"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Identifies a specific batch job.

## Contents
<a name="API_BatchJobIdentifier_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fileBatchJobIdentifier **   <a name="m2-Type-BatchJobIdentifier-fileBatchJobIdentifier"></a>
Specifies a file associated with a specific batch job.
Type: [FileBatchJobIdentifier](API_FileBatchJobIdentifier.md) object
Required: No

 ** restartBatchJobIdentifier **   <a name="m2-Type-BatchJobIdentifier-restartBatchJobIdentifier"></a>
Specifies the required information for restart, including `executionId` and `JobStepRestartMarker`.
Type: [RestartBatchJobIdentifier](API_RestartBatchJobIdentifier.md) object
Required: No

 ** s3BatchJobIdentifier **   <a name="m2-Type-BatchJobIdentifier-s3BatchJobIdentifier"></a>
Specifies an Amazon S3 location that identifies the batch jobs that you want to run. Use this identifier to run ad hoc batch jobs.
Type: [S3BatchJobIdentifier](API_S3BatchJobIdentifier.md) object
Required: No

 ** scriptBatchJobIdentifier **   <a name="m2-Type-BatchJobIdentifier-scriptBatchJobIdentifier"></a>
A batch job identifier in which the batch job to run is identified by the script name.
Type: [ScriptBatchJobIdentifier](API_ScriptBatchJobIdentifier.md) object
Required: No

## See Also
<a name="API_BatchJobIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/BatchJobIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/BatchJobIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/BatchJobIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
