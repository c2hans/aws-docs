---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateParticipantAuthentication.html
---

# UpdateParticipantAuthentication
<a name="API_UpdateParticipantAuthentication"></a>

Instructs Connect Customer to resume the authentication process. The subsequent actions depend on the request body contents:
+  **If a code is provided**: Connect retrieves the identity information from Amazon Cognito and imports it into Connect Customer Profiles.
+  **If an error is provided**: The error branch of the Authenticate Customer block is executed.

**Note**
The API returns a success response to acknowledge the request. However, the interaction and exchange of identity information occur asynchronously after the response is returned.

## Request Syntax
<a name="API_UpdateParticipantAuthentication_RequestSyntax"></a>

```
POST /contact/update-participant-authentication HTTP/1.1
Content-type: application/json

{
   "Code": "{{string}}",
   "Error": "{{string}}",
   "ErrorDescription": "{{string}}",
   "InstanceId": "{{string}}",
   "State": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateParticipantAuthentication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateParticipantAuthentication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Code](#API_UpdateParticipantAuthentication_RequestSyntax) **   <a name="connect-UpdateParticipantAuthentication-request-Code"></a>
The `code` query parameter provided by Cognito in the `redirectUri`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Error](#API_UpdateParticipantAuthentication_RequestSyntax) **   <a name="connect-UpdateParticipantAuthentication-request-Error"></a>
The `error` query parameter provided by Cognito in the `redirectUri`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\x20-\x21\x23-\x5B\x5D-\x7E]*$`
Required: No

 ** [ErrorDescription](#API_UpdateParticipantAuthentication_RequestSyntax) **   <a name="connect-UpdateParticipantAuthentication-request-ErrorDescription"></a>
The `error_description` parameter provided by Cognito in the `redirectUri`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\x20-\x21\x23-\x5B\x5D-\x7E]*$`
Required: No

 ** [InstanceId](#API_UpdateParticipantAuthentication_RequestSyntax) **   <a name="connect-UpdateParticipantAuthentication-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [State](#API_UpdateParticipantAuthentication_RequestSyntax) **   <a name="connect-UpdateParticipantAuthentication-request-State"></a>
The `state` query parameter that was provided by Cognito in the `redirectUri`. This will also match the `state` parameter provided in the `AuthenticationUrl` from the [GetAuthenticationUrl](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetAuthenticationUrl.html) response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Response Syntax
<a name="API_UpdateParticipantAuthentication_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateParticipantAuthentication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateParticipantAuthentication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Operation cannot be performed at this time as there is a conflict with another operation or contact state.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateParticipantAuthentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateParticipantAuthentication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateParticipantAuthentication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateParticipantAuthentication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateParticipantAuthentication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateParticipantAuthentication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateParticipantAuthentication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateParticipantAuthentication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateParticipantAuthentication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateParticipantAuthentication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateParticipantAuthentication)
