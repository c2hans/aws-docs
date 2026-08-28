---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/cloud-platformlanding-zone-qualification.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cloud Platform/Landing Zone Qualification
<a name="cloud-platformlanding-zone-qualification"></a>

 A landing zone, such as the one created by [AWS Control Tower](https://aws.amazon.com/controltower/), is a well-architected, multi-account AWS environment that's based on security and compliance best practices.

 The landing zone includes capabilities for centralized logging, security, account vending, and core network connectivity. We recommend that you then build features into the landing zone to satisfy as many regulatory requirements as possible and to effectively remove the burden from the development teams which build on it. The objective of the landing zone, and the team owning it, should be to provide the guardrails and features that free the developers to use the ‘right tools for the job’ and focus on delivering differentiated business value rather than on compliance.

 For example, account vending could be extended to include account bootstrapping to automatically direct logs to the central logging account, drop default VPCs and instantiate an approved VPC (if needed at all), deploy baseline stack sets, and establish standard roles to support things like automated installation qualification (IQ). The Shared Services account would house centralized capabilities and automations such as the mentioned automation of IQ. The centralized logging account could satisfy regulatory requirements around audit trails including, for example, record retention through the use of lifecycle policies. The addition of a backup and archive account could provide standard [backup and restore](https://aws.amazon.com/backup-restore/) along with archiving services for application teams to use.

 Similarly, a standardized approach to disaster recovery (DR) can be provided by the landing zone using tools like [CloudEndure Disaster Recovery](https://aws.amazon.com/cloudendure-disaster-recovery/).

 If you follow AWS guidance and implement a Cloud Center of Excellence (CCoE) and consider the landing zone as a product, the CCoE team takes on the responsibility of building these capabilities into the landing zone to satisfy regulatory requirements.

 The number of capabilities built into the landing zone is often influenced by the organizational structure around it. If you have a traditional structure with a divide between development teams and infrastructure, tasks like server and network management are centralized and these capabilities are built into the platform. If you adopt a product-centric operating model, the development teams become more autonomous and responsible for more of the stack, perhaps even the entire stack from the VPC and everything built on it. Also consider, with serverless architectures, you may not need a VPC because there are no servers to manage.

 This underlying cloud platform when supporting GxP applications should be qualified to demonstrate proper configuration and to ensure that a state of control and compliance is maintained. The qualification of the cloud can follow a traditional infrastructure qualification project which includes the planning, specification and design, risk assessment, qualification test planning, installation qualification (IQ), operational qualification (OQ), and handover (as described in Section 5 of GAMP IT, Qualification of Platforms).

 The components (configuration items) that make up the landing zone should all be deployed through automated means, i.e. an automated pipeline. This approach supports better change management going forward.

 After the completion of the infrastructure project and the creation of the operations and maintenance SOPs, you have a qualified cloud platform upon which GxP workloads can run. The SOPs cover topics such as account provisioning, access management, change management, and so on.

## Maintaining the Landing Zone’s Qualified State
<a name="maintaining-the-landing-zones-qualified-state"></a>

 Once the landing zone is live it must be maintained in a qualified state. Unless the operations are delegated to a partner, you typically create a Cloud Platform Operations and Maintenance SOP based on Section 6 of GAMP IT Infrastructure Control and Compliance.

 According to GAMP, there are several areas where control must be shown, such as change management, configuration management, security management, and others. GAMP guidance also suggests that ‘automatic tools’ should be used whenever possible. The following sections cover these control areas and how AWS services can help with automation.

### Change Management
<a name="change-management-1"></a>

 Change Management processes control how changes to configuration items are made. These processes should include an assessment of the potential impact on the GxP applications supported by the landing zone. As mentioned earlier, all of the landing zone components are deployed using an automated pipeline. Therefore, once a change has been approved and committed in the source code repository tool, like AWS CodeCommit, the pipeline is triggered and the change deployed. There will likely be multiple pipelines for the various parts that make up the landing zone.

 The landing zone is made up of infrastructure and automation components. Now, through the use of infrastructure as code, there is no real difference between how these different components are deployed.

 We recommend a continuous deployment methodology because it ensures changes are automatically built, tested, and deployed, with the goal of eliminating as many manual steps as possible. Continuous deployment seeks to eliminate the manual nature of this process and automate each step, allowing development teams to standardize the process and increase the efficiency with which they deploy code. In continuous deployment, an entire release process is a *pipeline* containing stages. AWS CodePipeline can be used along with AWS CodeCommit, AWS CodeBuild, and AWS CodeDeploy. For customers needing additional approval steps, AWS CodePipeline also supports the inclusion of manual steps.

 All changes to AWS services, either manual or automated are logged by AWS CloudTrail.

 [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. This event history simplifies security analysis, resource change tracking, and troubleshooting. In addition, you can use CloudTrail to detect unusual activity in your AWS accounts. These capabilities help simplify operational analysis and troubleshooting.

 Of course, customers also want to be alerted about any unauthorized and unintended changes. You can use a combination of AWS CloudTrail and AWS CloudWatch to detect unauthorized changes made to the production environment and even automate immediate remediation. [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) is a monitoring service for AWS Cloud resources and can be used to trigger responses to AWS CloudTrail events ([https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)).

### Configuration Management
<a name="configuration-management"></a>

 Going hand in hand with change management is configuration management. Configuration items (CIs) are the components that make up a system and CIs should only be modified through the change management process.

 [Infrastructure as Code](https://d1.awsstatic.com/whitepapers/infrastructure-as-code.pdf) brings automation to the provisioning process through tools like [AWS CloudFormation](https://aws.amazon.com/cloudformation/). Rather than relying on manually performed steps, both administrators and developers can instantiate infrastructure using configuration files. Infrastructure as Code treats these configuration files as software code. These files can be used to produce a set of artifacts, namely the compute, storage, network, and application services that comprise an operating environment. Infrastructure as Code eliminates configuration drift through automation, thereby increasing the speed and agility of infrastructure deployments.

 [AWS Tagging and Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html) lets you organize your AWS landscape by applying tags at different levels of granularity. Tags allow you to label, collect, and organize resources and components within services.

 The [Tag Editor](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html) lets you manage tags across services and AWS Regions. Using this approach, you can globally manage all the application, business, data, and technology components of your target landscape.

 A [Resource Group](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted.html) is a collection of resources that share one or more tags. It can be used to create an enterprise architecture view of your IT landscape, consolidating AWS resources into a per-project (that is, the on-going programs that realize your target landscape), per-entity (that is, capabilities, roles, processes), and per-domain (that is, Business, Application, Data, Technology) view.

 [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) is a service that lets you assess, audit, and evaluate the configurations of AWS resources. AWS Config continuously monitors and records your AWS resource configurations and lets you automate the evaluation of recorded configurations against desired configurations. With AWS Config, you can review changes in configurations and determine their overall compliance against the configurations specified in your internal guidelines. This enables you to simplify compliance auditing, security analysis, change management, and operational troubleshooting. In addition, AWS provides conformance packs for AWS Config to provide a general-purpose compliance framework designed to enable you to create security, operational or cost-optimization governance checks using managed or custom AWS Config rules and AWS Config remediation actions, including a [conformance pack for 21 CFR 11](https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-FDA-21CFR-Part-11.html).

 You can use AWS CloudFormation, AWS Config, Tagging, and Resource Groups to see exactly what cloud assets your company is using at any moment. These services also make it easier to detect when a rogue server or shadow application appear in your target production landscape.

### Security Management
<a name="security-management"></a>

 AWS has defined a set of best practices for customers who are designing the security infrastructure and configuration for applications running in Amazon Web Services (AWS).

 These [AWS resources](https://aws.amazon.com/architecture/security-identity-compliance/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc) provides security best practices that will help you define your Information Security Management System (ISMS) and build a set of security policies and processes for your organization so you can protect your data and assets in the AWS Cloud.

 These [AWS resources](https://aws.amazon.com/products/security/) also provide an overview of different security topics such as identifying, categorizing and protecting your assets on AWS, managing access to AWS resources using accounts, users and groups and suggesting ways you can secure your data, operating systems, applications and overall infrastructure in the cloud.

 AWS provides you with an [extensive set of tools](https://aws.amazon.com/products/security/) to secure workloads in the cloud.

 If you implement full automation it could negate the need for anyone to have direct access to any environment beyond development. However, if a situation occurs that requires someone to access a production environment, they must explicitly request access, have the access reviewed and approved by the appropriate owner, and upon approval, obtain temporary access with the least privilege needed and only for the duration required. You should then track their activities through logging while they have access. You can refer to this [AWS resource](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) for further information.

### Problem and Incident Management
<a name="problem-and-incident-management"></a>

 With AWS you get access to many tools and features to help you meet your problem and incident management objectives. These capabilities help you establish a configuration and security baseline that meets your objectives for your applications running in the cloud.

 When a deviation from your baseline does occur (such as by a misconfiguration), you may need to respond and investigate. To successfully do so, you must understand the basic concepts of security incident response within your AWS environment, as well as the issues needed to consider to prepare, educate, and train your cloud teams before security issues occur. It is important to know which controls and capabilities you can use, to review topical examples for resolving potential concerns, and to identify remediation methods that can be used to leverage automation and improve response speed.

 Because security incident response can be a complex topic, we encourage you to start small, develop runbooks, leverage basic capabilities, and create an initial library of incident response mechanisms to iterate from and improve upon. This initial work should include teams that are not involved with security and should include your legal departments, so that they are better able to understand the impact that incident response (IR), and the choices they have made, have on your corporate goals.

 For a comprehensive guide, see the [AWS Security Incident Response Guide](https://d1.awsstatic.com/whitepapers/aws_security_incident_response.pdf).

### Backup, Restore, Archiving
<a name="backup-restore-archiving"></a>

 The ability to back up and restore is required for all validated applications. It is therefore a common capability that can be centralized as part of the regulated landing zone. Backup and restore should not be confused with archiving and retrieval but the two areas can be combined into a centralized capability.

 For a cloud-based backup and restore capability, consider [AWS Backup](https://aws.amazon.com/backup).

 AWS Backup is a fully managed backup service that makes it easy to centralize and automate the backup of data across AWS services. Using AWS Backup, you can centrally configure backup policies and monitor backup activity for AWS resources, such as Amazon EBS volumes, Amazon EC2 instances, Amazon RDS databases, Amazon DynamoDB tables, Amazon EFS file systems, Amazon FSx file systems, and AWS Storage Gateway volumes. AWS Backup automates and consolidates backup tasks previously performed service-by-service, removing the need to create custom scripts and manual processes. With just a few clicks in the AWS Backup console, you can create backup policies that automate backup schedules and retention management. AWS Backup provides a fully managed, policy-based backup solution, simplifying your backup management, enabling you to meet your business and regulatory backup compliance requirements.

### Disaster Recovery
<a name="disaster-recovery"></a>

 In traditional on-premises situations, Disaster Recovery (DR) involves a separate data center located a certain distance from the primary data center. This separate data center only exists in case of a complete disaster impacting the primary data center. Often the infrastructure at the DR site sits idle, or at best hosts pre-production instances of applications thus running the risk of it being out-of-sync with production. With the advent of cloud, DR is now much easier and cheaper.

 The AWS global infrastructure is built around AWS Regions and Availability Zones (AZ). AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

 With AWS Availability Zones, it is very easy to create a multi-AZ architecture capable of withstanding a complete failure of one or more zones. For even more resilience, multiple AWS Regions can be used. With the use of Infrastructure as Code, the infrastructure and applications in a DR Region do not need to run all of the time. In case of a disaster, the entire application stack can be deployed into another Region. The only components that must run all the time are those keeping the data repositories in sync.

 With tooling like [CloudEndure Disaster Recovery](https://aws.amazon.com/cloudendure-disaster-recovery/), you can now automate disaster recovery.

### Performance Monitoring
<a name="performance-monitoring"></a>

 Amazon CloudWatch is a monitoring service for AWS Cloud resources and the applications you run on AWS. You can use CloudWatch to collect and track metrics, collect, and monitor log files, set alarms, and automatically react to changes in customer AWS resources. CloudWatch monitors and logs the behavior of the customer application landscape. CloudWatch can also trigger events based on the behavior of your application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
