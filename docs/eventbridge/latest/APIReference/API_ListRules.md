---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListRules.html
---

# ListRules
<a name="API_ListRules"></a>

Lists your Amazon EventBridge rules. You can either list all the rules or you can provide a prefix to match to the rule names.

The maximum number of results per page for requests is 100.

ListRules does not list the targets of a rule. To see the targets associated with a rule, use [ListTargetsByRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTargetsByRule.html).

## Request Syntax
<a name="API_ListRules_RequestSyntax"></a>

```
{
   "EventBusName": "{{string}}",
   "Limit": {{number}},
   "NamePrefix": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventBusName](#API_ListRules_RequestSyntax) **   <a name="eventbridge-ListRules-request-EventBusName"></a>
The name or ARN of the event bus to list the rules for. If you omit this, the default event bus is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(arn:aws[\w-]*:events:[a-z]+-[a-z]+-[\w-]+:[0-9]{12}:event-bus\/)?[/\.\-_A-Za-z0-9]+`
Required: No

 ** [Limit](#API_ListRules_RequestSyntax) **   <a name="eventbridge-ListRules-request-Limit"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NamePrefix](#API_ListRules_RequestSyntax) **   <a name="eventbridge-ListRules-request-NamePrefix"></a>
The prefix matching the rule name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** [NextToken](#API_ListRules_RequestSyntax) **   <a name="eventbridge-ListRules-request-NextToken"></a>
The token returned by a previous call, which you can use to retrieve the next set of results.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListRules_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Rules": [
      {
         "Arn": "string",
         "Description": "string",
         "EventBusName": "string",
         "EventPattern": "string",
         "ManagedBy": "string",
         "Name": "string",
         "RoleArn": "string",
         "ScheduleExpression": "string",
         "State": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRules_ResponseSyntax) **   <a name="eventbridge-ListRules-response-NextToken"></a>
A token indicating there are more results available. If there are no more results, no token is included in the response.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Rules](#API_ListRules_ResponseSyntax) **   <a name="eventbridge-ListRules-response-Rules"></a>
The rules that match the specified criteria.
Type: Array of [Rule](API_Rule.md) objects

## Errors
<a name="API_ListRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## Examples
<a name="API_ListRules_Examples"></a>

### Lists all the rules that start with the letter "t" with a page size of 1
<a name="API_ListRules_Example_1"></a>

The following is an example of a ListRules request and response.

#### Sample Request
<a name="API_ListRules_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.ListRules

{
    "NamePrefix": "t",
    "Limit": 1
}
```

#### Sample Response
<a name="API_ListRules_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
    "Rules": [
        {
            "EventPattern": "{\"source\":[\"aws.autoscaling\"],\"detail-type\":[\"EC2 Instance Launch Successful\",\"EC2 Instance Terminate Successful\",\"EC2 Instance Launch Unsuccessful\",\"EC2 Instance Terminate Unsuccessful\"]}",
            "State": "DISABLED",
            "Name": "test",
            "Arn": "arn:aws:events:us-east-1:123456789012:rule/test",
            "Description": "Test rule for Auto Scaling events"
        }
    ],
    "NextToken": "ABCDEgAAAAAAAAAAQAAABCXtD8i7XlyFv5XFKH8GrudAAAAQIoQ0+7qXp63vQf1pvVklfHFd+p2QgY36pjlAqsSsrkNbOtTePaCeJqN8O+jbu66UhpJh7huA9r0iY9zjdtZ3vsAAAAgAAAAAAAAAAF5MZWktllmMuLd9gUjryM4sL9EG5IkcPUm60Vq1tzyYw=="
}
```

## See Also
<a name="API_ListRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/ListRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/ListRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ListRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/ListRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ListRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/ListRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/ListRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/ListRules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/ListRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ListRules)
