---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartTimerDecisionAttributes.html
---

# StartTimerDecisionAttributes
<a name="API_StartTimerDecisionAttributes"></a>

Provides the details of the `StartTimer` decision.

 **Access Control**

You can use IAM policies to control this decision's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ You cannot use an IAM policy to constrain this action's parameters.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Contents
<a name="API_StartTimerDecisionAttributes_Contents"></a>

 ** startToFireTimeout **   <a name="SWF-Type-StartTimerDecisionAttributes-startToFireTimeout"></a>
 The duration to wait before firing the timer.
The duration is specified in seconds, an integer greater than or equal to `0`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Required: Yes

 ** timerId **   <a name="SWF-Type-StartTimerDecisionAttributes-timerId"></a>
 The unique ID of the timer.
The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` \| `\u007f-\u009f`). Also, it must *not* be the literal string `arn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** control **   <a name="SWF-Type-StartTimerDecisionAttributes-control"></a>
The data attached to the event that can be used by the decider in subsequent workflow tasks.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

## See Also
<a name="API_StartTimerDecisionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/StartTimerDecisionAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/StartTimerDecisionAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/StartTimerDecisionAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
