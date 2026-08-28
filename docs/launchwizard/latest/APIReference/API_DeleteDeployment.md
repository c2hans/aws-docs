---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeleteDeployment.html
---

# DeleteDeployment
<a name="API_DeleteDeployment"></a>

Deletes a deployment.

## Request Syntax
<a name="API_DeleteDeployment_RequestSyntax"></a>

```
POST /deleteDeployment HTTP/1.1
Content-type: application/json

{
   "deploymentId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteDeployment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteDeployment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [deploymentId](#API_DeleteDeployment_RequestSyntax) **   <a name="launchwizard-DeleteDeployment-request-deploymentId"></a>
The ID of the deployment.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteDeployment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_DeleteDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_DeleteDeployment_ResponseSyntax) **   <a name="launchwizard-DeleteDeployment-response-status"></a>
The status of the deployment.
Type: String
Valid Values: `COMPLETED | CREATING | DELETE_IN_PROGRESS | DELETE_INITIATING | DELETE_FAILED | DELETED | FAILED | IN_PROGRESS | VALIDATING | UPDATE_IN_PROGRESS | UPDATE_COMPLETED | UPDATE_FAILED | UPDATE_ROLLBACK_COMPLETED | UPDATE_ROLLBACK_FAILED`

 ** [statusReason](#API_DeleteDeployment_ResponseSyntax) **   <a name="launchwizard-DeleteDeployment-response-statusReason"></a>
The reason for the deployment status.
Type: String

## Errors
<a name="API_DeleteDeployment_Errors"></a>

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
<a name="API_DeleteDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/launch-wizard-2018-05-10/DeleteDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/launch-wizard-2018-05-10/DeleteDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/DeleteDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/launch-wizard-2018-05-10/DeleteDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/DeleteDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/launch-wizard-2018-05-10/DeleteDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/launch-wizard-2018-05-10/DeleteDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/launch-wizard-2018-05-10/DeleteDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/launch-wizard-2018-05-10/DeleteDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/DeleteDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Launch Wizard. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query launchwizard` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
