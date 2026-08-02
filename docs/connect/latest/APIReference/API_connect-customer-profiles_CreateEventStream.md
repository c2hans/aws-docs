---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_CreateEventStream.html
---

# CreateEventStream
<a name="API_connect-customer-profiles_CreateEventStream"></a>

Creates an event stream, which is a subscription to real-time events, such as when profiles are created and updated through Connect Customer Customer Profiles.

Each event stream can be associated with only one Kinesis Data Stream destination in the same region and AWS account as the customer profiles domain

## Request Syntax
<a name="API_connect-customer-profiles_CreateEventStream_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/event-streams/{{EventStreamName}} HTTP/1.1
Content-type: application/json

{
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Uri": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_CreateEventStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_CreateEventStream_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateEventStream-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [EventStreamName](#API_connect-customer-profiles_CreateEventStream_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateEventStream-request-uri-EventStreamName"></a>
The name of the event stream.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_CreateEventStream_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_connect-customer-profiles_CreateEventStream_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateEventStream-request-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [Uri](#API_connect-customer-profiles_CreateEventStream_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateEventStream-request-Uri"></a>
The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_CreateEventStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EventStreamArn": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-customer-profiles_CreateEventStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventStreamArn](#API_connect-customer-profiles_CreateEventStream_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateEventStream-response-EventStreamArn"></a>
A unique identifier for the event stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Tags](#API_connect-customer-profiles_CreateEventStream_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateEventStream-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-customer-profiles_CreateEventStream_Errors"></a>

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
<a name="API_connect-customer-profiles_CreateEventStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/CreateEventStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/CreateEventStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/CreateEventStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/CreateEventStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/CreateEventStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/CreateEventStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/CreateEventStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/CreateEventStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/CreateEventStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/CreateEventStream)
