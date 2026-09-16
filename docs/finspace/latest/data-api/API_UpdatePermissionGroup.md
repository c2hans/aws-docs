---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_UpdatePermissionGroup.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# UpdatePermissionGroup
<a name="API_UpdatePermissionGroup"></a>

Modifies the details of a permission group. You cannot modify a `permissionGroupID`.

## Request Syntax
<a name="API_UpdatePermissionGroup_RequestSyntax"></a>

```
PUT /permission-group/{{permissionGroupId}} HTTP/1.1
Content-type: application/json

{
   "applicationPermissions": [ "{{string}}" ],
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePermissionGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [permissionGroupId](#API_UpdatePermissionGroup_RequestSyntax) **   <a name="finspace-UpdatePermissionGroup-request-uri-permissionGroupId"></a>
The unique identifier for the permission group to update.
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_UpdatePermissionGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationPermissions](#API_UpdatePermissionGroup_RequestSyntax) **   <a name="finspace-UpdatePermissionGroup-request-applicationPermissions"></a>
The permissions that are granted to a specific group for accessing the FinSpace application.
When assigning application permissions, be aware that the permission `ManageUsersAndGroups` allows users to grant themselves or others access to any functionality in their FinSpace environment's application. It should only be granted to trusted users.
+  `CreateDataset` – Group members can create new datasets.
+  `ManageClusters` – Group members can manage Apache Spark clusters from FinSpace notebooks.
+  `ManageUsersAndGroups` – Group members can manage users and permission groups. This is a privileged permission that allows users to grant themselves or others access to any functionality in the application. It should only be granted to trusted users.
+  `ManageAttributeSets` – Group members can manage attribute sets.
+  `ViewAuditData` – Group members can view audit data.
+  `AccessNotebooks` – Group members will have access to FinSpace notebooks.
+  `GetTemporaryCredentials` – Group members can get temporary API credentials.
Type: Array of strings
Valid Values: `CreateDataset | ManageClusters | ManageUsersAndGroups | ManageAttributeSets | ViewAuditData | AccessNotebooks | GetTemporaryCredentials`
Required: No

 ** [clientToken](#API_UpdatePermissionGroup_RequestSyntax) **   <a name="finspace-UpdatePermissionGroup-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** [description](#API_UpdatePermissionGroup_RequestSyntax) **   <a name="finspace-UpdatePermissionGroup-request-description"></a>
A brief description for the permission group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Pattern: `[\s\S]*`
Required: No

 ** [name](#API_UpdatePermissionGroup_RequestSyntax) **   <a name="finspace-UpdatePermissionGroup-request-name"></a>
The name of the permission group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_UpdatePermissionGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "permissionGroupId": "string"
}
```

## Response Elements
<a name="API_UpdatePermissionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [permissionGroupId](#API_UpdatePermissionGroup_ResponseSyntax) **   <a name="finspace-UpdatePermissionGroup-response-permissionGroupId"></a>
The unique identifier for the updated permission group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `.*\S.*`

## Errors
<a name="API_UpdatePermissionGroup_Errors"></a>

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

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePermissionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/UpdatePermissionGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/UpdatePermissionGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/UpdatePermissionGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/UpdatePermissionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/UpdatePermissionGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/UpdatePermissionGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/UpdatePermissionGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/UpdatePermissionGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/UpdatePermissionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/UpdatePermissionGroup)
