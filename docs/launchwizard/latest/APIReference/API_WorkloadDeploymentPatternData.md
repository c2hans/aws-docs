---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_WorkloadDeploymentPatternData.html
---

# WorkloadDeploymentPatternData
<a name="API_WorkloadDeploymentPatternData"></a>

The data that details a workload deployment pattern.

## Contents
<a name="API_WorkloadDeploymentPatternData_Contents"></a>

 ** deploymentPatternName **   <a name="launchwizard-Type-WorkloadDeploymentPatternData-deploymentPatternName"></a>
The name of the deployment pattern.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][a-zA-Z0-9-]*`
Required: No

 ** deploymentPatternVersionName **   <a name="launchwizard-Type-WorkloadDeploymentPatternData-deploymentPatternVersionName"></a>
The version name of the deployment pattern.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `(([A-Za-z0-9][a-zA-Z0-9-]*)|(\d+\.\d+\.\d+))`
Required: No

 ** description **   <a name="launchwizard-Type-WorkloadDeploymentPatternData-description"></a>
The description of the deployment pattern.
Type: String
Required: No

 ** displayName **   <a name="launchwizard-Type-WorkloadDeploymentPatternData-displayName"></a>
The display name of the deployment pattern.
Type: String
Required: No

 ** specifications **   <a name="launchwizard-Type-WorkloadDeploymentPatternData-specifications"></a>
The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see [SAP deployment specifications](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html). To retrieve the specifications required to create a deployment for other workloads, use the [`GetWorkloadDeploymentPattern`](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html) operation.
Type: Array of [DeploymentSpecificationsField](API_DeploymentSpecificationsField.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** status **   <a name="launchwizard-Type-WorkloadDeploymentPatternData-status"></a>
The status of the deployment pattern.
Type: String
Valid Values: `ACTIVE | INACTIVE | DISABLED | DELETED`
Required: No

 ** statusMessage **   <a name="launchwizard-Type-WorkloadDeploymentPatternData-statusMessage"></a>
The status message of the deployment pattern.
Type: String
Required: No

 ** workloadName **   <a name="launchwizard-Type-WorkloadDeploymentPatternData-workloadName"></a>
The workload name of the deployment pattern.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z][a-zA-Z0-9-_]*`
Required: No

 ** workloadVersionName **   <a name="launchwizard-Type-WorkloadDeploymentPatternData-workloadVersionName"></a>
The workload version name of the deployment pattern.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `(([A-Za-z0-9][a-zA-Z0-9-]*)|(\d+\.\d+\.\d+))`
Required: No

## See Also
<a name="API_WorkloadDeploymentPatternData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/WorkloadDeploymentPatternData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/WorkloadDeploymentPatternData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/WorkloadDeploymentPatternData)
