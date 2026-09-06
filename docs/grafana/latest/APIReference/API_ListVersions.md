---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListVersions.html
---

# ListVersions
<a name="API_ListVersions"></a>

Lists available versions of Grafana. These are available when calling `CreateWorkspace`. Optionally, include a workspace to list the versions to which it can be upgraded.

## Request Syntax
<a name="API_ListVersions_RequestSyntax"></a>

```
GET /versions?maxResults={{maxResults}}&nextToken={{nextToken}}&workspace-id={{workspaceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListVersions_RequestSyntax) **   <a name="ManagedGrafana-ListVersions-request-uri-maxResults"></a>
The maximum number of results to include in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListVersions_RequestSyntax) **   <a name="ManagedGrafana-ListVersions-request-uri-nextToken"></a>
The token to use when requesting the next set of results. You receive this token from a previous `ListVersions` operation.

 ** [workspaceId](#API_ListVersions_RequestSyntax) **   <a name="ManagedGrafana-ListVersions-request-uri-workspaceId"></a>
The ID of the workspace to list the available upgrade versions. If not included, lists all versions of Grafana that are supported for `CreateWorkspace`.
Pattern: `g-[0-9a-f]{10}`

## Request Body
<a name="API_ListVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "grafanaVersions": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [grafanaVersions](#API_ListVersions_ResponseSyntax) **   <a name="ManagedGrafana-ListVersions-response-grafanaVersions"></a>
The Grafana versions available to create. If a workspace ID is included in the request, the Grafana versions to which this workspace can be upgraded.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [nextToken](#API_ListVersions_ResponseSyntax) **   <a name="ManagedGrafana-ListVersions-response-nextToken"></a>
The token to use in a subsequent `ListVersions` operation to return the next set of results.
Type: String

## Errors
<a name="API_ListVersions_Errors"></a>

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
<a name="API_ListVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/ListVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/ListVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/ListVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/ListVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/ListVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/ListVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/ListVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/ListVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/ListVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/ListVersions)
