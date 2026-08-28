---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListRuleNamesByTarget.html
---

# ListRuleNamesByTarget
<a name="API_ListRuleNamesByTarget"></a>

Lists the rules for the specified target. You can see which of the rules in Amazon EventBridge can invoke a specific target in your account.

The maximum number of results per page for requests is 100.

## Request Syntax
<a name="API_ListRuleNamesByTarget_RequestSyntax"></a>

```
{
   "EventBusName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "TargetArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRuleNamesByTarget_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventBusName](#API_ListRuleNamesByTarget_RequestSyntax) **   <a name="eventbridge-ListRuleNamesByTarget-request-EventBusName"></a>
The name or ARN of the event bus to list rules for. If you omit this, the default event bus is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(arn:aws[\w-]*:events:[a-z]+-[a-z]+-[\w-]+:[0-9]{12}:event-bus\/)?[/\.\-_A-Za-z0-9]+`
Required: No

 ** [Limit](#API_ListRuleNamesByTarget_RequestSyntax) **   <a name="eventbridge-ListRuleNamesByTarget-request-Limit"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListRuleNamesByTarget_RequestSyntax) **   <a name="eventbridge-ListRuleNamesByTarget-request-NextToken"></a>
The token returned by a previous call, which you can use to retrieve the next set of results.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [TargetArn](#API_ListRuleNamesByTarget_RequestSyntax) **   <a name="eventbridge-ListRuleNamesByTarget-request-TargetArn"></a>
The Amazon Resource Name (ARN) of the target resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: Yes

## Response Syntax
<a name="API_ListRuleNamesByTarget_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RuleNames": [ "string" ]
}
```

## Response Elements
<a name="API_ListRuleNamesByTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRuleNamesByTarget_ResponseSyntax) **   <a name="eventbridge-ListRuleNamesByTarget-response-NextToken"></a>
A token indicating there are more results available. If there are no more results, no token is included in the response.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [RuleNames](#API_ListRuleNamesByTarget_ResponseSyntax) **   <a name="eventbridge-ListRuleNamesByTarget-response-RuleNames"></a>
The names of the rules that can invoke the given target.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`

## Errors
<a name="API_ListRuleNamesByTarget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## Examples
<a name="API_ListRuleNamesByTarget_Examples"></a>

### Lists rule names by target with the specified ARN
<a name="API_ListRuleNamesByTarget_Example_1"></a>

The following is an example of a ListRuleNamesByTarget request and response.

#### Sample Request
<a name="API_ListRuleNamesByTarget_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.ListRuleNamesByTarget

{
    "TargetArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
    "NextToken": "",
    "Limit": 0
}
```

#### Sample Response
<a name="API_ListRuleNamesByTarget_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
    "RuleNames": [
        "test1",
        "test2",
        "test3",
        "test4",
        "test5"
    ]
}
```

## See Also
<a name="API_ListRuleNamesByTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/ListRuleNamesByTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/ListRuleNamesByTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ListRuleNamesByTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/ListRuleNamesByTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ListRuleNamesByTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/ListRuleNamesByTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/ListRuleNamesByTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/ListRuleNamesByTarget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/ListRuleNamesByTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ListRuleNamesByTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
