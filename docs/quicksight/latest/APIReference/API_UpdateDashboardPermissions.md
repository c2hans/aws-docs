---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardPermissions.html
---

# UpdateDashboardPermissions
<a name="API_UpdateDashboardPermissions"></a>

Updates read and write permissions on a dashboard.

## Request Syntax
<a name="API_UpdateDashboardPermissions_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}}/permissions HTTP/1.1
Content-type: application/json

{
   "GrantLinkPermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "GrantPermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "RevokeLinkPermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "RevokePermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateDashboardPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateDashboardPermissions_RequestSyntax) **   <a name="QS-UpdateDashboardPermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the dashboard whose permissions you're updating.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DashboardId](#API_UpdateDashboardPermissions_RequestSyntax) **   <a name="QS-UpdateDashboardPermissions-request-uri-DashboardId"></a>
The ID for the dashboard.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_UpdateDashboardPermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GrantLinkPermissions](#API_UpdateDashboardPermissions_RequestSyntax) **   <a name="QS-UpdateDashboardPermissions-request-GrantLinkPermissions"></a>
Grants link permissions to all users in a defined namespace.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** [GrantPermissions](#API_UpdateDashboardPermissions_RequestSyntax) **   <a name="QS-UpdateDashboardPermissions-request-GrantPermissions"></a>
The permissions that you want to grant on this resource.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** [RevokeLinkPermissions](#API_UpdateDashboardPermissions_RequestSyntax) **   <a name="QS-UpdateDashboardPermissions-request-RevokeLinkPermissions"></a>
Revokes link permissions from all users in a defined namespace.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** [RevokePermissions](#API_UpdateDashboardPermissions_RequestSyntax) **   <a name="QS-UpdateDashboardPermissions-request-RevokePermissions"></a>
The permissions that you want to revoke from this resource.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_UpdateDashboardPermissions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DashboardArn": "string",
   "DashboardId": "string",
   "LinkSharingConfiguration": {
      "Permissions": [
         {
            "Actions": [ "string" ],
            "Principal": "string"
         }
      ]
   },
   "Permissions": [
      {
         "Actions": [ "string" ],
         "Principal": "string"
      }
   ],
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateDashboardPermissions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateDashboardPermissions_ResponseSyntax) **   <a name="QS-UpdateDashboardPermissions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DashboardArn](#API_UpdateDashboardPermissions_ResponseSyntax) **   <a name="QS-UpdateDashboardPermissions-response-DashboardArn"></a>
The Amazon Resource Name (ARN) of the dashboard.
Type: String

 ** [DashboardId](#API_UpdateDashboardPermissions_ResponseSyntax) **   <a name="QS-UpdateDashboardPermissions-response-DashboardId"></a>
The ID for the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`

 ** [LinkSharingConfiguration](#API_UpdateDashboardPermissions_ResponseSyntax) **   <a name="QS-UpdateDashboardPermissions-response-LinkSharingConfiguration"></a>
Updates the permissions of a shared link to an Quick Sight dashboard.
Type: [LinkSharingConfiguration](API_LinkSharingConfiguration.md) object

 ** [Permissions](#API_UpdateDashboardPermissions_ResponseSyntax) **   <a name="QS-UpdateDashboardPermissions-response-Permissions"></a>
Information about the permissions on the dashboard.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.

 ** [RequestId](#API_UpdateDashboardPermissions_ResponseSyntax) **   <a name="QS-UpdateDashboardPermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateDashboardPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_UpdateDashboardPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateDashboardPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateDashboardPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateDashboardPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateDashboardPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateDashboardPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateDashboardPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateDashboardPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateDashboardPermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateDashboardPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateDashboardPermissions)
