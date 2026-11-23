---
source_url: https://docs.aws.amazon.com/agent-discovery/latest/APIReference/API_ProvenanceLink.html
---

# ProvenanceLink

Describes where a record came from.

## Contents
<a name="API_ProvenanceLink_Contents"></a>

 ** relation **   <a name="agentdiscovery-Type-ProvenanceLink-relation"></a>
How the record was obtained: `publishedFrom` for a record its owner published, `discoveredFrom` for a record discovered at a partner source, or `federatedFrom` for a record from a peer registry.
Type: String
Valid Values: `publishedFrom | discoveredFrom | federatedFrom`
Required: Yes

 ** sourceId **   <a name="agentdiscovery-Type-ProvenanceLink-sourceId"></a>
The source of the record. For `publishedFrom`, this is the record's identifier. For `discoveredFrom`, this is the name of the partner source. This value is not always a URI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_ProvenanceLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-discovery-2022-07-26/ProvenanceLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-discovery-2022-07-26/ProvenanceLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-discovery-2022-07-26/ProvenanceLink)
