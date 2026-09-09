---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ActionSummary.html
---

# ActionSummary
<a name="API_ActionSummary"></a>

Lists the properties of an *action*. An action represents an action or activity. Some examples are a workflow step and a model deployment. Generally, an action involves at least one input artifact or output artifact.

## Contents
<a name="API_ActionSummary_Contents"></a>

 ** ActionArn **   <a name="sagemaker-Type-ActionSummary-ActionArn"></a>
The Amazon Resource Name (ARN) of the action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:action/.*`
Required: No

 ** ActionName **   <a name="sagemaker-Type-ActionSummary-ActionName"></a>
The name of the action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** ActionType **   <a name="sagemaker-Type-ActionSummary-ActionType"></a>
The type of the action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** Source **   <a name="sagemaker-Type-ActionSummary-Source"></a>
The source of the action.
Type: [ActionSource](API_ActionSource.md) object
Required: No

 ** Status **   <a name="sagemaker-Type-ActionSummary-Status"></a>
The status of the action.
Type: String
Valid Values: `Unknown | InProgress | Completed | Failed | Stopping | Stopped`
Required: No

## See Also
<a name="API_ActionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ActionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ActionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ActionSummary)
