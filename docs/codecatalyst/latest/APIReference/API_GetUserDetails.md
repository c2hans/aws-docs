---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetUserDetails.html
---

# GetUserDetails
<a name="API_GetUserDetails"></a>

Returns information about a user.

## Request Syntax
<a name="API_GetUserDetails_RequestSyntax"></a>

```
GET /userDetails?id={{id}}&userName={{userName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetUserDetails_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetUserDetails_RequestSyntax) **   <a name="codecatalyst-GetUserDetails-request-uri-id"></a>
The system-generated unique ID of the user.
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [userName](#API_GetUserDetails_RequestSyntax) **   <a name="codecatalyst-GetUserDetails-request-uri-userName"></a>
The name of the user as displayed in Amazon CodeCatalyst.
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]{3,100}`

## Request Body
<a name="API_GetUserDetails_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetUserDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "displayName": "string",
   "primaryEmail": {
      "email": "string",
      "verified": boolean
   },
   "userId": "string",
   "userName": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_GetUserDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [displayName](#API_GetUserDetails_ResponseSyntax) **   <a name="codecatalyst-GetUserDetails-response-displayName"></a>
The friendly name displayed for the user in Amazon CodeCatalyst.
Type: String

 ** [primaryEmail](#API_GetUserDetails_ResponseSyntax) **   <a name="codecatalyst-GetUserDetails-response-primaryEmail"></a>
The email address provided by the user when they signed up.
Type: [EmailAddress](API_EmailAddress.md) object

 ** [userId](#API_GetUserDetails_ResponseSyntax) **   <a name="codecatalyst-GetUserDetails-response-userId"></a>
The system-generated unique ID of the user.
Type: String

 ** [userName](#API_GetUserDetails_ResponseSyntax) **   <a name="codecatalyst-GetUserDetails-response-userName"></a>
The name of the user as displayed in Amazon CodeCatalyst.
Type: String

 ** [version](#API_GetUserDetails_ResponseSyntax) **   <a name="codecatalyst-GetUserDetails-response-version"></a>

Type: String

## Errors
<a name="API_GetUserDetails_Errors"></a>

 ** AccessDeniedException **
The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.
HTTP Status Code: 403

 ** ConflictException **
The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.
HTTP Status Code: 400

## See Also
<a name="API_GetUserDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/GetUserDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/GetUserDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/GetUserDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/GetUserDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/GetUserDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/GetUserDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/GetUserDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/GetUserDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/GetUserDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/GetUserDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
