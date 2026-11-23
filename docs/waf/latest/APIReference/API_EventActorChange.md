---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_EventActorChange.html
---

# EventActorChange

A change to the network attributes of an event actor.

## Contents
<a name="API_EventActorChange_Contents"></a>

 ** Asn **   <a name="WAF-Type-EventActorChange-Asn"></a>
The autonomous system number (ASN) that is associated with the client IP address after the change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** AsnOrganization **   <a name="WAF-Type-EventActorChange-AsnOrganization"></a>
The name of the organization that owns the ASN after the change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ChangeTime **   <a name="WAF-Type-EventActorChange-ChangeTime"></a>
The time of the change.
Type: Timestamp
Required: No

 ** ClientIp **   <a name="WAF-Type-EventActorChange-ClientIp"></a>
The client IP address of the event actor after the change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Country **   <a name="WAF-Type-EventActorChange-Country"></a>
The country of the client IP address after the change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** TlsFingerprint **   <a name="WAF-Type-EventActorChange-TlsFingerprint"></a>
The TLS fingerprint of the event actor after the change, such as a JA3 or JA4 fingerprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_EventActorChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/EventActorChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/EventActorChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/EventActorChange)
