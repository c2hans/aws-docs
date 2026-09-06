---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/faq.html
---

# FAQ
<a name="faq"></a>

This section answers common questions about the CMMC program, the CMMC model and its relationship to NIST standards, assessment requirements and scoring, implementation timelines, the role of external service providers and FedRAMP, how the AWS Shared Responsibility Model applies to control inheritance, and how to prepare for a C3PAO assessment on AWS.

## About CMMC
<a name="about-cmmc"></a>

### When will CMMC assessments be required for Department of Defense contracts?
<a name="when-will-cmmc-assessments-be-required-for-department-of-defense-contracts-.7f99a1eb-4258-5710-b0a0-ae4e02bca928"></a>

The DoD began incorporating CMMC assessment requirements in applicable procurements on November 10, 2025, when the revised DFARS clause 252.204-7021 became effective. The first 12 months of implementation primarily focus on self-assessments. For further information on the DoD's phased implementation plan, see 32 CFR 170.3(e).

### How much will it cost to achieve CMMC compliance?
<a name="how-much-will-it-cost-to-achieve-cmmc-compliance-.1718f44c-205f-55de-be76-cf9ee2ded945"></a>

Costs incurred to implement existing contract requirements for safeguarding information (for example, DFARS 252.204-7012) are not considered part of the CMMC compliance cost. The cost of achieving CMMC compliance (self-assessment or certification) depends on various factors, including the CMMC level required, the complexity of the DIB company's unclassified network, the existing cybersecurity posture of the organization, and market forces of supply and demand.

### What resources are available to assist companies in complying with DoD cybersecurity requirements?
<a name="what-resources-are-available-to-assist-companies-in-complying-with-dod-cybersecurity-requirements-.7e0cbf67-bc92-51d1-9631-02f5279456d1"></a>

The DoD provides several resources to help businesses reach cybersecurity compliance:
+ The DoD CIO DIB Cybersecurity Program has compiled no-cost Cybersecurity-as-a-Service resources to reduce barriers to DIB community compliance.
+ The Cyber AB Marketplace lists certified CMMC assessors, professionals, and registered practitioner organizations.
+ The Defense Acquisition University (DAU) offers free online CMMC and cybersecurity training.
+ The DoD Office of Small Business Programs has compiled resources aimed at helping small and medium-sized businesses understand security requirements.

In addition, AWS provides resources to support your compliance journey, including the AWS CMMC Compliance page, the AWS NIST SP 800-171 / CMMC 2.0 Level 2 CRM, and AWS Artifact for on-demand access to AWS compliance reports.

### Who is the point of contact for general inquiries regarding the CMMC Program?
<a name="who-is-the-point-of-contact-for-general-inquiries-regarding-the-cmmc-program-.5964e4a9-a169-5771-8bbd-d6f3851f1f31"></a>
+ CMMC Program, model, or policy: Use the CMMC PMO contact form.
+ Registered Practitioner (RP/RPA) and C3PAO application status: Contact the Cyber AB at support@cyberab.org.
+ Certified Professional (CCP) or Certified Assessor (CCA) application status: Contact the Cybersecurity Assessor and Instructor Certification Organization (CAICO) at support@cyberab.org.

## CMMC model
<a name="cmmc-model"></a>

### How will my organization know what CMMC level is required for a contract?
<a name="how-will-my-organization-know-what-cmmc-level-is-required-for-a-contract-.ca587b85-db95-5530-bb7f-0283b045af52"></a>

The DoD specifies the required CMMC level in the solicitation and the resulting contract. The level is determined by the type and sensitivity of the information the contractor will handle:
+ Level 1 (Foundational): 15 basic safeguarding requirements from Federal Acquisition Regulation (FAR) 52.204-21. Annual self-assessment. Applies when only FCI is present.
+ Level 2 (Advanced): 110 security requirements from NIST SP 800-171 Revision 2. Self-assessment or C3PAO assessment. Applies when CUI is present.
+ Level 3 (Expert): 24 additional requirements from NIST SP 800-172, on top of the 110 Level 2 requirements. Government-led assessment by DIBCAC. Applies to the most sensitive CUI.

### What is the relationship between NIST SP 800-171 and CMMC?
<a name="what-is-the-relationship-between-nist-sp-800-171-and-cmmc-.fd4e8226-115e-5727-b1a0-a19a17de6312"></a>

NIST SP 800-171 is the federal safeguarding standard for CUI required by 32 CFR Part 2002, which the DoD implemented contractually through DFARS clause 252.204-7012. Beginning November 10, 2025, applicable contractors are required to undergo a Level 2 self-assessment or a CMMC third-party assessment to verify compliance with NIST SP 800-171 Revision 2 requirements.

