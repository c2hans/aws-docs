---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_DeploymentModel.html
---

# DeploymentModel
<a name="API_edge_DeploymentModel"></a>

Information about a model deployed on an edge device that is registered with SageMaker Edge Manager.

## Contents
<a name="API_edge_DeploymentModel_Contents"></a>

 ** DesiredState **   <a name="sagemaker-Type-edge_DeploymentModel-DesiredState"></a>
The desired state of the model.
Type: String
Valid Values: `DEPLOY | UNDEPLOY`
Required: No

 ** ModelHandle **   <a name="sagemaker-Type-edge_DeploymentModel-ModelHandle"></a>
The name by which the device refers to the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
Required: No

 ** ModelName **   <a name="sagemaker-Type-edge_DeploymentModel-ModelName"></a>
The name of the model.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 255.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
Required: No

 ** ModelVersion **   <a name="sagemaker-Type-edge_DeploymentModel-ModelVersion"></a>
The version of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\ \_\.]+`
Required: No

 ** RollbackFailureReason **   <a name="sagemaker-Type-edge_DeploymentModel-RollbackFailureReason"></a>
Returns the error message if there is a rollback.
Type: String
Required: No

 ** State **   <a name="sagemaker-Type-edge_DeploymentModel-State"></a>
Returns the current state of the model.
Type: String
Valid Values: `DEPLOY | UNDEPLOY`
Required: No

 ** Status **   <a name="sagemaker-Type-edge_DeploymentModel-Status"></a>
Returns the deployment status of the model.
Type: String
Valid Values: `SUCCESS | FAIL`
Required: No

 ** StatusReason **   <a name="sagemaker-Type-edge_DeploymentModel-StatusReason"></a>
Returns the error message for the deployment status result.
Type: String
Required: No

## See Also
<a name="API_edge_DeploymentModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-edge-2020-09-23/DeploymentModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-edge-2020-09-23/DeploymentModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-edge-2020-09-23/DeploymentModel)
