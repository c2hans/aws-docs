---
source_url: https://docs.aws.amazon.com/account-access-runtime/latest/APIReference/API_ListRoles.html
---

# ListRoles
<a name="API_ListRoles"></a>

Returns the roles that you are entitled to access within a tenant. The results are paginated. Use a returned role with `GetRoleCredentials` to obtain temporary credentials. This operation requires the `account_access:read_only` scope.

## Request Syntax
<a name="API_ListRoles_RequestSyntax"></a>

```
GET /access?maxResults={{maxResults}}&nextToken={{nextToken}}&tenantId={{tenantId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRoles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListRoles_RequestSyntax) **   <a name="accountaccessruntime-ListRoles-request-uri-maxResults"></a>
The maximum number of roles to return in a single response. This operation may return fewer or even an empty set of results. If more roles are available than were returned, the response includes a `nextToken` value that you can use to retrieve the next page of results. If you don't specify a value, the service uses a default page size of 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListRoles_RequestSyntax) **   <a name="accountaccessruntime-ListRoles-request-uri-nextToken"></a>
The pagination token from a previous `ListRoles` response. Use it to retrieve the next page of results. Omit this parameter on the first call to retrieve the first page of results.

 ** [tenantId](#API_ListRoles_RequestSyntax) **   <a name="accountaccessruntime-ListRoles-request-uri-tenantId"></a>
The identifier of the tenant whose roles you want to list. A tenant ID begins with `aa-`.
Length Constraints: Minimum length of 3. Maximum length of 24.
Pattern: `[a-z0-9-]+`
Required: Yes

## Request Body
<a name="API_ListRoles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRoles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "roles": [
      {
         "accountId": "string",
         "accountName": "string",
         "roleArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRoles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRoles_ResponseSyntax) **   <a name="accountaccessruntime-ListRoles-response-nextToken"></a>
The pagination token to include in a subsequent `ListRoles` request to retrieve the next page of results. As few as 0 results may be returned on any `ListRoles` call. To list all roles, always check if this field is set and continue making requests until `nextToken` is null. This value is absent when there are no more results to return.
Type: String

 ** [roles](#API_ListRoles_ResponseSyntax) **   <a name="accountaccessruntime-ListRoles-response-roles"></a>
The list of roles that you can access in the tenant. Each entry describes an AWS account and a role.
Type: Array of [AccessDetails](API_AccessDetails.md) objects

## Errors
<a name="API_ListRoles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_ListRoles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-access-runtime-2018-05-10/ListRoles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-access-runtime-2018-05-10/ListRoles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-runtime-2018-05-10/ListRoles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-access-runtime-2018-05-10/ListRoles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-runtime-2018-05-10/ListRoles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-access-runtime-2018-05-10/ListRoles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-access-runtime-2018-05-10/ListRoles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-access-runtime-2018-05-10/ListRoles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/account-access-runtime-2018-05-10/ListRoles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-runtime-2018-05-10/ListRoles)
