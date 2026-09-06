---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemoveTargets.html
---

# RemoveTargets
<a name="API_RemoveTargets"></a>

Removes the specified targets from the specified rule. When the rule is triggered, those targets are no longer be invoked.

**Note**
A successful execution of `RemoveTargets` doesn't guarantee all targets are removed from the rule, it means that the target(s) listed in the request are removed.

When you remove a target, when the associated rule triggers, removed targets might continue to be invoked. Allow a short period of time for changes to take effect.

This action can partially fail if too many requests are made at the same time. If that happens, `FailedEntryCount` is non-zero in the response and each entry in `FailedEntries` provides the ID of the failed target and the error code.

The maximum number of entries per request is 10.

## Request Syntax
<a name="API_RemoveTargets_RequestSyntax"></a>

```
{
   "EventBusName": "{{string}}",
   "Force": {{boolean}},
   "Ids": [ "{{string}}" ],
   "Rule": "{{string}}"
}
```

## Request Parameters
<a name="API_RemoveTargets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventBusName](#API_RemoveTargets_RequestSyntax) **   <a name="eventbridge-RemoveTargets-request-EventBusName"></a>
The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(arn:aws[\w-]*:events:[a-z]+-[a-z]+-[\w-]+:[0-9]{12}:event-bus\/)?[/\.\-_A-Za-z0-9]+`
Required: No

 ** [Force](#API_RemoveTargets_RequestSyntax) **   <a name="eventbridge-RemoveTargets-request-Force"></a>
If this is a managed rule, created by an AWS service on your behalf, you must specify `Force` as `True` to remove targets. This parameter is ignored for rules that are not managed rules. You can check whether a rule is a managed rule by using `DescribeRule` or `ListRules` and checking the `ManagedBy` field of the response.
Type: Boolean
Required: No

 ** [Ids](#API_RemoveTargets_RequestSyntax) **   <a name="eventbridge-RemoveTargets-request-Ids"></a>
The IDs of the targets to remove from the rule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

 ** [Rule](#API_RemoveTargets_RequestSyntax) **   <a name="eventbridge-RemoveTargets-request-Rule"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_RemoveTargets_ResponseSyntax"></a>

```
{
   "FailedEntries": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "TargetId": "string"
      }
   ],
   "FailedEntryCount": number
}
```

## Response Elements
<a name="API_RemoveTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedEntries](#API_RemoveTargets_ResponseSyntax) **   <a name="eventbridge-RemoveTargets-response-FailedEntries"></a>
The failed target entries.
Type: Array of [RemoveTargetsResultEntry](API_RemoveTargetsResultEntry.md) objects

 ** [FailedEntryCount](#API_RemoveTargets_ResponseSyntax) **   <a name="eventbridge-RemoveTargets-response-FailedEntryCount"></a>
The number of failed entries.
Type: Integer

## Errors
<a name="API_RemoveTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ManagedRuleException **
This rule was created by an AWS service on behalf of your account. It is managed by that service. If you see this error in response to `DeleteRule` or `RemoveTargets`, you can use the `Force` parameter in those calls to delete the rule or remove targets from the rule. You cannot modify these managed rules by using `DisableRule`, `EnableRule`, `PutTargets`, `PutRule`, `TagResource`, or `UntagResource`.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## Examples
<a name="API_RemoveTargets_Examples"></a>

### Removes a target with ID "MyTargetId" from a rule named "test"
<a name="API_RemoveTargets_Example_1"></a>

The following is an example of a RemoveTargets request.

#### Sample Request
<a name="API_RemoveTargets_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.RemoveTargets

{
    "Rule": "test",
    "Ids": [
        "MyTargetId"
    ]
}
```

#### Sample Response
<a name="API_RemoveTargets_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
    "FailedEntries": [],
    "FailedEntryCount": 0
}
```

## See Also
<a name="API_RemoveTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/RemoveTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/RemoveTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/RemoveTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/RemoveTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/RemoveTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/RemoveTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/RemoveTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/RemoveTargets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/RemoveTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/RemoveTargets)
