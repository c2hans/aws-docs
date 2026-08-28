---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_RestartBatchJobIdentifier.html
---

# RestartBatchJobIdentifier
<a name="API_RestartBatchJobIdentifier"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

An identifier for the `StartBatchJob` API to show that it is a restart operation.

## Contents
<a name="API_RestartBatchJobIdentifier_Contents"></a>

 ** executionId **   <a name="m2-Type-RestartBatchJobIdentifier-executionId"></a>
The `executionId` from the `StartBatchJob` response when the job ran for the first time.
Type: String
Pattern: `\S{1,80}`
Required: Yes

 ** jobStepRestartMarker **   <a name="m2-Type-RestartBatchJobIdentifier-jobStepRestartMarker"></a>
The step/procedure step information for a restart batch job operation.
Type: [JobStepRestartMarker](API_JobStepRestartMarker.md) object
Required: Yes

## See Also
<a name="API_RestartBatchJobIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/RestartBatchJobIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/RestartBatchJobIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/RestartBatchJobIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
