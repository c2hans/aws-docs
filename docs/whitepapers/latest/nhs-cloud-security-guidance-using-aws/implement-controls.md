---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/implement-controls.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implement controls
<a name="implement-controls"></a>

 *Appendix A: Detailed Advice and Guidance* of the [Good Practice Guide](https://digital.nhs.uk/data-and-information/looking-after-information/data-security-and-information-governance/nhs-and-social-care-data-off-shoring-and-the-use-of-public-cloud-services) describes in detail both the security controls that AWS customers should require of a cloud provider and the controls that they should implement when consuming that provider’s services – AWS, in this case. These follow the structure of the [NCSC’s 14 Cyber-Security Principles](https://www.ncsc.gov.uk/guidance/implementing-cloud-security-principles), examining each in turn and detailing provider requirements under the heading *The Cloud Provider should:* and customer responsibilities under *The Service User should:*. For the remainder of this whitepaper, the AWS customer is synonymous with the *Service User*. The guidance in the Good Practice Guide recognises the concept of the [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) for security in the cloud, which apportions responsibility for the security of element of the cloud and its use to the party most appropriate to manage it. In summary, AWS is responsible for the security *of* the cloud, while customers are responsible for security *in* the cloud.

 This section provides prescriptive guidance on how to make concrete the required controls in AWS, specifically. It is intended to be read in conjunction with the companion AWS whitepaper [https://d1.awsstatic.com/whitepapers/compliance/AWS_CESG_UK_Cloud_Security_Principles.pdf](https://d1.awsstatic.com/whitepapers/compliance/AWS_CESG_UK_Cloud_Security_Principles.pdf) (which explains how AWS fulfils its responsibility for the security of the cloud) and document “Security Controls Mapping - Health and Social Care Cloud Security” (derived directly from the guidance, and obtainable on request. To request the document, [contact Compliance Support](https://aws.amazon.com/contact-us/compliance-support/)).

**Note**
Not all of the controls described in this section are necessarily required for a given system being deployed to AWS; those required depend on the system’s Risk Classification. Refer to *Appendix A: Detailed Advice and Guidance* of the Good Practice Guide for authoritative information on which controls to apply.
