---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ScheduleLambdaFunctionFailedEventAttributes.html
---

# ScheduleLambdaFunctionFailedEventAttributes
<a name="API_ScheduleLambdaFunctionFailedEventAttributes"></a>

Provides the details of the `ScheduleLambdaFunctionFailed` event. It isn't set for other event types.

## Contents
<a name="API_ScheduleLambdaFunctionFailedEventAttributes_Contents"></a>

 ** cause **   <a name="SWF-Type-ScheduleLambdaFunctionFailedEventAttributes-cause"></a>
The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.
Type: String
Valid Values: `ID_ALREADY_IN_USE | OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED | LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED | LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION`
Required: Yes

 ** decisionTaskCompletedEventId **   <a name="SWF-Type-ScheduleLambdaFunctionFailedEventAttributes-decisionTaskCompletedEventId"></a>
The ID of the `LambdaFunctionCompleted` event corresponding to the decision that resulted in scheduling this Lambda task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** id **   <a name="SWF-Type-ScheduleLambdaFunctionFailedEventAttributes-id"></a>
The ID provided in the `ScheduleLambdaFunction` decision that failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** name **   <a name="SWF-Type-ScheduleLambdaFunctionFailedEventAttributes-name"></a>
The name of the Lambda function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_ScheduleLambdaFunctionFailedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ScheduleLambdaFunctionFailedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ScheduleLambdaFunctionFailedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ScheduleLambdaFunctionFailedEventAttributes)
