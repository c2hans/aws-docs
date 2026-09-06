---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetCalendarState.html
---

# GetCalendarState
<a name="API_GetCalendarState"></a>

Gets the state of a AWS Systems Manager change calendar at the current time or a specified time. If you specify a time, `GetCalendarState` returns the state of the calendar at that specific time, and returns the next time that the change calendar state will transition. If you don't specify a time, `GetCalendarState` uses the current time. Change Calendar entries have two possible states: `OPEN` or `CLOSED`.

If you specify more than one calendar in a request, the command returns the status of `OPEN` only if all calendars in the request are open. If one or more calendars in the request are closed, the status returned is `CLOSED`.

For more information about Change Calendar, a tool in AWS Systems Manager, see [AWS Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar.html) in the * AWS Systems Manager User Guide*.

## Request Syntax
<a name="API_GetCalendarState_RequestSyntax"></a>

```
{
   "AtTime": "{{string}}",
   "CalendarNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetCalendarState_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AtTime](#API_GetCalendarState_RequestSyntax) **   <a name="systemsmanager-GetCalendarState-request-AtTime"></a>
(Optional) The specific time for which you want to get calendar state information, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. If you don't specify a value or `AtTime`, the current time is used.
Type: String
Required: No

 ** [CalendarNames](#API_GetCalendarState_RequestSyntax) **   <a name="systemsmanager-GetCalendarState-request-CalendarNames"></a>
The names of Amazon Resource Names (ARNs) of the Systems Manager documents (SSM documents) that represent the calendar entries for which you want to get the state.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_GetCalendarState_ResponseSyntax"></a>

```
{
   "AtTime": "string",
   "NextTransitionTime": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_GetCalendarState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AtTime](#API_GetCalendarState_ResponseSyntax) **   <a name="systemsmanager-GetCalendarState-response-AtTime"></a>
The time, as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string, that you specified in your command. If you don't specify a time, `GetCalendarState` uses the current time.
Type: String

 ** [NextTransitionTime](#API_GetCalendarState_ResponseSyntax) **   <a name="systemsmanager-GetCalendarState-response-NextTransitionTime"></a>
The time, as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string, that the calendar state will change. If the current calendar state is `OPEN`, `NextTransitionTime` indicates when the calendar state changes to `CLOSED`, and vice-versa.
Type: String

 ** [State](#API_GetCalendarState_ResponseSyntax) **   <a name="systemsmanager-GetCalendarState-response-State"></a>
The state of the calendar. An `OPEN` calendar indicates that actions are allowed to proceed, and a `CLOSED` calendar indicates that actions aren't allowed to proceed.
Type: String
Valid Values: `OPEN | CLOSED`

## Errors
<a name="API_GetCalendarState_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidDocumentType **
The SSM document type isn't valid. Valid document types are described in the `DocumentType` property.
HTTP Status Code: 400

 ** UnsupportedCalendarException **
The calendar entry contained in the specified SSM document isn't supported.
HTTP Status Code: 400

## Examples
<a name="API_GetCalendarState_Examples"></a>

### Example
<a name="API_GetCalendarState_Example_1"></a>

This example illustrates one usage of GetCalendarState.

#### Sample Request
<a name="API_GetCalendarState_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetCalendarState
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240224T191829Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 67

{
    "CalendarNames": [
        "MyCalendar"
    ],
    "AtTime": "2024-02-25T19:05:47Z"
}
```

#### Sample Response
<a name="API_GetCalendarState_Example_1_Response"></a>

```
{
    "AtTime": "2024-02-25T19:05:47Z",
    "State": "OPEN"
}
```

## See Also
<a name="API_GetCalendarState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetCalendarState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetCalendarState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetCalendarState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetCalendarState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetCalendarState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetCalendarState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetCalendarState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetCalendarState)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetCalendarState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetCalendarState)
