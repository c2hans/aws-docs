---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_EventActorSummary.html
---

# EventActorSummary

High-level information about an event actor, returned by [ListEventActors](API_ListEventActors.md).

## Contents
<a name="API_EventActorSummary_Contents"></a>

 ** EventActorId **   <a name="WAF-Type-EventActorSummary-EventActorId"></a>
The unique identifier of the event actor. You provide this to [GetEventActor](API_GetEventActor.md) to retrieve the details of the event actor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: Yes

 ** Asn **   <a name="WAF-Type-EventActorSummary-Asn"></a>
The autonomous system number (ASN) that is associated with the client IP address of the event actor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** AsnOrganization **   <a name="WAF-Type-EventActorSummary-AsnOrganization"></a>
The name of the organization that owns the ASN. For example, `AMAZON-02`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** AuthFingerprint **   <a name="WAF-Type-EventActorSummary-AuthFingerprint"></a>
A hash of the authentication credentials that the client of the event actor provides in the request. These can include a JSON Web Token (JWT), a JSON Web Encryption (JWE) token, an AWS Signature Version 4 (SigV4) signature, or basic authentication credentials. You can use the fingerprint to match the same client across events and in your AWS WAF logs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** ClientIp **   <a name="WAF-Type-EventActorSummary-ClientIp"></a>
The client IP address of the event actor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Country **   <a name="WAF-Type-EventActorSummary-Country"></a>
The country of the client IP address of the event actor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** CreatedAt **   <a name="WAF-Type-EventActorSummary-CreatedAt"></a>
The time when AWS WAF first observed the event actor.
Type: Timestamp
Required: No

 ** EventCount **   <a name="WAF-Type-EventActorSummary-EventCount"></a>
The number of API security events that the event actor is associated with in the requested time window.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TlsFingerprint **   <a name="WAF-Type-EventActorSummary-TlsFingerprint"></a>
The TLS fingerprint of the event actor, such as a JA3 or JA4 fingerprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_EventActorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/EventActorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/EventActorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/EventActorSummary)
