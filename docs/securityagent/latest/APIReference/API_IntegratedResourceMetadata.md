---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_IntegratedResourceMetadata.html
---

# IntegratedResourceMetadata
<a name="API_IntegratedResourceMetadata"></a>

Contains metadata about an integrated resource. This is a union type that contains provider-specific metadata.

## Contents
<a name="API_IntegratedResourceMetadata_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** azureDevOpsRepository **   <a name="securityagent-Type-IntegratedResourceMetadata-azureDevOpsRepository"></a>
The Azure DevOps repository metadata.
Type: [AzureDevOpsRepositoryMetadata](API_AzureDevOpsRepositoryMetadata.md) object
Required: No

 ** bitbucketRepository **   <a name="securityagent-Type-IntegratedResourceMetadata-bitbucketRepository"></a>
Metadata for an integrated Bitbucket repository.
Type: [BitbucketRepositoryMetadata](API_BitbucketRepositoryMetadata.md) object
Required: No

 ** confluenceDocument **   <a name="securityagent-Type-IntegratedResourceMetadata-confluenceDocument"></a>
Metadata for an integrated Confluence document.
Type: [ConfluenceDocumentMetadata](API_ConfluenceDocumentMetadata.md) object
Required: No

 ** githubRepository **   <a name="securityagent-Type-IntegratedResourceMetadata-githubRepository"></a>
The GitHub repository metadata.
Type: [GitHubRepositoryMetadata](API_GitHubRepositoryMetadata.md) object
Required: No

 ** gitlabRepository **   <a name="securityagent-Type-IntegratedResourceMetadata-gitlabRepository"></a>
Metadata for an integrated GitLab repository.
Type: [GitLabRepositoryMetadata](API_GitLabRepositoryMetadata.md) object
Required: No

## See Also
<a name="API_IntegratedResourceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/IntegratedResourceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/IntegratedResourceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/IntegratedResourceMetadata)
