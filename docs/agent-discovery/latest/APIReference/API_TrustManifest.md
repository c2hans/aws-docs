---
source_url: https://docs.aws.amazon.com/agent-discovery/latest/APIReference/API_TrustManifest.html
---

# TrustManifest

Trust metadata that one contributor states about a record.

## Contents
<a name="API_TrustManifest_Contents"></a>

 ** contributor **   <a name="agentdiscovery-Type-TrustManifest-contributor"></a>
The URI of the contributor that the claims are attributed to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** provenance **   <a name="agentdiscovery-Type-TrustManifest-provenance"></a>
Where the contributor obtained the record.
Type: Array of [ProvenanceLink](API_ProvenanceLink.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_TrustManifest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-discovery-2022-07-26/TrustManifest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-discovery-2022-07-26/TrustManifest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-discovery-2022-07-26/TrustManifest)
