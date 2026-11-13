---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DomainOverride.html
---

# DomainOverride
<a name="API_DomainOverride"></a>

The public domain names for a gateway that clients reach through your own proxy or custom domain. When you configure a domain override, the gateway advertises these domains instead of the inbound Host header in the URLs that it returns for OAuth discovery, such as the protected resource metadata and the `WWW-Authenticate` challenge.

## Contents
<a name="API_DomainOverride_Contents"></a>

 ** default **   <a name="bedrockagentcorecontrol-Type-DomainOverride-default"></a>
The default public domain name for the gateway. The gateway advertises this domain when a request doesn't select a specific domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)(?:\.(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?))+`
Required: Yes

 ** alternateDomains **   <a name="bedrockagentcorecontrol-Type-DomainOverride-alternateDomains"></a>
Additional public domain names for the gateway, up to 10. Don't repeat the default domain or list a domain more than once. A request can select one of these domains, or the default domain, with the `x-amzn-bedrock-agentcore-gateway-domain` header. The gateway rejects a request that selects a domain that isn't configured.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)(?:\.(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?))+`
Required: No

## See Also
<a name="API_DomainOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DomainOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DomainOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DomainOverride)
