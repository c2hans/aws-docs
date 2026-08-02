---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateFolderPermissions.html
---

# UpdateFolderPermissions
<a name="API_UpdateFolderPermissions"></a>

Updates permissions of a folder.

## Request Syntax
<a name="API_UpdateFolderPermissions_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/folders/{{FolderId}}/permissions HTTP/1.1
Content-type: application/json

{
   "GrantPermissions": [
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
<a name="API_UpdateFolderPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateFolderPermissions_RequestSyntax) **   <a name="QS-UpdateFolderPermissions-request-uri-AwsAccountId"></a>
The ID for the AWS account that contains the folder to update.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [FolderId](#API_UpdateFolderPermissions_RequestSyntax) **   <a name="QS-UpdateFolderPermissions-request-uri-FolderId"></a>
The ID of the folder.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_UpdateFolderPermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GrantPermissions](#API_UpdateFolderPermissions_RequestSyntax) **   <a name="QS-UpdateFolderPermissions-request-GrantPermissions"></a>
The permissions that you want to grant on a resource. Namespace ARNs are not supported `Principal` values for folder permissions.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

 ** [RevokePermissions](#API_UpdateFolderPermissions_RequestSyntax) **   <a name="QS-UpdateFolderPermissions-request-RevokePermissions"></a>
The permissions that you want to revoke from a resource. Namespace ARNs are not supported `Principal` values for folder permissions.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

## Response Syntax
<a name="API_UpdateFolderPermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "FolderId": "string",
   "Permissions": [
      {
         "Actions": [ "string" ],
         "Principal": "string"
      }
   ],
   "RequestId": "string",
   "Status": number
}
```

## Response Elements
<a name="API_UpdateFolderPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateFolderPermissions_ResponseSyntax) **   <a name="QS-UpdateFolderPermissions-response-Arn"></a>
The Amazon Resource Name (ARN) of the folder.
Type: String

 ** [FolderId](#API_UpdateFolderPermissions_ResponseSyntax) **   <a name="QS-UpdateFolderPermissions-response-FolderId"></a>
The ID of the folder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+`

 ** [Permissions](#API_UpdateFolderPermissions_ResponseSyntax) **   <a name="QS-UpdateFolderPermissions-response-Permissions"></a>
Information about the permissions for the folder.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.

 ** [RequestId](#API_UpdateFolderPermissions_ResponseSyntax) **   <a name="QS-UpdateFolderPermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [Status](#API_UpdateFolderPermissions_ResponseSyntax) **   <a name="QS-UpdateFolderPermissions-response-Status"></a>
The HTTP status of the request.
Type: Integer

## Errors
<a name="API_UpdateFolderPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

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
<a name="API_UpdateFolderPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateFolderPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateFolderPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateFolderPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateFolderPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateFolderPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateFolderPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateFolderPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateFolderPermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateFolderPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateFolderPermissions)
