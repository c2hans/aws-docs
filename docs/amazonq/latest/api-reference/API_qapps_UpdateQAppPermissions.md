---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateQAppPermissions.html
---

# UpdateQAppPermissions
<a name="API_qapps_UpdateQAppPermissions"></a>

Updates read permissions for a Amazon Q App in Amazon Q Business application environment instance.

## Request Syntax
<a name="API_qapps_UpdateQAppPermissions_RequestSyntax"></a>

```
POST /apps.updateQAppPermissions HTTP/1.1
instance-id: {{instanceId}}
Content-type: application/json

{
   "appId": "{{string}}",
   "grantPermissions": [
      {
         "action": "{{string}}",
         "principal": "{{string}}"
      }
   ],
   "revokePermissions": [
      {
         "action": "{{string}}",
         "principal": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_qapps_UpdateQAppPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_UpdateQAppPermissions_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQAppPermissions-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

## Request Body
<a name="API_qapps_UpdateQAppPermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appId](#API_qapps_UpdateQAppPermissions_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQAppPermissions-request-appId"></a>
The unique identifier of the Amazon Q App for which permissions are being updated.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** [grantPermissions](#API_qapps_UpdateQAppPermissions_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQAppPermissions-request-grantPermissions"></a>
The list of permissions to grant for the Amazon Q App.
Type: Array of [PermissionInput](API_qapps_PermissionInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [revokePermissions](#API_qapps_UpdateQAppPermissions_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQAppPermissions-request-revokePermissions"></a>
The list of permissions to revoke for the Amazon Q App.
Type: Array of [PermissionInput](API_qapps_PermissionInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_qapps_UpdateQAppPermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appId": "string",
   "permissions": [
      {
         "action": "string",
         "principal": {
            "email": "string",
            "userId": "string",
            "userType": "string"
         }
      }
   ],
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_qapps_UpdateQAppPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appId](#API_qapps_UpdateQAppPermissions_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQAppPermissions-response-appId"></a>
The unique identifier of the Amazon Q App for which permissions were updated.
Type: String

 ** [permissions](#API_qapps_UpdateQAppPermissions_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQAppPermissions-response-permissions"></a>
The updated list of permissions for the Amazon Q App.
Type: Array of [PermissionOutput](API_qapps_PermissionOutput.md) objects

 ** [resourceArn](#API_qapps_UpdateQAppPermissions_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQAppPermissions-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q App for which permissions were updated.
Type: String

## Errors
<a name="API_qapps_UpdateQAppPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
HTTP Status Code: 404

 ** ThrottlingException **
The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.
 ** quotaCode **
The code of the quota that was exceeded
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
 ** serviceCode **
The code for the service where the quota was exceeded
HTTP Status Code: 429

 ** UnauthorizedException **
The client is not authenticated or authorized to perform the requested operation.
HTTP Status Code: 401

 ** ValidationException **
The input failed to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_qapps_UpdateQAppPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/UpdateQAppPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/UpdateQAppPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/UpdateQAppPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/UpdateQAppPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/UpdateQAppPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/UpdateQAppPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/UpdateQAppPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/UpdateQAppPermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/UpdateQAppPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/UpdateQAppPermissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