### Will the DoD update CMMC to use NIST SP 800-171 Revision 3?
<a name="will-the-dod-update-cmmc-to-use-nist-sp-800-171-revision-3-.a2c9d4ab-e53e-5f84-938a-cd8ed1bda862"></a>

Yes. The DoD will incorporate Revision 3 through future rulemaking. In the interim, the DoD has issued a class deviation to DFARS clause 252.204-7012 to maintain Revision 2 as the assessment standard until Revision 3 has been incorporated into the 32 CFR CMMC Program rule.

### Can DoD contractors implement NIST SP 800-171 Revision 3 now?
<a name="can-dod-contractors-implement-nist-sp-800-171-revision-3-now-.389dab76-4fc0-5417-958d-d7488afa0231"></a>

Yes. Companies can implement Revision 3 but must use the DoD's ODPs defined in the April 2025 memorandum. Because CMMC assessments will be conducted against Revision 2 until the class deviation is withdrawn or superseded, DIB companies must ensure any identified gaps between Revision 2 and Revision 3 are addressed.

### What is the relationship between NIST SP 800-172 and CMMC?
<a name="what-is-the-relationship-between-nist-sp-800-172-and-cmmc-.1411bf4e-61e8-5e3e-89cb-bfae2561b32e"></a>

NIST SP 800-172 provides security requirements designed to address advanced persistent threats and forms the basis for CMMC Level 3. Contractors must implement 24 requirements from NIST SP 800-172 in addition to the 110 requirements from NIST SP 800-171 when the DoD identifies Level 3 as a contract requirement.

### Will CMMC requirements flow down to subcontractors?
<a name="will-cmmc-requirements-flow-down-to-subcontractors-.e5ae18b6-724f-546a-922b-beca9f814b97"></a>

Yes. Per 32 CFR 170.23, CMMC requirements flow down to subcontractors based on the type of data (FCI or CUI) that will be processed, stored, or transmitted on the subcontractor's information system:
+ Subcontractor handles FCI only: Level 1 (Self-Assessment) required.
+ Subcontractor handles CUI, prime requires Level 2 (Self): Level 2 (Self) minimum.
+ Subcontractor handles CUI, prime requires Level 2 (C3PAO): Level 2 (C3PAO) minimum.
+ Prime contract requires Level 3: Minimum flow-down is Level 2 (C3PAO), unless the government provides specific contractual guidance (for example, a Security Classification Guide).

### What is the difference between FCI and CUI?
<a name="what-is-the-difference-between-fci-and-cui-.ee0040c8-bcdf-5929-83aa-d0869b550242"></a>

Both FCI and CUI are information that is "not intended for public release." However, CUI requires additional safeguarding and may also be subject to dissemination controls.
+ FCI is defined in FAR clause 52.204-21.
+ CUI is defined in 32 CFR Part 2002. The DoD's CUI Quick Reference Guide includes additional information on marking and handling.

CMMC makes no changes to CUI definitions or safeguarding requirements. If your contract involves CUI, you need Level 2. If it involves only FCI, Level 1 applies.

### Is encrypted CUI still considered to be CUI?
<a name="is-encrypted-cui-still-considered-to-be-cui-.eada1b66-0754-5d01-941e-22fe0bbc53fa"></a>

Yes. Per 32 CFR Part 2002, CUI remains controlled until it is formally decontrolled. Encrypted CUI data retains the control designation given to the plain text counterpart. While certain risks (for example, transmission across unsecured networks) are accepted for cipher text that would not be accepted for plain text, this does not mean the original controlled information is considered decontrolled.

This has direct implications for cloud deployments: even if CUI is encrypted at rest in a CSP environment, the CSP must still meet FedRAMP Moderate baseline requirements per DFARS 252.204-7012.

## Assessments
<a name="assessments"></a>

### How frequently will assessments be required?
<a name="how-frequently-will-assessments-be-required-.7ea2add4-83fd-5d6b-b612-1c1dcafe02dc"></a>

Level 1 self-assessments are required annually. CMMC Levels 2 and 3 assessments are required every three years. An affirmation of continued compliance is required for all CMMC levels at the time of assessment and annually thereafter. See 32 CFR 170.3(e) for the phased implementation timeline.

### Will my organization need to be independently assessed if it does not handle CUI?
<a name="will-my-organization-need-to-be-independently-assessed-if-it-does-not-handle-cui-.b3a2c05f-b6cf-5696-a089-2edccd718386"></a>

