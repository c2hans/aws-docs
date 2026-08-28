---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ScopeConfiguration.html
---

# ScopeConfiguration
<a name="API_ScopeConfiguration"></a>

Specifies the scope of resources to record from a third-party cloud service provider.

## Contents
<a name="API_ScopeConfiguration_Contents"></a>

 ** allRegions **   <a name="config-Type-ScopeConfiguration-allRegions"></a>
Specifies whether to record resources from all supported regions for the third-party cloud service provider.
Type: Boolean
Required: Yes

 ** scopeType **   <a name="config-Type-ScopeConfiguration-scopeType"></a>
The type of scope for the third-party cloud resources. Valid values include `tenant` and `subscription`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** includedRegions **   <a name="config-Type-ScopeConfiguration-includedRegions"></a>
The list of regions from the third-party cloud service provider to include when recording resources. Used when `allRegions` is set to `false`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** scopeValues **   <a name="config-Type-ScopeConfiguration-scopeValues"></a>
The list of specific scope values for the third-party cloud resources. For example, a list of Azure subscriptions or management groups.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_ScopeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ScopeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ScopeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ScopeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
