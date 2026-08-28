---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_CertificateAuthorityScheduledEvents.html
---

# CertificateAuthorityScheduledEvents
<a name="API_CertificateAuthorityScheduledEvents"></a>

The scheduled events during which Amazon EKS may automatically activate a certificate authority, computed from its validity period. These events help ensure that a cluster's signing certificate authority is rotated before its certificate expires.

## Contents
<a name="API_CertificateAuthorityScheduledEvents_Contents"></a>

 ** finalAutoActivation **   <a name="AmazonEKS-Type-CertificateAuthorityScheduledEvents-finalAutoActivation"></a>
The Unix epoch timestamp in seconds by which Amazon EKS will automatically activate this certificate authority if you haven't already activated it.
Type: Timestamp
Required: No

 ** firstAutoActivation **   <a name="AmazonEKS-Type-CertificateAuthorityScheduledEvents-firstAutoActivation"></a>
The earliest Unix epoch timestamp in seconds at which Amazon EKS may automatically activate this certificate authority.
Type: Timestamp
Required: No

## See Also
<a name="API_CertificateAuthorityScheduledEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CertificateAuthorityScheduledEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CertificateAuthorityScheduledEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CertificateAuthorityScheduledEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
