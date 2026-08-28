---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ResourceServerConfig.html
---

# ResourceServerConfig
<a name="API_ResourceServerConfig"></a>

A structure that describes the configuration of a resource server.

## Contents
<a name="API_ResourceServerConfig_Contents"></a>

 ** Scopes **   <a name="singlesignon-Type-ResourceServerConfig-Scopes"></a>
A list of the IAM Identity Center access scopes that are associated with this resource server.
Type: String to [ResourceServerScopeDetails](API_ResourceServerScopeDetails.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 80.
Key Pattern: `[^:=\-\.\s][0-9a-zA-Z_:\-\.]+`
Required: No

## See Also
<a name="API_ResourceServerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/ResourceServerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/ResourceServerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/ResourceServerConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