No. If a DIB company does not process, store, or transmit CUI, it does not need an independent (C3PAO) assessment. If the company handles FCI only, a CMMC Level 1 self-assessment is required.

### Will CMMC assessments be required for classified systems or classified environments?
<a name="will-cmmc-assessments-be-required-for-classified-systems-or-classified-environments-.5ddafccf-f4a2-5249-b444-c1d89199d979"></a>

No. CMMC only applies to DIB contractors' nonfederal unclassified information systems that process, store, or transmit FCI or CUI.

### Will assessment results be made public?
<a name="will-assessment-results-be-made-public-.8ec1cde4-c7a2-5784-a23e-41cf79928839"></a>

The public will not have access to a listing of DIB companies that have completed CMMC self-assessments or received certificates. Such information is available to DoD officers leading procurement activities.

A company can view its own scores and status in SPRS. Suppliers may print verification of their status from SPRS to share with primes. Subcontractors may voluntarily share their CMMC Status, assessment scores, or certificates to facilitate business teaming arrangements.

### Does my company need a specific CAGE code for each location to comply with CMMC?
<a name="does-my-company-need-a-specific-cage-code-for-each-location-to-comply-with-cmmc-.32470700-8732-5f14-b4a2-965d2f5149c4"></a>

No. Another existing Commercial and Government Entity (CAGE) code in the company's hierarchy may be used to submit the appropriate assessment identified by the CMMC Unique Identifier (UID). The CMMC UID must contain the scope that covers the assessment. CAGE codes (including the Highest-Level Owner) are used for metrics purposes, to enforce authorized access to data in SPRS, and to perform annual affirmations.

### Which requirements are not allowed on a Plan of Action and Milestones?
<a name="which-requirements-are-not-allowed-on-a-plan-of-action-and-milestones-.031c0e22-3ee1-5437-a9c8-6a1461804261"></a>

The 26 POA&M-ineligible requirements are identified in 32 CFR 170.21. These are primarily Basic security requirements that must be MET at the time of assessment. If any POA&M-ineligible requirement is NOT MET, the organization cannot achieve even Conditional CMMC Status regardless of overall score.

The POA&M-ineligible requirements are:
+ Access Control (AC): 3.1.1, 3.1.2, 3.1.20, 3.1.22
+ Audit and Accountability (AU): 3.3.1, 3.3.2
+ Configuration Management (CM): 3.4.1, 3.4.2
+ Identification and Authentication (IA): 3.5.1, 3.5.2
+ Media Protection (MP): 3.8.3
+ Personnel Security (PS): 3.9.1, 3.9.2
+ Physical Protection (PE): 3.10.1, 3.10.2
+ Risk Assessment (RA): 3.11.1
+ Security Assessment (CA): 3.12.1, 3.12.3, 3.12.4
+ System and Communications Protection (SC): 3.13.1, 3.13.2, 3.13.5
+ System and Information Integrity (SI): 3.14.1, 3.14.2, 3.14.4, 3.14.5

On AWS, many of these map to foundational services such as IAM, CloudTrail, AWS Config, and Amazon VPC. Organizations should prioritize these requirements first in any remediation effort.

### What happens after a POA&M Closeout Assessment if requirements are still not met?
<a name="what-happens-after-a-poa9999999999999999amp-m-closeout-assessment-if-requirements-are-still-not-met-.2d67e2cd-30b9-5f6a-8611-066edbad420f"></a>

During the 180-day period after achieving Conditional CMMC Status, a POA&M Closeout Assessment can only be finalized in the CMMC Enterprise Mission Assurance Support System (eMASS) one time. If one or more security requirements are still NOT MET, the Conditional CMMC Status will be terminated once the POA&M Closeout Assessment is finalized, and the Organization Seeking Assessment (OSA) will have to begin again with a new assessment. If a POA&M Closeout Assessment is not finalized in CMMC eMASS within 180 days of the CMMC Status Date, the Conditional CMMC Status will automatically expire.

### What is the difference between an Operational Plan of Action and a POA&M?
<a name="what-is-the-difference-between-an-operational-plan-of-action-and-a-poa9999999999999999amp-m-.aa39b285-1dc8-554e-a27d-c2ddc1fbdec1"></a>

Operational Plans of Action (OPAs) are measures implemented to manage risks or vulnerabilities that arise after the initial implementation of security requirements, such as applying patches, addressing temporary deficiencies, or performing routine system maintenance. OPAs are not tied to a specific timeline for completion.

