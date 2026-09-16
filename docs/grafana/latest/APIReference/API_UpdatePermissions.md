---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdatePermissions.html
---

# UpdatePermissions
<a name="API_UpdatePermissions"></a>

Updates which users in a workspace have the Grafana `Admin` or `Editor` roles.

## Request Syntax
<a name="API_UpdatePermissions_RequestSyntax"></a>

```
PATCH /workspaces/{{workspaceId}}/permissions HTTP/1.1
Content-type: application/json

{
   "updateInstructionBatch": [
      {
         "action": "{{string}}",
         "role": "{{string}}",
         "users": [
            {
               "id": "{{string}}",
               "type": "{{string}}"
            }
         ]
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdatePermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_UpdatePermissions_RequestSyntax) **   <a name="ManagedGrafana-UpdatePermissions-request-uri-workspaceId"></a>
The ID of the workspace to update.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_UpdatePermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [updateInstructionBatch](#API_UpdatePermissions_RequestSyntax) **   <a name="ManagedGrafana-UpdatePermissions-request-updateInstructionBatch"></a>
An array of structures that contain the permission updates to make.
Type: Array of [UpdateInstruction](API_UpdateInstruction.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

## Response Syntax
<a name="API_UpdatePermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "causedBy": {
            "action": "string",
            "role": "string",
            "users": [
               {
                  "id": "string",
                  "type": "string"
               }
            ]
         },
         "code": number,
         "message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_UpdatePermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_UpdatePermissions_ResponseSyntax) **   <a name="ManagedGrafana-UpdatePermissions-response-errors"></a>
An array of structures that contain the errors from the operation, if any.
Type: Array of [UpdateError](API_UpdateError.md) objects

## Errors
<a name="API_UpdatePermissions_Errors"></a>

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
<a name="API_UpdatePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/UpdatePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/UpdatePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/UpdatePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/UpdatePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/UpdatePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/UpdatePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/UpdatePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/UpdatePermissions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/UpdatePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/UpdatePermissions)
