---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_LambdaFunctionScheduledEventAttributes.html
---

# LambdaFunctionScheduledEventAttributes
<a name="API_LambdaFunctionScheduledEventAttributes"></a>

Provides the details of the `LambdaFunctionScheduled` event. It isn't set for other event types.

## Contents
<a name="API_LambdaFunctionScheduledEventAttributes_Contents"></a>

 ** decisionTaskCompletedEventId **   <a name="SWF-Type-LambdaFunctionScheduledEventAttributes-decisionTaskCompletedEventId"></a>
The ID of the `LambdaFunctionCompleted` event corresponding to the decision that resulted in scheduling this activity task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** id **   <a name="SWF-Type-LambdaFunctionScheduledEventAttributes-id"></a>
The unique ID of the Lambda task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** name **   <a name="SWF-Type-LambdaFunctionScheduledEventAttributes-name"></a>
The name of the Lambda function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** control **   <a name="SWF-Type-LambdaFunctionScheduledEventAttributes-control"></a>
Data attached to the event that the decider can use in subsequent workflow tasks. This data isn't sent to the Lambda task.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** input **   <a name="SWF-Type-LambdaFunctionScheduledEventAttributes-input"></a>
The input provided to the Lambda task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Required: No

 ** startToCloseTimeout **   <a name="SWF-Type-LambdaFunctionScheduledEventAttributes-startToCloseTimeout"></a>
The maximum amount of time a worker can take to process the Lambda task.
Type: String
Length Constraints: Maximum length of 8.
Required: No

## See Also
<a name="API_LambdaFunctionScheduledEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/LambdaFunctionScheduledEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/LambdaFunctionScheduledEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/LambdaFunctionScheduledEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
