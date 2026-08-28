---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopEdgeDeploymentStage.html
---

# StopEdgeDeploymentStage
<a name="API_StopEdgeDeploymentStage"></a>

Stops a stage in an edge deployment plan.

## Request Syntax
<a name="API_StopEdgeDeploymentStage_RequestSyntax"></a>

```
{
   "EdgeDeploymentPlanName": "{{string}}",
   "StageName": "{{string}}"
}
```

## Request Parameters
<a name="API_StopEdgeDeploymentStage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EdgeDeploymentPlanName](#API_StopEdgeDeploymentStage_RequestSyntax) **   <a name="sagemaker-StopEdgeDeploymentStage-request-EdgeDeploymentPlanName"></a>
The name of the edge deployment plan to stop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [StageName](#API_StopEdgeDeploymentStage_RequestSyntax) **   <a name="sagemaker-StopEdgeDeploymentStage-request-StageName"></a>
The name of the stage to stop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Elements
<a name="API_StopEdgeDeploymentStage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopEdgeDeploymentStage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_StopEdgeDeploymentStage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/StopEdgeDeploymentStage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/StopEdgeDeploymentStage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/StopEdgeDeploymentStage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/StopEdgeDeploymentStage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/StopEdgeDeploymentStage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/StopEdgeDeploymentStage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/StopEdgeDeploymentStage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/StopEdgeDeploymentStage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/StopEdgeDeploymentStage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/StopEdgeDeploymentStage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
