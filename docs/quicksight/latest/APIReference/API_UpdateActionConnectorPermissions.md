---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateActionConnectorPermissions.html
---

# UpdateActionConnectorPermissions
<a name="API_UpdateActionConnectorPermissions"></a>

Updates the permissions for an action connector by granting or revoking access for specific users and groups. You can control who can view, use, or manage the action connector.

## Request Syntax
<a name="API_UpdateActionConnectorPermissions_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/action-connectors/{{ActionConnectorId}}/permissions HTTP/1.1
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
<a name="API_UpdateActionConnectorPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ActionConnectorId](#API_UpdateActionConnectorPermissions_RequestSyntax) **   <a name="QS-UpdateActionConnectorPermissions-request-uri-ActionConnectorId"></a>
The unique identifier of the action connector whose permissions you want to update.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** [AwsAccountId](#API_UpdateActionConnectorPermissions_RequestSyntax) **   <a name="QS-UpdateActionConnectorPermissions-request-uri-AwsAccountId"></a>
The AWS account ID that contains the action connector.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateActionConnectorPermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GrantPermissions](#API_UpdateActionConnectorPermissions_RequestSyntax) **   <a name="QS-UpdateActionConnectorPermissions-request-GrantPermissions"></a>
The permissions to grant to users and groups for this action connector.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

 ** [RevokePermissions](#API_UpdateActionConnectorPermissions_RequestSyntax) **   <a name="QS-UpdateActionConnectorPermissions-request-RevokePermissions"></a>
The permissions to revoke from users and groups for this action connector.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

## Response Syntax
<a name="API_UpdateActionConnectorPermissions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "ActionConnectorId": "string",
   "Arn": "string",
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
<a name="API_UpdateActionConnectorPermissions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateActionConnectorPermissions_ResponseSyntax) **   <a name="QS-UpdateActionConnectorPermissions-response-Status"></a>
The HTTP status code of the request.

The following data is returned in JSON format by the service.

 ** [ActionConnectorId](#API_UpdateActionConnectorPermissions_ResponseSyntax) **   <a name="QS-UpdateActionConnectorPermissions-response-ActionConnectorId"></a>
The unique identifier of the action connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`

 ** [Arn](#API_UpdateActionConnectorPermissions_ResponseSyntax) **   <a name="QS-UpdateActionConnectorPermissions-response-Arn"></a>
The Amazon Resource Name (ARN) of the action connector.
Type: String

 ** [Permissions](#API_UpdateActionConnectorPermissions_ResponseSyntax) **   <a name="QS-UpdateActionConnectorPermissions-response-Permissions"></a>
The updated permissions configuration for the action connector.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.

 ** [RequestId](#API_UpdateActionConnectorPermissions_ResponseSyntax) **   <a name="QS-UpdateActionConnectorPermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateActionConnectorPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

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
<a name="API_UpdateActionConnectorPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateActionConnectorPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateActionConnectorPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateActionConnectorPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateActionConnectorPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateActionConnectorPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateActionConnectorPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateActionConnectorPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateActionConnectorPermissions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateActionConnectorPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateActionConnectorPermissions)
