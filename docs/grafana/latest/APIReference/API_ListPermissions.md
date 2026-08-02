---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListPermissions.html
---

# ListPermissions
<a name="API_ListPermissions"></a>

Lists the users and groups who have the Grafana `Admin` and `Editor` roles in this workspace. If you use this operation without specifying `userId` or `groupId`, the operation returns the roles of all users and groups. If you specify a `userId` or a `groupId`, only the roles for that user or group are returned. If you do this, you can specify only one `userId` or one `groupId`.

## Request Syntax
<a name="API_ListPermissions_RequestSyntax"></a>

```
GET /workspaces/{{workspaceId}}/permissions?groupId={{groupId}}&maxResults={{maxResults}}&nextToken={{nextToken}}&userId={{userId}}&userType={{userType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [groupId](#API_ListPermissions_RequestSyntax) **   <a name="ManagedGrafana-ListPermissions-request-uri-groupId"></a>
(Optional) Limits the results to only the group that matches this ID.
Length Constraints: Minimum length of 1. Maximum length of 47.

 ** [maxResults](#API_ListPermissions_RequestSyntax) **   <a name="ManagedGrafana-ListPermissions-request-uri-maxResults"></a>
The maximum number of results to include in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListPermissions_RequestSyntax) **   <a name="ManagedGrafana-ListPermissions-request-uri-nextToken"></a>
The token to use when requesting the next set of results. You received this token from a previous `ListPermissions` operation.

 ** [userId](#API_ListPermissions_RequestSyntax) **   <a name="ManagedGrafana-ListPermissions-request-uri-userId"></a>
(Optional) Limits the results to only the user that matches this ID.
Length Constraints: Minimum length of 1. Maximum length of 47.

 ** [userType](#API_ListPermissions_RequestSyntax) **   <a name="ManagedGrafana-ListPermissions-request-uri-userType"></a>
(Optional) If you specify `SSO_USER`, then only the permissions of IAM Identity Center users are returned. If you specify `SSO_GROUP`, only the permissions of IAM Identity Center groups are returned.
Valid Values: `SSO_USER | SSO_GROUP`

 ** [workspaceId](#API_ListPermissions_RequestSyntax) **   <a name="ManagedGrafana-ListPermissions-request-uri-workspaceId"></a>
The ID of the workspace to list permissions for. This parameter is required.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_ListPermissions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "permissions": [
      {
         "role": "string",
         "user": {
            "id": "string",
            "type": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPermissions_ResponseSyntax) **   <a name="ManagedGrafana-ListPermissions-response-nextToken"></a>
The token to use in a subsequent `ListPermissions` operation to return the next set of results.
Type: String

 ** [permissions](#API_ListPermissions_ResponseSyntax) **   <a name="ManagedGrafana-ListPermissions-response-permissions"></a>
The permissions returned by the operation.
Type: Array of [PermissionEntry](API_PermissionEntry.md) objects

## Errors
<a name="API_ListPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error while processing the request. Retry the request.
 ** message **
A description of the error.
 ** retryAfterSeconds **
How long to wait before you retry this operation.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** message **
The value of a parameter in the request caused an error.
 ** resourceId **
The ID of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling. Retry the request.
 ** message **
A description of the error.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The value of a parameter in the request caused an error.
 ** fieldList **
A list of fields that might be associated with the error.
 ** message **
A description of the error.
 ** reason **
The reason that the operation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/ListPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/ListPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/ListPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/ListPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/ListPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/ListPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/ListPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/ListPermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/ListPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/ListPermissions)
