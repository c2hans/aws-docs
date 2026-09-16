---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_DescribeWorkspaceConfiguration.html
---

# DescribeWorkspaceConfiguration
<a name="API_DescribeWorkspaceConfiguration"></a>

Gets the current configuration string for the given workspace.

## Request Syntax
<a name="API_DescribeWorkspaceConfiguration_RequestSyntax"></a>

```
GET /workspaces/{{workspaceId}}/configuration HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeWorkspaceConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_DescribeWorkspaceConfiguration_RequestSyntax) **   <a name="ManagedGrafana-DescribeWorkspaceConfiguration-request-uri-workspaceId"></a>
The ID of the workspace to get configuration information for.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_DescribeWorkspaceConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeWorkspaceConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": "string",
   "grafanaVersion": "string"
}
```

## Response Elements
<a name="API_DescribeWorkspaceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_DescribeWorkspaceConfiguration_ResponseSyntax) **   <a name="ManagedGrafana-DescribeWorkspaceConfiguration-response-configuration"></a>
The configuration string for the workspace that you requested. For more information about the format and configuration options available, see [Working in your Grafana workspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 65536.

 ** [grafanaVersion](#API_DescribeWorkspaceConfiguration_ResponseSyntax) **   <a name="ManagedGrafana-DescribeWorkspaceConfiguration-response-grafanaVersion"></a>
The supported Grafana version for the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_DescribeWorkspaceConfiguration_Errors"></a>

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

## See Also
<a name="API_DescribeWorkspaceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/DescribeWorkspaceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/DescribeWorkspaceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/DescribeWorkspaceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/DescribeWorkspaceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/DescribeWorkspaceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/DescribeWorkspaceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/DescribeWorkspaceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/DescribeWorkspaceConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/DescribeWorkspaceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/DescribeWorkspaceConfiguration)
