---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplicationCall.html
---

# UpdateSipMediaApplicationCall
<a name="API_voice-chime_UpdateSipMediaApplicationCall"></a>

Invokes the AWS Lambda function associated with the SIP media application and transaction ID in an update request. The Lambda function can then return a new set of actions.

## Request Syntax
<a name="API_voice-chime_UpdateSipMediaApplicationCall_RequestSyntax"></a>

```
POST /sip-media-applications/{{sipMediaApplicationId}}/calls/{{transactionId}} HTTP/1.1
Content-type: application/json

{
   "Arguments": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_voice-chime_UpdateSipMediaApplicationCall_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sipMediaApplicationId](#API_voice-chime_UpdateSipMediaApplicationCall_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateSipMediaApplicationCall-request-uri-SipMediaApplicationId"></a>
The ID of the SIP media application handling the call.
Pattern: `.*\S.*`
Required: Yes

 ** [transactionId](#API_voice-chime_UpdateSipMediaApplicationCall_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateSipMediaApplicationCall-request-uri-TransactionId"></a>
The ID of the call transaction.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_UpdateSipMediaApplicationCall_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arguments](#API_voice-chime_UpdateSipMediaApplicationCall_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateSipMediaApplicationCall-request-Arguments"></a>
Arguments made available to the Lambda function as part of the `CALL_UPDATE_REQUESTED` event. Can contain 0-20 key-value pairs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

## Response Syntax
<a name="API_voice-chime_UpdateSipMediaApplicationCall_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "SipMediaApplicationCall": {
      "TransactionId": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_UpdateSipMediaApplicationCall_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [SipMediaApplicationCall](#API_voice-chime_UpdateSipMediaApplicationCall_ResponseSyntax) **   <a name="chimesdk-voice-chime_UpdateSipMediaApplicationCall-response-SipMediaApplicationCall"></a>
A `Call` instance for a SIP media application.
Type: [SipMediaApplicationCall](API_voice-chime_SipMediaApplicationCall.md) object

## Errors
<a name="API_voice-chime_UpdateSipMediaApplicationCall_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
The requested resource couldn't be found.
HTTP Status Code: 404

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
<a name="API_voice-chime_UpdateSipMediaApplicationCall_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/UpdateSipMediaApplicationCall)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/UpdateSipMediaApplicationCall)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/UpdateSipMediaApplicationCall)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/UpdateSipMediaApplicationCall)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/UpdateSipMediaApplicationCall)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/UpdateSipMediaApplicationCall)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/UpdateSipMediaApplicationCall)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/UpdateSipMediaApplicationCall)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/UpdateSipMediaApplicationCall)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/UpdateSipMediaApplicationCall)
