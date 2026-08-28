---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_DeploymentResult.html
---

# DeploymentResult
<a name="API_edge_DeploymentResult"></a>

Information about the result of a deployment on an edge device that is registered with SageMaker Edge Manager.

## Contents
<a name="API_edge_DeploymentResult_Contents"></a>

 ** DeploymentEndTime **   <a name="sagemaker-Type-edge_DeploymentResult-DeploymentEndTime"></a>
The timestamp of when the deployment was ended, and the agent got the deployment results.
Type: Timestamp
Required: No

 ** DeploymentModels **   <a name="sagemaker-Type-edge_DeploymentResult-DeploymentModels"></a>
Returns a list of models deployed on the agent.
Type: Array of [DeploymentModel](API_edge_DeploymentModel.md) objects
Required: No

 ** DeploymentName **   <a name="sagemaker-Type-edge_DeploymentResult-DeploymentName"></a>
The name and unique ID of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
Required: No

 ** DeploymentStartTime **   <a name="sagemaker-Type-edge_DeploymentResult-DeploymentStartTime"></a>
The timestamp of when the deployment was started on the agent.
Type: Timestamp
Required: No

 ** DeploymentStatus **   <a name="sagemaker-Type-edge_DeploymentResult-DeploymentStatus"></a>
Returns the bucket error code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
Required: No

 ** DeploymentStatusMessage **   <a name="sagemaker-Type-edge_DeploymentResult-DeploymentStatusMessage"></a>
Returns the detailed error message.
Type: String
Required: No

## See Also
<a name="API_edge_DeploymentResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-edge-2020-09-23/DeploymentResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-edge-2020-09-23/DeploymentResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-edge-2020-09-23/DeploymentResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
