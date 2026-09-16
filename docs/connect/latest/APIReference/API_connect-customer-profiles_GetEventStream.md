---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetEventStream.html
---

# GetEventStream
<a name="API_connect-customer-profiles_GetEventStream"></a>

Returns information about the specified event stream in a specific domain.

## Request Syntax
<a name="API_connect-customer-profiles_GetEventStream_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/event-streams/{{EventStreamName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetEventStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetEventStream_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetEventStream-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [EventStreamName](#API_connect-customer-profiles_GetEventStream_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetEventStream-request-uri-EventStreamName"></a>
The name of the event stream provided during create operations.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetEventStream_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetEventStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "DestinationDetails": {
      "Message": "string",
      "Status": "string",
      "UnhealthySince": number,
      "Uri": "string"
   },
   "DomainName": "string",
   "EventStreamArn": "string",
   "State": "string",
   "StoppedSince": number,
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetEventStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-customer-profiles_GetEventStream_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventStream-response-CreatedAt"></a>
The timestamp of when the export was created.
Type: Timestamp

 ** [DestinationDetails](#API_connect-customer-profiles_GetEventStream_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventStream-response-DestinationDetails"></a>
Details regarding the Kinesis stream.
Type: [EventStreamDestinationDetails](API_connect-customer-profiles_EventStreamDestinationDetails.md) object

 ** [DomainName](#API_connect-customer-profiles_GetEventStream_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventStream-response-DomainName"></a>
The unique name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [EventStreamArn](#API_connect-customer-profiles_GetEventStream_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventStream-response-EventStreamArn"></a>
A unique identifier for the event stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [State](#API_connect-customer-profiles_GetEventStream_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventStream-response-State"></a>
The operational state of destination stream for export.
Type: String
Valid Values: `RUNNING | STOPPED`

 ** [StoppedSince](#API_connect-customer-profiles_GetEventStream_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventStream-response-StoppedSince"></a>
The timestamp when the `State` changed to `STOPPED`.
Type: Timestamp

 ** [Tags](#API_connect-customer-profiles_GetEventStream_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventStream-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-customer-profiles_GetEventStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_GetEventStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetEventStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetEventStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetEventStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetEventStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetEventStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetEventStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetEventStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetEventStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetEventStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetEventStream)
