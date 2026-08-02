---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-modern-healthcare-data/appendix-d.html
---

# Appendix D. Additional guidance on implementing a modern health-data strategy
<a name="appendix-d"></a>

Organizations can implement modern healthcare-data strategies in various ways. The specific implementation details for an organization depend on its existing data infrastructure, the availability of engineers to build and deploy technical components, and the time allotted for implementation.

Healthcare organizations can build or buy data system components, depending on their existing infrastructure, capabilities, and relationships with technology providers. Organizations that need a ready-built data solution can choose software as a service (SaaS) solutions, which reduce implementation time and effort. Organizations that choose a SaaS solution must make sure that it meets their needs for data ingestion, processing, and analytics. They must also confirm that it can interoperate with other cloud services to fulfill these needs.

Alternatively, organizations can build a data solution using cloud data and analytics services. This approach is the most flexible. However, it requires expertise and resources. A purpose-built solution gives organizations full control over data storage and processing. This approach also reduces the chances of an organization outgrowing their data strategy. Building a healthcare-data solution requires an organization to invest in experts to develop and maintain cloud infrastructure. Over time, these experts become a key organizational asset. In addition, cloud consultants, such as [AWS Professional Services](https://aws.amazon.com/professional-services/) and members of the [AWS Partner Network](https://aws.amazon.com/partners/work-with-partners/), can accelerate capabilities and increase value when developing components of a data solution. Organizations that build a modern healthcare-data strategy should also consider the ongoing maintenance of their cloud data solution, which often means hiring cloud operations engineers.

Organizations can also consider adopting a platform as a service (PaaS) solution for cloud data. These solutions simplify common data processing workflows so that organizations can devote more time and resources to deriving insights from their data. PaaS solutions help reduce the time and effort required to implement and maintain a cloud data solution while enabling organizations to retain a high degree of flexibility and control. PaaS solutions require cloud engineers trained specifically in maintenance and use of the data solution, which increases the complexity of hiring and training cloud engineers.

Finally, organizations should also consider their security and compliance requirements when building a modern healthcare-data strategy. When using PaaS and SaaS solutions, organizations must work with solution providers to clarify these requirements and responsibilities. Building a data solution requires engineers who are well versed in security and compliance best practices for the cloud. AWS provides resources such as the [HIPAA Eligible Services Reference](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/). These resources help guide and train cloud architects and engineers in achieving security and compliance goals.

A data solution that supports a modern healthcare-data strategy should make it possible for organizations to derive value from all of their data assets. It should do so while providing a secure, scalable, high-performance, sustainable, and easy-to-use environment for accessing, analyzing, and deriving insights from data. Key features include the following:
+ Security and compliance requirements addressed through logging, fine-grained access controls, and centralized monitoring and alerting.
+ Support for entity resolution, anonymization of PHI and personally identifiable information (PII), patient-centric data models, and patient consent management.
+ Specialized data stores that are designed for specific needs. These needs can include documents, logs, images, key-value pairs, and semistructured and unstructured data.
+ Federated data management, with centralized data discovery, auditing, and governance using frameworks for data federation.
+ Support for diverse data use cases through common data models, such as [Observational Medical Outcomes Partnership (OMOP) Common Data Model](https://ohdsi.github.io/CommonDataModel/) and the [Informatics for Integrating Biology and the Bedside (i2b2)](https://www.i2b2.org/) framework.
+ Interoperability and data sharing by using standards such as the following:
  + [Health Level Seven International (HL7)](https://www.hl7.org/fhir/overview.html) V2
  + HL7 [Fast Healthcare Interoperability Resources (FHIR)](https://www.hl7.org/fhir/overview.html)
  + HL7 [Consolidated Clinical Document Architecture (C-CDA)](https://build.fhir.org/ig/HL7/CDA-ccda-2.2/)
  + EDI 835 remittance advice
  + EDI 837 claim documents

AWS offers a robust suite of services and capabilities to address each aspect of a modern healthcare-data architecture. Deploying workloads on AWS brings the following benefits:
+ **Agility** – Teams can experiment and innovate quickly and frequently, without impacting production systems.
+ **Elasticity** – Resources can be scaled up and down as the needs of the business change.
+ **Cost savings** – Only resources that are being used incur expenses.
+ **Innovation** – Organizations can focus on business differentiators, not infrastructure.
+ **Security and compliance** – AWS core infrastructure is built to satisfy the security requirements for high-sensitivity organizations. This is backed by a deep set of cloud security tools, with more than 300 security, compliance, and governance services and features. AWS supports 143 security standards and compliance certifications, including:
  + Payment Card Industry Data Security Standard (PCI-DSS)
  + HIPAA and the Health Information Technology for Economic and Clinical Health (HITECH) Act
  + Federal Risk and Authorization Management Program (FedRAMP)
  + General Data Protection Regulation (GDPR)
  + Federal Information Processing Standards (FIPS) 140-2
  + National Institute of Standards and Technology (NIST) 800-171
