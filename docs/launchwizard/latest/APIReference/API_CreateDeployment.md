---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_CreateDeployment.html
---

# CreateDeployment
<a name="API_CreateDeployment"></a>

Creates a deployment for the given workload. Deployments created by this operation are not available in the Launch Wizard console to use the `Clone deployment` action on.

## Request Syntax
<a name="API_CreateDeployment_RequestSyntax"></a>

```
POST /createDeployment HTTP/1.1
Content-type: application/json

{
   "deploymentPatternName": "{{string}}",
   "dryRun": {{boolean}},
   "name": "{{string}}",
   "specifications": {
      "{{string}}" : "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "workloadName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDeployment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDeployment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [deploymentPatternName](#API_CreateDeployment_RequestSyntax) **   <a name="launchwizard-CreateDeployment-request-deploymentPatternName"></a>
The name of the deployment pattern supported by a given workload. You can use the [`ListWorkloadDeploymentPatterns`](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html) operation to discover supported values for this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][a-zA-Z0-9-]*`
Required: Yes

 ** [dryRun](#API_CreateDeployment_RequestSyntax) **   <a name="launchwizard-CreateDeployment-request-dryRun"></a>
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 ** [name](#API_CreateDeployment_RequestSyntax) **   <a name="launchwizard-CreateDeployment-request-name"></a>
The name of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[A-Za-z0-9_\.-]+`
Required: Yes

 ** [specifications](#API_CreateDeployment_RequestSyntax) **   <a name="launchwizard-CreateDeployment-request-specifications"></a>
The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see [SAP deployment specifications](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html). To retrieve the specifications required to create a deployment for other workloads, use the [`GetWorkloadDeploymentPattern`](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html) operation.
Type: String to string map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 3. Maximum length of 256.
Key Pattern: `[a-zA-Z0-9-:]+`
Value Length Constraints: Minimum length of 1. Maximum length of 1500.
Required: Yes

 ** [tags](#API_CreateDeployment_RequestSyntax) **   <a name="launchwizard-CreateDeployment-request-tags"></a>
The tags to add to the deployment.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z+-=._:/]*`
Required: No

 ** [workloadName](#API_CreateDeployment_RequestSyntax) **   <a name="launchwizard-CreateDeployment-request-workloadName"></a>
The name of the workload. You can use the [`ListWorkloads`](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html) operation to discover supported values for this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z][a-zA-Z0-9-_]*`
Required: Yes

## Response Syntax
<a name="API_CreateDeployment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "deploymentId": "string"
}
```

## Response Elements
<a name="API_CreateDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deploymentId](#API_CreateDeployment_ResponseSyntax) **   <a name="launchwizard-CreateDeployment-response-deploymentId"></a>
The ID of the deployment.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9-]+`

## Errors
<a name="API_CreateDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on [re:Post](https://repost.aws/).
HTTP Status Code: 500

 ** ResourceLimitException **
You have exceeded an AWS Launch Wizard resource limit. For example, you might have too many deployments in progress.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified workload or deployment resource can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/launch-wizard-2018-05-10/CreateDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/launch-wizard-2018-05-10/CreateDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/CreateDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/launch-wizard-2018-05-10/CreateDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/CreateDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/launch-wizard-2018-05-10/CreateDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/launch-wizard-2018-05-10/CreateDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/launch-wizard-2018-05-10/CreateDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/launch-wizard-2018-05-10/CreateDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/CreateDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Launch Wizard. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query launchwizard` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
