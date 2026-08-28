---
source_url: https://docs.aws.amazon.com/whitepapers/latest/logical-separation/case-study.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Case Study
<a name="case-study"></a>

 **US Defense Department accepts logical storage separation approach for sensitive unclassified workloads**

 In December 2011, the U.S. Federal Chief Information Officer established a government-wide policy mandating federal agencies use the Federal Risk and Authorization Management Program (FedRAMP) — a standardized, federal-wide program for the security authorization of cloud services. FedRAMP maintains three standardized security baselines — Low, Moderate, and High impact — based on Federal Information Processing Standards Publication (FIPS) 199 categorizations. These baselines were developed through the collaboration of cybersecurity experts across private industry and the U.S. Government (including the Department of Defense (DoD)). While the DoD established reciprocity with the FedRAMP Moderate baseline, it has not established reciprocity with the FedRAMP High baseline. Instead, the DoD developed and implemented what is effectively a “FedRAMP plus” set of security controls and requirements via the DoD Cloud Computing Security Requirements Guide (SRG).

 In particular, DoD through the SRG requires separation between DoD and Federal government tenants/missions either via physical or logical means. More specifically, the SRG states that “CSPs must provide evidence of strong virtual separation controls and monitoring, and the ability to meet ‘search and seizure’ requests without the release of DoD information and data.” Even further, for Impact Level 5 systems (IL5), DoD requires “physical separation (e.g., dedicated infrastructure) from non-DoD/non-Federal Government tenants.” These DoD requirements are intended to address DoD concerns regarding the co-mingling of DoD data with other tenant data from unintended data disclosure and the unauthorized access or tampering of DoD data by a non-DoD tenant.

 To implement an outcome-focused best practice, the SRG acknowledged the use of logical separation as a viable approach to meet DoD IL5 separation requirements:

 *“A CSP may offer alternate solutions that provide equivalent security to the stated requirements. Approval will be assessed on a case by case basis during the PA [provisional authorization] assessment process.”*

****
 Through DoD’s cloud computing SRG assessment and authorization (i.e., accreditation) process, AWS demonstrated the sufficiency of logical separation *combined with dedicated tenancy* to meet the intent behind a requirement for dedicated, physically isolated infrastructure for DoD’s most sensitive unclassified workloads. (Refer to the previous section on "Host and Instance Features".) Our accepted approach confirms that multi-tenant logically separated environments that meet robust security controls can provide a level of security superior to dedicated private cloud deployments, while providing significant advantages in availability, scalability, and lower cost. Modern cloud technology from established providers can offer novel solutions that can meet the objective of traditional technology security as long as accreditation approaches are flexible enough to accommodate alternative implementations.

## 5.2.2.2 Impact Level 5 Location and Separation Requirements
<a name="impact-level-5"></a>

 Information that must be processed and stored at Impact Level 5 can only be processed in a dedicated infrastructure, on-premises or off-premises in any cloud deployment model that restricts the physical location of the information as described in section 5.2.1, “Jurisdiction/ Location Requirements.” This excludes public service offerings.

 The following applies:
+  Only DoD private, DoD community or Federal Government community clouds are eligible for Impact Level 5.
+  Each deployment model may support multiple missions or tenants / missions from each customer organization.
+  Virtual/logical separation between DoD and Federal Government tenants / missions is permitted.
+  Virtual/logical separation between tenant/mission systems is minimally required.
+  Physical separation (e.g. Dedicated Infrastructure) from non-DoD/non-Federal Government tenants is required.

 [Department of Defense Cloud Computing Security Requirements Guide V1R3](https://public.cyber.mil/dccs/dccs-documents/)

**Note**
A CSP may offer alternate solutions that provide equivalent security to the stated requirements. Approval will be assessed on a case by case basis during the PA assessment process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