POA&Ms are formal plans that identify cybersecurity gaps the OSA must address to achieve CMMC compliance. These gaps must be resolved within 180 days, as outlined in 32 CFR 170.21.

When a significant change occurs in an information system that affects the satisfaction of NIST SP 800-171 security requirements:
+ If the change introduces a temporary deficiency after the system was initially compliant, an OPA may be created to document the remediation plan.
+ If the change is identified during a CMMC assessment and results in a requirement being assessed as NOT MET, a POA&M must be created to address the gap within the 180-day window.

For detailed definitions, see 32 CFR 170.4.

### I entered my CMMC self-assessment into SPRS and received "No CMMC Status" or "No CMMC Score." How do I fix this?
<a name="i-entered-my-cmmc-self-assessment-into-sprs-and-received--no-cmmc-status--or--no-cmmc-score.--how-do-i-fix-this-.22a0879b-a307-5ecd-b0e7-836acd66f282"></a>

No Score: You marked "Not Met" for security requirement CA.L2-3.12.4 (System Security Plan). The absence of an up-to-date SSP at the time of assessment results in a finding that an assessment could not be completed due to incomplete information and noncompliance with DFARS clause 252.204-7012. See 32 CFR 170.24 for the scoring methodology.

No Status: One or more of these conditions exist:
+ The assessment score divided by the total number of Level 2 security requirements is less than 0.8 (equivalent to a score below 88).
+ You have placed security requirements on a POA&M that are not permitted per 32 CFR 170.21. Review each POA&M item to confirm it is not one of the 26 POA&M-ineligible requirements.

### Are CMMC assessments required for organizations that only handle hard-copy CUI?
<a name="are-cmmc-assessments-required-for-organizations-that-only-handle-hard-copy-cui-.d9822c29-223a-5dbe-9f1d-25c1b63aa06e"></a>

No. CMMC assessment requirements address cybersecurity-related risk to CUI and apply only when CUI is processed, stored, or transmitted on a contractor-owned information technology system. Organizations that only handle hard-copy CUI should not be required to complete a CMMC assessment. However, contractors are still required to protect hard-copy CUI per DoDI 5200.48.

If a contractor who was only provided hard-copy CUI plans to place it on an information technology system (for example, scanned, entered, photographed, uploaded, printed, emailed), that system is subject to the applicable CMMC assessment requirements before the CUI is placed on it.

For organizations that handle paper CUI in addition to digital CUI, the CMMC assessment will address both, in accordance with the applicable NIST SP 800-171 security requirements.

### Can encryption alone create logical separation for a network within a CMMC Assessment Scope?
<a name="can-encryption-alone-create-logical-separation-for-a-network-within-a-cmmc-assessment-scope-.78ad173a-980a-53c4-9f1c-95528fc9fe67"></a>

No. Logical separation occurs when data transfer between physically connected assets (wired or wireless) is prevented by non-physical means such as software or network assets (for example, firewalls, routers, VPNs, VLANs). While properly implemented encryption provides necessary confidentiality protection, it does not, by itself, prevent data transfer or enforce the security boundary of a network.

On AWS logical separation is typically achieved through Amazon VPC configurations (subnets, security groups, network access control lists), AWS Transit Gateway routing policies, and AWS PrivateLink for private connectivity, in combination with encryption provided by AWS KMS.

### If our enclave relies on enterprise networking components outside the enclave, and all CUI data is encrypted before leaving the enclave, must the enterprise networking components be in scope?
<a name="if-our-enclave-relies-on-enterprise-networking-components-outside-the-enclave--and-all-cui-data-is-encrypted-before-leaving-the-enclave--must-the-enterprise-networking-components-be-in-scope-.4ebafb7d-799d-5755-8dab-7fed42c7cf4f"></a>

No. So long as the enclave is otherwise logically separated from the greater enterprise network, the transmission of properly encrypted CUI data does not incur an extension of the CMMC Assessment Scope to include the enterprise networking components.

This principle applies to AWS architectures where a CUI-processing Amazon VPC transmits encrypted data through shared networking infrastructure (for example, AWS Transit Gateway or AWS Direct Connect) to reach other enclaves or on-premises systems. The shared networking components do not need to be in the CMMC Assessment Scope, provided the CUI enclave is logically separated and CUI is encrypted in transit.

## Implementation
<a name="implementation"></a>

### How will the DoD implement CMMC?
<a name="how-will-the-dod-implement-cmmc-.4ecffc82-1f82-52d8-9a2b-4450b8eb0e36"></a>

