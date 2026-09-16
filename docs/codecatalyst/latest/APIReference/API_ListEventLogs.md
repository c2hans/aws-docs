---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListEventLogs.html
---

# ListEventLogs
<a name="API_ListEventLogs"></a>

Retrieves a list of events that occurred during a specific time in a space. You can use these events to audit user and system activity in a space. For more information, see [Monitoring](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-monitoring.html) in the *Amazon CodeCatalyst User Guide*.

**Note**
ListEventLogs guarantees events for the last 30 days in a given space. You can also view and retrieve a list of management events over the last 90 days for Amazon CodeCatalyst in the AWS CloudTrail console by viewing Event history, or by creating a trail to create and maintain a record of events that extends past 90 days. For more information, see [Working with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) and [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-getting-started.html).

## Request Syntax
<a name="API_ListEventLogs_RequestSyntax"></a>

```
POST /v1/spaces/{{spaceName}}/eventLogs HTTP/1.1
Content-type: application/json

{
   "endTime": "{{string}}",
   "eventName": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "startTime": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListEventLogs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [spaceName](#API_ListEventLogs_RequestSyntax) **   <a name="codecatalyst-ListEventLogs-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_ListEventLogs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [endTime](#API_ListEventLogs_RequestSyntax) **   <a name="codecatalyst-ListEventLogs-request-endTime"></a>
The time after which you do not want any events retrieved, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp
Required: Yes

 ** [eventName](#API_ListEventLogs_RequestSyntax) **   <a name="codecatalyst-ListEventLogs-request-eventName"></a>
The name of the event.
Type: String
Required: No

 ** [maxResults](#API_ListEventLogs_RequestSyntax) **   <a name="codecatalyst-ListEventLogs-request-maxResults"></a>
The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a `NextToken` element, which you can use to obtain additional results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 250.
Required: No

 ** [nextToken](#API_ListEventLogs_RequestSyntax) **   <a name="codecatalyst-ListEventLogs-request-nextToken"></a>
A token returned from a call to this API to indicate the next batch of results to return, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

 ** [startTime](#API_ListEventLogs_RequestSyntax) **   <a name="codecatalyst-ListEventLogs-request-startTime"></a>
The date and time when you want to start retrieving events, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_ListEventLogs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "errorCode": "string",
         "eventCategory": "string",
         "eventName": "string",
         "eventSource": "string",
         "eventTime": "string",
         "eventType": "string",
         "id": "string",
         "operationType": "string",
         "projectInformation": {
            "name": "string",
            "projectId": "string"
         },
         "requestId": "string",
         "requestPayload": {
            "contentType": "string",
            "data": "string"
         },
         "responsePayload": {
            "contentType": "string",
            "data": "string"
         },
         "sourceIpAddress": "string",
         "userAgent": "string",
         "userIdentity": {
            "awsAccountId": "string",
            "principalId": "string",
            "userName": "string",
            "userType": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEventLogs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListEventLogs_ResponseSyntax) **   <a name="codecatalyst-ListEventLogs-response-items"></a>
Information about each event retrieved in the list.
Type: Array of [EventLogEntry](API_EventLogEntry.md) objects

 ** [nextToken](#API_ListEventLogs_ResponseSyntax) **   <a name="codecatalyst-ListEventLogs-response-nextToken"></a>
A token returned from a call to this API to indicate the next batch of results to return, if any.
Type: String

## Errors
<a name="API_ListEventLogs_Errors"></a>

 ** AccessDeniedException **
The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.
HTTP Status Code: 403

 ** ConflictException **
The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.
HTTP Status Code: 400

## Examples
<a name="API_ListEventLogs_Examples"></a>

### Example
<a name="API_ListEventLogs_Example_1"></a>

This example illustrates one usage of ListEventLogs.

#### Sample Request
<a name="API_ListEventLogs_Example_1_Request"></a>

```
POST https://codecatalyst.global.api.aws/v1/ExampleCorp/eventLogs
      {
        "startTime": "2022-11-30",
        "endTime": "2022-12-01",
        "maxResults": 2,
        "nextToken": "EXAMPLE"
      }
```

#### Sample Response
<a name="API_ListEventLogs_Example_1_Response"></a>

```
200 OK 411b
Content-Type: application/json; charset=utf-8
Date: Fri Dec 2 2022 13:16:05 GMT

{
    "nextToken": "EXAMPLE",
    "items": [
        {
            "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "eventName": "listEventLogs",
            "eventType": "AwsApiCall",
            "eventCategory": "MANAGEMENT",
            "eventSource": "manage",
            "eventTime": "2022-12-01T22:47:24.605000+00:00",
            "operationType": "READONLY",
            "userIdentity": {
                "userType": "USER",
                "principalId": "a1b2c3d4e5-678fgh90-1a2b-3c4d-e5f6-EXAMPLE11111",
                "userName": "MaryMajor"
            },
            "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "requestPayload": {
                "contentType": "application/json",
                "data": "{\"spaceName\":\"ExampleCorp\",\"startTime\":\"2022-12-01T00:00:00Z\",\"endTime\":\"2022-12-10T00:00:00Z\",\"maxResults\":\"2\"}"
            },
            "sourceIpAddress": "127.0.0.1",
            "userAgent": "aws-cli/2.9.0 Python/3.9.11 Darwin/21.3.0 exe/x86_64 prompt/off command/codecatalyst.list-event-logs"
        },
        {
            "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
            "eventName": "createProject",
            "eventType": "AwsApiCall",
            "eventCategory": "MANAGEMENT",
            "eventSource": "manage",
            "eventTime": "2022-12-01T09:15:32.068000+00:00",
            "operationType": "MUTATION",
            "userIdentity": {
                "userType": "USER",
                "principalId": "a1b2c3d4e5-678fgh90-1a2b-3c4d-e5f6-EXAMPLE11111",
                "userName": "MaryMajor"
            },
            "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "requestPayload": {
                "contentType": "application/json",
                "data": "{\"spaceName\":\"ExampleCorp\",\"name\":\"MyFirstProject\",\"displayName\":\"MyFirstProject\"}"
            },
            "responsePayload": {
                "contentType": "application/json",
                "data": "{\"spaceName\":\"ExampleCorp\",\"name\":\"MyFirstProject\",\"displayName\":\"MyFirstProject\",\"id\":\"a1b2c3d4-5678-90ab-cdef-EXAMPLE4444\"}"
            },
            "sourceIpAddress": "192.0.2.23",
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
    ]
}
```

## See Also
<a name="API_ListEventLogs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/ListEventLogs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/ListEventLogs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/ListEventLogs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/ListEventLogs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/ListEventLogs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/ListEventLogs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/ListEventLogs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/ListEventLogs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/ListEventLogs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/ListEventLogs)
