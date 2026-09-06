---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_DefinitionRepository.html
---

# DefinitionRepository
<a name="API_DefinitionRepository"></a>

Contains information about a source code repository that hosts the workflow definition files.

## Contents
<a name="API_DefinitionRepository_Contents"></a>

 ** connectionArn **   <a name="omics-Type-DefinitionRepository-connectionArn"></a>
The Amazon Resource Name (ARN) of the connection to the source code repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
Required: Yes

 ** fullRepositoryId **   <a name="omics-Type-DefinitionRepository-fullRepositoryId"></a>
The full repository identifier, including the repository owner and name. For example, 'repository-owner/repository-name'.
Type: String
Pattern: `.+/.+`
Required: Yes

 ** excludeFilePatterns **   <a name="omics-Type-DefinitionRepository-excludeFilePatterns"></a>
A list of file patterns to exclude when retrieving the workflow definition from the repository.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** sourceReference **   <a name="omics-Type-DefinitionRepository-sourceReference"></a>
The source reference for the repository, such as a branch name, tag, or commit ID.
Type: [SourceReference](API_SourceReference.md) object
Required: No

## See Also
<a name="API_DefinitionRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/DefinitionRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/DefinitionRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/DefinitionRepository)
