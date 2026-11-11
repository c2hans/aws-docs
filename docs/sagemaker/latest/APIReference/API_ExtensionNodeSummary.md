---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExtensionNodeSummary.html
---

# ExtensionNodeSummary
<a name="API_ExtensionNodeSummary"></a>

A summary of an extension's installation across the nodes of a SageMaker HyperPod cluster.

## Contents
<a name="API_ExtensionNodeSummary_Contents"></a>

 ** ActiveCount **   <a name="sagemaker-Type-ExtensionNodeSummary-ActiveCount"></a>
The number of nodes that are running the extension's current version and configuration. While SageMaker HyperPod creates or updates the extension, `ActiveCount` is lower than `TotalCount`.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** TotalCount **   <a name="sagemaker-Type-ExtensionNodeSummary-TotalCount"></a>
The number of nodes in your cluster that the extension targets. SageMaker HyperPod targets every running node in your cluster, including nodes that you add after you create the extension.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_ExtensionNodeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ExtensionNodeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ExtensionNodeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ExtensionNodeSummary)
