---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetDeploymentPatternVersion.html
---

# GetDeploymentPatternVersion
<a name="API_GetDeploymentPatternVersion"></a>

Returns information about a deployment pattern version.

## Request Syntax
<a name="API_GetDeploymentPatternVersion_RequestSyntax"></a>

```
POST /getDeploymentPatternVersion HTTP/1.1
Content-type: application/json

{
   "deploymentPatternName": "{{string}}",
   "deploymentPatternVersionName": "{{string}}",
   "workloadName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetDeploymentPatternVersion_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetDeploymentPatternVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [deploymentPatternName](#API_GetDeploymentPatternVersion_RequestSyntax) **   <a name="launchwizard-GetDeploymentPatternVersion-request-deploymentPatternName"></a>
The name of the deployment pattern. You can use the [`ListWorkloadDeploymentPatterns`](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html) operation to discover supported values for this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][a-zA-Z0-9-]*`
Required: Yes

 ** [deploymentPatternVersionName](#API_GetDeploymentPatternVersion_RequestSyntax) **   <a name="launchwizard-GetDeploymentPatternVersion-request-deploymentPatternVersionName"></a>
The name of the deployment pattern version.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `(([A-Za-z0-9][a-zA-Z0-9-]*)|(\d+\.\d+\.\d+))`
Required: Yes

 ** [workloadName](#API_GetDeploymentPatternVersion_RequestSyntax) **   <a name="launchwizard-GetDeploymentPatternVersion-request-workloadName"></a>
The name of the workload. You can use the [`ListWorkloads`](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html) operation to discover supported values for this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z][a-zA-Z0-9-_]*`
Required: Yes

## Response Syntax
<a name="API_GetDeploymentPatternVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "deploymentPatternVersion": {
      "deploymentPatternName": "string",
      "deploymentPatternVersionName": "string",
      "description": "string",
      "documentationUrl": "string",
      "workloadName": "string"
   }
}
```

## Response Elements
<a name="API_GetDeploymentPatternVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deploymentPatternVersion](#API_GetDeploymentPatternVersion_ResponseSyntax) **   <a name="launchwizard-GetDeploymentPatternVersion-response-deploymentPatternVersion"></a>
The deployment pattern version.
Type: [DeploymentPatternVersionDataSummary](API_DeploymentPatternVersionDataSummary.md) object

## Errors
<a name="API_GetDeploymentPatternVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on [re:Post](https://repost.aws/).
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified workload or deployment resource can't be found.
HTTP Status Code: 404

## See Also
<a name="API_GetDeploymentPatternVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/launch-wizard-2018-05-10/GetDeploymentPatternVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/launch-wizard-2018-05-10/GetDeploymentPatternVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/GetDeploymentPatternVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/launch-wizard-2018-05-10/GetDeploymentPatternVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/GetDeploymentPatternVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/launch-wizard-2018-05-10/GetDeploymentPatternVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/launch-wizard-2018-05-10/GetDeploymentPatternVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/launch-wizard-2018-05-10/GetDeploymentPatternVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/launch-wizard-2018-05-10/GetDeploymentPatternVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/GetDeploymentPatternVersion)
