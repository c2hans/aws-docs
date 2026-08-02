---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentDataSummary.html
---

# DeploymentDataSummary
<a name="API_DeploymentDataSummary"></a>

A summary of the deployment data.

## Contents
<a name="API_DeploymentDataSummary_Contents"></a>

 ** createdAt **   <a name="launchwizard-Type-DeploymentDataSummary-createdAt"></a>
The time the deployment was created.
Type: Timestamp
Required: No

 ** id **   <a name="launchwizard-Type-DeploymentDataSummary-id"></a>
The ID of the deployment.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** modifiedAt **   <a name="launchwizard-Type-DeploymentDataSummary-modifiedAt"></a>
The time the deployment was last modified.
Type: Timestamp
Required: No

 ** name **   <a name="launchwizard-Type-DeploymentDataSummary-name"></a>
The name of the deployment
Type: String
Required: No

 ** patternName **   <a name="launchwizard-Type-DeploymentDataSummary-patternName"></a>
The name of the workload deployment pattern.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][a-zA-Z0-9-]*`
Required: No

 ** status **   <a name="launchwizard-Type-DeploymentDataSummary-status"></a>
The status of the deployment.
Type: String
Valid Values: `COMPLETED | CREATING | DELETE_IN_PROGRESS | DELETE_INITIATING | DELETE_FAILED | DELETED | FAILED | IN_PROGRESS | VALIDATING | UPDATE_IN_PROGRESS | UPDATE_COMPLETED | UPDATE_FAILED | UPDATE_ROLLBACK_COMPLETED | UPDATE_ROLLBACK_FAILED`
Required: No

 ** workloadName **   <a name="launchwizard-Type-DeploymentDataSummary-workloadName"></a>
The name of the workload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z][a-zA-Z0-9-_]*`
Required: No

## See Also
<a name="API_DeploymentDataSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/DeploymentDataSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/DeploymentDataSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/DeploymentDataSummary)
