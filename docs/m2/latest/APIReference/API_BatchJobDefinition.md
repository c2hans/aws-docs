---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_BatchJobDefinition.html
---

# BatchJobDefinition
<a name="API_BatchJobDefinition"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Defines the details of a batch job.

## Contents
<a name="API_BatchJobDefinition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fileBatchJobDefinition **   <a name="m2-Type-BatchJobDefinition-fileBatchJobDefinition"></a>
Specifies a file containing a batch job definition.
Type: [FileBatchJobDefinition](API_FileBatchJobDefinition.md) object
Required: No

 ** scriptBatchJobDefinition **   <a name="m2-Type-BatchJobDefinition-scriptBatchJobDefinition"></a>
A script containing a batch job definition.
Type: [ScriptBatchJobDefinition](API_ScriptBatchJobDefinition.md) object
Required: No

## See Also
<a name="API_BatchJobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/BatchJobDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/BatchJobDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/BatchJobDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
