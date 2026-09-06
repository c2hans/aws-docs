---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ActiveCertificateAuthority.html
---

# ActiveCertificateAuthority
<a name="API_ActiveCertificateAuthority"></a>

Identifies the certificate authority that is currently signing certificates for the cluster.

## Contents
<a name="API_ActiveCertificateAuthority_Contents"></a>

 ** activatedBy **   <a name="AmazonEKS-Type-ActiveCertificateAuthority-activatedBy"></a>
The entity that activated the current signing certificate authority, either `CUSTOMER` or `EKS`.
Type: String
Valid Values: `EKS | CUSTOMER`
Required: No

 ** id **   <a name="AmazonEKS-Type-ActiveCertificateAuthority-id"></a>
The unique identifier of the certificate authority that is currently signing certificates for the cluster.
Type: String
Required: No

## See Also
<a name="API_ActiveCertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ActiveCertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ActiveCertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ActiveCertificateAuthority)
