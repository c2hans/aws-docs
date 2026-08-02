---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentData.html
---

# DeploymentData
<a name="API_DeploymentData"></a>

The data associated with a deployment.

## Contents
<a name="API_DeploymentData_Contents"></a>

 ** createdAt **   <a name="launchwizard-Type-DeploymentData-createdAt"></a>
The time the deployment was created.
Type: Timestamp
Required: No

 ** deletedAt **   <a name="launchwizard-Type-DeploymentData-deletedAt"></a>
The time the deployment was deleted.
Type: Timestamp
Required: No

 ** deploymentArn **   <a name="launchwizard-Type-DeploymentData-deploymentArn"></a>
The Amazon Resource Name (ARN) of the deployment.
Type: String
Required: No

 ** id **   <a name="launchwizard-Type-DeploymentData-id"></a>
The ID of the deployment.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** modifiedAt **   <a name="launchwizard-Type-DeploymentData-modifiedAt"></a>
The time the deployment was last modified.
Type: Timestamp
Required: No

 ** name **   <a name="launchwizard-Type-DeploymentData-name"></a>
The name of the deployment.
Type: String
Required: No

 ** patternName **   <a name="launchwizard-Type-DeploymentData-patternName"></a>
The pattern name of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][a-zA-Z0-9-]*`
Required: No

 ** resourceGroup **   <a name="launchwizard-Type-DeploymentData-resourceGroup"></a>
The resource group of the deployment.
Type: String
Required: No

 ** specifications **   <a name="launchwizard-Type-DeploymentData-specifications"></a>
The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see [SAP deployment specifications](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html). To retrieve the specifications required to create a deployment for other workloads, use the [https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html) operation.
Type: String to string map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 3. Maximum length of 256.
Key Pattern: `[a-zA-Z0-9-:]+`
Value Length Constraints: Minimum length of 1. Maximum length of 1500.
Required: No

 ** status **   <a name="launchwizard-Type-DeploymentData-status"></a>
The status of the deployment.
Type: String
Valid Values: `COMPLETED | CREATING | DELETE_IN_PROGRESS | DELETE_INITIATING | DELETE_FAILED | DELETED | FAILED | IN_PROGRESS | VALIDATING | UPDATE_IN_PROGRESS | UPDATE_COMPLETED | UPDATE_FAILED | UPDATE_ROLLBACK_COMPLETED | UPDATE_ROLLBACK_FAILED`
Required: No

 ** tags **   <a name="launchwizard-Type-DeploymentData-tags"></a>
Information about the tags attached to a deployment.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z+-=._:/]*`
Required: No

 ** workloadName **   <a name="launchwizard-Type-DeploymentData-workloadName"></a>
The name of the workload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z][a-zA-Z0-9-_]*`
Required: No

## See Also
<a name="API_DeploymentData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/DeploymentData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/DeploymentData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/DeploymentData)
