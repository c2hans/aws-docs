---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/regulated-landing-zone.html
---

# Cloud platform and regulated landing zone qualification
<a name="regulated-landing-zone"></a>

A landing zone is a well-architected, multi-account AWS environment that's based on security and compliance best practices.

One of the main functions of the landing zone is to provide a solid foundation for development teams to build on, and address as many regulatory requirements as possible, thus removing the responsibility from the development teams.

The GAMP IT Infrastructure Control and Compliance guidance document follows a platform-based approach to the qualification of IT infrastructure which aligns perfectly with a customer's need to qualify their landing zone.

The landing zone includes capabilities for centralized logging, security, account vending, and core network connectivity. There are 2 main ways of establishing a landing zone:

1. Create one using [AWS Control Tower](https://aws.amazon.com/controltower/)

1. Use the [AWS Landing Zone Accelerator](https://aws.amazon.com/blogs/industries/introducing-landing-zone-accelerator-for-healthcare/)

We recommend that you use the Landing Zone Accelerator (LZA) for Healthcare which is an industry specific deployment of the LZA solution architected to align with AWS best practices and in conformance with multiple, global compliance frameworks. It is available for free as open source software on [GitHub](https://github.com/aws-samples/landing-zone-accelerator-on-aws-for-healthcare). One reason why the LZA is a good choice for a regulated landing zone is that it is configured through a template that can easily be demonstrated to be kept under a state of control. In the same way infrastructure as code (IaC) can be managed and controlled by using source code repositories and deployment automation, so can the LZA configuration.

The LZA solution expands upon the basic AWS Control Tower framework, which includes Management, Audit, and Log Archive accounts, and adds extra resources and guardrails designed to strengthen your platform's security, compliance, and operational readiness. Keep in mind that deploying LZA for Healthcare is not a complete compliance solution on its own. Instead, think of it as a strong foundation that can be augmented with other solutions to meet your needs. Your organization remains responsible for thoroughly reviewing, testing, and validating that the solution aligns with your specific security requirements, including your unique tools, features, and system configurations. The objective of the landing zone, and the team owning it, should be to provide the guardrails and features that free the developers to use the right tools for the job and focus on delivering differentiated business value rather than on compliance.

The LZA for Healthcare Solution incorporates security and compliance controls aligned with multiple international healthcare standards, including HIPAA (United States), NCSC (United Kingdom), ENS High (Spain), C5 (Germany), and Fascicolo Sanitario Elettronico (Italy). Before implementing the LZA on AWS for Healthcare solution, we recommend discussing your specific compliance requirements with your AWS representative to ensure proper alignment.

This solution implements comprehensive security controls in AWS environments through both detective (AWS Config rules) and preventative (service control policies) guardrails. AWS Config monitors and records AWS resource configurations, evaluates compliance against rules, and tracks changes for auditing and security. Service control policies are AWS Organizations rules that limit permissions across accounts, controlling which services and actions users can access.

The configuration framework addresses three critical areas: organizational controls, security settings, and global parameters. Organizational controls include policies for service management, resource tagging, and backup strategies, while security settings enable core AWS security services and implement detective guardrails through multiple compliance frameworks such as AWS Security Hub, CIS Benchmarks, NIST guidelines, and HIPAA compliance rules. Global settings manage configurations for active Regions and centralized logging through CloudTrail and Amazon CloudWatch services. All these components work together to create a robust security foundation, though organizations should review and customize these configurations to align with their specific compliance requirements and operational needs.

## Tooling and automation
<a name="tooling-and-automation"></a>

Many customers include common tooling and automation as part of a landing zone so it can be qualified and validated once and used by all development teams. This common tooling is often within the shared services account of the landing zone.

For example, standard tooling around requirements management, test management, CI/CD, and so on need to be qualified and validated.

Similarly, any automation of IT processes also needs to be validated. For example, it's possible to automate the infrastructure verification step of your computer systems validation process.

## Using managed services
<a name="leveraging-managed-services"></a>

Instead of building and operating a landing zone yourself, you have the option of delegating this responsibility. This delegation could be to AWS by using [AWS Managed Services](https://aws.amazon.com/managed-services/) or to a partner within the [AWS Partner Network](https://aws.amazon.com/partners/) (APN). This means the service provider is responsible for building a landing zone based on AWS best practices, operating it in accordance with industry best practices and providing sufficient evidence to you in meeting your expectations.

## Maintaining the landing zone's qualified state
<a name="maintaining-the-landing-zones-qualified-state"></a>

After the landing zone is live, it must be maintained in a qualified state. Unless the operations are delegated to a partner, you typically create a Cloud Platform Operations and Maintenance SOP based on Section 6 of GAMP IT Infrastructure Control and Compliance.

According to GAMP, there are several areas where control must be shown, such as change management, configuration management, security management, and others. GAMP guidance also suggests that 'automatic tools' should be used whenever possible. The following sections cover these control areas and how AWS services can help with automation.

### Change management
<a name="change-management-lz"></a>

Change management processes control how changes to configuration items are made. These processes should include an assessment of the potential impact on the GxP applications supported by the landing zone. As mentioned earlier, all of the landing zone components are deployed using an automated pipeline. Therefore, after a change has been approved and committed in the source code repository tool, the pipeline is triggered and the change deployed. There will likely be multiple pipelines for the various parts that make up the landing zone.

The landing zone is made up of infrastructure and automation components. Now, using infrastructure as code, such as through CloudFormation, there is no real difference between how these different components are deployed.

We recommend a continuous deployment methodology because it ensures changes are automatically built, tested, and deployed, with the goal of eliminating as many manual steps as possible. Continuous deployment seeks to eliminate the manual nature of this process and automate each step, allowing development teams to standardize the process and increase the efficiency with which they deploy code. In continuous deployment, an entire release process is a pipeline containing stages. [AWS CodePipeline](https://aws.amazon.com/codepipeline/) can be used along with [AWS CodeCommit](https://aws.amazon.com/codecommit/), [AWS CodeBuild](https://aws.amazon.com/codebuild/), and [AWS CodeDeploy](https://aws.amazon.com/codedeploy/). For customers needing additional approval steps, CodePipeline also supports the inclusion of manual steps.

[AWS Config](https://aws.amazon.com/config/) provides continuous monitoring and assessment of AWS resource configurations. It helps track changes to resources over time and evaluate them against desired configurations, with ability to set up rules for compliance checking.

All changes to AWS services, either manual or automated, are logged by [AWS CloudTrail](https://aws.amazon.com/cloudtrail/). CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. This event history simplifies security analysis, resource change tracking, and troubleshooting. In addition, you can use CloudTrail to detect unusual activity in your AWS accounts. These capabilities help simplify operational analysis and troubleshooting.

Of course, customers also want to be alerted about any unauthorized and unintended changes. You can use a combination of CloudTrail and Amazon CloudWatch to [detect unauthorized changes made to the production environment](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html) and even automate immediate remediation.

[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) is a monitoring service for AWS Cloud resources and alarms can be used to trigger responses to CloudTrail events.

[Amazon EventBridge](https://aws.amazon.com/eventbridge/) is a serverless event bus service that can detect changes in AWS services and trigger automated responses. It is useful for creating automated workflows around change management processes.

[AWS Systems Manager Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html) is a framework for requesting, approving, implementing, and reporting on operational changes to application configuration and infrastructure. It includes pre-approved change templates and automated approval workflows.

### Configuration management
<a name="configuration-management"></a>

Going hand in hand with change management is configuration management. Configuration items (CIs) are the components that make up a system, and CIs should only be modified through the change management process.

[Infrastructure as code](https://d1.awsstatic.com/whitepapers/infrastructure-as-code.pdf) (IaC) brings automation to the provisioning process through tools like [CloudFormation](https://aws.amazon.com/cloudformation/). Rather than relying on manually performed steps, both administrators and developers can instantiate infrastructure using configuration files. Infrastructure as code treats these configuration files as software code. These files can be used to produce a set of artifacts, namely the compute, storage, network, and application services that comprise an operating environment. Infrastructure as Code eliminates configuration drift through automation, thereby increasing the speed and agility of infrastructure deployments.

[AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html) and tagging let you organize your AWS landscape by applying tags at different levels of granularity. Tags allow you to label, collect, and organize resources and components within services.

The [Tag Editor](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html) lets you manage tags across services and AWS Regions. Using this approach, you can globally manage all the application, business, data, and technology components of your target landscape.

A [Resource Group](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted.html) is a collection of resources that share one or more tags. It can be used to create an enterprise architecture view of your IT landscape, consolidating AWS resources into a per-project (that is, the on-going programs that realize your target landscape), per-entity (that is, capabilities, roles, processes), and per-domain (that is, Business, Application, Data, Technology) view.

[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) is a service that lets you assess, audit, and evaluate the configurations of AWS resources. AWS Config continuously monitors and records your AWS resource configurations and lets you automate the evaluation of recorded configurations against desired configurations. With AWS Config, you can review changes in configurations and determine their overall compliance against the configurations specified in your internal guidelines. This enables you to simplify compliance auditing, security analysis, change management, and operational troubleshooting. In addition, AWS provides conformance packs for AWS Config to provide a general-purpose compliance framework designed to enable you to create security, operational, or cost-optimization governance checks using managed or custom AWS Config rules and AWS Config remediation actions, including a [conformance pack for 21 CFR 11](https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-FDA-21CFR-Part-11.html).

[AWS Systems Manager](https://aws.amazon.com/systems-manager/) serves as a unified interface for infrastructure control across AWS and on-premises environments. It includes several key components: Parameter Store for secure configuration storage, State Manager for maintaining consistent configurations, automation for scripting common maintenance and deployment tasks, and Fleet Manager for remote node management. This integrated approach makes it a powerful tool for comprehensive configuration management across diverse environments.

[AWS Service Catalog](https://aws.amazon.com/servicecatalog/) facilitates the creation and management of approved IT services and configurations catalogs. Through version-controlled templates and robust access controls, it enforces standardization across the organization. The service supports delegated administration and self-service provisioning within approved boundaries, while integrating with AWS Organizations for comprehensive multi-account governance.

[AWS Resource Access Manager (AWS RAM)](https://aws.amazon.com/ram/) enables secure and controlled sharing of AWS resources across accounts. It maintains consistent configurations across shared resources while providing centralized control over resource sharing permissions. Its integration with AWS Organizations makes it particularly valuable for managing resource sharing in complex organizational structures.

[AWS Proton](https://aws.amazon.com/proton/) focuses on managing and deploying container and serverless applications using standardized templates. It maintains consistency through versioned service templates and infrastructure configurations, enables automated updates across multiple environments, and provides centralized configuration management specifically designed for microservices architectures. This makes it particularly valuable for organizations adopting modern application architectures.

### Security management
<a name="security-management"></a>

AWS has defined a set of best practices for customers who are designing the security infrastructure and configuration for applications running in AWS.

[Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/) provides security best practices that will help you define your information security management system (ISMS) and build a set of security policies and processes for your organization so you can protect your data and assets in the AWS Cloud.

[Security, Identity, and Compliance on AWS](https://aws.amazon.com/products/security/) provides an overview of different security topics such as identifying, categorizing, and protecting your assets on AWS, managing access to AWS resources using accounts, users, and groups and suggesting ways you can secure your data, operating system, applications, and overall infrastructure in the cloud.

AWS provides you with an [extensive set of tools](https://aws.amazon.com/products/security/) to secure workloads in the cloud.

If you implement full automation, it could negate the need for anyone to have direct access to any environment beyond development. However, if a situation occurs that requires someone to access a production environment, they must explicitly request access, have the access reviewed and approved by the appropriate owner, and upon approval, obtain temporary access with the least privilege needed and only for the duration required. You should then track their activities through logging while they have access. See [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) for further information.

### Problem and incident management
<a name="problem-and-incident-management"></a>

With AWS, you get access to many tools and features to help you meet your problem and incident management objectives. These capabilities help you establish a configuration and security baseline that meets your objectives for your applications running in the cloud.

When a deviation from your baseline does occur (such as by a misconfiguration), you might need to respond and investigate. To successfully do so, you must understand the basic concepts of security incident response within your AWS environment and the issues you need to consider to prepare, educate, and train your cloud teams before security issues occur. It is important to know which controls and capabilities you can use, to review topical examples for resolving potential concerns, and to identify remediation methods that can be use automation and improve response speed.

Because security incident response can be a complex topic, we encourage you to start small, develop runbooks, use basic capabilities, and create an initial library of incident response mechanisms to iterate from and improve upon. This initial work should include teams that are not involved with security and should include your legal departments, so that they are better able to understand the impact that incident response (IR), and the choices they have made, have on your corporate goals.

For a comprehensive guide, see the [AWS Security Incident Response Guide](https://docs.aws.amazon.com/security-ir/latest/userguide/security-incident-response-guide.html).

### Backup and restore
<a name="backup-and-restore"></a>

The ability to back up and restore is required for all validated applications. It is therefore a common capability that can be centralized as part of the regulated landing zone. Backup and restore should not be confused with archiving and retrieval.

For a cloud-based backup and restore capability, consider [AWS Backup](https://aws.amazon.com/backup/).

AWS Backup is a fully managed backup service that makes it easy to centralize and automate the backup of data across AWS services. Using AWS Backup, you can centrally configure backup policies and monitor backup activity for AWS resources, such as Amazon EBS volumes, Amazon EC2 instances, Amazon RDS databases, DynamoDB tables, Amazon EFS file systems, Amazon FSx file systems, and AWS Storage Gateway volumes. AWS Backup automates and consolidates backup tasks previously performed service-by-service, removing the need to create custom scripts and manual processes. With a few clicks in the AWS Backup console, you can create backup policies that automate backup schedules and retention management. AWS Backup provides a fully managed, policy-based backup solution, simplifying your backup management, enabling you to meet your business and regulatory backup compliance requirements.

### Disaster recovery
<a name="disaster-recovery"></a>

In traditional on-premises situations, disaster recovery (DR) involves a separate data center located a certain distance from the primary data center. This separate data center only exists in case of a complete disaster impacting the primary data center. Often the infrastructure at the DR site sits idle, or at best hosts pre-production instances of applications thus running the risk of it being out-of-sync with production. With the advent of the cloud, DR is now much easier and cheaper.

The AWS global infrastructure is built around AWS Regions and Availability Zones (AZ). AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected by low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

With Availability Zones, it is easy to create a multi-AZ architecture capable of withstanding a complete failure of one or more zones. For even more resilience, multiple AWS Regions can be used. With the use of infrastructure as code, the infrastructure and applications in a DR Region do not need to run all of the time. In case of a disaster, the entire application stack can be deployed into another Region. The only components that must run all the time are those keeping the data repositories in sync.

[AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) (AWS DRS), formerly known as CloudEndure Disaster Recovery, is a highly automated disaster recovery service that enables quick and reliable recovery of physical, virtual, and cloud-based servers into AWS. The service continuously replicates your servers (including operating system, system state configuration, databases, applications, and files) into a low-cost staging area in your target AWS account and preferred Region. During an actual disaster or disaster recovery drill, AWS DRS can automatically convert your servers to run natively on AWS, typically within minutes of initiating the recovery, with minimal data loss and near-zero downtime.

### Helpdesk
<a name="help-desk"></a>

The helpdesk serves as a critical component in maintaining the validated state of GxP systems by functioning as the primary point of contact for incident management, change requests, and user support while ensuring regulatory compliance. It must operate under documented procedures that clearly define incident classification, escalation protocols, and resolution workflows, with established severity levels and response time requirements specifically tailored for GxP-critical systems. The helpdesk staff must be properly trained to understand the impact of changes and maintain a comprehensive record of all actions taken in compliance with predefined procedures. Communication protocols play a vital role in helpdesk operations, requiring clear channels with users and stakeholders, regular status updates on critical incidents, and well-defined escalation procedures for high-priority issues. The helpdesk must maintain strong integration with the change control board and quality assurance team, while implementing effective feedback mechanisms for system improvements. This ensures that all stakeholders are properly informed and involved in maintaining the validated state of GxP systems.

Regular performance evaluation through established metrics, quality reviews, and compliance assessments helps ensure the helpdesk maintains its qualified state and continues to support the validated environment effectively. This includes monitoring response times, resolution rates, documentation quality, and compliance with established procedures. The helpdesk must maintain detailed records of all activities, ensuring traceability and providing evidence of maintained system validation status for regulatory inspections and audits.

[Amazon Connect](https://aws.amazon.com/products/connect/customer/) is a cloud-based contact center service that can be used to create a comprehensive helpdesk solution. The service offers an omnichannel experience, supporting voice, chat, and task management through a unified interface, while enabling seamless integration with existing CRM systems and other business applications. It provides intelligent routing, real-time and historical analytics, and integration capabilities with other AWS services and external systems. Amazon Connect offers features like call recording, queue management, and interactive voice response (IVR), making it suitable for organizations requiring a full-featured helpdesk phone system with scalability.

### Performance monitoring
<a name="performance-monitoring"></a>

Performance monitoring in GxP-regulated environments requires a systematic approach to continuously track, analyze, and maintain system performance while ensuring compliance with regulatory requirements. Organizations must establish comprehensive monitoring programs that include defined performance metrics, thresholds, and alert mechanisms for critical system parameters that could impact product quality or data integrity. The monitoring system should provide real-time visibility into system performance, with automated alerts for deviations from established parameters, and maintain detailed audit trails of all monitoring activities and responses to performance issues.

[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) serves as the primary monitoring service, collecting and tracking metrics, logs, and events across AWS resources and applications. It provides real-time monitoring capabilities with customizable dashboards and alerting mechanisms, enabling comprehensive performance tracking and automated responses to performance issues. The detailed metrics and analytics capabilities of CloudWatch help organizations understand system behavior and identify potential performance bottlenecks before they impact operations.

[Amazon CloudWatch Application Signals](https://aws.amazon.com/cloudwatch/features/application-signals/) provides application performance monitoring for distributed applications, offering end-to-end visibility into request traces, service dependencies, and latency issues across microservices architectures. Supporting OpenTelemetry as the instrumentation standard, Application Signals enables service maps, automated SLO tracking, and detailed performance optimization of complex distributed systems.

[Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) and [AWS Managed Grafana](https://aws.amazon.com/grafana/) provide powerful monitoring and visualization capabilities for containerized environments. These services enable collection of high-cardinality metrics and creation of rich dashboards for monitoring container and microservice performance, while offering scalable, managed solutions for metric storage and visualization.

### Periodic review
<a name="periodic-review"></a>

While our objective is to establish continuous compliance, while manual processes still exist periodic reviews are required and represent a critical quality assurance process designed to ensure systems maintain their qualified state and continue to operate effectively within regulatory requirements. This systematic assessment involves comprehensive evaluation of system performance, security measures, compliance status, and documentation to identify any gaps or areas requiring improvement. The process helps organizations maintain regulatory compliance while ensuring systems remain fit for their intended use through regular assessment of operational effectiveness and control mechanisms. Periodic reviews must be conducted according to established schedules based on system criticality and risk assessment, with all activities documented to demonstrate ongoing compliance.

On top of AWS Config, Amazon CloudWatch, and Amazon Inspector mentioned previously, [AWS Audit Manager](https://aws.amazon.com/audit-manager/) simplifies the review process by continuously auditing AWS usage and simplifying risk and compliance assessments. It provides pre-built frameworks for common industry standards and maintains evidence collection and audit documentation. [Amazon Macie](https://aws.amazon.com/macie/) enhances security reviews by automatically discovering and protecting sensitive data in AWS, providing ongoing monitoring and risk assessment of data security, and generating detailed reports for security and compliance reviews.

[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) offers real-time guidance for following AWS best practices, providing recommendations across cost optimization, security, fault tolerance, and performance domains. Systems Manager supplements this by offering tools for viewing and controlling infrastructure state, providing operational insights and patch compliance status, and enabling automated compliance reporting and system maintenance. AWS Organizations facilitates management of multiple AWS accounts centrally for governance, enabling policy-based management and compliance across accounts.
