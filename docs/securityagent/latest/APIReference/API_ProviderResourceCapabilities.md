---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ProviderResourceCapabilities.html
---

# ProviderResourceCapabilities
<a name="API_ProviderResourceCapabilities"></a>

The capabilities for an integrated resource from a third-party provider. This is a union type that contains provider-specific capabilities.

## Contents
<a name="API_ProviderResourceCapabilities_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** bitbucket **   <a name="securityagent-Type-ProviderResourceCapabilities-bitbucket"></a>
Capabilities for an integrated Bitbucket repository.
Type: [BitbucketResourceCapabilities](API_BitbucketResourceCapabilities.md) object
Required: No

 ** confluence **   <a name="securityagent-Type-ProviderResourceCapabilities-confluence"></a>
Capabilities for an integrated Confluence space.
Type: [ConfluenceResourceCapabilities](API_ConfluenceResourceCapabilities.md) object
Required: No

 ** github **   <a name="securityagent-Type-ProviderResourceCapabilities-github"></a>
The GitHub-specific resource capabilities.
Type: [GitHubResourceCapabilities](API_GitHubResourceCapabilities.md) object
Required: No

 ** gitlab **   <a name="securityagent-Type-ProviderResourceCapabilities-gitlab"></a>
Capabilities for an integrated GitLab repository.
Type: [GitLabResourceCapabilities](API_GitLabResourceCapabilities.md) object
Required: No

## See Also
<a name="API_ProviderResourceCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ProviderResourceCapabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ProviderResourceCapabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ProviderResourceCapabilities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
