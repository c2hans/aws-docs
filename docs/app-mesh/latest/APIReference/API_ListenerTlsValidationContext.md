---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListenerTlsValidationContext.html
---

# ListenerTlsValidationContext
<a name="API_ListenerTlsValidationContext"></a>

An object that represents a listener's Transport Layer Security (TLS) validation context.

## Contents
<a name="API_ListenerTlsValidationContext_Contents"></a>

 ** trust **   <a name="appmesh-Type-ListenerTlsValidationContext-trust"></a>
A reference to where to retrieve the trust chain when validating a peer’s Transport Layer Security (TLS) certificate.
Type: [ListenerTlsValidationContextTrust](API_ListenerTlsValidationContextTrust.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** subjectAlternativeNames **   <a name="appmesh-Type-ListenerTlsValidationContext-subjectAlternativeNames"></a>
A reference to an object that represents the SANs for a listener's Transport Layer Security (TLS) validation context.
Type: [SubjectAlternativeNames](API_SubjectAlternativeNames.md) object
Required: No

## See Also
<a name="API_ListenerTlsValidationContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ListenerTlsValidationContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ListenerTlsValidationContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ListenerTlsValidationContext)
