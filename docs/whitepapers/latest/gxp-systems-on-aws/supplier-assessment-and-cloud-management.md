---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/supplier-assessment-and-cloud-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Supplier Assessment and Cloud Management
<a name="supplier-assessment-and-cloud-management"></a>

 As mentioned earlier, gaining trust in a Cloud Service Provider is critical as you will be inheriting certain cloud infrastructure and security controls from the Cloud Service Provider. The approach described by industry guidance involves several steps which we will cover here.

## Basic Supplier Assessment
<a name="basic-supplier-assessment"></a>

 The first (optional) step is to perform a basic supplier assessment to check the supplier’s market reputation, knowledge and experience working in regulated industries, prior experience working with other regulated companies and what certifications they hold.

 You can leverage industry assessments such as Gartner’s assessment on the AWS News Blog post, [AWS Named as a Cloud Leader for the 10th Consecutive Year in Gartner’s Infrastructure & Platform Services Magic Quadrant](https://aws.amazon.com/blogs/aws/aws-named-as-a-cloud-leader-for-the-10th-consecutive-year-in-gartners-infrastructure-platform-services-magic-quadrant/), and [customer testimonials](https://aws.amazon.com/compliance/testimonials/).

## Documentation Review
<a name="documentation-review"></a>

 A supplier assessment often includes a deep dive into the assets available from the supplier describing their QMS and operations. This includes reviewing certifications, audit reports and whitepapers. For more information, see the [AWS Risk and Compliance whitepaper](https://d1.awsstatic.com/whitepapers/compliance/AWS_Risk_and_Compliance_Whitepaper.pdf).

 AWS and its customers share control over the IT environment, and both parties have responsibility for managing the IT environment. The AWS part in this shared responsibility includes providing services on a highly secure and controlled platform and providing a wide array of security features customers can use. The customer’s responsibility includes configuring their IT environments in a secure and controlled manner for their purposes. While customers don’t communicate their use and configurations to AWS, AWS does communicate its security and control environment relevant to customers. AWS does this by doing the following:
+  Obtaining industry certifications and independent third-party attestations
+  Publishing information about the AWS security and control practices in whitepapers and web site content
+  Providing certificates, reports, and other documentation directly to AWS customers under NDA (as required)

 For a more detailed description of AWS Security, see [AWS Cloud Security](https://aws.amazon.com/security/).

 [AWS Artifact](https://aws.amazon.com/artifact/) provides on-demand access to AWS security and compliance reports and select online agreements. Reports available in AWS Artifact include our Service Organization Control (SOC) reports, Payment Card Industry (PCI) reports, and certifications from accreditation bodies across geographies and compliance verticals that validate the implementation and operating effectiveness of AWS security controls. Agreements available in AWS Artifact include the Business Associate Addendum (BAA) and the Nondisclosure Agreement (NDA). For a more detailed description of AWS Compliance, see [AWS Compliance](https://aws.amazon.com/compliance/).

 If you have additional questions about the AWS certifications or the compliance documentation AWS makes available, please bring those questions to your account team.

## Review Service Level Agreements (SLA)
<a name="review-service-level-agreements-sla"></a>

 AWS offers service level agreements for certain AWS services. Further information can be found under [Service Level Agreements (SLAs)](https://aws.amazon.com/legal/service-level-agreements/).

## Audit
<a name="audit"></a>

 **Mail Audit –** To supplement the AWS documentation you have gathered, a mail audit questionnaire (sometimes referred to as a supplier questionnaire) may be submitted to AWS to gather additional information or to ask clarifying questions. You should work with your account team to request a mail audit.

 **Onsite Audit –** AWS regularly undergoes independent third-party attestation audits to provide assurance that control activities are operating as intended.  Currently, AWS participates in over 50 different audit programs.  The results of these audits are documented by the assessing body and made available for all AWS customers through [AWS Artifact](https://aws.amazon.com/artifact/). These third-party attestations and certifications of AWS provide you with visibility and independent validation of the control environment, eliminating the need for customers to perform individual onsite audits. Such attestations and certifications may also help relieve you of the requirement to perform certain validation work yourself for your IT environment in the AWS Cloud. For details, see the [AWS Quality Management System](aws-quality-management-system.md) section of this whitepaper

## Contractual Agreement
<a name="contractual-agreement"></a>

 Once you have completed a supplier assessment of AWS, the next step is to set up a contractual agreement for using AWS services. The AWS Customer Agreement is available at: [https://aws.amazon.com/agreement/](https://aws.amazon.com/agreement/)). You are responsible for interpreting regulations and determining whether the appropriate requirements are included in a contract with standard terms. If you have any questions about entering into a service agreement with AWS, please contact your account team.

## Cloud Management Processes
<a name="cloud-management-processes"></a>

 There are certain processes that span the shared responsibility model and typically must be captured in your QMS in the form of SOPs and work instructions.

### Change Management
<a name="change-management"></a>

 Change Management is a bidirectional process when dealing with a cloud service provider. On the one hand, AWS is continually making changes to improve its services as mentioned earlier in this paper. On the other hand, you can make feature requests, which is highly encouraged as [90% of the AWS service features are as a result of direct customer feedback](https://cio.economictimes.indiatimes.com/news/cloud-computing/90-of-our-roadmap-and-features-are-direct-result-of-customer-feedback-stephen-orban-global-head-of-enterprise-strategy-aws/58508358).

 Customers typically use a risk-based approach appropriate for the type of change to determine the subsequent actions.

 Changes to AWS services which add functionality are not usually a concern because no application will be using that new functionality yet. However, new functionality may trigger an internal assessment to determine if it affects the risk profile of the service and should be allowed for use. If mandated by your QMS, this may trigger a re-qualification of building blocks prior to allowing the new functionality.

 Deprecations are considered more critical because they could break an application. A deprecation may include a third-party library, utility, or version of languages such as Python. The deprecation of a service or feature is rare. Once you receive the notification of a deprecation, you should trigger an impact assessment. If an impact is found, the application teams should plan changes to remediate the impact. The notice period for a deprecation should allow for time for assessment and remediation. AWS will also help you understand the impact of the change.

 There are other changes such as enhancements and bug fixes which do not change the functionality of the service and do not trigger notifications to customers. These types of changes are synonymous with “standard” changes in ITIL which are usually pre-authorized, low risk, relatively common and follow a specific procedure. If you want to generate evidence showing no regression is introduced due to this class of change, you could create a test bed which repeatedly tests the AWS services to detect regression.

 Should a problem be uncovered, it should immediately be reported to AWS for resolution.

### Incident Management
<a name="incident-management"></a>

 The Amazon Security Operations team employs industry-standard diagnostic procedures to drive resolution during business-impacting events. Staff operators provide 24x7x365 coverage to detect incidents and to manage the impact and resolution. As part of the process, potential breaches of customer content are investigated and escalated to AWS Security and AWS Legal. Affected customers and regulators are notified of breaches and incidents where legally required. You can subscribe to the AWS Security Bulletins page ([https://aws.amazon.com/security/security-bulletins](https://aws.amazon.com/security/security-bulletins)), which provides information regarding identified security issues. You can subscribe to the Security Bulletin RSS Feed to keep abreast of security announcements on the Security Bulletin webpage.

 You are responsible for reporting incidents involving your storage, virtual machines, and applications, unless the incident is caused by AWS.

 For more information refer to the AWS Vulnerability Reporting webpage: [https://aws.amazon.com/security/vulnerability-reporting/](https://aws.amazon.com/security/vulnerability-reporting/).

### Customer Support
<a name="customer-support"></a>

 AWS develops and maintains customer support procedures that include metrics to verify performance. When you contact AWS to report that AWS services do not meet their quality objectives, your issue is investigated and, where required, commercially reasonable actions are taken to resolve it. Where AWS is the first to become aware of a customer impacting issue, procedures exist for notifying impacted customers according to their contract requirements and/or via the AWS Service Health Dashboard [http://status.aws.amazon.com/](http://status.aws.amazon.com/).

 You should ensure that your policies and procedures align to the customer support options provided by AWS. Additional details may be found in the [Customer Complaints](quality-infrastructure-and-support-processes.md#customer-complaints) and [Customer Training](software-development.md#customer-training) sections in this document.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
