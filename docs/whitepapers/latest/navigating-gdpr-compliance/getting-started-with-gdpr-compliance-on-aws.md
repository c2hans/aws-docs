---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/getting-started-with-gdpr-compliance-on-aws.html
---

# Getting Started with GDPR Compliance on AWS
<a name="getting-started-with-gdpr-compliance-on-aws"></a>

AWS makes available services, features, and documentation that customers can use to configure their environments in alignment with GDPR requirements. Customers remain responsible for evaluating their own use of AWS services and defining their individual compliance approach.

To get started, customers should consider the following structured process:
+ **Understand your notification obligations**:Before designing your cloud architecture, ensure you are ready to meet key GDPR obligations, such as the 72-hour breach notification requirement under Article 33 of the GDPR. AWS provides tools like [Amazon GuardDuty](https://aws.amazon.com/guardduty/), [AWS CloudTrail](https://aws.amazon.com/cloudtrail), and [AWS Security Hub](https://aws.amazon.com/security-hub/) to support incident detection and response, but customers must establish procedures for severity assessment, notification decisions, and regulator coordination.
+ **Conduct a data processing assessment**:Identify what personal data is being processed, for what purposes, and where it flows. This includes reviewing data types, processing activities, and any cross-border transfers. Map these findings to the AWS services and accounts you use or plan to use.
+ **Design your account and service architecture**:Use [AWS Organizations](https://aws.amazon.com/organizations/) and [AWS Control Tower](https://aws.amazon.com/controltower/) to implement a structured multi-account setup. This can help isolate workloads, manage permissions, and enforce guardrails from the beginning.
+ **Define your compliance roadmap**:Plan and implement the required technical and organizational measures. This typically includes:
+ Technical: encryption, access management, logging, and monitoring
+ Organizational: privacy policies, consent handling, DPIA processes, and staff training
+ **Assign clear roles and responsibilities**:Ensure all key stakeholders are identified early, including Data Protection Officers (DPOs), legal counsel, and technical leads. Each must understand their part in maintaining compliance.
+ **Establish and maintain documentation**:Tools like [AWS CloudTrail](https://aws.amazon.com/de/cloudtrail/), [AWS Config](https://aws.amazon.com/config/), [AWS Security Hub](https://aws.amazon.com/security-hub/) and [AWS Audit Manager](https://aws.amazon.com/audit-manager/) can help create and maintain an evidence-based assessment framework aligned with GDPR requirements.
+ **Plan for continuous compliance**:Implement processes for ongoing monitoring, regular reviews, and incident response. AWS provides various templates, checklists, and technical documentation through [AWS Prescriptive Guidance](https://aws.amazon.com/prescriptive-guidance/?ams%23interactive-card-vertical%23pattern-data.filter=%257B%2522filters%2522%253A%255B%255D%257D) and [AWS Solutions Library](https://aws.amazon.com/solutions/) to help customers implement GDPR-compliant architectures.

AWS provides infrastructure and service-level controls, and customers are responsible for defining their data protection strategy, configuring services, and managing compliance over time.

## Example Step-by-Step GDPR Compliance Process
<a name="example-step-by-step-gdpr-compliance-process"></a>

This section provides an example step-by-step approach, based on common practices, for customers to get started with their GDPR compliance on AWS:
+ *Data Inventory, Purpose for Processing, and Mapping*: Identify all personal data processed and for which purposes; map the data flows, including cross-border transfers.
+ *GDPR Readiness Assessment*: Evaluate current compliance status against GDPR requirements; identify gaps in policies, procedures, and technical measures.
+ *Establish a Governance Structure*: Appoint key roles (e.g., Data Protection Officer if required); Define responsibilities and reporting lines; set up a cross-functional GDPR compliance team.
+ *Update Policies and Procedures*: Review and update privacy policies, consent mechanisms; develop procedures for handling data subject rights; and create data retention and deletion policies.
+ *Implement Technical Measures*: Enable encryption for data at rest and in transit; set up access controls and authentication; implement logging and monitoring including a mechanism for sensitive data discovery; use [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) to guide secure and compliant design.
+ *Conduct Data Protection Impact Assessments (DPIAs)*: Identify high-risk processing activities and perform DPIAs for these activities.
+ *Implement Data Subject Rights Processes*: Set up mechanisms to handle access, deletion, and portability requests; implement data rectification processes.
+ *Establish Breach Notification Procedures*: Develop an incident response plan; set up detection and notification systems; conduct breach notification drills.
+ *Training and Awareness*: Conduct GDPR training for staff; create role-specific guidance for teams; use AWS training resources to support cloud-specific compliance knowledge.
+ *Documentation and Record-Keeping*: Maintain records of processing activities, document compliance measures and decisions; use [AWS CloudTrail](https://aws.amazon.com/cloudtrail) and [AWS Config](https://aws.amazon.com/config/) for maintaining audit trails.
+ *Continuous Monitoring and Improvement*: Regularly review and update compliance measures; stay informed about AWS service updates and new compliance features; conduct periodic audits and assessments.

Remember, this is a general approach and should be tailored to each organization's specific circumstances and use of AWS services. It is advisable to consult with legal and privacy professionals familiar with the GDPR and AWS to ensure comprehensive compliance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
