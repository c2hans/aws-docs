---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CertificateAssociationSummary.html
---

# CertificateAssociationSummary
<a name="API_CertificateAssociationSummary"></a>

Describes a summary of a certificate association.

## Contents
<a name="API_CertificateAssociationSummary_Contents"></a>

 ** acmCertificateArn **   <a name="rtbfabric-Type-CertificateAssociationSummary-acmCertificateArn"></a>
The Amazon Resource Name (ARN) of the ACM certificate.
Type: String
Length Constraints: Minimum length of 75. Maximum length of 256.
Pattern: `arn:(aws|aws-cn|aws-us-gov):acm:[a-z0-9-]+:[0-9]{12}:certificate/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** status **   <a name="rtbfabric-Type-CertificateAssociationSummary-status"></a>
The status of the certificate association.
Type: String
Valid Values: `PENDING_ASSOCIATION | ASSOCIATED | PENDING_DISASSOCIATION | DISASSOCIATED | FAILED`
Required: Yes

 ** associatedAt **   <a name="rtbfabric-Type-CertificateAssociationSummary-associatedAt"></a>
The timestamp of when the certificate was associated.
Type: Timestamp
Required: No

 ** updatedAt **   <a name="rtbfabric-Type-CertificateAssociationSummary-updatedAt"></a>
The timestamp of when the certificate association was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_CertificateAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/CertificateAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/CertificateAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/CertificateAssociationSummary)
