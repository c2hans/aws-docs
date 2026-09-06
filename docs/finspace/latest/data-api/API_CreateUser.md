---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_CreateUser.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# CreateUser
<a name="API_CreateUser"></a>

Creates a new user in FinSpace.

## Request Syntax
<a name="API_CreateUser_RequestSyntax"></a>

```
POST /user HTTP/1.1
Content-type: application/json

{
   "ApiAccess": "{{string}}",
   "apiAccessPrincipalArn": "{{string}}",
   "clientToken": "{{string}}",
   "emailAddress": "{{string}}",
   "firstName": "{{string}}",
   "lastName": "{{string}}",
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateUser_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [emailAddress](#API_CreateUser_RequestSyntax) **   <a name="finspace-CreateUser-request-emailAddress"></a>
The email address of the user that you want to register. The email address serves as a uniquer identifier for each user and cannot be changed after it's created.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 320.
Pattern: `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}`
Required: Yes

 ** [type](#API_CreateUser_RequestSyntax) **   <a name="finspace-CreateUser-request-type"></a>
The option to indicate the type of user. Use one of the following options to specify this parameter:
+  `SUPER_USER` – A user with permission to all the functionality and data in FinSpace.
+  `APP_USER` – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.
Type: String
Valid Values: `SUPER_USER | APP_USER`
Required: Yes

 ** [ApiAccess](#API_CreateUser_RequestSyntax) **   <a name="finspace-CreateUser-request-ApiAccess"></a>
The option to indicate whether the user can use the `GetProgrammaticAccessCredentials` API to obtain credentials that can then be used to access other FinSpace Data API operations.
+  `ENABLED` – The user has permissions to use the APIs.
+  `DISABLED` – The user does not have permissions to use any APIs.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [apiAccessPrincipalArn](#API_CreateUser_RequestSyntax) **   <a name="finspace-CreateUser-request-apiAccessPrincipalArn"></a>
The ARN identifier of an AWS user or role that is allowed to call the `GetProgrammaticAccessCredentials` API to obtain a credentials token for a specific FinSpace user. This must be an IAM role within your FinSpace account.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** [clientToken](#API_CreateUser_RequestSyntax) **   <a name="finspace-CreateUser-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** [firstName](#API_CreateUser_RequestSyntax) **   <a name="finspace-CreateUser-request-firstName"></a>
The first name of the user that you want to register.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*\S.*`
Required: No

 ** [lastName](#API_CreateUser_RequestSyntax) **   <a name="finspace-CreateUser-request-lastName"></a>
The last name of the user that you want to register.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_CreateUser_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "userId": "string"
}
```

## Response Elements
<a name="API_CreateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [userId](#API_CreateUser_ResponseSyntax) **   <a name="finspace-CreateUser-response-userId"></a>
The unique identifier for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `.*\S.*`

## Errors
<a name="API_CreateUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with an existing resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** LimitExceededException **
A limit has exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/CreateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/CreateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/CreateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/CreateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/CreateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/CreateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/CreateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/CreateUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/CreateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/CreateUser)
