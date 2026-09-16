---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeRule.html
---

# DescribeRule
<a name="API_DescribeRule"></a>

Describes the specified rule.

DescribeRule does not list the targets of a rule. To see the targets associated with a rule, use [ListTargetsByRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTargetsByRule.html).

## Request Syntax
<a name="API_DescribeRule_RequestSyntax"></a>

```
{
   "EventBusName": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventBusName](#API_DescribeRule_RequestSyntax) **   <a name="eventbridge-DescribeRule-request-EventBusName"></a>
The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(arn:aws[\w-]*:events:[a-z]+-[a-z]+-[\w-]+:[0-9]{12}:event-bus\/)?[/\.\-_A-Za-z0-9]+`
Required: No

 ** [Name](#API_DescribeRule_RequestSyntax) **   <a name="eventbridge-DescribeRule-request-Name"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DescribeRule_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "CreatedBy": "string",
   "Description": "string",
   "EventBusName": "string",
   "EventPattern": "string",
   "ManagedBy": "string",
   "Name": "string",
   "RoleArn": "string",
   "ScheduleExpression": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_DescribeRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeRule_ResponseSyntax) **   <a name="eventbridge-DescribeRule-response-Arn"></a>
The Amazon Resource Name (ARN) of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.

 ** [CreatedBy](#API_DescribeRule_ResponseSyntax) **   <a name="eventbridge-DescribeRule-response-CreatedBy"></a>
The account ID of the user that created the rule. If you use `PutRule` to put a rule on an event bus in another account, the other account is the owner of the rule, and the rule ARN includes the account ID for that account. However, the value for `CreatedBy` is the account ID as the account that created the rule in the other account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [Description](#API_DescribeRule_ResponseSyntax) **   <a name="eventbridge-DescribeRule-response-Description"></a>
The description of the rule.
Type: String
Length Constraints: Maximum length of 512.

 ** [EventBusName](#API_DescribeRule_ResponseSyntax) **   <a name="eventbridge-DescribeRule-response-EventBusName"></a>
The name of the event bus associated with the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[/\.\-_A-Za-z0-9]+`

 ** [EventPattern](#API_DescribeRule_ResponseSyntax) **   <a name="eventbridge-DescribeRule-response-EventPattern"></a>
The event pattern. For more information, see [Events and Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html) in the * *Amazon EventBridge User Guide* *.
Type: String
Length Constraints: Maximum length of 4096.

 ** [ManagedBy](#API_DescribeRule_ResponseSyntax) **   <a name="eventbridge-DescribeRule-response-ManagedBy"></a>
If this is a managed rule, created by an AWS service on your behalf, this field displays the principal name of the AWS service that created the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [Name](#API_DescribeRule_ResponseSyntax) **   <a name="eventbridge-DescribeRule-response-Name"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`

 ** [RoleArn](#API_DescribeRule_ResponseSyntax) **   <a name="eventbridge-DescribeRule-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.

 ** [ScheduleExpression](#API_DescribeRule_ResponseSyntax) **   <a name="eventbridge-DescribeRule-response-ScheduleExpression"></a>
The scheduling expression. For example, "cron(0 20 \* \* ? \*)", "rate(5 minutes)".
Type: String
Length Constraints: Maximum length of 256.

 ** [State](#API_DescribeRule_ResponseSyntax) **   <a name="eventbridge-DescribeRule-response-State"></a>
Specifies whether the rule is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED | ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS`

## Errors
<a name="API_DescribeRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeRule_Examples"></a>

### Describes a rule named "test"
<a name="API_DescribeRule_Example_1"></a>

The following is an example of a DescribeRule request and response.

#### Sample Request
<a name="API_DescribeRule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.DescribeRule

{
    "Name": "test"
}
```

#### Sample Response
<a name="API_DescribeRule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
    "Name": "test",
    "EventPattern": "{\"source\":[\"aws.autoscaling\"],\"detail-type\":[\"EC2 Instance Launch Successful\",\"EC2 Instance Terminate Successful\",\"EC2 Instance Launch Unsuccessful\",\"EC2 Instance Terminate Unsuccessful\"]}",
    "State": "ENABLED",
    "Arn": "arn:aws:events:us-east-1:123456789012:rule/test",
    "Description": "Test rule for Auto Scaling events"
}
```

## See Also
<a name="API_DescribeRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DescribeRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DescribeRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DescribeRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DescribeRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DescribeRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DescribeRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DescribeRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DescribeRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DescribeRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DescribeRule)
