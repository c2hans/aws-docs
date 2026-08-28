---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/aws-risk-and-compliance-program.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS risk and compliance program
<a name="aws-risk-and-compliance-program"></a>

AWS has integrated a risk and compliance program throughout the organization. This program aims to manage risk in all phases of service design and deployment and continually improve and reassess the organization’s risk-related activities. The components of the AWS integrated risk and compliance program are discussed in greater detail in the following sections.

## AWS business risk management
<a name="aws-business-risk-management"></a>

AWS has a business risk management (BRM) program that partners with AWS business units to provide the AWS Board of Directors and AWS senior leadership a holistic view of key risks across AWS. The BRM program demonstrates independent risk oversight over AWS functions. Specifically, the BRM program does the following:
+  Performs risk assessments and risk monitoring of key AWS functional areas
+  Identifies and drives remediation of risks

To drive the remediation of risks, the BRM program reports the results of its efforts, and escalates where necessary, to directors and vice presidents across the business to inform business decision-making.

## Operational and business management
<a name="operational-and-business-management"></a>

AWS uses a combination of weekly, monthly, and quarterly meetings and reports to, among other things, ensure communication of risks across all components of the risk management process. In addition, AWS implements an escalation process to provide management visibility into high priority risks across the organization. These efforts, taken together, help ensure that risk is managed consistently with the complexity of the AWS business model.

In addition, through a cascading responsibility structure, vice presidents (business owners) are responsible for the oversight of their business. To this end, AWS conducts weekly meetings to review operational metrics and identify key trends and risks before they impact the business.

Executive and senior leadership play important roles in establishing the AWS tone and core values. Every employee is provided with the company’s Code of Business Conduct and Ethics, and employees complete periodic training. Compliance audits are performed so that employees understand and follow established policies.

The AWS organizational structure provides a framework for planning, executing, and controlling business operations. The organizational structure includes roles and responsibilities to provide for adequate staffing, efficiency of operations, and the segregation of duties. Management has also established appropriate lines of reporting for key personnel. The company’s hiring verification processes include validation of education, previous employment, and, in some cases, background checks as permitted by law and regulation for employees commensurate with the employee’s position and level of access to AWS facilities. The company follows a structured on-boarding process to familiarize new employees with Amazon tools, processes, systems, policies, and procedures.

## Control environment and automation
<a name="control-environment-and-automation"></a>

AWS implements security controls as a foundational element to manage risk across the organization. The AWS control environment is comprised of the standards, processes, and structures that provide the basis for implementing a minimum set of security requirements across AWS.

While processes and standards included as part of the AWS control environment stand on their own, AWS also leverages aspects of Amazon’s overall control environment. Leveraged tools include:
+  Tools used across all Amazon businesses, such as the tool that manages separation of duties
+  Certain Amazon-wide business functions, such as legal, human resources, and finance

In instances where AWS leverages Amazon’s overall control environment, the standards and processes governing these mechanisms are tailored specifically for the AWS business. This means that the expectations for their use and application within the AWS control environment may differ from the expectations for their use and application within the overall Amazon environment. The AWS control environment ultimately acts as the foundation for the secure delivery of AWS service offerings.

Control automation is a way for AWS to reduce human intervention in certain recurring processes comprising the AWS control environment. It is key to effective information security control implementation and associated management of risks. Control automation seeks to proactively minimize potential inconsistencies in process execution that might arise due to the flawed nature of humans conducting a repetitive process. Through control automation, potential process deviations are eliminated. This provides increased levels of assurance that a control will be applied as designed.

Engineering teams at AWS across security functions are responsible for engineering the AWS control environment to support increased levels of control automation wherever possible. Examples of automated controls at AWS include:
+  **Governance and Oversight:** Policy versioning and approval
+  **Personnel Management:** Automated training delivery, rapid employee termination
+  **Development and Configuration Management:** Code deployment pipelines, code scanning, code backup, integrated deployment testing
+  **Identity and Access Management:** Automated segregation of duties, access reviews, permissions management
+  **Monitoring and Logging:** Automated log collection and correlation, alarming
+  **Physical Security:** Automated processes related to AWS data centers, including hardware management, data center security training, access alarming, and physical access management
+  **Scanning and Patch Management:** Automated vulnerability scanning, patch management, and deployment

