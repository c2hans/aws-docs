---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_CertificateAssociation.html
---

# CertificateAssociation

An association between an ACM certificate and a proxy.

## Contents
<a name="API_CertificateAssociation_Contents"></a>

 ** certificateArn **   <a name="elasticloadbalancing-Type-CertificateAssociation-certificateArn"></a>
The Amazon Resource Name (ARN) of the ACM certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:[a-z0-9\-]+:acm:[a-z0-9\-]+:[0-9]{12}:certificate/.+`
Required: Yes

 ** status **   <a name="elasticloadbalancing-Type-CertificateAssociation-status"></a>
The status of the association.
Type: [CertificateAssociationStatus](API_CertificateAssociationStatus.md) object
Required: Yes

 ** createdAt **   <a name="elasticloadbalancing-Type-CertificateAssociation-createdAt"></a>
The date and time that the association was created.
Type: Timestamp
Required: No

## See Also
<a name="API_CertificateAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/CertificateAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/CertificateAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/CertificateAssociation)
