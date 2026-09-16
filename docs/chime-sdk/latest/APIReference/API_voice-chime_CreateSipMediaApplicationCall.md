---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplicationCall.html
---

# CreateSipMediaApplicationCall
<a name="API_voice-chime_CreateSipMediaApplicationCall"></a>

Creates an outbound call to a phone number from the phone number specified in the request, and it invokes the endpoint of the specified `sipMediaApplicationId`.

## Request Syntax
<a name="API_voice-chime_CreateSipMediaApplicationCall_RequestSyntax"></a>

```
POST /sip-media-applications/{{sipMediaApplicationId}}/calls HTTP/1.1
Content-type: application/json

{
   "ArgumentsMap": {
      "{{string}}" : "{{string}}"
   },
   "FromPhoneNumber": "{{string}}",
   "SipHeaders": {
      "{{string}}" : "{{string}}"
   },
   "ToPhoneNumber": "{{string}}"
}
```

## URI Request Parameters
<a name="API_voice-chime_CreateSipMediaApplicationCall_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sipMediaApplicationId](#API_voice-chime_CreateSipMediaApplicationCall_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipMediaApplicationCall-request-uri-SipMediaApplicationId"></a>
The ID of the SIP media application.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_CreateSipMediaApplicationCall_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ArgumentsMap](#API_voice-chime_CreateSipMediaApplicationCall_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipMediaApplicationCall-request-ArgumentsMap"></a>
Context passed to a CreateSipMediaApplication API call. For example, you could pass key-value pairs such as: `"FirstName": "John", "LastName": "Doe"`
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [FromPhoneNumber](#API_voice-chime_CreateSipMediaApplicationCall_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipMediaApplicationCall-request-FromPhoneNumber"></a>
The phone number that a user calls from. This is a phone number in your Amazon Chime SDK phone number inventory.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: Yes

 ** [SipHeaders](#API_voice-chime_CreateSipMediaApplicationCall_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipMediaApplicationCall-request-SipHeaders"></a>
The SIP headers added to an outbound call leg.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [ToPhoneNumber](#API_voice-chime_CreateSipMediaApplicationCall_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipMediaApplicationCall-request-ToPhoneNumber"></a>
The phone number that the service should call.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: Yes

## Response Syntax
<a name="API_voice-chime_CreateSipMediaApplicationCall_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "SipMediaApplicationCall": {
      "TransactionId": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_CreateSipMediaApplicationCall_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [SipMediaApplicationCall](#API_voice-chime_CreateSipMediaApplicationCall_ResponseSyntax) **   <a name="chimesdk-voice-chime_CreateSipMediaApplicationCall-response-SipMediaApplicationCall"></a>
The actual call.
Type: [SipMediaApplicationCall](API_voice-chime_SipMediaApplicationCall.md) object

## Errors
<a name="API_voice-chime_CreateSipMediaApplicationCall_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** AccessDeniedException **
You don't have the permissions needed to run this action.
HTTP Status Code: 403

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The number of customer requests exceeds the request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client isn't authorized to request a resource.
HTTP Status Code: 401

## See Also
<a name="API_voice-chime_CreateSipMediaApplicationCall_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/CreateSipMediaApplicationCall)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/CreateSipMediaApplicationCall)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/CreateSipMediaApplicationCall)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/CreateSipMediaApplicationCall)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/CreateSipMediaApplicationCall)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/CreateSipMediaApplicationCall)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/CreateSipMediaApplicationCall)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/CreateSipMediaApplicationCall)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/CreateSipMediaApplicationCall)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/CreateSipMediaApplicationCall)
