---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html
---

# GetRandomPassword
<a name="API_GetRandomPassword"></a>

Generates a random password. We recommend that you specify the maximum length and include every character type that the system you are generating a password for can support. By default, Secrets Manager uses uppercase and lowercase letters, numbers, and the following characters in passwords: `!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~`

Secrets Manager generates a CloudTrail log entry when you call this action.

 **Required permissions: ** `secretsmanager:GetRandomPassword`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_GetRandomPassword_RequestSyntax"></a>

```
{
   "ExcludeCharacters": "{{string}}",
   "ExcludeLowercase": {{boolean}},
   "ExcludeNumbers": {{boolean}},
   "ExcludePunctuation": {{boolean}},
   "ExcludeUppercase": {{boolean}},
   "IncludeSpace": {{boolean}},
   "PasswordLength": {{number}},
   "RequireEachIncludedType": {{boolean}}
}
```

## Request Parameters
<a name="API_GetRandomPassword_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExcludeCharacters](#API_GetRandomPassword_RequestSyntax) **   <a name="SecretsManager-GetRandomPassword-request-ExcludeCharacters"></a>
A string of the characters that you don't want in the password.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [ExcludeLowercase](#API_GetRandomPassword_RequestSyntax) **   <a name="SecretsManager-GetRandomPassword-request-ExcludeLowercase"></a>
Specifies whether to exclude lowercase letters from the password. If you don't include this switch, the password can contain lowercase letters.
Type: Boolean
Required: No

 ** [ExcludeNumbers](#API_GetRandomPassword_RequestSyntax) **   <a name="SecretsManager-GetRandomPassword-request-ExcludeNumbers"></a>
Specifies whether to exclude numbers from the password. If you don't include this switch, the password can contain numbers.
Type: Boolean
Required: No

 ** [ExcludePunctuation](#API_GetRandomPassword_RequestSyntax) **   <a name="SecretsManager-GetRandomPassword-request-ExcludePunctuation"></a>
Specifies whether to exclude the following punctuation characters from the password: `! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~`. If you don't include this switch, the password can contain punctuation.
Type: Boolean
Required: No

 ** [ExcludeUppercase](#API_GetRandomPassword_RequestSyntax) **   <a name="SecretsManager-GetRandomPassword-request-ExcludeUppercase"></a>
Specifies whether to exclude uppercase letters from the password. If you don't include this switch, the password can contain uppercase letters.
Type: Boolean
Required: No

 ** [IncludeSpace](#API_GetRandomPassword_RequestSyntax) **   <a name="SecretsManager-GetRandomPassword-request-IncludeSpace"></a>
Specifies whether to include the space character. If you include this switch, the password can contain space characters.
Type: Boolean
Required: No

 ** [PasswordLength](#API_GetRandomPassword_RequestSyntax) **   <a name="SecretsManager-GetRandomPassword-request-PasswordLength"></a>
The length of the password. If you don't include this parameter, the default length is 32 characters.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 4096.
Required: No

 ** [RequireEachIncludedType](#API_GetRandomPassword_RequestSyntax) **   <a name="SecretsManager-GetRandomPassword-request-RequireEachIncludedType"></a>
Specifies whether to include at least one upper and lowercase letter, one number, and one punctuation. If you don't include this switch, the password contains at least one of every character type.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetRandomPassword_ResponseSyntax"></a>

```
{
   "RandomPassword": "string"
}
```

## Response Elements
<a name="API_GetRandomPassword_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RandomPassword](#API_GetRandomPassword_ResponseSyntax) **   <a name="SecretsManager-GetRandomPassword-response-RandomPassword"></a>
A string with the password.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

## Errors
<a name="API_GetRandomPassword_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InternalServiceError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidParameterException **
The parameter name or value is invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
A parameter value is not valid for the current state of the resource.
Possible causes:
+ The secret is scheduled for deletion.
+ You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call.
+ The secret is managed by another service, and you must use that service to update it. For more information, see [Secrets managed by other AWS services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).
HTTP Status Code: 400

## Examples
<a name="API_GetRandomPassword_Examples"></a>

### Example
<a name="API_GetRandomPassword_Example_1"></a>

The following example shows how to request a randomly generated password of 20 characters.

#### Sample Request
<a name="API_GetRandomPassword_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.GetRandomPassword
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "PasswordLength": 20
}
```

#### Sample Response
<a name="API_GetRandomPassword_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "RandomPassword":"N+Z43a,>vx7j O8^*<8i3"
}
```

## See Also
<a name="API_GetRandomPassword_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/GetRandomPassword)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/GetRandomPassword)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/GetRandomPassword)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/GetRandomPassword)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/GetRandomPassword)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/GetRandomPassword)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/GetRandomPassword)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/GetRandomPassword)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/GetRandomPassword)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/GetRandomPassword)
