---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html
---

# PutEvents
<a name="API_PutEvents"></a>

Sends custom events to Amazon EventBridge so that they can be matched to rules.

You can batch multiple event entries into one request for efficiency. However, the total entry size must be less than 1MB. You can calculate the entry size before you send the events. For more information, see [Calculating PutEvents event entry size](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-putevents.html#eb-putevent-size) in the * *Amazon EventBridge User Guide* *.

PutEvents accepts the data in JSON format. For the JSON number (integer) data type, the constraints are: a minimum value of -9,223,372,036,854,775,808 and a maximum value of 9,223,372,036,854,775,807.

**Note**
PutEvents will only process nested JSON up to 1000 levels deep.

## Request Syntax
<a name="API_PutEvents_RequestSyntax"></a>

```
{
   "EndpointId": "{{string}}",
   "Entries": [
      {
         "Detail": "{{string}}",
         "DetailType": "{{string}}",
         "EventBusName": "{{string}}",
         "Resources": [ "{{string}}" ],
         "Source": "{{string}}",
         "Time": {{number}},
         "TraceHeader": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointId](#API_PutEvents_RequestSyntax) **   <a name="eventbridge-PutEvents-request-EndpointId"></a>
The URL subdomain of the endpoint. For example, if the URL for Endpoint is https://abcde.veo.endpoints.event.amazonaws.com, then the EndpointId is `abcde.veo`.
When using Java, you must include `auth-crt` on the class path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[A-Za-z0-9\-]+[\.][A-Za-z0-9\-]+$`
Required: No

 ** [Entries](#API_PutEvents_RequestSyntax) **   <a name="eventbridge-PutEvents-request-Entries"></a>
The entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.
Type: Array of [PutEventsRequestEntry](API_PutEventsRequestEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_PutEvents_ResponseSyntax"></a>

```
{
   "Entries": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "EventId": "string"
      }
   ],
   "FailedEntryCount": number
}
```

## Response Elements
<a name="API_PutEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entries](#API_PutEvents_ResponseSyntax) **   <a name="eventbridge-PutEvents-response-Entries"></a>
The successfully and unsuccessfully ingested events results. If the ingestion was successful, the entry has the event ID in it. Otherwise, you can use the error code and error message to identify the problem with the entry.
For each record, the index of the response element is the same as the index in the request array.
Type: Array of [PutEventsResultEntry](API_PutEventsResultEntry.md) objects

 ** [FailedEntryCount](#API_PutEvents_ResponseSyntax) **   <a name="eventbridge-PutEvents-response-FailedEntryCount"></a>
The number of failed entries.
Type: Integer

## Errors
<a name="API_PutEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

## Examples
<a name="API_PutEvents_Examples"></a>

### Sends two custom events
<a name="API_PutEvents_Example_1"></a>

The following is an example of a PutEvents request and response.

#### Sample Request
<a name="API_PutEvents_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutEvents

{
   "Entries":[
      {
         "Source":"com.mycompany.myapp",
         "Detail":"{ \"key1\": \"value1\", \"key2\": \"value2\" }",
         "Resources":[
            "resource1",
            "resource2"
         ],
         "DetailType":"myDetailType"
      },
      {
         "Source":"com.mycompany.myapp",
         "Detail":"{ \"key1\": \"value3\", \"key2\": \"value4\" }",
         "Resources":[
            "resource1",
            "resource2"
         ],
         "DetailType":"myDetailType"
      }
   ]
}
```

#### Sample Response
<a name="API_PutEvents_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
    "FailedEntryCount": 0,
    "Entries": [
        {
            "EventId": "11710aed-b79e-4468-a20b-bb3c0c3b4860"
        },
        {
            "EventId": "d804d26a-88db-4b66-9eaf-9a11c708ae82"
        }
    ]
}
```

## See Also
<a name="API_PutEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/PutEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/PutEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/PutEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/PutEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/PutEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/PutEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/PutEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/PutEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/PutEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/PutEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
