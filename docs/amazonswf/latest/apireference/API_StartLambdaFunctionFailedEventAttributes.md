---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartLambdaFunctionFailedEventAttributes.html
---

# StartLambdaFunctionFailedEventAttributes
<a name="API_StartLambdaFunctionFailedEventAttributes"></a>

Provides the details of the `StartLambdaFunctionFailed` event. It isn't set for other event types.

## Contents
<a name="API_StartLambdaFunctionFailedEventAttributes_Contents"></a>

 ** cause **   <a name="SWF-Type-StartLambdaFunctionFailedEventAttributes-cause"></a>
The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
If `cause` is set to `OPERATION_NOT_PERMITTED`, the decision failed because the IAM role attached to the execution lacked sufficient permissions. For details and example IAM policies, see [Lambda Tasks](https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html) in the *Amazon SWF Developer Guide*.
Type: String
Valid Values: `ASSUME_ROLE_FAILED`
Required: No

 ** message **   <a name="SWF-Type-StartLambdaFunctionFailedEventAttributes-message"></a>
A description that can help diagnose the cause of the fault.
Type: String
Length Constraints: Maximum length of 1728.
Required: No

 ** scheduledEventId **   <a name="SWF-Type-StartLambdaFunctionFailedEventAttributes-scheduledEventId"></a>
The ID of the `ActivityTaskScheduled` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
Type: Long
Required: No

## See Also
<a name="API_StartLambdaFunctionFailedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/StartLambdaFunctionFailedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/StartLambdaFunctionFailedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/StartLambdaFunctionFailedEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
