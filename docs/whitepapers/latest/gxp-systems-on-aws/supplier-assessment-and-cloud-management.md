---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/supplier-assessment-and-cloud-management.html
---

# Supplier assessment
<a name="supplier-assessment-and-cloud-management"></a>

Industry guidance suggests you use a supplier's experience, knowledge, and documentation as much as possible. With so much responsibility now delegated to a supplier, the supplier assessment becomes even more important. A regulated company is still ultimately accountable for demonstrating that a GxP system is compliant, even if a supplier is responsible for parts of that system, so the regulated customer needs to establish enough trust in their supplier.

The cloud service provider must be assessed to determine if they can deliver the services offered, but also to determine the suitability of their quality system and that it is systematically followed. The supplier needs to show that they have a QMS and follow a documented set of procedures and standards governing activities such as:
+ Infrastructure verification and operation
+ Software development
+ Change management
+ Release management
+ Configuration management
+ Supplier management
+ Training
+ System security

Details of the AWS QMS are covered in the [AWS Quality Management System](aws-quality-management-system.md) section of this whitepaper. The capabilities of AWS to satisfy these areas might be reassessed on a periodic basis, typically by reviewing the latest materials available through AWS Artifact (for example, AWS certifications and audit reports).

The approach described by industry guidance involves several steps which we will cover here.

## Basic supplier assessment
<a name="basic-supplier-assessment"></a>

The first step is to perform a basic supplier assessment to check the supplier's market reputation, knowledge, and experience working in regulated industries and prior experience working with other regulated companies and what certifications they hold.

