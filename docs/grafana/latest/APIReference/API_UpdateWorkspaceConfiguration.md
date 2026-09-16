---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspaceConfiguration.html
---

# UpdateWorkspaceConfiguration
<a name="API_UpdateWorkspaceConfiguration"></a>

Updates the configuration string for the given workspace

## Request Syntax
<a name="API_UpdateWorkspaceConfiguration_RequestSyntax"></a>

```
PUT /workspaces/{{workspaceId}}/configuration HTTP/1.1
Content-type: application/json

{
   "configuration": "{{string}}",
   "grafanaVersion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWorkspaceConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_UpdateWorkspaceConfiguration_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspaceConfiguration-request-uri-workspaceId"></a>
The ID of the workspace to update.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_UpdateWorkspaceConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_UpdateWorkspaceConfiguration_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspaceConfiguration-request-configuration"></a>
The new configuration string for the workspace. For more information about the format and configuration options available, see [Working in your Grafana workspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 65536.
Required: Yes

 ** [grafanaVersion](#API_UpdateWorkspaceConfiguration_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspaceConfiguration-request-grafanaVersion"></a>
Specifies the version of Grafana to support in the workspace. If not specified, keeps the current version of the workspace.
Can only be used to upgrade (for example, from 8.4 to 9.4), not downgrade (for example, from 9.4 to 8.4).
To know what versions are available to upgrade to for a specific workspace, see the [ListVersions](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListVersions.html) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_UpdateWorkspaceConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_UpdateWorkspaceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_UpdateWorkspaceConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
A resource was in an inconsistent state during an update or a deletion.
 ** message **
A description of the error.
 ** resourceId **
The ID of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 409

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
<a name="API_UpdateWorkspaceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/UpdateWorkspaceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/UpdateWorkspaceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/UpdateWorkspaceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/UpdateWorkspaceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/UpdateWorkspaceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/UpdateWorkspaceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/UpdateWorkspaceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/UpdateWorkspaceConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/UpdateWorkspaceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/UpdateWorkspaceConfiguration)
