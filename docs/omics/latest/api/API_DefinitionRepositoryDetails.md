---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_DefinitionRepositoryDetails.html
---

# DefinitionRepositoryDetails
<a name="API_DefinitionRepositoryDetails"></a>

Contains detailed information about the source code repository that hosts the workflow definition files.

## Contents
<a name="API_DefinitionRepositoryDetails_Contents"></a>

 ** connectionArn **   <a name="omics-Type-DefinitionRepositoryDetails-connectionArn"></a>
The Amazon Resource Name (ARN) of the connection to the source code repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
Required: No

 ** fullRepositoryId **   <a name="omics-Type-DefinitionRepositoryDetails-fullRepositoryId"></a>
The full repository identifier, including the repository owner and name. For example, 'repository-owner/repository-name'.
Type: String
Pattern: `.+/.+`
Required: No

 ** providerEndpoint **   <a name="omics-Type-DefinitionRepositoryDetails-providerEndpoint"></a>
The endpoint URL of the source code repository provider.
Type: String
Required: No

 ** providerType **   <a name="omics-Type-DefinitionRepositoryDetails-providerType"></a>
The provider type of the source code repository, such as Bitbucket, GitHub, GitHubEnterpriseServer, GitLab, and GitLabSelfManaged.
Type: String
Required: No

 ** sourceReference **   <a name="omics-Type-DefinitionRepositoryDetails-sourceReference"></a>
The source reference for the repository, such as a branch name, tag, or commit ID.
Type: [SourceReference](API_SourceReference.md) object
Required: No

## See Also
<a name="API_DefinitionRepositoryDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/DefinitionRepositoryDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/DefinitionRepositoryDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/DefinitionRepositoryDetails)
