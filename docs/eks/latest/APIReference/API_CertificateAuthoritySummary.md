---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_CertificateAuthoritySummary.html
---

# CertificateAuthoritySummary
<a name="API_CertificateAuthoritySummary"></a>

Summary information about a certificate authority (CA) for an Amazon EKS cluster, returned by [`ListCertificateAuthorities`](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListCertificateAuthorities.html) and the certificate-authority write operations.

## Contents
<a name="API_CertificateAuthoritySummary_Contents"></a>

 ** activatedAt **   <a name="AmazonEKS-Type-CertificateAuthoritySummary-activatedAt"></a>
The Unix epoch timestamp in seconds for when the certificate authority was last activated. This value is absent if the certificate authority has never been activated.
Type: Timestamp
Required: No

 ** activatedBy **   <a name="AmazonEKS-Type-CertificateAuthoritySummary-activatedBy"></a>
The entity that most recently activated the certificate authority, either `CUSTOMER` or `EKS`.
Type: String
Valid Values: `EKS | CUSTOMER`
Required: No

 ** createdAt **   <a name="AmazonEKS-Type-CertificateAuthoritySummary-createdAt"></a>
The Unix epoch timestamp in seconds for when the certificate authority was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="AmazonEKS-Type-CertificateAuthoritySummary-createdBy"></a>
The entity that created the certificate authority, either `CUSTOMER` or `EKS`.
Type: String
Valid Values: `EKS | CUSTOMER`
Required: No

 ** distributionStatus **   <a name="AmazonEKS-Type-CertificateAuthoritySummary-distributionStatus"></a>
The distribution status of the certificate authority: `IN_PROGRESS`, `COMPLETE`, `FAILED`, or `DELETING`.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED | DELETING`
Required: No

 ** id **   <a name="AmazonEKS-Type-CertificateAuthoritySummary-id"></a>
The unique identifier of the certificate authority.
Type: String
Required: No

 ** signingStatus **   <a name="AmazonEKS-Type-CertificateAuthoritySummary-signingStatus"></a>
The signing status of the certificate authority: `IN_USE`, `ACTIVATING`, or `NOT_USED`.
Type: String
Valid Values: `NOT_USED | ACTIVATING | IN_USE`
Required: No

## See Also
<a name="API_CertificateAuthoritySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CertificateAuthoritySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CertificateAuthoritySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CertificateAuthoritySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
