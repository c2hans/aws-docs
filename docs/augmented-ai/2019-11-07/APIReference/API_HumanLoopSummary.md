---
source_url: https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_HumanLoopSummary.html
---

# HumanLoopSummary
<a name="API_HumanLoopSummary"></a>

Summary information about the human loop.

## Contents
<a name="API_HumanLoopSummary_Contents"></a>

 ** CreationTime **   <a name="augmentedai-Type-HumanLoopSummary-CreationTime"></a>
When Amazon Augmented AI created the human loop.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="augmentedai-Type-HumanLoopSummary-FailureReason"></a>
The reason why the human loop failed. A failure reason is returned when the status of the human loop is `Failed`.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** FlowDefinitionArn **   <a name="augmentedai-Type-HumanLoopSummary-FlowDefinitionArn"></a>
The Amazon Resource Name (ARN) of the flow definition used to configure the human loop.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:flow-definition/.*`
Required: No

 ** HumanLoopName **   <a name="augmentedai-Type-HumanLoopSummary-HumanLoopName"></a>
The name of the human loop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](-*[a-z0-9])*$`
Required: No

 ** HumanLoopStatus **   <a name="augmentedai-Type-HumanLoopSummary-HumanLoopStatus"></a>
The status of the human loop.
Type: String
Valid Values: `InProgress | Failed | Completed | Stopped | Stopping`
Required: No

## See Also
<a name="API_HumanLoopSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-a2i-runtime-2019-11-07/HumanLoopSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-a2i-runtime-2019-11-07/HumanLoopSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-a2i-runtime-2019-11-07/HumanLoopSummary)
