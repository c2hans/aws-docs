---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_IntegratedResource.html
---

# IntegratedResource
<a name="API_IntegratedResource"></a>

Represents an integrated resource from a third-party provider. This is a union type that contains provider-specific resource information.

## Contents
<a name="API_IntegratedResource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** bitbucketRepository **   <a name="securityagent-Type-IntegratedResource-bitbucketRepository"></a>
A Bitbucket repository integrated as a resource.
Type: [BitbucketRepositoryResource](API_BitbucketRepositoryResource.md) object
Required: No

 ** confluenceDocument **   <a name="securityagent-Type-IntegratedResource-confluenceDocument"></a>
A Confluence document (page) integrated as a resource.
Type: [ConfluenceDocumentResource](API_ConfluenceDocumentResource.md) object
Required: No

 ** githubRepository **   <a name="securityagent-Type-IntegratedResource-githubRepository"></a>
The GitHub repository resource information.
Type: [GitHubRepositoryResource](API_GitHubRepositoryResource.md) object
Required: No

 ** gitlabRepository **   <a name="securityagent-Type-IntegratedResource-gitlabRepository"></a>
A GitLab repository integrated as a resource.
Type: [GitLabRepositoryResource](API_GitLabRepositoryResource.md) object
Required: No

## See Also
<a name="API_IntegratedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/IntegratedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/IntegratedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/IntegratedResource)
