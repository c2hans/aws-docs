---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_CertificateAuthority.html
---

# CertificateAuthority
<a name="API_CertificateAuthority"></a>

An object representing a certificate authority (CA) for an Amazon EKS cluster.

## Contents
<a name="API_CertificateAuthority_Contents"></a>

 ** activatedAt **   <a name="AmazonEKS-Type-CertificateAuthority-activatedAt"></a>
The Unix epoch timestamp in seconds for when the certificate authority was last activated as the cluster's signer. This value is absent if the certificate authority has never been activated.
Type: Timestamp
Required: No

 ** activatedBy **   <a name="AmazonEKS-Type-CertificateAuthority-activatedBy"></a>
The entity that most recently activated the certificate authority. A value of `EKS` indicates that Amazon EKS activated it automatically; `CUSTOMER` indicates that you activated it.
Type: String
Valid Values: `EKS | CUSTOMER`
Required: No

 ** createdAt **   <a name="AmazonEKS-Type-CertificateAuthority-createdAt"></a>
The Unix epoch timestamp in seconds for when the certificate authority was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="AmazonEKS-Type-CertificateAuthority-createdBy"></a>
The entity that created the certificate authority. Certificate authorities that you create are `CUSTOMER`; those that Amazon EKS provisions on your behalf, such as a cluster's initial certificate authority, are `EKS`.
Type: String
Valid Values: `EKS | CUSTOMER`
Required: No

 ** data **   <a name="AmazonEKS-Type-CertificateAuthority-data"></a>
The Base64-encoded public certificate of the certificate authority.
Type: String
Required: No

 ** distributionStatus **   <a name="AmazonEKS-Type-CertificateAuthority-distributionStatus"></a>
The distribution status of the certificate authority, which tracks whether Amazon EKS has distributed its trust to the AWS managed components in your cluster (the control plane, Amazon EKS Auto Mode instances, and AWS Fargate nodes). Valid values are `IN_PROGRESS`, `COMPLETE`, `FAILED`, and `DELETING`. A successor CA can only be activated after its distribution status is `COMPLETE`.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED | DELETING`
Required: No

 ** id **   <a name="AmazonEKS-Type-CertificateAuthority-id"></a>
The unique identifier of the certificate authority.
Type: String
Required: No

 ** rollbackAvailable **   <a name="AmazonEKS-Type-CertificateAuthority-rollbackAvailable"></a>
Indicates whether CA rollback is still available for this certificate authority. After you activate a successor CA, rollback lets you revert to the outgoing CA for a limited period while you finish updating any worker nodes or clients that were missed.
Type: Boolean
Required: No

 ** scheduledEvents **   <a name="AmazonEKS-Type-CertificateAuthority-scheduledEvents"></a>
The scheduled auto-activation events for the certificate authority, computed from its validity period.
Type: [CertificateAuthorityScheduledEvents](API_CertificateAuthorityScheduledEvents.md) object
Required: No

 ** signingStatus **   <a name="AmazonEKS-Type-CertificateAuthority-signingStatus"></a>
The signing status of the certificate authority. `IN_USE` means the certificate authority is currently signing certificates for the cluster, `ACTIVATING` means it's being promoted to the signer, and `NOT_USED` means it's trusted by the cluster (for example, a successor CA during a rotation, or a retired outgoing CA) but isn't the signer.
Type: String
Valid Values: `NOT_USED | ACTIVATING | IN_USE`
Required: No

 ** validity **   <a name="AmazonEKS-Type-CertificateAuthority-validity"></a>
The validity period of the certificate authority's certificate.
Type: [CertificateAuthorityValidity](API_CertificateAuthorityValidity.md) object
Required: No

## See Also
<a name="API_CertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CertificateAuthority)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