You can use industry assessments such as [Gartner's analyst report](https://pages.awscloud.com/gartner-magic-quadrant-for-cloud-ai-developer-services-ardm-2024.html) which recognizes AWS as a Leader and has been placed highest on Ability to Execute, [customer testimonials](https://aws.amazon.com/solutions/case-studies/) and [customer case studies](https://aws.amazon.com/solutions/case-studies/?awsf.customer-references-industry=industry%23life-sciences).

The earlier sections of this whitepaper provide useful information for this initial assessment.

## Documentation review
<a name="documentation-review"></a>

A supplier assessment often includes a deep dive into the assets available from the supplier describing their QMS and operations. This includes reviewing certifications, audit reports and whitepapers. For more information, see the [AWS Risk and Compliance whitepaper](https://d1.awsstatic.com/whitepapers/compliance/AWS_Risk_and_Compliance_Whitepaper.pdf).

AWS and its customers share control over the IT environment, and both parties have responsibility for managing the IT environment. The AWS part in this shared responsibility includes providing services on a highly secure and controlled platform and providing a wide array of security features customers can use. The customers' responsibility includes configuring their IT environments in a secure and controlled manner for their purposes. While customers don't communicate their use and configurations to AWS, AWS does communicate its security and control environment relevant to customers. AWS does this by doing the following:
+ Obtaining industry certifications and independent third-party attestations
+ Publishing information about the AWS security and control practices in whitepapers and website content
+ Providing certificates, reports, and other documentation directly to AWS customers under NDA (as required)

For a more detailed description of AWS Security, see [AWS Cloud Security](https://aws.amazon.com/security/).

[AWS Artifact](https://aws.amazon.com/artifact/) provides on-demand access to AWS security and compliance reports and select online agreements. Reports available in AWS Artifact include our Service Organization Control (SOC) reports, Payment Card Industry (PCI) reports, and certifications from accreditation bodies across geographies and compliance verticals that validate the implementation and operating effectiveness of AWS security controls. Agreements available in AWS Artifact include the Business Associate Addendum (BAA) and the Nondisclosure Agreement (NDA). For a more detailed description of AWS Compliance, see [AWS Compliance](https://aws.amazon.com/compliance/).

If you have additional questions about the AWS certifications or the compliance documentation AWS makes available, bring those questions to your account team.

## Review service level agreements (SLA)
<a name="review-service-level-agreements-sla"></a>

AWS offers service level agreements for certain AWS services. Further information can be found under [Service Level Agreements (SLAs)](https://aws.amazon.com/legal/service-level-agreements/).

## Audit
<a name="audit"></a>

**Mail audit** – To supplement the AWS documentation you have gathered, a mail audit questionnaire (sometimes referred to as a supplier questionnaire) can be submitted to AWS to gather additional information or to ask clarifying questions. A questionnaire tailored to cloud service providers rather than a generic questionnaire will expedite the processes. You should work with your account team to request a mail audit.

**Onsite audit** – AWS regularly undergoes independent third-party attestation audits to provide assurance that control activities are operating as intended. Currently, AWS participates in over 50 different audit programs. The results of these audits are documented by the assessing body and made available for all AWS customers through [AWS Artifact](https://aws.amazon.com/artifact/). These third-party attestations and certifications of AWS provide you with visibility and independent validation of the control environment, eliminating the need for customers to perform individual onsite audits. Such attestations and certifications might also help relieve you of the requirement to perform certain validation work yourself for your IT environment in the AWS Cloud. For details, see the [AWS Quality Management System](aws-quality-management-system.md) section of this whitepaper.

AWS has also been assessed by the Ingelheim Kreis Initiative Joint Audits group which represents quality and compliance professionals from some of our largest pharmaceutical and life sciences customers. Details can be found in [this blog post](https://aws.amazon.com/blogs/security/aws-completes-the-first-cloud-audit-by-the-ingelheim-kreis-initiative-joint-audits-group-for-the-pharmaceutical-and-life-sciences-sector/).

## Contractual agreement
<a name="contractual-agreement"></a>

After you have completed a supplier assessment of AWS, the next step is to set up a contractual agreement for using AWS services. The AWS Customer Agreement is available at: [https://aws.amazon.com/agreement/](https://aws.amazon.com/agreement/). You are responsible for interpreting regulations and determining whether the appropriate requirements are included in a contract with standard terms. If you have any questions about entering into a service agreement with AWS, contact your account team.

## Cloud management
<a name="cloud-management"></a>

It is important to consider and plan how operational processes that span the shared responsibility model will operate. For example, how to manage changes made by AWS to services used as part of your landing zone or applications, incident response management in cases of outages, or portability requirements should there be a need to change cloud service provider.

### Customer quality management system
<a name="customer-quality-management-system"></a>

It is important for you to analyze your existing quality management system (QMS) and the impact adopting cloud technology might have on it. It was probably written based on the use of on-premises infrastructure and some policies and procedures will need updating or exceptions raised. For example, a policy on IT asset management might imposes processes that no longer fit with cloud best practices, such as the need to record every IT asset in a CMDB. In the cloud this is done automatically with AWS Config. Using a CMDB also doesn't fit with scenarios such as auto-scaling groups where the number of servers (or assets) can grow and shrink on demand based on load. Another example might be procedures governing infrastructure installation qualification, which are often document-centric and don't take advantage of infrastructure as code (IaC).

There are also certain processes that now span the shared responsibility model and so will need updating.

### Change management
<a name="change-management"></a>

Change management is a bidirectional process when dealing with a cloud service provider. On the one hand, AWS is continually making changes to improve its services as mentioned earlier in this paper. On the other hand, you can make feature requests, which is highly encouraged because [90% of AWS service features are a direct result of customer feedback](https://cio.economictimes.indiatimes.com/news/cloud-computing/90-of-our-roadmap-and-features-are-direct-result-of-customer-feedback-stephen-orban-global-head-of-enterprise-strategy-aws/58508358).

Customers typically use a risk-based approach appropriate for the type of change to determine the subsequent actions.

Changes to AWS services that add functionality are not usually a concern because no application will be using that new functionality yet. However, new functionality might trigger an internal assessment to determine if it affects the risk profile of the service and should be allowed for use. If mandated by your QMS, this might trigger a re-qualification of building blocks prior to allowing the new functionality.

Deprecations are considered more critical because they could break an application. A deprecation might include a third-party library, utility, or version of languages such as Python. The deprecation of a service or feature is rare. When you receive the notification of a deprecation, you should trigger an impact assessment. If an impact is found, the application teams should plan changes to remediate the impact. The notice period for a deprecation should allow for time for assessment and remediation. AWS will also help you understand the impact of the change.

There are other changes such as enhancements and bug fixes that don't change the functionality of the service and don't trigger notifications to customers. These types of changes are synonymous with standard changes in ITIL which are usually pre-authorized, low risk, relatively common and follow a specific procedure.

### Incident management
<a name="incident-management"></a>

The Amazon Security Operations team employs industry-standard diagnostic procedures to drive resolution during business-impacting events. Staff operators provide continuous coverage to detect incidents and to manage the impact and resolution. As part of the process, potential breaches of customer content are investigated and escalated to AWS Security and AWS Legal. Affected customers and regulators are notified of breaches and incidents where legally required. You can subscribe to the AWS Security Bulletins web page ([https://aws.amazon.com/security/security-bulletins](https://aws.amazon.com/security/security-bulletins)), which provides information regarding identified security issues. You can subscribe to the Security Bulletin RSS Feed to keep abreast of security announcements on the Security Bulletins webpage.

You are responsible for reporting incidents involving your storage, virtual machines, and applications, unless the incident is caused by AWS.

For more information see [AWS Vulnerability Reporting](https://aws.amazon.com/security/vulnerability-reporting/).

### Customer support
<a name="customer-support"></a>

AWS develops and maintains customer support procedures that include metrics to verify performance. When you contact AWS to report that AWS services do not meet your quality objectives, your issue is investigated and, where required, commercially reasonable actions are taken to resolve it. Where AWS is the first to become aware of a customer impacting issue, procedures exist for notifying impacted customers according to their contract requirements or through the [AWS Service Health Dashboard](https://health.aws.amazon.com/health/status)).

You should ensure that your policies and procedures align to the customer support options provided by AWS. Additional details can be found in the [Customer complaints](quality-infrastructure-and-support-processes.md#customer-complaints) and [Customer training](software-development.md#customer-training) sections in this document.