Beginning November 10, 2025, the DoD is implementing CMMC requirements in four phases over a three-year period, as described in 32 CFR 170.3(e):
+ Phase 1 (November 2025): DoD begins including Level 1 and Level 2 self-assessment requirements in new solicitations and contracts. The first 12 months focus primarily on self-assessments.
+ Phase 2 (November 2026): DoD begins including Level 2 C3PAO certification requirements in applicable solicitations.
+ Phase 3 (November 2027): DoD begins including Level 3 DIBCAC assessment requirements in applicable solicitations.
+ Phase 4 (November 2028): Full implementation across all applicable solicitations and contracts, including option periods.

The phased approach is intended to address ramp-up issues, provide time to train assessors, allow companies time to implement requirements, and minimize financial impacts to defense contractors (especially small businesses) and disruption to the defense supply chain.

### How can businesses best prepare for CMMC?
<a name="how-can-businesses-best-prepare-for-cmmc-.f89bf46b-9662-5f42-aedd-6477b1b65a6b"></a>

Whether a company has previously been awarded a defense contract with DFARS clause 252.204-7012 or is new to defense contracting, the best preparation is to carefully conduct a self-assessment of contractor-owned information systems to verify implementation of the necessary cybersecurity measures for FAR clause 52.204-21 (for FCI) or DFARS clause 252.204-7012 (for CUI). If the self-assessment identifies unmet requirements, companies should take corrective action to address those gaps and fully implement the necessary security measures before initiating a CMMC assessment.

For organizations building on AWS, this includes reviewing the AWS CRM to understand which of the 110 requirements are fully inheritable from AWS, which are shared, and which are solely the customer's responsibility.

### Will CMMC apply to non-U.S. companies?
<a name="will-cmmc-apply-to-non-u.s.-companies-.2b75c697-338f-5864-ba9d-33840836d790"></a>

Yes. When CMMC requirements are identified in DoD solicitations, they apply to all companies performing under the resulting contract, whether domestic or international.

### Can non-U.S. citizens or organizations be part of the CMMC Ecosystem?
<a name="can-non-u.s.-citizens-or-organizations-be-part-of-the-cmmc-ecosystem-.d06d9014-6ac2-5bb3-b34e-04e4b763288b"></a>

Yes. Individuals and organizations that meet all requirements established under 32 CFR Part 170 are eligible to apply to be members of the CMMC Ecosystem, regardless of nationality or country of origin.

### During Phase 1, does DoD policy require Program Managers to include CMMC Level 2 (C3PAO) in a solicitation if the contractor will handle CUI from the Defense Organizational Index Grouping?
<a name="during-phase-1--does-dod-policy-require-program-managers-to-include-cmmc-level-2--c3pao--in-a-solicitation-if-the-contractor-will-handle-cui-from-the-defense-organizational-index-grouping-.ffe95ba7-b46c-5501-86de-775ff3d5e8c8"></a>

No. During Phase 1, the DoD's intent is that all solicitations focus on including the right CMMC self-assessment requirement: Level 1 when only FCI will be processed, stored, or transmitted, and Level 2 (Self) when any CUI will be processed, stored, or transmitted in contractor-owned information systems.

While 32 CFR Part 170 provides Program Managers some discretion to include Level 2 (C3PAO) requirements during Phase 1, it is not required. The DoD anticipates that during Phase 1, some solicitations will only include a Level 2 (Self) assessment requirement, even when the CUI comes from the Defense Organizational Index Group.

Program Managers may also discuss with their Contracting Officer the possibility of including the CMMC clause with a Level 2 (Self) requirement at the time of award but specifying that Level 2 (C3PAO) will be required at the time of any option period exercise. Program Managers should only use the discretion to include Level 2 (C3PAO) during Phase 1 when, informed by adequate market research, there is reason to believe enough qualified offerors exist to provide adequate competition.

## External service providers, cloud, and FedRAMP
<a name="external-service-providers-cloud-and-fed-ramp"></a>

### Must my CSP meet FedRAMP Moderate baseline requirements if it processes, stores, or transmits CUI?
<a name="must-my-csp-meet-fedramp-moderate-baseline-requirements-if-it-processes--stores--or-transmits-cui-.ea9d0374-a5a4-58d3-9486-960becf6c1f8"></a>

Yes. Per DFARS 252.204-7012, if the contractor intends to use a CSP to store, process, or transmit CUI in the performance of a contract, the contractor shall require and ensure that the CSP meets security requirements equivalent to those established by the government for the FedRAMP Moderate baseline. This can be met by:
+ Using a FedRAMP Moderate (or higher) authorized service provider, or
+ Using a provider that meets the requirements for equivalency as specified in the DoD's December 2023 FedRAMP Equivalency memo

