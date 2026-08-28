---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

Creates an account access manager instance and its AWS account access application in the associated IAM Identity Center instance. This operation is idempotent; calling it multiple times with the same parameters returns the existing application.

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
POST /applications HTTP/1.1
Content-type: application/json

{
   "identitySource": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [identitySource](#API_CreateApplication_RequestSyntax) **   <a name="accountaccess-CreateApplication-request-identitySource"></a>
Specifies the identity source for the application. The identity source defines the IAM Identity Center instance that provides principals for entitlements.
Type: [IdentitySource](API_IdentitySource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [tags](#API_CreateApplication_RequestSyntax) **   <a name="accountaccess-CreateApplication-request-tags"></a>
Specifies the tags to assign to the application.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "string"
}
```

## Response Elements
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_CreateApplication_ResponseSyntax) **   <a name="accountaccess-CreateApplication-response-applicationArn"></a>
The Amazon Resource Name (ARN) of the created application.
Type: String
Length Constraints: Minimum length of 49. Maximum length of 2048.
Pattern: `arn:[a-z0-9-]+:account-access:[a-z0-9]+(-[a-z0-9]+)*:[0-9]{12}:application/[a-zA-Z0-9-]+`

## Errors
<a name="API_CreateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this operation.
HTTP Status Code: 403

 ** AlreadyCreatedException **
The resource you are trying to create already exists. To retrieve the existing resource, use the corresponding Get operation.
HTTP Status Code: 400

 ** ConflictException **
The request conflicts with the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
An internal service error occurred. Try your request again later.
HTTP Status Code: 500

 ** ValidationException **
The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-access-2018-05-10/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-access-2018-05-10/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-access-2018-05-10/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-access-2018-05-10/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-access-2018-05-10/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-access-2018-05-10/CreateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-access-2018-05-10/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/CreateApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account access manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query account-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
