---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetFederationToken.html
---

# GetFederationToken
<a name="API_GetFederationToken"></a>

Supports SAML sign-in for Connect Customer. Retrieves a token for federation. The token is for the Connect Customer user which corresponds to the IAM credentials that were used to invoke this action.

For more information about how SAML sign-in works in Connect Customer, see [Configure SAML with IAM for Connect Customer in the *Connect Customer Administrator Guide*.](https://docs.aws.amazon.com/connect/latest/adminguide/configure-saml.html )

**Note**
This API doesn't support root users. If you try to invoke GetFederationToken with root credentials, an error message similar to the following one appears:
 `Provided identity: Principal: .... User: .... cannot be used for federation with Connect Customer`

## Request Syntax
<a name="API_GetFederationToken_RequestSyntax"></a>

```
GET /user/federate/{{InstanceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFederationToken_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_GetFederationToken_RequestSyntax) **   <a name="connect-GetFederationToken-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_GetFederationToken_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFederationToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Credentials": {
      "AccessToken": "string",
      "AccessTokenExpiration": number,
      "RefreshToken": "string",
      "RefreshTokenExpiration": number
   },
   "SignInUrl": "string",
   "UserArn": "string",
   "UserId": "string"
}
```

## Response Elements
<a name="API_GetFederationToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Credentials](#API_GetFederationToken_ResponseSyntax) **   <a name="connect-GetFederationToken-response-Credentials"></a>
The credentials to use for federation.
Type: [Credentials](API_Credentials.md) object

 ** [SignInUrl](#API_GetFederationToken_ResponseSyntax) **   <a name="connect-GetFederationToken-response-SignInUrl"></a>
The URL to sign into the user's instance.
Type: String

 ** [UserArn](#API_GetFederationToken_ResponseSyntax) **   <a name="connect-GetFederationToken-response-UserArn"></a>
The Amazon Resource Name (ARN) of the user.
Type: String

 ** [UserId](#API_GetFederationToken_ResponseSyntax) **   <a name="connect-GetFederationToken-response-UserId"></a>
The identifier for the user. This can be the ID or the ARN of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_GetFederationToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

 ** UserNotFoundException **
No user with the specified credentials was found in the Connect Customer instance.
HTTP Status Code: 404

## See Also
<a name="API_GetFederationToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetFederationToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetFederationToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetFederationToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetFederationToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetFederationToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetFederationToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetFederationToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetFederationToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetFederationToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetFederationToken)
