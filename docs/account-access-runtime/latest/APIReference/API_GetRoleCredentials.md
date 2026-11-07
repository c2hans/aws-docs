---
source_url: https://docs.aws.amazon.com/account-access-runtime/latest/APIReference/API_GetRoleCredentials.html
---

# GetRoleCredentials
<a name="API_GetRoleCredentials"></a>

Returns temporary AWS credentials for a role that you are entitled to assume within a tenant. You can use these credentials for programmatic access with the AWS CLI or an AWS SDK. If you aren't entitled to the role, the request fails with an `AccessDeniedException` error. This operation requires the `account_access:assume` scope.

## Request Syntax
<a name="API_GetRoleCredentials_RequestSyntax"></a>

```
GET /access/credentials?accessType={{accessType}}&roleArn={{roleArn}}&sessionDuration={{sessionDuration}}&sessionName={{sessionName}}&tenantId={{tenantId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRoleCredentials_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessType](#API_GetRoleCredentials_RequestSyntax) **   <a name="accountaccessruntime-GetRoleCredentials-request-uri-accessType"></a>
The type of access to request for the role. Specify `PROGRAMMATIC_ACCESS` to receive access key credentials for use with the AWS CLI or an AWS SDK.
Valid Values: `PROGRAMMATIC_ACCESS`
Required: Yes

 ** [roleArn](#API_GetRoleCredentials_RequestSyntax) **   <a name="accountaccessruntime-GetRoleCredentials-request-uri-roleArn"></a>
The Amazon Resource Name (ARN) of the role to retrieve credentials for. You must be entitled to assume this role.
Required: Yes

 ** [sessionDuration](#API_GetRoleCredentials_RequestSyntax) **   <a name="accountaccessruntime-GetRoleCredentials-request-uri-sessionDuration"></a>
The duration, in seconds, that the returned credentials remain valid. If you don't specify a value, the service uses the maximum session duration configured for the role. The value you specify can't exceed the role's maximum session duration.
Valid Range: Minimum value of 900. Maximum value of 43200.

 ** [sessionName](#API_GetRoleCredentials_RequestSyntax) **   <a name="accountaccessruntime-GetRoleCredentials-request-uri-sessionName"></a>
An optional name for the role session. The session name appears in AWS CloudTrail logs for the assumed role session. If you don't specify a session name, your AWS IAM Identity Center user ID is used as a default.
Pattern: `[a-zA-Z0-9_+=,.@-]{2,64}`

 ** [tenantId](#API_GetRoleCredentials_RequestSyntax) **   <a name="accountaccessruntime-GetRoleCredentials-request-uri-tenantId"></a>
The identifier of the tenant that the request applies to. A tenant ID begins with `aa-`.
Length Constraints: Minimum length of 3. Maximum length of 24.
Pattern: `[a-z0-9-]+`
Required: Yes

## Request Body
<a name="API_GetRoleCredentials_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRoleCredentials_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "credentialsDetails": { ... }
}
```

## Response Elements
<a name="API_GetRoleCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [credentialsDetails](#API_GetRoleCredentials_ResponseSyntax) **   <a name="accountaccessruntime-GetRoleCredentials-response-credentialsDetails"></a>
The temporary credentials that the service returns for the requested role.
Type: [CredentialsDetails](API_CredentialsDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_GetRoleCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are authenticated but not authorized to perform the requested action, such as assuming a role that you aren't entitled to. This error returns an HTTP 403 status code.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry the request. If the problem persists, contact AWS Support. This error returns an HTTP 500 status code.
HTTP Status Code: 500

 ** ThrottlingException **
The request rate exceeded the allowed limit. Reduce your request rate, and then retry the request. This error returns an HTTP 429 status code.
HTTP Status Code: 429

 ** UnauthorizedException **
The bearer token is missing, invalid, or expired. Obtain a new token, and then retry the request. This error returns an HTTP 401 status code.
HTTP Status Code: 401

 ** ValidationException **
The request is missing a required parameter, or a parameter value doesn't satisfy its constraints, such as its length or pattern. Correct the input, and then retry the request. This error returns an HTTP 400 status code.
HTTP Status Code: 400

## Examples
<a name="API_GetRoleCredentials_Examples"></a>

### Example – Response format
<a name="API_GetRoleCredentials_Example_1"></a>

 `GetRoleCredentials` response format:

#### Sample Response
<a name="API_GetRoleCredentials_Example_1_Response"></a>

```
{
   "credentialsDetails": {
      "programmaticAccess": {
         "accessKeyId": "<access-key-id>",
         "secretAccessKey": "<secret-access-key>",
         "sessionToken": "<session-token>",
         "expiresAt": <expires-at>
      }
   }
}
```

## See Also
<a name="API_GetRoleCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-access-runtime-2018-05-10/GetRoleCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-access-runtime-2018-05-10/GetRoleCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-runtime-2018-05-10/GetRoleCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-access-runtime-2018-05-10/GetRoleCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-runtime-2018-05-10/GetRoleCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-access-runtime-2018-05-10/GetRoleCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-access-runtime-2018-05-10/GetRoleCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-access-runtime-2018-05-10/GetRoleCredentials)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/account-access-runtime-2018-05-10/GetRoleCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-runtime-2018-05-10/GetRoleCredentials)
