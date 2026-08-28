---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CancelReplay.html
---

# CancelReplay
<a name="API_CancelReplay"></a>

Cancels the specified replay.

## Request Syntax
<a name="API_CancelReplay_RequestSyntax"></a>

```
{
   "ReplayName": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelReplay_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReplayName](#API_CancelReplay_RequestSyntax) **   <a name="eventbridge-CancelReplay-request-ReplayName"></a>
The name of the replay to cancel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_CancelReplay_ResponseSyntax"></a>

```
{
   "ReplayArn": "string",
   "State": "string",
   "StateReason": "string"
}
```

## Response Elements
<a name="API_CancelReplay_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplayArn](#API_CancelReplay_ResponseSyntax) **   <a name="eventbridge-CancelReplay-response-ReplayArn"></a>
The ARN of the replay to cancel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/[\.\-_A-Za-z0-9]+$`

 ** [State](#API_CancelReplay_ResponseSyntax) **   <a name="eventbridge-CancelReplay-response-State"></a>
The current state of the replay.
Type: String
Valid Values: `STARTING | RUNNING | CANCELLING | COMPLETED | CANCELLED | FAILED`

 ** [StateReason](#API_CancelReplay_ResponseSyntax) **   <a name="eventbridge-CancelReplay-response-StateReason"></a>
The reason that the replay is in the current state.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`

## Errors
<a name="API_CancelReplay_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** IllegalStatusException **
An error occurred because a replay can be canceled only when the state is Running or Starting.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_CancelReplay_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/CancelReplay)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/CancelReplay)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/CancelReplay)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/CancelReplay)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/CancelReplay)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/CancelReplay)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/CancelReplay)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/CancelReplay)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/CancelReplay)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/CancelReplay)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