## Controls assessment and continuous monitoring
<a name="controls-assessment-and-continuous-monitoring"></a>

AWS implements a variety of activities prior to and after service deployment to further reduce risk within the AWS environment. These activities integrate security and compliance requirements during the design and development of each AWS service and then validate that services are operating securely after they are moved into production (launched).

Risk management and compliance activities include two pre-launch activities and two post-launch activities. The pre-launch activities are:
+  AWS Application Security risk management review to validate that security risks have been identified and mitigated
+  Architecture readiness review to help customers ensure alignment with compliance regimes

At the time of its deployment, a service will have gone through rigorous assessments against detailed security requirements to meet the AWS high bar for security. The post-launch activities are:
+  AWS Application Security ongoing review to help ensure service security posture is maintained
+  Ongoing vulnerability management scanning

These control assessments and continuous monitoring allow regulated customers the ability to confidently build compliant solutions on AWS services. For a list of services in the scope for various compliance programs see the [AWS Services in Scope](https://aws.amazon.com/compliance/services-in-scope/) webpage.

## AWS certifications, programs, reports, and third-party attestations
<a name="aws-certifications-programs-reports-and-third-party-attestations"></a>

AWS regularly undergoes independent third-party attestation audits to provide assurance that control activities are operating as intended. More specifically, AWS is audited against a variety of global and regional security frameworks dependent on region and industry. AWS participates in over 50 different audit programs.

The results of these audits are documented by the assessing body and made available for all AWS customers through [AWS Artifact](https://aws.amazon.com/artifact/). AWS Artifact is a no cost self-service portal for on-demand access to AWS compliance reports. When new reports are released, they are made available in AWS Artifact, allowing customers to continuously monitor the security and compliance of AWS with immediate access to new reports.

Depending on a country’s or industry’s local regulatory or contractual requirements, AWS may also undergo audits directly with customers or governmental auditors. These audits provide additional oversight of the AWS control environment to ensure that customers have the tools to help themselves operate confidently, compliantly, and in a risk-based manner using AWS services.

For more detailed information about the AWS certification programs, reports, and third-party attestations, visit the [AWS Compliance Program](https://aws.amazon.com/compliance/programs/) webpage. You can also visit the [AWS Services in Scope](https://aws.amazon.com/compliance/services-in-scope/) webpage for service-specific information.

## Cloud Security Alliance
<a name="cloud-security-alliance"></a>

AWS participates in the voluntary Cloud Security Alliance (CSA) Security, Trust & Assurance Registry (STAR) Self-Assessment to document its compliance with CSA-published best practices. The [CSA](https://cloudsecurityalliance.org/about/) is “the world’s leading organization dedicated to defining and raising awareness of best practices to help ensure a secure cloud computing environment”.The CSA Consensus Assessments Initiative Questionnaire (CAIQ) provides a set of questions the CSA anticipates a cloud customer and/or a cloud auditor would ask of a cloud provider. It provides a series of security, control, and process questions, which can then be used for a wide range of efforts, including cloud provider selection and security evaluation.

There are two resources available to customers that document the alignment of AWS to the CSA CAIQ. The first is the [CSA CAIQ Whitepaper](https://d1.awsstatic.com/whitepapers/compliance/CSA_Consensus_Assessments_Initiative_Questionnaire.pdf), and the second is a more detailed control mapping to our SOC-2 controls which is available to via [AWS Artifact](https://aws.amazon.com/artifact/). For more information about the AWS participation in CSA CAIQ, see the [AWS CSA site](https://aws.amazon.com/compliance/csa/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
