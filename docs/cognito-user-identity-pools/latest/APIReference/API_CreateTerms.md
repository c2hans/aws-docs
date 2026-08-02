---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateTerms.html
---

# CreateTerms
<a name="API_CreateTerms"></a>

Creates terms documents for the requested app client. When Terms and conditions and Privacy policy documents are configured, the app client displays links to them in the sign-up page of managed login for the app client.

You can provide URLs for terms documents in the languages that are supported by [managed login localization](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-localization). Amazon Cognito directs users to the terms documents for their current language, with fallback to `default` if no document exists for the language.

Each request accepts one type of terms document and a map of language-to-link for that document type. You must provide both types of terms documents in at least one language before Amazon Cognito displays your terms documents. Supply each type in separate requests.

For more information, see [Terms documents](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-terms-documents).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_CreateTerms_RequestSyntax"></a>

```
{
   "ClientId": "{{string}}",
   "Enforcement": "{{string}}",
   "Links": {
      "{{string}}" : "{{string}}"
   },
   "TermsName": "{{string}}",
   "TermsSource": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateTerms_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientId](#API_CreateTerms_RequestSyntax) **   <a name="CognitoUserPools-CreateTerms-request-ClientId"></a>
The ID of the app client where you want to create terms documents. Must be an app client in the requested user pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: Yes

 ** [Enforcement](#API_CreateTerms_RequestSyntax) **   <a name="CognitoUserPools-CreateTerms-request-Enforcement"></a>
This parameter is reserved for future use and currently accepts only one value.
Type: String
Valid Values: `NONE`
Required: Yes

 ** [Links](#API_CreateTerms_RequestSyntax) **   <a name="CognitoUserPools-CreateTerms-request-Links"></a>
A map of URLs to languages. For each localized language that will view the requested `TermsName`, assign a URL. A selection of `cognito:default` displays for all languages that don't have a language-specific URL.
For example, `"cognito:default": "https://terms.example.com", "cognito:spanish": "https://terms.example.com/es"`.
Type: String to string map
Map Entries: Maximum number of 13 items.
Key Pattern: `^cognito:(default|dutch|english|french|spanish|german|bahasa-indonesia|italian|japanese|korean|portuguese-brazil|chinese-(simplified|traditional))$`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `^[\p{L}\p{M}\p{S}\p{N}\p{P}]+$`
Required: No

 ** [TermsName](#API_CreateTerms_RequestSyntax) **   <a name="CognitoUserPools-CreateTerms-request-TermsName"></a>
A friendly name for the document that you want to create in the current request. Must begin with `terms-of-use` or `privacy-policy` as identification of the document type. Provide URLs for both `terms-of-use` and `privacy-policy` in separate requests.
Type: String
Pattern: `^(terms-of-use|privacy-policy)$`
Required: Yes

 ** [TermsSource](#API_CreateTerms_RequestSyntax) **   <a name="CognitoUserPools-CreateTerms-request-TermsSource"></a>
This parameter is reserved for future use and currently accepts only one value.
Type: String
Valid Values: `LINK`
Required: Yes

 ** [UserPoolId](#API_CreateTerms_RequestSyntax) **   <a name="CognitoUserPools-CreateTerms-request-UserPoolId"></a>
The ID of the user pool where you want to create terms documents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_CreateTerms_ResponseSyntax"></a>

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
<a name="API_CreateTerms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Terms](#API_CreateTerms_ResponseSyntax) **   <a name="CognitoUserPools-CreateTerms-response-Terms"></a>
A summary of your terms documents. Includes a unique identifier for later changes to the terms documents.
Type: [TermsType](API_TermsType.md) object

## Errors
<a name="API_CreateTerms_Errors"></a>

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

 ** LimitExceededException **
This exception is thrown when a user exceeds the limit for a requested AWS resource.
 ** message **
The message returned when Amazon Cognito throws a limit exceeded exception.
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

 ** TermsExistsException **
Terms document names must be unique to the app client. This exception is thrown when you attempt to create terms documents with a duplicate `TermsName`.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## Examples
<a name="API_CreateTerms_Examples"></a>

### Example
<a name="API_CreateTerms_Example_1"></a>

The following example operation creates a privacy policy terms document for app client `1example23456789` with URLs for default, French, and Portuguese (Brazil) languages.

#### Sample Request
<a name="API_CreateTerms_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.CreateTerms
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
   "ClientId": "1example23456789",
   "Enforcement": "NONE",
   "Links": {
      "cognito:default" : "https://example.com/privacy/",
      "cognito:french" : "https://example.com/fr/privacy/",
      "cognito:portuguese-brazil" : "https://example.com/pt/privacy/"
   },
   "TermsName": "privacy-policy",
   "TermsSource": "LINK",
   "UserPoolId": "us-east-1_EXAMPLE"
}
```

#### Sample Response
<a name="API_CreateTerms_Example_1_Response"></a>

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
        "CreationDate": 1755793809.755,
        "Enforcement": "NONE",
        "LastModifiedDate": 1755793845.123,
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
<a name="API_CreateTerms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/CreateTerms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/CreateTerms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CreateTerms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/CreateTerms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CreateTerms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/CreateTerms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/CreateTerms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/CreateTerms)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/CreateTerms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CreateTerms)
