---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_DeploymentConfigurationJobSummary.html
---

# DeploymentConfigurationJobSummary

Contains summary information about a deployment configuration job, including its identifier, status, configuration, and creation time.

## Contents
<a name="API_marketplace-deployment_DeploymentConfigurationJobSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** configuration **   <a name="AWSMarketplaceService-Type-marketplace-deployment_DeploymentConfigurationJobSummary-configuration"></a>
The deployment configuration submitted with the job.
Type: [DeploymentConfigurationDetail](API_marketplace-deployment_DeploymentConfigurationDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** createdAt **   <a name="AWSMarketplaceService-Type-marketplace-deployment_DeploymentConfigurationJobSummary-createdAt"></a>
The date and time when the job was created.
Type: Timestamp
Required: Yes

 ** jobId **   <a name="AWSMarketplaceService-Type-marketplace-deployment_DeploymentConfigurationJobSummary-jobId"></a>
The unique identifier of the deployment configuration job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** status **   <a name="AWSMarketplaceService-Type-marketplace-deployment_DeploymentConfigurationJobSummary-status"></a>
The status of the deployment configuration job.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`
Required: Yes

## See Also
<a name="API_marketplace-deployment_DeploymentConfigurationJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-deployment-2023-01-25/DeploymentConfigurationJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-deployment-2023-01-25/DeploymentConfigurationJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-deployment-2023-01-25/DeploymentConfigurationJobSummary)
