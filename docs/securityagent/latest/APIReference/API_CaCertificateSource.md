---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CaCertificateSource.html
---

# CaCertificateSource
<a name="API_CaCertificateSource"></a>

The source of a trusted CA certificate. Exactly one member must be set.

## Contents
<a name="API_CaCertificateSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** artifactId **   <a name="securityagent-Type-CaCertificateSource-artifactId"></a>
The artifact ID of an uploaded certificate file.
Type: String
Required: No

 ** inlinePem **   <a name="securityagent-Type-CaCertificateSource-inlinePem"></a>
A PEM-encoded X.509 certificate supplied inline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** s3Location **   <a name="securityagent-Type-CaCertificateSource-s3Location"></a>
The Amazon S3 location URI of a customer-staged certificate.
Type: String
Required: No

## See Also
<a name="API_CaCertificateSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CaCertificateSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CaCertificateSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CaCertificateSource)
