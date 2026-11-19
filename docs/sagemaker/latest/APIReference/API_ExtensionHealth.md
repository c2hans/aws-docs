---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExtensionHealth.html
---

# ExtensionHealth

Contains information about the problems that affect an extension on the nodes of a SageMaker HyperPod cluster, including how many nodes each problem affects. `DescribeClusterExtension` returns `ExtensionHealth` only when at least one node has a problem.

## Contents
<a name="API_ExtensionHealth_Contents"></a>

 ** Issues **   <a name="sagemaker-Type-ExtensionHealth-Issues"></a>
The problems that affect the extension, grouped by cause, from the problem that affects the most nodes to the one that affects the fewest. SageMaker HyperPod counts each node in at most one issue. The list contains at most 20 issues. If more than 20 different problems exist, the list shows the 19 that affect the most nodes, and the 20th issue has the code `Other` and counts the nodes that the remaining problems affect.
Type: Array of [ExtensionHealthIssue](API_ExtensionHealthIssue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

## See Also
<a name="API_ExtensionHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ExtensionHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ExtensionHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ExtensionHealth)
