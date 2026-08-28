---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html
---

# GetWorkloadDeploymentPattern
<a name="API_GetWorkloadDeploymentPattern"></a>

Returns details for a given workload and deployment pattern, including the available specifications. You can use the [ListWorkloads](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html) operation to discover the available workload names and the [ListWorkloadDeploymentPatterns](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html) operation to discover the available deployment pattern names of a given workload.

## Request Syntax
<a name="API_GetWorkloadDeploymentPattern_RequestSyntax"></a>

```
POST /getWorkloadDeploymentPattern HTTP/1.1
Content-type: application/json

{
   "deploymentPatternName": "{{string}}",
   "workloadName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetWorkloadDeploymentPattern_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetWorkloadDeploymentPattern_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [deploymentPatternName](#API_GetWorkloadDeploymentPattern_RequestSyntax) **   <a name="launchwizard-GetWorkloadDeploymentPattern-request-deploymentPatternName"></a>
The name of the deployment pattern.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][a-zA-Z0-9-]*`
Required: Yes

 ** [workloadName](#API_GetWorkloadDeploymentPattern_RequestSyntax) **   <a name="launchwizard-GetWorkloadDeploymentPattern-request-workloadName"></a>
The name of the workload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z][a-zA-Z0-9-_]*`
Required: Yes

## Response Syntax
<a name="API_GetWorkloadDeploymentPattern_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "workloadDeploymentPattern": {
      "deploymentPatternName": "string",
      "deploymentPatternVersionName": "string",
      "description": "string",
      "displayName": "string",
      "specifications": [
         {
            "allowedValues": [ "string" ],
            "conditionals": [
               {
                  "comparator": "string",
                  "name": "string",
                  "value": "string"
               }
            ],
            "description": "string",
            "name": "string",
            "required": "string"
         }
      ],
      "status": "string",
      "statusMessage": "string",
      "workloadName": "string",
      "workloadVersionName": "string"
   }
}
```

## Response Elements
<a name="API_GetWorkloadDeploymentPattern_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workloadDeploymentPattern](#API_GetWorkloadDeploymentPattern_ResponseSyntax) **   <a name="launchwizard-GetWorkloadDeploymentPattern-response-workloadDeploymentPattern"></a>
Details about the workload deployment pattern.
Type: [WorkloadDeploymentPatternData](API_WorkloadDeploymentPatternData.md) object

## Errors
<a name="API_GetWorkloadDeploymentPattern_Errors"></a>

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
<a name="API_GetWorkloadDeploymentPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/launch-wizard-2018-05-10/GetWorkloadDeploymentPattern)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/launch-wizard-2018-05-10/GetWorkloadDeploymentPattern)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/GetWorkloadDeploymentPattern)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/launch-wizard-2018-05-10/GetWorkloadDeploymentPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/GetWorkloadDeploymentPattern)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/launch-wizard-2018-05-10/GetWorkloadDeploymentPattern)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/launch-wizard-2018-05-10/GetWorkloadDeploymentPattern)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/launch-wizard-2018-05-10/GetWorkloadDeploymentPattern)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/launch-wizard-2018-05-10/GetWorkloadDeploymentPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/GetWorkloadDeploymentPattern)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Launch Wizard. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query launchwizard` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
