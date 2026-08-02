---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BitbucketRepositoryMetadata.html
---

# BitbucketRepositoryMetadata
<a name="API_BitbucketRepositoryMetadata"></a>

Metadata for an integrated Bitbucket repository.

## Contents
<a name="API_BitbucketRepositoryMetadata_Contents"></a>

 ** name **   <a name="securityagent-Type-BitbucketRepositoryMetadata-name"></a>
Name of the resource e.g. repository name, etc.
Type: String
Required: Yes

 ** providerResourceId **   <a name="securityagent-Type-BitbucketRepositoryMetadata-providerResourceId"></a>
Provider Id of the resource e.g. GitHub repository id, etc.
Type: String
Required: Yes

 ** workspace **   <a name="securityagent-Type-BitbucketRepositoryMetadata-workspace"></a>
The workspace slug that owns the repository.
Type: String
Required: Yes

 ** accessType **   <a name="securityagent-Type-BitbucketRepositoryMetadata-accessType"></a>
Defines the visibility level of provider resources. PRIVATE indicates restricted access, while PUBLIC indicates open access.
Type: String
Valid Values: `PRIVATE | PUBLIC`
Required: No

## See Also
<a name="API_BitbucketRepositoryMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BitbucketRepositoryMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BitbucketRepositoryMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BitbucketRepositoryMetadata)
