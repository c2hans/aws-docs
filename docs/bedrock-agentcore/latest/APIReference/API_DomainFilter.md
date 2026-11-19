---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DomainFilter.html
---

# DomainFilter

The domains to include in or exclude from the results. A root domain also matches its subdomains. For example, `example.com` also matches `docs.example.com`.

## Contents
<a name="API_DomainFilter_Contents"></a>

 ** exclude **   <a name="BedrockAgentCore-Type-DomainFilter-exclude"></a>
The domains to never return results from.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?(\.[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*`
Required: No

 ** include **   <a name="BedrockAgentCore-Type-DomainFilter-include"></a>
The domains to return results from. Results from other domains are not returned.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?(\.[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*`
Required: No

## See Also
<a name="API_DomainFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DomainFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DomainFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DomainFilter)
