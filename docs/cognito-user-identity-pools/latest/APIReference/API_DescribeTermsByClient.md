---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeTermsByClient.html
---

# DescribeTermsByClient
<a name="API_DescribeTermsByClient"></a>

Returns details for the terms documents that are associated with an app client, identified by the app client ID, user pool ID, and terms name. For more information, see [Terms documents](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-terms-documents).

To call `DescribeTermsByClient`, you must have the `cognito-idp:DescribeTermsByClient` AWS Identity and Access Management (IAM) permission. An IAM policy that denies `cognito-idp:DescribeTerms` also denies requests to `DescribeTermsByClient`.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_DescribeTermsByClient_RequestSyntax"></a>

```
{
   "ClientId": "{{string}}",
   "TermsName": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTermsByClient_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientId](#API_DescribeTermsByClient_RequestSyntax) **   <a name="CognitoUserPools-DescribeTermsByClient-request-ClientId"></a>
The ID of the app client that the terms documents are associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: Yes

 ** [TermsName](#API_DescribeTermsByClient_RequestSyntax) **   <a name="CognitoUserPools-DescribeTermsByClient-request-TermsName"></a>
The name of the terms documents that you want to describe.
Type: String
Pattern: `^(terms-of-use|privacy-policy)$`
Required: Yes

 ** [UserPoolId](#API_DescribeTermsByClient_RequestSyntax) **   <a name="CognitoUserPools-DescribeTermsByClient-request-UserPoolId"></a>
The ID of the user pool that contains the terms documents that you want to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_DescribeTermsByClient_ResponseSyntax"></a>

```
{
   "Terms": {
      "ClientId": "string",
      "CreationDate": number,
      "Enforcement": "string",
      "LastModifiedDate": number,
      "Links": {
         "string" : "string"
      },
      "TermsId": "string",
      "TermsName": "string",
      "TermsSource": "string",
      "UserPoolId": "string"
   }
}
```

## Response Elements
<a name="API_DescribeTermsByClient_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Terms](#API_DescribeTermsByClient_ResponseSyntax) **   <a name="CognitoUserPools-DescribeTermsByClient-response-Terms"></a>
A summary of the requested terms documents, including a unique identifier for later changes to the terms documents.
Type: [TermsType](API_TermsType.md) object

## Errors
<a name="API_DescribeTermsByClient_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DescribeTermsByClient_Examples"></a>

### Example
<a name="API_DescribeTermsByClient_Example_1"></a>

This example retrieves the terms documents for an app client, using the app client ID, the user pool ID, and the terms name.

#### Sample Request
<a name="API_DescribeTermsByClient_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.DescribeTermsByClient
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
   "ClientId": "1example23456789",
   "UserPoolId": "us-east-1_EXAMPLE",
   "TermsName": "privacy-policy"
}
```

#### Sample Response
<a name="API_DescribeTermsByClient_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
    "Terms": {
        "ClientId": "1example23456789",
        "CreationDate": 1755794156.892,
        "Enforcement": "NONE",
        "LastModifiedDate": 1755794201.567,
        "Links": {
            "cognito:default": "https://example.com/privacy/",
            "cognito:french": "https://example.com/fr/privacy/",
            "cognito:portuguese-brazil": "https://example.com/pt/privacy/"
        },
        "TermsId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "TermsName": "privacy-policy",
        "TermsSource": "LINK",
        "UserPoolId": "us-east-1_EXAMPLE"
    }
}
```

## See Also
<a name="API_DescribeTermsByClient_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/DescribeTermsByClient)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/DescribeTermsByClient)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DescribeTermsByClient)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/DescribeTermsByClient)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DescribeTermsByClient)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/DescribeTermsByClient)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/DescribeTermsByClient)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/DescribeTermsByClient)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/DescribeTermsByClient)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DescribeTermsByClient)
