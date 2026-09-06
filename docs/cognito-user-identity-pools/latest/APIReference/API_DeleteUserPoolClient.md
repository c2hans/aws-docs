---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolClient.html
---

# DeleteUserPoolClient
<a name="API_DeleteUserPoolClient"></a>

Deletes a user pool app client. After you delete an app client, users can no longer sign in to the associated application.

## Request Syntax
<a name="API_DeleteUserPoolClient_RequestSyntax"></a>

```
{
   "ClientId": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteUserPoolClient_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientId](#API_DeleteUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-DeleteUserPoolClient-request-ClientId"></a>
The ID of the user pool app client that you want to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: Yes

 ** [UserPoolId](#API_DeleteUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-DeleteUserPoolClient-request-UserPoolId"></a>
The ID of the user pool where you want to delete the client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Elements
<a name="API_DeleteUserPoolClient_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteUserPoolClient_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
This exception is thrown if two or more modifications are happening concurrently.
 ** message **
The message provided when the concurrent exception is thrown.
HTTP Status Code: 400

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## Examples
<a name="API_DeleteUserPoolClient_Examples"></a>

### Example
<a name="API_DeleteUserPoolClient_Example_1"></a>

The following example request deletes the user pool client with ID `1example23456789` from user pool `us-west-2_EXAMPLE`.

#### Sample Request
<a name="API_DeleteUserPoolClient_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.DeleteUserPoolClient
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "ClientId": "1example23456789",
   "UserPoolId": "us-west-2_EXAMPLE"
}
```

## See Also
<a name="API_DeleteUserPoolClient_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/DeleteUserPoolClient)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/DeleteUserPoolClient)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DeleteUserPoolClient)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/DeleteUserPoolClient)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DeleteUserPoolClient)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/DeleteUserPoolClient)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/DeleteUserPoolClient)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/DeleteUserPoolClient)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/DeleteUserPoolClient)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DeleteUserPoolClient)
