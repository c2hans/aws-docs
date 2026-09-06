---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_TlsValidationContextTrust.html
---

# TlsValidationContextTrust
<a name="API_TlsValidationContextTrust"></a>

An object that represents a Transport Layer Security (TLS) validation context trust.

## Contents
<a name="API_TlsValidationContextTrust_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** acm **   <a name="appmesh-Type-TlsValidationContextTrust-acm"></a>
A reference to an object that represents a Transport Layer Security (TLS) validation context trust for an AWS Certificate Manager certificate.
Type: [TlsValidationContextAcmTrust](API_TlsValidationContextAcmTrust.md) object
Required: No

 ** file **   <a name="appmesh-Type-TlsValidationContextTrust-file"></a>
An object that represents a Transport Layer Security (TLS) validation context trust for a local file.
Type: [TlsValidationContextFileTrust](API_TlsValidationContextFileTrust.md) object
Required: No

 ** sds **   <a name="appmesh-Type-TlsValidationContextTrust-sds"></a>
A reference to an object that represents a Transport Layer Security (TLS) Secret Discovery Service validation context trust.
Type: [TlsValidationContextSdsTrust](API_TlsValidationContextSdsTrust.md) object
Required: No

## See Also
<a name="API_TlsValidationContextTrust_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/TlsValidationContextTrust)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/TlsValidationContextTrust)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/TlsValidationContextTrust)
