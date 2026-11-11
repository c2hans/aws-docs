---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExtensionSummary.html
---

# ExtensionSummary
<a name="API_ExtensionSummary"></a>

A summary of an extension installed on a SageMaker HyperPod cluster.

## Contents
<a name="API_ExtensionSummary_Contents"></a>

 ** ExtensionArn **   <a name="sagemaker-Type-ExtensionSummary-ExtensionArn"></a>
The Amazon Resource Name (ARN) of the extension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:extension/(sagemaker|eks|pcs)-[a-z0-9-]+/[a-z0-9-]+/[a-z0-9]+`
Required: Yes

 ** ExtensionName **   <a name="sagemaker-Type-ExtensionSummary-ExtensionName"></a>
The name of the extension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-z]([a-z0-9]|-[a-z0-9])*`
Required: Yes

 ** ExtensionVersion **   <a name="sagemaker-Type-ExtensionSummary-ExtensionVersion"></a>
The version of the extension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9]+\.[0-9]+\.[0-9]+`
Required: Yes

 ** Status **   <a name="sagemaker-Type-ExtensionSummary-Status"></a>
The status of the extension. For the meaning of each status, see `ExtensionDetails`.
Type: String
Valid Values: `Creating | Active | CreateFailed | Updating | Deleting | DeleteFailed | Degraded | UpdateFailed`
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-ExtensionSummary-CreationTime"></a>
The time when the extension was created.
Type: Timestamp
Required: No

## See Also
<a name="API_ExtensionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ExtensionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ExtensionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ExtensionSummary)
