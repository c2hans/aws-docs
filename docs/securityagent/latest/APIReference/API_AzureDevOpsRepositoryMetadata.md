---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_AzureDevOpsRepositoryMetadata.html
---

# AzureDevOpsRepositoryMetadata
<a name="API_AzureDevOpsRepositoryMetadata"></a>

Metadata for an integrated Azure DevOps repository.

## Contents
<a name="API_AzureDevOpsRepositoryMetadata_Contents"></a>

 ** name **   <a name="securityagent-Type-AzureDevOpsRepositoryMetadata-name"></a>
Name of the resource e.g. repository name, etc.
Type: String
Required: Yes

 ** organization **   <a name="securityagent-Type-AzureDevOpsRepositoryMetadata-organization"></a>
The name of the Azure DevOps organization that owns the repository.
Type: String
Required: Yes

 ** providerResourceId **   <a name="securityagent-Type-AzureDevOpsRepositoryMetadata-providerResourceId"></a>
Provider Id of the resource e.g. GitHub repository id, etc.
Type: String
Required: Yes

 ** accessType **   <a name="securityagent-Type-AzureDevOpsRepositoryMetadata-accessType"></a>
Defines the visibility level of provider resources. PRIVATE indicates restricted access, while PUBLIC indicates open access.
Type: String
Valid Values: `PRIVATE | PUBLIC`
Required: No

 ** project **   <a name="securityagent-Type-AzureDevOpsRepositoryMetadata-project"></a>
The name of the Azure DevOps project that contains the repository.
Type: String
Required: No

 ** projectId **   <a name="securityagent-Type-AzureDevOpsRepositoryMetadata-projectId"></a>
The GUID of the Azure DevOps project that contains the repository.
Type: String
Required: No

## See Also
<a name="API_AzureDevOpsRepositoryMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/AzureDevOpsRepositoryMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/AzureDevOpsRepositoryMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/AzureDevOpsRepositoryMetadata)
