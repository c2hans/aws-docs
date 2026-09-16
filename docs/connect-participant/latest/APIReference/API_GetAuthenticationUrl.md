---
source_url: https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_GetAuthenticationUrl.html
---

# GetAuthenticationUrl
<a name="API_connect-participant_GetAuthenticationUrl"></a>

Retrieves the AuthenticationUrl for the current authentication session for the AuthenticateCustomer flow block.

For security recommendations, see [Connect Customer Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat).

**Note**
This API can only be called within one minute of receiving the authenticationInitiated event.
The current supported channel is chat. This API is not supported for Apple Messages for Business, WhatsApp, or SMS chats.

**Note**
 `ConnectionToken` is used for invoking this API instead of `ParticipantToken`.

The Amazon Connect Participant Service APIs do not use [Signature Version 4 authentication](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Request Syntax
<a name="API_connect-participant_GetAuthenticationUrl_RequestSyntax"></a>

```
POST /participant/authentication-url HTTP/1.1
X-Amz-Bearer: {{ConnectionToken}}
Content-type: application/json

{
   "RedirectUri": "{{string}}",
   "SessionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-participant_GetAuthenticationUrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionToken](#API_connect-participant_GetAuthenticationUrl_RequestSyntax) **   <a name="connect-connect-participant_GetAuthenticationUrl-request-ConnectionToken"></a>
The authentication token associated with the participant's connection.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_connect-participant_GetAuthenticationUrl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RedirectUri](#API_connect-participant_GetAuthenticationUrl_RequestSyntax) **   <a name="connect-connect-participant_GetAuthenticationUrl-request-RedirectUri"></a>
The URL where the customer will be redirected after Amazon Cognito authorizes the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [SessionId](#API_connect-participant_GetAuthenticationUrl_RequestSyntax) **   <a name="connect-connect-participant_GetAuthenticationUrl-request-SessionId"></a>
The sessionId provided in the authenticationInitiated event.
Type: String
Length Constraints: Fixed length of 36.
Required: Yes

## Response Syntax
<a name="API_connect-participant_GetAuthenticationUrl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AuthenticationUrl": "string"
}
```

## Response Elements
<a name="API_connect-participant_GetAuthenticationUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthenticationUrl](#API_connect-participant_GetAuthenticationUrl_ResponseSyntax) **   <a name="connect-connect-participant_GetAuthenticationUrl-response-AuthenticationUrl"></a>
The URL where the customer will sign in to the identity provider. This URL contains the authorize endpoint for the Cognito UserPool used in the authentication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2083.

## Errors
<a name="API_connect-participant_GetAuthenticationUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the Amazon Connect service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by Amazon Connect.
HTTP Status Code: 400

## See Also
<a name="API_connect-participant_GetAuthenticationUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectparticipant-2018-09-07/GetAuthenticationUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectparticipant-2018-09-07/GetAuthenticationUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/GetAuthenticationUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectparticipant-2018-09-07/GetAuthenticationUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/GetAuthenticationUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectparticipant-2018-09-07/GetAuthenticationUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectparticipant-2018-09-07/GetAuthenticationUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectparticipant-2018-09-07/GetAuthenticationUrl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectparticipant-2018-09-07/GetAuthenticationUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/GetAuthenticationUrl)