AWS GovCloud (US) is FedRAMP High authorized (exceeds the Moderate requirement). AWS US East/West commercial regions are FedRAMP Moderate authorized (meets the requirement when properly configured).

### Can a non-FedRAMP Moderate cloud service offering store encrypted CUI data?
<a name="can-a-non-fedramp-moderate-cloud-service-offering-store-encrypted-cui-data-.6f8c000c-1eb8-51ae-996f-716120a74f64"></a>

No. If a contractor intends to use an external CSP in the performance of a DoD contract to store encrypted CUI data, the contractor shall require and ensure that the CSP meets security requirements equivalent to those established for the FedRAMP Moderate baseline. Encryption alone does not remove the FedRAMP requirement.

### An OSA stores CUI in a system provided by a Managed Service Provider that is not a cloud offering. Does the MSP require its own CMMC assessment?
<a name="an-osa-stores-cui-in-a-system-provided-by-a-managed-service-provider-that-is-not-a-cloud-offering.-does-the-msp-require-its-own-cmmc-assessment-.d012502a-28f4-5206-9655-67691f6faec6"></a>

No. The MSP is not required to have its own CMMC assessment but may elect to perform its own self-assessment or undergo a certification assessment. If the MSP chooses to attain a CMMC certification to simplify the OSA's assessment, the assessment level and type need to be the same, or above, as the level and type specified in the OSA's contract with the DoD and cover those assets that are in scope for the OSA's assessment.

The MSP's services are assessed as part of the OSA's assessment. A CRM documenting the division of responsibilities between the OSA and the MSP is required and will be evaluated by the C3PAO Assessment Team.

### We outsource IT support to one ESP (an MSP) and security tools to another ESP (a Managed Security Service Provider, or MSSP). No CUI is sent to either vendor. Are they required to be assessed?
<a name="we-outsource-it-support-to-one-esp--an-msp--and-security-tools-to-another-esp--a-managed-security-service-provider--or-mssp-.-no-cui-is-sent-to-either-vendor.-are-they-required-to-be-assessed-.813f21e1-48ff-5356-8ea9-6f39f6ab9aad"></a>

Yes. Both the MSP and the MSSP qualify as ESPs and will be assessed as part of the OSA's assessment against applicable security requirements. The ESPs do not require their own CMMC certification, but a CRM is required for each.

On AWS, this scenario commonly arises when an organization uses a third-party MSP to administer their AWS environment and a separate MSSP to manage Security Hub, GuardDuty, or other security tooling. Even though CUI is not sent to these providers, they handle SPD (log files, configuration data, vulnerability data, credentials) and are in scope.

### We store CUI in the cloud and our MSP administers the environment. Is the MSP a CSP?
<a name="we-store-cui-in-the-cloud-and-our-msp-administers-the-environment.-is-the-msp-a-csp-.6ebf1885-f305-5cca-aa0a-54d031319dea"></a>

It depends on the relationships between the CSP, the MSP, and the OSA:
+ If the cloud tenant is subscribed or licensed to the OSA (even if the MSP resells the service), the MSP is not a CSP.
+ If the MSP contracts with the CSP and modifies the basic cloud service, the MSP may be a CSP and must meet applicable FedRAMP or equivalency requirements.

For example, if your organization holds the AWS account directly and the MSP administers it on your behalf, the MSP is an ESP (not a CSP), and AWS remains the CSP. If the MSP operates its own platform built on AWS and provides that platform to you as a service, the MSP may itself be a CSP.

### CUI is processed, stored, and transmitted in a Virtual Desktop Infrastructure. Are the endpoints used to access the VDI in scope as CUI assets?
<a name="cui-is-processed--stored--and-transmitted-in-a-virtual-desktop-infrastructure.-are-the-endpoints-used-to-access-the-vdi-in-scope-as-cui-assets-.a17c987f-595a-50d7-a303-2fa76df6fa73"></a>

An endpoint hosting a Virtual Desktop Infrastructure (VDI) client is considered an Out-of-Scope Asset if it is configured to not allow any processing, storage, or transmission of CUI beyond the keyboard, video, and mouse data sent to the VDI client. Proper configuration of the VDI client must be verified. If the configuration allows the endpoint to process, store, or transmit CUI, the endpoint will be considered a CUI Asset and is in scope.

On AWS, Amazon WorkSpaces or Amazon AppStream 2.0 can serve as VDI solutions. The scoping determination depends on the client configuration, not the AWS service itself.

