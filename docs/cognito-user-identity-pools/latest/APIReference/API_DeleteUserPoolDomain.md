---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolDomain.html
---

# DeleteUserPoolDomain
<a name="API_DeleteUserPoolDomain"></a>

Given a user pool ID and domain identifier, deletes a user pool domain. After you delete a user pool domain, your managed login pages and authorization server are no longer available.

## Request Syntax
<a name="API_DeleteUserPoolDomain_RequestSyntax"></a>

```
{
   "Domain": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteUserPoolDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Domain](#API_DeleteUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-DeleteUserPoolDomain-request-Domain"></a>
The domain that you want to delete. For custom domains, this is the fully-qualified domain name like `auth.example.com`. For Amazon Cognito prefix domains, this is the prefix alone, like `myprefix`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?$`
Required: Yes

 ** [UserPoolId](#API_DeleteUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-DeleteUserPoolDomain-request-UserPoolId"></a>
The ID of the user pool where you want to delete the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Elements
<a name="API_DeleteUserPoolDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteUserPoolDomain_Errors"></a>

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

## Examples
<a name="API_DeleteUserPoolDomain_Examples"></a>

### Example
<a name="API_DeleteUserPoolDomain_Example_1"></a>

The following example request deletes the Amazon Cognito prefix domain `mytestdomain` from the user pool `us-west-2_EXAMPLE`.

#### Sample Request
<a name="API_DeleteUserPoolDomain_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.DeleteUserPoolDomain
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "Domain": "mytestdomain",
   "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_DeleteUserPoolDomain_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{}
```

## See Also
<a name="API_DeleteUserPoolDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/DeleteUserPoolDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/DeleteUserPoolDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DeleteUserPoolDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/DeleteUserPoolDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DeleteUserPoolDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/DeleteUserPoolDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/DeleteUserPoolDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/DeleteUserPoolDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/DeleteUserPoolDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DeleteUserPoolDomain)
