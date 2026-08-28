---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DisableRule.html
---

# DisableRule
<a name="API_DisableRule"></a>

Disables the specified rule. A disabled rule won't match any events, and won't self-trigger if it has a schedule expression.

When you disable a rule, incoming events might continue to match to the disabled rule. Allow a short period of time for changes to take effect.

## Request Syntax
<a name="API_DisableRule_RequestSyntax"></a>

```
{
   "EventBusName": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DisableRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventBusName](#API_DisableRule_RequestSyntax) **   <a name="eventbridge-DisableRule-request-EventBusName"></a>
The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(arn:aws[\w-]*:events:[a-z]+-[a-z]+-[\w-]+:[0-9]{12}:event-bus\/)?[/\.\-_A-Za-z0-9]+`
Required: No

 ** [Name](#API_DisableRule_RequestSyntax) **   <a name="eventbridge-DisableRule-request-Name"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Elements
<a name="API_DisableRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisableRule_Errors"></a>

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
<a name="API_DisableRule_Examples"></a>

### Disables a rule named "test"
<a name="API_DisableRule_Example_1"></a>

The following is an example of a DisableRule request.

#### Sample Request
<a name="API_DisableRule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.DisableRule

{
    "Name": "test"
}
```

#### Sample Response
<a name="API_DisableRule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_DisableRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DisableRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DisableRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DisableRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DisableRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DisableRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DisableRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DisableRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DisableRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DisableRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DisableRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