### Can the endpoint used to access a VDI be considered "out of scope" if CUI remains entirely within the VDI instance?
<a name="can-the-endpoint-used-to-access-a-vdi-be-considered--out-of-scope--if-cui-remains-entirely-within-the-vdi-instance-.23d2ea28-0b89-50af-911b-25424da4c68d"></a>

Yes, the endpoint could be considered out of scope, but this depends on how the VDI and VDI server are implemented. To achieve out-of-scope status, these conditions must be met:
+ The virtual desktop server must be configured to block copy-paste, file transfers, or any other data exchange across the session.
+ The VDI should only transmit video, keyboard, and mouse data.
+ Users must log into the virtual desktop and handle CUI entirely within the session.
+ MFA to the VDI server must be separate from the unmanaged client, such as using a hardware-based one-time password token or Public Key Infrastructure (PKI) token with a password or PIN.
+ Only authorized users should be allowed to access the virtual desktop environment, and access should be restricted to allowable locations.

VDI systems may include features that cache data on the client device or allow the virtual desktop to connect to the local machine's file system, printers, or other resources, depending on the implementation. To support NIST SP 800-171 compliance and out-of-scope endpoint determinations, any such features should be disabled on the server side to help prevent unmanaged endpoints from mounting drives, printing files, or performing other actions that invoke system protocols beyond the basic VDI protocol. Verify the specific configuration options available in your VDI platform.

For Amazon WorkSpaces, this means configuring the WorkSpaces directory settings to disable clipboard redirection, drive redirection, and printing redirection, and enforcing MFA through the WorkSpaces client authentication settings.

## AWS shared responsibility and inheritance
<a name="aws-shared-responsibility-and-inheritance"></a>

### How does the AWS Shared Responsibility Model apply to CMMC Level 2?
<a name="how-does-the-9999999999999999aws--shared-responsibility-model-apply-to-cmmc-level-2-.4995af68-ff06-5ce5-a414-445f4ebd2db8"></a>

Under the AWS Shared Responsibility Model, AWS is responsible for security "of" the cloud (physical infrastructure, hypervisor, managed services), and the customer is responsible for security "in" the cloud (data, identity management, application configuration, network controls, encryption). For CMMC Level 2, the AWS CRM maps all 110 requirements as follows:
+ 21 Fully Inheritable controls: AWS satisfies these entirely. The customer must still document the inheritance in their SSP via the CRM.
+ 79 Partially Inheritable controls: Shared responsibility. AWS provides infrastructure-level controls; the customer must configure, operate, and provide evidence for their portion.
+ 10 Customer-Only controls: No AWS service coverage. These require organizational policies or non-AWS technology.

### Which controls are fully inheritable from AWS?
<a name="which-controls-are-fully-inheritable-from-9999999999999999aws--.7a1e2f8c-bfe1-516d-83cb-62abd8686beb"></a>

The 21 fully inheritable controls are primarily in the Physical Protection, Media Protection, and Maintenance families:
+ Physical Protection (PE): All 6 practices (3.10.1 through 3.10.6), covering AWS data center physical security
+ Media Protection (MP): 8 of 9 practices (3.8.1 through 3.8.8), covering AWS media handling and sanitization
+ Maintenance (MA): 3.7.1, 3.7.2, 3.7.3, 3.7.4, 3.7.6, covering AWS infrastructure maintenance
+ Access Control (AC): 3.1.16, 3.1.17, covering wireless access and authentication for AWS-managed infrastructure

For each fully inheritable control, the customer must document the inheritance relationship in their SSP and reference the CRM. The C3PAO accepts the FedRAMP authorization as evidence for these controls.

### What are the 10 customer-only controls that AWS cannot address?
<a name="what-are-the-10-customer-only-controls-that-9999999999999999aws--cannot-address-.9d3a6583-d84e-50f2-bcd0-58298d6ea5b3"></a>

These controls require organizational policies, endpoint management, or non-AWS technology:

|
|
| Practice ID | Requirement | Customer action |
| --- |--- |--- |
| AC.L2-3.1.8 | Unsuccessful logon attempts | Implement lockout policy and mechanism |
| AC.L2-3.1.18 | Mobile device connection | Establish organizational policy |
| AC.L2-3.1.19 | Encrypt CUI on mobile devices | Enforce encryption on mobile endpoints |
| AC.L2-3.1.21 | Portable storage use | Establish organizational policy |
| IA.L2-3.5.7 | Password complexity | Configure in IAM password policy and organizational policy |
| IA.L2-3.5.8 | Password reuse prohibition | Configure in IAM password policy and organizational policy |
| IA.L2-3.5.9 | Temporary password use | Establish organizational policy |
| SC.L2-3.13.7 | Split tunneling prevention | Configure network and VPN settings |
| SC.L2-3.13.12 | Collaborative device control | Establish organizational policy for conferencing equipment |
| SC.L2-3.13.14 | Voice/video protection | Implement encryption for communications |

