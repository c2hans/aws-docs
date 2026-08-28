---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-financial-services-guidance-australia/appendix-1-key-aspects-of-apra-cps234.html
---

# Appendix 1: Key aspects of APRA CPS234
<a name="appendix-1-key-aspects-of-apra-cps234"></a>

## Roles and responsibilities
<a name="roles-and-responsibilities"></a>

 Paragraphs 13 and 14 of CPS 234 state that the Board of an ARI must ensure that the entity maintains information security in a manner commensurate with the size and extent of threats to its information assets, and that enables the continued sound operation of the ARI. Additionally, ARIs must clearly define the information security-related roles and responsibilities of the Board, senior management, governing bodies, and individuals with responsibility for decision-making, approval, oversight, operations, and other information security functions.

 While AWS considers the ARI's definition of information security-related roles and responsibilities as an action for the ARI to independently complete, there are a number of AWS resources and services available to help customers meet these requirements.

 A common theme among the most successful customers of AWS is that they have an engaged board and senior management team who are enthusiastic about the benefits of moving to the cloud and are aware of the changed risks and responsibilities of operating in the cloud. The AWS [C-suite Guide to Shared Responsibility for Cloud Security](https://pages.awscloud.com/csuite-shared-responsibility-ebook.html) and [Data-Safe Cloud eBook](https://pages.awscloud.com/data-safe-cloud-ebook-download.html) on the [AWS Data Safe Cloud Checklist](https://aws.amazon.com/campaigns/cloud-security/data-safe-cloud-checklist/) site inform boards and senior management about the benefits and risks of operating in the cloud.

 At an operational level, customers can use [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam) to manage access to AWS services and resources securely. Using IAM, customers can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources. IAM can be used to grant employees and applications [federated access](https://aws.amazon.com/identity/federation/) to the AWS Management Console and AWS service APIs, using existing identity systems such as Microsoft Active Directory or an [identity management](https://docs.aws.amazon.com/IAM/latest/UserGuide/IdP-solution-providers.html) solution that supports [Security Assertion Markup Language (SAML) 2.0](https://aws.amazon.com/identity/saml/).

 IAM helps customers [analyze access](https://aws.amazon.com/iam/features/analyze-access/) across their AWS environments. Security teams and administrators can quickly validate that policies only provide the intended public and cross-account access to resources, and customers can also identify and refine policies to allow access to only the services being used.

 This helps customers to better adhere to the principle of least privilege—granting only the permissions required to perform a task.

 Using [AWS multi-factor authentication](https://aws.amazon.com/iam/features/mfa/) (MFA) is an IAM best practice that requires a second authentication factor in addition to user name and password sign-in credentials.. MFA requires users to prove physical possession of a hardware MFA token or MFA-enabled mobile device by providing a valid MFA code.

## Information security capability
<a name="information-security-capability"></a>

 Paragraphs 15 to 17 of CPS 234 require ARIs to have an information security capability commensurate with the size and extent of threats to their information assets and to assess the information security capability of any related or third party who manages information assets of the ARI. An ARI is also required to actively maintain its information security capability with respect to changes in vulnerabilities and threats. CPS 234 defines an *information security capability* as the totality of resources, skills and controls that provide the ability and capacity to maintain information security.

 AWS has developed and implemented a security control environment designed to protect the confidentiality, integrity, and availability of customers' systems and content. AWS maintains a broad range of industry and geography specific compliance programs and is continually assessed by external certifying bodies and independent auditors to provide assurance the policies, processes, and controls established and operated by AWS are in alignment with these program standards and the highest industry standards.

 AWS considers the development and maintenance of an ARI's information security capability as an action for the ARI to independently complete. The following resources help customers meet these requirements.

 A range of [security, identify, and compliance whitepapers](https://aws.amazon.com/security/security-learning/?nc=sn&loc=5&whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc) are available for download from AWS. AWS [training and certification programs](https://aws.amazon.com/training/?nav=tc&loc=1) offer a range of complimentary digital courses, classroom-based training, and AWS certifications to develop and maintain an information security capability to help meet APRA requirements.

 [AWS Managed Services (AMS)](https://aws.amazon.com/managed-services/) and [AWS Security Competency Partners](https://aws.amazon.com/security/partner-solutions/) can be used by customers to augment internal capabilities or to fill gaps where recruiting in-house resources is cost-prohibitive or while in-house capability is being developed. [AMS](https://aws.amazon.com/managed-services/) can automate common activities, such as change requests, monitoring, patch management, security, and backup services, and provides full lifecycle services to provision, run, and support customer infrastructure. AWS Security Competency Partners support customers in multiple areas including infrastructure security, policy management, identity management, security monitoring, vulnerability management, data protection, and consulting services.

## Policy framework
<a name="policy-framework"></a>

 Paragraphs 18 and 19 of CPS 234 require ARIs to maintain an information security policy framework commensurate with their exposures to vulnerabilities and threats. This policy must provide direction on the responsibilities to all parties who have an obligation to maintain information security.

 AWS implements formal, documented policies and procedures that provide guidance for operations and information security within an AWS organization and the supporting AWS environments. Policies address purpose, scope, roles, responsibilities, and management commitment.

 AWS considers the development and maintenance of an ARI's information security policy framework as an action for the ARI to independently complete. The following AWS services can assist with policy implementation and compliance monitoring to help customers meet their above-the-line compliance requirements with this area of CPS 234.

 In conjunction with IAM policies, AWS customers can use [AWS Organizations](https://aws.amazon.com/organizations/) to implement service control policy (SCP) permission guardrails to help make sure that users can only perform actions that meet corporate security and compliance policy requirements. Additionally, customers can configure central logging of actions performed across their organization using [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) and centrally aggregate data for [AWS Config](https://aws.amazon.com/config/), enabling customers to audit their environment for compliance and react quickly to changes.

 Customers can use [AWS Control Tower](https://aws.amazon.com/controltower/) to set up and govern a secure, compliance-aligned, multi-account AWS environment based on best practices established by working with thousands of enterprises. With AWS Control Tower, users on distributed teams can provision new AWS accounts quickly. Meanwhile, central cloud administrators will know that accounts are aligned with centrally established, company-wide compliance policies.

## Information asset identification and classification
<a name="information-asset-identification-and-classification"></a>

 Paragraph 20 of CPS 234 requires ARIs to classify their information assets (software, hardware, and data) by criticality and sensitivity, including those managed by related parties and third parties. This classification must reflect the degree to which an information security incident affecting an information asset has the potential to affect—financially or non-financially—the entity or the interests of depositors, policyholders, beneficiaries, or other customers.

 To help make sure that asset management inventory and maintenance procedures are properly implemented, AWS assets are assigned an owner, tracked, and monitored with AWS proprietary inventory management tools.

 AWS services are content agnostic, in that they offer the same high level of security to customers, regardless of the type of content being stored. AWS is vigilant about our customers' security and has implemented sophisticated technical and physical measures against unauthorized access.

 AWS has no insight as to what type of content the customer chooses to store in AWS and the customer retains complete control of how they choose to classify their content, where it's stored, used, and protected from disclosure.

 AWS considers the identification and classification of an ARI's information assets an action for the ARI to independently complete. The following AWS services and resources might assist customers.

 [AWS Config](https://aws.amazon.com/config/) provides a detailed inventory of customers' AWS resources and configuration, and continuously records configuration changes. [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) provides data and actionable insights to monitor applications, understand and respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health.

 [AWS Systems Manager](https://aws.amazon.com/systems-manager/) gives visibility and control of customer infrastructure on AWS. Systems Manager provides a unified user interface to view operational data from multiple AWS services and allows automation of operational tasks across AWS resources. [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) provides visibility into Amazon EC2 and on-premises computing environments by collecting metadata from your managed instances.

 Customers can store metadata in a central [Amazon S3](https://aws.amazon.com/s3/) bucket, and then use built-in tools to query the data and quickly determine which instances are running the software and configurations required by policy, and which instances need to be updated. Customers can configure Inventory on managed instances by using a one-click procedure and configure and view inventory data from multiple Regions and accounts.

 [AWS Cost Management](https://aws.amazon.com/aws-cost-management/) tools give customers visibility into AWS costs and usage. There is a range of Cost Management tools to help access, organize, understand, control, and optimize costs, which is an important aspect of cloud governance.

## Implementation of controls
<a name="implementation-of-controls"></a>

 Paragraphs 21 and 22 of CPS 234 require ARIs to have information security controls are in place to protect their information assets (software, hardware, and data), including those managed by related parties and third parties. These controls must be commensurate with vulnerabilities and threats to the information assets, criticality and sensitivity of the information assets, the lifecycle stage of the information asset, and the potential consequences of an information security incident.

 AWS has established an information security management program with designated roles and responsibilities that are appropriately aligned within AWS organizations. AWS management reviews and evaluates the risks identified in the risk management program at least annually. The risk management program encompasses the following phases:
+  Discovery – The discovery phase includes listing out risks (threats and vulnerabilities) that exist in the environment. This phase provides a basis for other risk management activities.
+  Research – The research phase considers the potential impacts of identified risks to the business and its likelihood of occurrence and includes an evaluation of internal control effectiveness.
+  Evaluate – The evaluate phase includes making sure controls, processes, and other physical and virtual safeguards are in place to help prevent and detect identified and assessed risks.
+  Resolve – The resolve phase results in risk reports provided to managers with the data they need to make effective business decisions and to comply with internal policies and applicable regulations.
+  Monitor – The monitor phase includes performing monitoring activities to evaluate whether processes, initiatives, functions, and activities are mitigating the risk as designed.

 The implementation of controls to protect information assets is a shared responsibility between AWS and ARIs. The following AWS services and resources can assist customers with their portion of shared controls.

 [AWS Artifact](https://aws.amazon.com/artifact/) provides on-demand access to AWS security and compliance reports, encompassing over 2,500 controls. Reports include our Service Organization Control (SOC) reports, Payment Card Industry (PCI) reports, and certifications from accreditation bodies across geographies and compliance verticals that validate the implementation and operating effectiveness of AWS security controls.

 AWS defines the most important aspects of security *in* the cloud for customers through mechanisms such as the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) and the [AWS Cloud Adoption Framework](https://aws.amazon.com/professional-services/CAF/). Both of those frameworks have specific security areas including detailed whitepapers that help focus on how to [design](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) and [build](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html) secure cloud environments.

## Incident management
<a name="incident-management"></a>

 Paragraphs 23 to 26 of CPS 234 require ARIs to have robust mechanisms in place to detect and respond timely to information security incidents, and to respond to those incidents the ARI considers could plausibly occur (that is, information security response plans). An ARI's information security response plan must include the mechanisms for managing all relevant stages of an incident including escalation and reporting. ARIs must annually review and test their information security response plans to ensure they remain effective and fit-for-purpose.

 AWS has implemented a formal, documented incident response policy and program. The policy addresses purpose, scope, roles, responsibilities, and management commitment.

 To help verify the effectiveness of the AWS Incident Management plan, AWS conducts incident response testing. This testing provides excellent coverage for the discovery of previously unknown defects and failure modes. In addition, it allows the AWS security and service teams to test the systems for potential customer impact and further prepare staff to handle incidents through detection and analysis, containment, eradication, recovery, and post-incident activities.

 AWS runs its Incident Response Test Plan annually, in conjunction with the Incident Response Plan. The test plan includes multiple scenarios, potential vectors of threats, the inclusion of the systems integrator in reporting and coordination (when applicable), in addition to varying reporting and detection avenues (such as customer reporting and detecting and AWS reporting and detecting).

 AWS considers the development and implementation of mechanisms and plans to detect and respond to information security incidents as a shared responsibility between AWS and ARIs. The effectiveness of AWS controls for its portion of these shared responsibilities is described in the assurance reports available in [AWS Artifact.](https://aws.amazon.com/artifact/)

 For customer responsibilities, and as mentioned in the guidance in the Information security capability section above, [AWS Managed Services (AMS)](https://aws.amazon.com/managed-services/) and [AWS Security Competency Partners](https://aws.amazon.com/security/partner-solutions/) can be used by customers to augment internal capabilities or to fill gaps where recruiting in-house resources is cost prohibitive. AWS Security Competency Partners support customers in multiple areas including infrastructure security, policy management, identity management, security monitoring, vulnerability management, data protection, and consulting services.

 The [AWS Security Incident Response Guide](https://docs.aws.amazon.com/security-ir/latest/userguide/security-incident-response-guide.html) presents an overview of the fundamentals of responding to security incidents within a customer's AWS Cloud environment. It focuses on an overview of cloud security and incident response concepts, and identifies cloud capabilities, services, and mechanisms that are available to customers who are responding to security issues.

 With [CloudTrail](https://aws.amazon.com/cloudtrail/), customers can discover and troubleshoot security and operational issues by capturing a comprehensive history of changes that occurred in an AWS account within a specified period of time. [AWS Config](https://aws.amazon.com/config/) allows customers to continuously audit and assess the overall compliance of AWS resource configurations with organizational policies and guidelines.

 [Amazon GuardDuty](https://aws.amazon.com/guardduty/) is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to help protect customers' AWS accounts and workloads. [Amazon Detective](https://aws.amazon.com/detective/) automatically collects log data from AWS resources and uses machine learning, statistical analysis, and graph theory to build a linked set of data that enables faster and more efficient security investigations.

 Finally, [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) gives customers a comprehensive view of high-priority security alerts and compliance status across their AWS accounts. With Security Hub CSPM, customers have a single place that aggregates, organizes, and prioritizes security alerts, or findings, from multiple AWS services.

## Testing control effectiveness
<a name="testing-control-effectiveness"></a>

 Paragraphs 27 and 28 of CPS 234 require ARIs to test the effectiveness of their information security controls through a systematic testing program. The nature and frequency of this testing program must be commensurate with the rate at which the vulnerabilities and threats change, the criticality and sensitivity of the information assets, the consequences of information security incidents, the risks associated with exposure to environments where the ARI is unable to enforce its information security policies, and the materiality and frequency of change to information assets. Where an ARI's information assets are managed by a related party or third party and the ARI is reliant on that party's information security control testing, the ARI must assess whether the nature and frequency of testing of controls is commensurate with the above items.

 Paragraphs 29 to 31 of CPS 234 require ARIs to escalate and report to the Board or senior management any testing results that identify information security control deficiencies that cannot be remediated in a timely manner and to ensure that the testing is conducted by appropriately skilled and functionally independent specialists. ARIs must also review the sufficiency of the testing program at least annually or when there is a material change to information assets or the business environment.

 AWS has established a formal audit program that includes continual, independent internal and external assessments to validate the implementation and operating effectiveness of the AWS control environment.

 AWS plans and performs internal and external audits according to a documented audit schedule to review the continued performance of AWS against standards-based criteria like the ISO/IEC 27001 and to identify improvement opportunities.

 The AWS Compliance reports identify the scope of AWS services and regions assessed, as well the assessor's attestation of compliance.

 AWS considers the testing of information security controls as a shared responsibility between AWS and ARIs. The effectiveness of AWS controls for its shared responsibilities is described in the assurance reports available in [AWS Artifact.](https://aws.amazon.com/artifact/)

 To help customers meet CPS 234 requirements for their portion of shared controls, [Amazon Inspector](https://aws.amazon.com/inspector/) is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. Amazon Inspector automatically assesses applications for exposure, vulnerabilities, and deviations from best practices. After performing an assessment, Amazon Inspector produces a detailed list of security findings prioritized by level of severity. These findings can be reviewed directly or as part of detailed assessment reports, which are available through the Amazon Inspector console or API.

 [Amazon Inspector](https://aws.amazon.com/inspector/) security assessments also check for unintended network accessibility of Amazon EC2 instances and for vulnerabilities on those EC2 instances. Amazon [Inspector](https://aws.amazon.com/inspector/) assessments are offered as pre-defined rules packages mapped to common security best practices and vulnerability definitions. Examples of built-in rules include checking for access to your EC2 instances from the internet, remote root login being enabled, or vulnerable software versions installed. These rules are regularly updated by AWS security researchers.

 AWS customers are welcome to carry out [security assessments or penetration tests](https://aws.amazon.com/security/penetration-testing/) against their AWS infrastructure.

## Internal audit
<a name="internal-audit"></a>

 Paragraphs 32 and 33 of CPS 234 require an ARI's internal audit activities to review the design and operating effectiveness of information security controls, including those maintained by related parties and third parties (information security control assurance). ARIs must ensure that this information security control assurance is provided by appropriately skilled personnel.

 Paragraph 34 of CPS 234 states that an ARI's internal audit function must assess the information security control assurance provided by a related party or third party where:

1.  An information security incident affecting the information assets has the potential to materially affect, financially or non-financially, the entity or the interests of depositors, policyholders, beneficiaries, or other customers, and

1.  The ARI's internal audit function intends to rely on the information security control assurance provided by the related party or third party.

 AWS Compliance reports are made available to customers to enable them to evaluate AWS. AWS considers the audit of information security controls to validate the design and operating effectiveness as a shared responsibility between AWS and ARIs.

 For customers auditing of their own environments[, CloudTrail](https://aws.amazon.com/cloudtrail/) is a service that enables governance, compliance, operational auditing, and risk auditing of AWS accounts. With CloudTrail, customers can log, continuously monitor, and retain account activity related to actions across their AWS infrastructure. CloudTrail provides event history of AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services.

## APRA notification
<a name="apra-notification"></a>

 Paragraphs 35 and 36 of CPS 234 require ARIs to notify APRA as soon as possible and, in any case, no later than 72 hours, after becoming aware of an information security incident that materially affected, or had the potential to materially affect, financially or non-financially, the entity or the interests of depositors, policy holders, beneficiaries, or other customers or that has been notified to other regulators. An ARI must also notify APRA as soon as possible and no later than 10 business days, after it becomes aware of a material information security control weakness that the entity expects it will not be able to remediate in a timely manner.

 AWS defines, administers, and monitors for security incidents for the underlying cloud infrastructure. AWS will promptly notify a customer and take reasonable steps to reduce the effects of a security incident if AWS becomes aware of unlawful or unauthorized access to customer data on AWS equipment or in AWS facilities, and if this unlawful or unauthorized access results in loss, disclosure, or alteration of customer data.

 AWS maintains procedures for notifying customers of customer-impacting issues using the [Health Dashboard](http://status.aws.amazon.com/). The Health Dashboard publishes up-to-the-minute information on service availability, where customers can subscribe to an RSS feed to be notified of interruptions to each individual service and a full status history of each individual service health.

 AWS considers the ARI's notification to APRA as an action for the ARI to independently complete.

 AWS gives customers access to the necessary information to help them meet APRA's notification requirements under CPS 234, paragraphs 35 and 36. There are three ways for customers to get notifications of the status of the workloads they have running on AWS. The best source of security and privacy events related to AWS services are the [AWS Security Bulletins](https://aws.amazon.com/security/security-bulletins/?card-body.sort-by=item.additionalFields.bulletinDateSort&card-body.sort-order=desc), which AWS uses to keep its customers apprised of security announcements, including the AWS timelines for remediation.

 The [Health Dashboard](https://status.aws.amazon.com/) publishes up-to-the-minute information on service availability in Regions around the world. Customers can also take advantage of near real time monitoring and alerting services such as CloudTrail, CloudWatch, GuardDuty, and Security Hub CSPM. Customers are always encouraged to implement manners of auditing, intrusion detection, or other detective controls that monitor for attempted unauthorized access within the instances and services they are using in AWS.

 Customers can integrate these sources into automatic notification systems, for example by subscribing to the RSS feeds for the AWS Service Health Dashboard and the AWS Security Bulletins. Monitoring these sites is the best way for customers to access the information required to help meet APRA's requirements for notification.

 Customers should also keep their accounts up to date with accurate email addresses and security contact information to facilitate timely response and notification.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
