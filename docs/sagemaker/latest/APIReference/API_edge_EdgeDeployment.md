---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_EdgeDeployment.html
---

# EdgeDeployment
<a name="API_edge_EdgeDeployment"></a>

Information about a deployment on an edge device that is registered with SageMaker Edge Manager.

## Contents
<a name="API_edge_EdgeDeployment_Contents"></a>

 ** Definitions **   <a name="sagemaker-Type-edge_EdgeDeployment-Definitions"></a>
Returns a list of Definition objects.
Type: Array of [Definition](API_edge_Definition.md) objects
Required: No

 ** DeploymentName **   <a name="sagemaker-Type-edge_EdgeDeployment-DeploymentName"></a>
The name and unique ID of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
Required: No

 ** FailureHandlingPolicy **   <a name="sagemaker-Type-edge_EdgeDeployment-FailureHandlingPolicy"></a>
Determines whether to rollback to previous configuration if deployment fails.
Type: String
Valid Values: `ROLLBACK_ON_FAILURE | DO_NOTHING`
Required: No

 ** Type **   <a name="sagemaker-Type-edge_EdgeDeployment-Type"></a>
The type of the deployment.
Type: String
Valid Values: `Model`
Required: No

## See Also
<a name="API_edge_EdgeDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-edge-2020-09-23/EdgeDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-edge-2020-09-23/EdgeDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-edge-2020-09-23/EdgeDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
