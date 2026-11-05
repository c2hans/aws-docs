---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAppPermissions.html
---

# UpdateAppPermissions
<a name="API_UpdateAppPermissions"></a>

Updates the resource permissions for an app. You can grant or revoke permissions and, optionally, change the app's visibility.

## Request Syntax
<a name="API_UpdateAppPermissions_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/apps/{{AppId}}/permissions HTTP/1.1
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
   ],
   "Visibility": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAppPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AppId](#API_UpdateAppPermissions_RequestSyntax) **   <a name="QS-UpdateAppPermissions-request-uri-AppId"></a>
The ID of the app.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [AwsAccountId](#API_UpdateAppPermissions_RequestSyntax) **   <a name="QS-UpdateAppPermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the app.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateAppPermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GrantPermissions](#API_UpdateAppPermissions_RequestSyntax) **   <a name="QS-UpdateAppPermissions-request-GrantPermissions"></a>
The permissions that you want to grant on the app.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

 ** [RevokePermissions](#API_UpdateAppPermissions_RequestSyntax) **   <a name="QS-UpdateAppPermissions-request-RevokePermissions"></a>
The permissions that you want to revoke from the app.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

 ** [Visibility](#API_UpdateAppPermissions_RequestSyntax) **   <a name="QS-UpdateAppPermissions-request-Visibility"></a>
The visibility to set for the app. Currently, only `PRIVATE` is accepted, which removes public (anonymous) access from the app. If you don't specify a value, the app's visibility is unchanged. Setting an app to `PUBLIC` through this operation is not supported.
Type: String
Valid Values: `PRIVATE | PUBLIC`
Required: No

## Response Syntax
<a name="API_UpdateAppPermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppId": "string",
   "Arn": "string",
   "Permissions": [
      {
         "Actions": [ "string" ],
         "Principal": "string"
      }
   ],
   "RequestId": "string",
   "Visibility": "string"
}
```

## Response Elements
<a name="API_UpdateAppPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppId](#API_UpdateAppPermissions_ResponseSyntax) **   <a name="QS-UpdateAppPermissions-response-AppId"></a>
The ID of the app.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [Arn](#API_UpdateAppPermissions_ResponseSyntax) **   <a name="QS-UpdateAppPermissions-response-Arn"></a>
The Amazon Resource Name (ARN) of the app.
Type: String

 ** [Permissions](#API_UpdateAppPermissions_ResponseSyntax) **   <a name="QS-UpdateAppPermissions-response-Permissions"></a>
The updated resource permissions for the app.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.

 ** [RequestId](#API_UpdateAppPermissions_ResponseSyntax) **   <a name="QS-UpdateAppPermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [Visibility](#API_UpdateAppPermissions_ResponseSyntax) **   <a name="QS-UpdateAppPermissions-response-Visibility"></a>
The visibility of the app after the update (`PRIVATE` or `PUBLIC`).
Type: String
Valid Values: `PRIVATE | PUBLIC`

## Errors
<a name="API_UpdateAppPermissions_Errors"></a>

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

 ** InvalidParameterException **
One or more parameter has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

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

## See Also
<a name="API_UpdateAppPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateAppPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateAppPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateAppPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateAppPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateAppPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateAppPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateAppPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateAppPermissions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateAppPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateAppPermissions)
