---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogRecord.html
---

# GetLogRecord
<a name="API_GetLogRecord"></a>

Retrieves all of the fields and values of a single log event. All fields are retrieved, even if the original query that produced the `logRecordPointer` retrieved only a subset of fields. Fields are returned as field name/field value pairs.

The full unparsed log event is returned within `@message`.

## Request Syntax
<a name="API_GetLogRecord_RequestSyntax"></a>

```
{
   "logRecordPointer": "{{string}}",
   "unmask": {{boolean}}
}
```

## Request Parameters
<a name="API_GetLogRecord_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [logRecordPointer](#API_GetLogRecord_RequestSyntax) **   <a name="CWL-GetLogRecord-request-logRecordPointer"></a>
The pointer corresponding to the log event record you want to retrieve. You get this from the response of a `GetQueryResults` operation. In that response, the value of the `@ptr` field for a log event is the value to use as `logRecordPointer` to retrieve that complete log event record.
Type: String
Required: Yes

 ** [unmask](#API_GetLogRecord_RequestSyntax) **   <a name="CWL-GetLogRecord-request-unmask"></a>
Specify `true` to display the log event fields with all sensitive data unmasked and visible. The default is `false`.
To use this operation with this parameter, you must be signed into an account with the `logs:Unmask` permission.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetLogRecord_ResponseSyntax"></a>

```
{
   "logRecord": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetLogRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [logRecord](#API_GetLogRecord_ResponseSyntax) **   <a name="CWL-GetLogRecord-response-logRecord"></a>
The requested log event, as a JSON string.
Type: String to string map

## Errors
<a name="API_GetLogRecord_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_GetLogRecord_Examples"></a>

### To retrieve all fields for a specified log event
<a name="API_GetLogRecord_Example_1"></a>

The following example retrieves the fields for a specified log event.

#### Sample Request
<a name="API_GetLogRecord_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.GetLogRecord
{
   "logRecordPointer": "123456789"
}
```

#### Sample Response
<a name="API_GetLogRecord_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "logRecord": {
      "@timestamp" : "1536857812",
      "@message" : "123456789012 eni-1234567890abcde123 6 33 ACCEPT"
      "accountId" : "123456789012",
      "interfaceId" : "eni-1234567890abcde123",
      "protocol" : "6",
      "packets" : "33",
      "action" : "ACCEPT"
   }
}
```

## See Also
<a name="API_GetLogRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetLogRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetLogRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetLogRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetLogRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetLogRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetLogRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetLogRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetLogRecord)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetLogRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetLogRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
