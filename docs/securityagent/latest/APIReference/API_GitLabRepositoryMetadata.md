---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_GitLabRepositoryMetadata.html
---

# GitLabRepositoryMetadata
<a name="API_GitLabRepositoryMetadata"></a>

Metadata for an integrated GitLab repository.

## Contents
<a name="API_GitLabRepositoryMetadata_Contents"></a>

 ** name **   <a name="securityagent-Type-GitLabRepositoryMetadata-name"></a>
Name of the resource e.g. repository name, etc.
Type: String
Required: Yes

 ** namespace **   <a name="securityagent-Type-GitLabRepositoryMetadata-namespace"></a>
The namespace (group or user path) that owns the project.
Type: String
Required: Yes

 ** providerResourceId **   <a name="securityagent-Type-GitLabRepositoryMetadata-providerResourceId"></a>
Provider Id of the resource e.g. GitHub repository id, etc.
Type: String
Required: Yes

 ** accessType **   <a name="securityagent-Type-GitLabRepositoryMetadata-accessType"></a>
Defines the visibility level of provider resources. PRIVATE indicates restricted access, while PUBLIC indicates open access.
Type: String
Valid Values: `PRIVATE | PUBLIC`
Required: No

## See Also
<a name="API_GitLabRepositoryMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/GitLabRepositoryMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/GitLabRepositoryMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/GitLabRepositoryMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
