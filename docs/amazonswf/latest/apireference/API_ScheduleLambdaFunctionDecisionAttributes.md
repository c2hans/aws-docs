---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ScheduleLambdaFunctionDecisionAttributes.html
---

# ScheduleLambdaFunctionDecisionAttributes
<a name="API_ScheduleLambdaFunctionDecisionAttributes"></a>

Decision attributes specified in `scheduleLambdaFunctionDecisionAttributes` within the list of decisions `decisions` passed to [RespondDecisionTaskCompleted](API_RespondDecisionTaskCompleted.md).

## Contents
<a name="API_ScheduleLambdaFunctionDecisionAttributes_Contents"></a>

 ** id **   <a name="SWF-Type-ScheduleLambdaFunctionDecisionAttributes-id"></a>
A string that identifies the Lambda function execution in the event history.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** name **   <a name="SWF-Type-ScheduleLambdaFunctionDecisionAttributes-name"></a>
The name, or ARN, of the Lambda function to schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** control **   <a name="SWF-Type-ScheduleLambdaFunctionDecisionAttributes-control"></a>
The data attached to the event that the decider can use in subsequent workflow tasks. This data isn't sent to the Lambda task.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** input **   <a name="SWF-Type-ScheduleLambdaFunctionDecisionAttributes-input"></a>
The optional input data to be supplied to the Lambda function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Required: No

 ** startToCloseTimeout **   <a name="SWF-Type-ScheduleLambdaFunctionDecisionAttributes-startToCloseTimeout"></a>
The timeout value, in seconds, after which the Lambda function is considered to be failed once it has started. This can be any integer from 1-900 (1s-15m).
If no value is supplied, then a default value of 300s is assumed.
Type: String
Length Constraints: Maximum length of 8.
Required: No

## See Also
<a name="API_ScheduleLambdaFunctionDecisionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ScheduleLambdaFunctionDecisionAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ScheduleLambdaFunctionDecisionAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ScheduleLambdaFunctionDecisionAttributes)
