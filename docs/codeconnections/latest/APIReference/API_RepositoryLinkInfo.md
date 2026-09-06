---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_RepositoryLinkInfo.html
---

# RepositoryLinkInfo
<a name="API_RepositoryLinkInfo"></a>

Information about the repository link resource, such as the repository link ARN, the associated connection ARN, encryption key ARN, and owner ID.

## Contents
<a name="API_RepositoryLinkInfo_Contents"></a>

 ** ConnectionArn **   <a name="codeconnections-Type-RepositoryLinkInfo-ConnectionArn"></a>
The Amazon Resource Name (ARN) of the connection associated with the repository link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
Required: Yes

 ** OwnerId **   <a name="codeconnections-Type-RepositoryLinkInfo-OwnerId"></a>
The owner ID for the repository associated with the repository link, such as the owner ID in GitHub.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^.*$`
Required: Yes

 ** ProviderType **   <a name="codeconnections-Type-RepositoryLinkInfo-ProviderType"></a>
The provider type for the connection, such as GitHub, associated with the repository link.
Type: String
Valid Values: `Bitbucket | GitHub | GitHubEnterpriseServer | GitLab | GitLabSelfManaged | AzureDevOps`
Required: Yes

 ** RepositoryLinkArn **   <a name="codeconnections-Type-RepositoryLinkInfo-RepositoryLinkArn"></a>
The Amazon Resource Name (ARN) of the repository link.
Type: String
Pattern: `^arn:aws(?:-[a-z]+)*:(codestar-connections|codeconnections):[a-z\-0-9]+:\d{12}:repository-link\/[a-zA-Z0-9\-:/]+`
Required: Yes

 ** RepositoryLinkId **   <a name="codeconnections-Type-RepositoryLinkInfo-RepositoryLinkId"></a>
The ID of the repository link.
Type: String
Pattern: `^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`
Required: Yes

 ** RepositoryName **   <a name="codeconnections-Type-RepositoryLinkInfo-RepositoryName"></a>
The name of the repository associated with the repository link.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^.*$`
Required: Yes

 ** EncryptionKeyArn **   <a name="codeconnections-Type-RepositoryLinkInfo-EncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the encryption key for the repository associated with the repository link.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(-[\w]+)*:kms:[a-z\-0-9]+:\d{12}:key/[a-zA-Z0-9\-]+`
Required: No

## See Also
<a name="API_RepositoryLinkInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/RepositoryLinkInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/RepositoryLinkInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/RepositoryLinkInfo)
