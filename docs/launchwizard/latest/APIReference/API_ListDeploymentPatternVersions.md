---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListDeploymentPatternVersions.html
---

# ListDeploymentPatternVersions
<a name="API_ListDeploymentPatternVersions"></a>

Lists the deployment pattern versions.

## Request Syntax
<a name="API_ListDeploymentPatternVersions_RequestSyntax"></a>

```
POST /listDeploymentPatternVersions HTTP/1.1
Content-type: application/json

{
   "deploymentPatternName": "{{string}}",
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "workloadName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListDeploymentPatternVersions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListDeploymentPatternVersions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [deploymentPatternName](#API_ListDeploymentPatternVersions_RequestSyntax) **   <a name="launchwizard-ListDeploymentPatternVersions-request-deploymentPatternName"></a>
The name of the deployment pattern. You can use the [`ListWorkloadDeploymentPatterns`](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html) operation to discover supported values for this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][a-zA-Z0-9-]*`
Required: Yes

 ** [filters](#API_ListDeploymentPatternVersions_RequestSyntax) **   <a name="launchwizard-ListDeploymentPatternVersions-request-filters"></a>
Filters to apply when listing deployment pattern versions.
Type: Array of [DeploymentPatternVersionFilter](API_DeploymentPatternVersionFilter.md) objects
Required: No

 ** [maxResults](#API_ListDeploymentPatternVersions_RequestSyntax) **   <a name="launchwizard-ListDeploymentPatternVersions-request-maxResults"></a>
The maximum number of deployment pattern versions to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListDeploymentPatternVersions_RequestSyntax) **   <a name="launchwizard-ListDeploymentPatternVersions-request-nextToken"></a>
The token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [workloadName](#API_ListDeploymentPatternVersions_RequestSyntax) **   <a name="launchwizard-ListDeploymentPatternVersions-request-workloadName"></a>
The name of the workload. You can use the [`ListWorkloads`](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html) operation to discover supported values for this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z][a-zA-Z0-9-_]*`
Required: Yes

## Response Syntax
<a name="API_ListDeploymentPatternVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "deploymentPatternVersions": [
      {
         "deploymentPatternName": "string",
         "deploymentPatternVersionName": "string",
         "description": "string",
         "documentationUrl": "string",
         "workloadName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDeploymentPatternVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deploymentPatternVersions](#API_ListDeploymentPatternVersions_ResponseSyntax) **   <a name="launchwizard-ListDeploymentPatternVersions-response-deploymentPatternVersions"></a>
The deployment pattern versions.
Type: Array of [DeploymentPatternVersionDataSummary](API_DeploymentPatternVersionDataSummary.md) objects

 ** [nextToken](#API_ListDeploymentPatternVersions_ResponseSyntax) **   <a name="launchwizard-ListDeploymentPatternVersions-response-nextToken"></a>
The token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListDeploymentPatternVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on [re:Post](https://repost.aws/).
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified workload or deployment resource can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListDeploymentPatternVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/launch-wizard-2018-05-10/ListDeploymentPatternVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/launch-wizard-2018-05-10/ListDeploymentPatternVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/ListDeploymentPatternVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/launch-wizard-2018-05-10/ListDeploymentPatternVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/ListDeploymentPatternVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/launch-wizard-2018-05-10/ListDeploymentPatternVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/launch-wizard-2018-05-10/ListDeploymentPatternVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/launch-wizard-2018-05-10/ListDeploymentPatternVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/launch-wizard-2018-05-10/ListDeploymentPatternVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/ListDeploymentPatternVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Launch Wizard. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query launchwizard` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
