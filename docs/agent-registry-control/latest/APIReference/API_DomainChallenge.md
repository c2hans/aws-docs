---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_DomainChallenge.html
---

# DomainChallenge

The Domain Name System (DNS) TXT record that you create to prove that you control a publisher's domain.

## Contents
<a name="API_DomainChallenge_Contents"></a>

 ** recordName **   <a name="agentregistrycontrol-Type-DomainChallenge-recordName"></a>
The name of the DNS TXT record to create, such as `_acme-challenge.example.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** recordValue **   <a name="agentregistrycontrol-Type-DomainChallenge-recordValue"></a>
The value to publish in the DNS TXT record. A new value is issued each time verification restarts, and earlier values no longer verify the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_DomainChallenge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/DomainChallenge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/DomainChallenge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/DomainChallenge)
