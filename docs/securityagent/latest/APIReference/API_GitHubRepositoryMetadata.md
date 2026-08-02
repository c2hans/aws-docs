---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_GitHubRepositoryMetadata.html
---

# GitHubRepositoryMetadata
<a name="API_GitHubRepositoryMetadata"></a>

Contains metadata about a GitHub repository that is integrated with the service.

## Contents
<a name="API_GitHubRepositoryMetadata_Contents"></a>

 ** name **   <a name="securityagent-Type-GitHubRepositoryMetadata-name"></a>
The name of the GitHub repository.
Type: String
Required: Yes

 ** owner **   <a name="securityagent-Type-GitHubRepositoryMetadata-owner"></a>
The owner of the GitHub repository.
Type: String
Required: Yes

 ** providerResourceId **   <a name="securityagent-Type-GitHubRepositoryMetadata-providerResourceId"></a>
The provider-specific resource identifier for the GitHub repository.
Type: String
Required: Yes

 ** accessType **   <a name="securityagent-Type-GitHubRepositoryMetadata-accessType"></a>
The access type of the GitHub repository. Valid values are PRIVATE and PUBLIC.
Type: String
Valid Values: `PRIVATE | PUBLIC`
Required: No

## See Also
<a name="API_GitHubRepositoryMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/GitHubRepositoryMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/GitHubRepositoryMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/GitHubRepositoryMetadata)
