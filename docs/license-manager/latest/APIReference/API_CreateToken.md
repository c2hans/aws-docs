---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateToken.html
---

# CreateToken
<a name="API_CreateToken"></a>

Creates a long-lived token.

A refresh token is a JWT token used to get an access token. With an access token, you can call AssumeRoleWithWebIdentity to get role credentials that you can use to call License Manager to manage the specified license.

## Request Syntax
<a name="API_CreateToken_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "ExpirationInDays": {{number}},
   "LicenseArn": "{{string}}",
   "RoleArns": [ "{{string}}" ],
   "TokenProperties": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_CreateToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateToken_RequestSyntax) **   <a name="licensemanager-CreateToken-request-ClientToken"></a>
Idempotency token, valid for 10 minutes.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: Yes

 ** [ExpirationInDays](#API_CreateToken_RequestSyntax) **   <a name="licensemanager-CreateToken-request-ExpirationInDays"></a>
Token expiration, in days, counted from token creation. The default is 365 days.
Type: Integer
Required: No

 ** [LicenseArn](#API_CreateToken_RequestSyntax) **   <a name="licensemanager-CreateToken-request-LicenseArn"></a>
Amazon Resource Name (ARN) of the license. The ARN is mapped to the aud claim of the JWT token.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** [RoleArns](#API_CreateToken_RequestSyntax) **   <a name="licensemanager-CreateToken-request-RoleArns"></a>
Amazon Resource Name (ARN) of the IAM roles to embed in the token. License Manager does not check whether the roles are in use.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** [TokenProperties](#API_CreateToken_RequestSyntax) **   <a name="licensemanager-CreateToken-request-TokenProperties"></a>
Data specified by the caller to be included in the JWT token. The data is mapped to the amr claim of the JWT token.
Type: Array of strings
Array Members: Maximum number of 3 items.
Required: No

## Response Syntax
<a name="API_CreateToken_ResponseSyntax"></a>

```
{
   "Token": "string",
   "TokenId": "string",
   "TokenType": "string"
}
```

## Response Elements
<a name="API_CreateToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Token](#API_CreateToken_ResponseSyntax) **   <a name="licensemanager-CreateToken-response-Token"></a>
Refresh token, encoded as a JWT token.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `\S+`

 ** [TokenId](#API_CreateToken_ResponseSyntax) **   <a name="licensemanager-CreateToken-response-TokenId"></a>
Token ID.
Type: String

 ** [TokenType](#API_CreateToken_ResponseSyntax) **   <a name="licensemanager-CreateToken-response-TokenType"></a>
Token type.
Type: String
Valid Values: `REFRESH_TOKEN`

## Errors
<a name="API_CreateToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** RedirectException **
This is not the correct Region for the resource. Try again.
HTTP Status Code: 400

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource cannot be found.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_CreateToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/CreateToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/CreateToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/CreateToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/CreateToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/CreateToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/CreateToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/CreateToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/CreateToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/CreateToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/CreateToken)
