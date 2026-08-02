---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_TestEventPattern.html
---

# TestEventPattern
<a name="API_TestEventPattern"></a>

Tests whether the specified event pattern matches the provided event.

Most services in AWS treat : or / as the same character in Amazon Resource Names (ARNs). However, EventBridge uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.

## Request Syntax
<a name="API_TestEventPattern_RequestSyntax"></a>

```
{
   "Event": "{{string}}",
   "EventPattern": "{{string}}"
}
```

## Request Parameters
<a name="API_TestEventPattern_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Event](#API_TestEventPattern_RequestSyntax) **   <a name="eventbridge-TestEventPattern-request-Event"></a>
The event, in JSON format, to test against the event pattern. The JSON must follow the format specified in [AWS Events](https://docs.aws.amazon.com/eventbridge/latest/userguide/aws-events.html), and the following fields are mandatory:
+  `id`
+  `account`
+  `source`
+  `time`
+  `region`
+  `resources`
+  `detail-type`
Type: String
Required: Yes

 ** [EventPattern](#API_TestEventPattern_RequestSyntax) **   <a name="eventbridge-TestEventPattern-request-EventPattern"></a>
The event pattern. For more information, see [Events and Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html) in the * *Amazon EventBridge User Guide* *.
Type: String
Length Constraints: Maximum length of 4096.
Required: Yes

## Response Syntax
<a name="API_TestEventPattern_ResponseSyntax"></a>

```
{
   "Result": boolean
}
```

## Response Elements
<a name="API_TestEventPattern_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Result](#API_TestEventPattern_ResponseSyntax) **   <a name="eventbridge-TestEventPattern-response-Result"></a>
Indicates whether the event matches the event pattern.
Type: Boolean

## Errors
<a name="API_TestEventPattern_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** InvalidEventPatternException **
The event pattern is not valid.
HTTP Status Code: 400

## Examples
<a name="API_TestEventPattern_Examples"></a>

### Tests that a given event matches a given event pattern
<a name="API_TestEventPattern_Example_1"></a>

The following is an example of a TestEventPattern request and response.

#### Sample Request
<a name="API_TestEventPattern_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.TestEventPattern

{
    "EventPattern": "{\"source\": [\"com.mycompany.myapp\"]}",
    "Event": "{\"id\": \"e00c66cb-fe7a-4fcc-81ad-58eb60f5d96b\", \"detail-type\": \"myDetailType\", \"source\": \"com.mycompany.myapp\", \"account\": \"123456789012\", \"time\": \"2016-01-10T01:29:23Z\", \"region\": \"us-east-1\", \"resources\": [\"resource1\",  \"resource2\"], \"detail\": {\"key1\": \"value1\", \"key2\": \"value2\"}}"
  }
}
```

#### Sample Response
<a name="API_TestEventPattern_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
    "Result": true
}
```

## See Also
<a name="API_TestEventPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/TestEventPattern)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/TestEventPattern)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/TestEventPattern)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/TestEventPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/TestEventPattern)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/TestEventPattern)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/TestEventPattern)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/TestEventPattern)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/TestEventPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/TestEventPattern)