### Which AWS services are most relevant to CMMC Level 2?
<a name="which-9999999999999999aws--services-are-most-relevant-to-cmmc-level-2-.6ccfbc66-4200-5ed7-980a-019fac5c3655"></a>

|
|
| AWS service | Controls supported | Primary use |
| --- |--- |--- |
| AWS Identity and Access Management (IAM) | \~30 controls | Identity, access, least privilege, MFA, sessions |
| CloudTrail | \~19 controls | Audit logging, accountability, change tracking |
| AWS Config | \~19 controls | Baselines, compliance rules, drift detection |
| AWS Security Hub | \~13 controls | Compliance findings, standards, evidence aggregation |
| Systems Manager | \~11 controls | Patching, configuration, remote access |
| CloudWatch | \~10 controls | Monitoring, alerting, log management |
| Amazon VPC | \~10 controls | Network segmentation, boundary protection, flow control |
| GuardDuty | \~6 controls | Threat detection, anomaly monitoring |
| AWS KMS | \~5 controls | Encryption key management |
| EventBridge | \~5 controls | Event-driven automation |

See the AWS CRM for the complete service-to-control mapping.

## Preparing for assessment on AWS
<a name="preparing-for-assessment-on-aws"></a>

### What should I do first to prepare for CMMC Level 2 on AWS?
<a name="what-should-i-do-first-to-prepare-for-cmmc-level-2-on-9999999999999999aws--.1fe1a9fa-8c81-502c-b804-9c8661871bb2"></a>

1. Determine your scope. Identify which systems process, store, or transmit CUI. Classify all assets into the five scoping categories defined in 32 CFR 170.19(c)(1) and the CMMC Scoping Guide Level 2 v2.13 (CUI Assets, Security Protection Assets, CRMAs, Specialized Assets, Out-of-Scope Assets).

1. Obtain the AWS CRM. Download the AWS NIST SP 800-171 / CMMC 2.0 Level 2 CRM from the AWS CMMC Compliance page. Understand which controls are fully inheritable, shared, or customer-only.

1. Develop your SSP. Document your system boundary, data flows, asset inventory, and control implementation narratives addressing all 320 assessment objectives across the 110 requirements.

1. Conduct a gap assessment. Evaluate your current implementation against each requirement and calculate your projected SPRS score. Prioritize POA&M-ineligible requirements and 5-point Basic requirements first.

1. Build your evidence package. Collect artifacts (policies, configurations, screenshots, logs) mapped to examine, interview, and test methods per NIST SP 800-171A. Evidence must be in final form.

1. Engage a C3PAO. If your contract requires C3PAO certification, engage early. The Pre-Assessment phase (SSP review, scope validation) must be completed before the formal assessment begins.

### What SPRS score do I need?
<a name="what-sprs-score-do-i-need-.29d578ec-abc0-5168-a234-e72e404584b1"></a>

The SPRS scoring model for Level 2:
+ Maximum score: 110 (one point per requirement when MET)
+ Basic requirements (30 total) deduct 5 points each if NOT MET
+ Derived requirements (80 total) deduct 1 point each if NOT MET
+ Conditional CMMC Status threshold: 88 or above (with all NOT MET items on eligible POA&Ms)
+ Final CMMC Status: All 110 requirements MET, all POA&Ms closed
+ Certificate validity: Three years from the Final CMMC Status Date, with annual affirmation

### Can AWS help me achieve CMMC compliance?
<a name="can-9999999999999999aws--help-me-achieve-cmmc-compliance-.c3f83a10-2729-586e-bc5e-41fb2a02890f"></a>

AWS provides services, resources, and programs designed to support your CMMC compliance journey:
+ AWS Compliance Programs: Documentation of AWS compliance certifications and attestations, including FedRAMP.
+ AWS Artifact: On-demand access to AWS compliance reports and select online agreements.
+ Security Hub: Aggregates security findings and checks compliance against standards including NIST SP 800-171.
+ AWS Security Assurance Services: Advisory and implementation support for compliance programs.
+ AWS CRM: Maps all 110 CMMC Level 2 requirements to AWS services with detailed implementation guidance.

AWS helps support your compliance requirements, but achieving CMMC certification is the customer's responsibility under the Shared Responsibility Model.
