---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListWorkspaces.html
---

# ListWorkspaces
<a name="API_ListWorkspaces"></a>

Returns a list of Amazon Managed Grafana workspaces in the account, with some information about each workspace. For more complete information about one workspace, use [DescribeWorkspace](https://docs.aws.amazon.com/grafana/latest/APIReference/API_DescribeWorkspace.html).

## Request Syntax
<a name="API_ListWorkspaces_RequestSyntax"></a>

```
GET /workspaces?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWorkspaces_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListWorkspaces_RequestSyntax) **   <a name="ManagedGrafana-ListWorkspaces-request-uri-maxResults"></a>
The maximum number of workspaces to include in the results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListWorkspaces_RequestSyntax) **   <a name="ManagedGrafana-ListWorkspaces-request-uri-nextToken"></a>
The token for the next set of workspaces to return. (You receive this token from a previous `ListWorkspaces` operation.)

## Request Body
<a name="API_ListWorkspaces_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWorkspaces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "workspaces": [
      {
         "authentication": {
            "providers": [ "string" ],
            "samlConfigurationStatus": "string"
         },
         "created": number,
         "description": "string",
         "endpoint": "string",
         "grafanaToken": "string",
         "grafanaVersion": "string",
         "id": "string",
         "licenseType": "string",
         "modified": number,
         "name": "string",
         "notificationDestinations": [ "string" ],
         "status": "string",
         "tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkspaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWorkspaces_ResponseSyntax) **   <a name="ManagedGrafana-ListWorkspaces-response-nextToken"></a>
The token to use when requesting the next set of workspaces.
Type: String

 ** [workspaces](#API_ListWorkspaces_ResponseSyntax) **   <a name="ManagedGrafana-ListWorkspaces-response-workspaces"></a>
An array of structures that contain some information about the workspaces in the account.
Type: Array of [WorkspaceSummary](API_WorkspaceSummary.md) objects

## Errors
<a name="API_ListWorkspaces_Errors"></a>

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
<a name="API_ListWorkspaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/ListWorkspaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/ListWorkspaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/ListWorkspaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/ListWorkspaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/ListWorkspaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/ListWorkspaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/ListWorkspaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/ListWorkspaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/ListWorkspaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/ListWorkspaces)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
