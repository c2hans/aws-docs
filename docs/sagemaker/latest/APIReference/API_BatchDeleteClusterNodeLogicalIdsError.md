---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchDeleteClusterNodeLogicalIdsError.html
---

# BatchDeleteClusterNodeLogicalIdsError
<a name="API_BatchDeleteClusterNodeLogicalIdsError"></a>

Information about an error that occurred when attempting to delete a node identified by its `NodeLogicalId`.

## Contents
<a name="API_BatchDeleteClusterNodeLogicalIdsError_Contents"></a>

 ** Code **   <a name="sagemaker-Type-BatchDeleteClusterNodeLogicalIdsError-Code"></a>
The error code associated with the failure. Possible values include `NodeLogicalIdNotFound`, `InvalidNodeStatus`, and `InternalError`.
Type: String
Valid Values: `NodeIdNotFound | InvalidNodeStatus | NodeIdInUse`
Required: Yes

 ** Message **   <a name="sagemaker-Type-BatchDeleteClusterNodeLogicalIdsError-Message"></a>
A descriptive message providing additional details about the error.
Type: String
Required: Yes

 ** NodeLogicalId **   <a name="sagemaker-Type-BatchDeleteClusterNodeLogicalIdsError-NodeLogicalId"></a>
The `NodeLogicalId` of the node that could not be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`
Required: Yes

## See Also
<a name="API_BatchDeleteClusterNodeLogicalIdsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BatchDeleteClusterNodeLogicalIdsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BatchDeleteClusterNodeLogicalIdsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BatchDeleteClusterNodeLogicalIdsError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
