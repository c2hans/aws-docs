---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExtensionHealthIssue.html
---

# ExtensionHealthIssue
<a name="API_ExtensionHealthIssue"></a>

Information about a problem that affects an extension on one or more nodes of a SageMaker HyperPod cluster, including the number of nodes that it affects.

## Contents
<a name="API_ExtensionHealthIssue_Contents"></a>

 ** Code **   <a name="sagemaker-Type-ExtensionHealthIssue-Code"></a>
A code that describes the type of issue.
Type: String
Valid Values: `InvalidConfiguration | ConfigurationConflict | AccessDenied | ResourceNotFound | DependencyUnreachable | ExtensionUnhealthy | InternalFailure | Other`
Required: Yes

 ** Message **   <a name="sagemaker-Type-ExtensionHealthIssue-Message"></a>
A description of the problem, for example the setting or component to check. Every node with the same problem has the same message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** NodeCount **   <a name="sagemaker-Type-ExtensionHealthIssue-NodeCount"></a>
The number of nodes that have this problem.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_ExtensionHealthIssue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ExtensionHealthIssue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ExtensionHealthIssue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ExtensionHealthIssue)
