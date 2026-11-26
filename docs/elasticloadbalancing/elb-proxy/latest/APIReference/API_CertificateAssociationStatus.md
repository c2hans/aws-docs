---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_CertificateAssociationStatus.html
---

# CertificateAssociationStatus

The status of a certificate association.

## Contents
<a name="API_CertificateAssociationStatus_Contents"></a>

 ** code **   <a name="elasticloadbalancing-Type-CertificateAssociationStatus-code"></a>
The status code of the association.
Type: String
Valid Values: `associate-in-progress | active | associate-failed | disassociate-in-progress | disassociated`
Required: Yes

 ** reasons **   <a name="elasticloadbalancing-Type-CertificateAssociationStatus-reasons"></a>
The reasons for the current status of the association.
Type: Array of [CertificateAssociationStatusReason](API_CertificateAssociationStatusReason.md) objects
Required: Yes

## See Also
<a name="API_CertificateAssociationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/CertificateAssociationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/CertificateAssociationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/CertificateAssociationStatus)
