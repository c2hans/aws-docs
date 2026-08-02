---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/principle-5-operational-security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Principle 5: Operational security
<a name="principle-5-operational-security"></a>

****
 The service needs to be operated and managed securely in order to impede, detect, or prevent attacks. Good operational security should not require complex, bureaucratic, time consuming, or expensive processes.

## Section 5.1: Configuration and change management
<a name="section-5.1-configuration-and-change-management"></a>

****
 You should ensure that changes to the system have been properly tested and authorised. Changes should not unexpectedly alter security properties.

 AWS offers its customers several methods to help configure and manage infrastructure deployed on the AWS Cloud. These methods range from AWS managed configuration management services to third-party AWS Partner Network (APN) products.

 There are several best practices to consider when managing infrastructure configuration. First, it is important to understand the types of resources to manage, and their different characteristics that must be accounted for in a configuration management system. For example, the configuration and orchestration of AWS resources (such as security groups, Auto Scaling groups, Elastic Load Balancing load balancers, and so on) is very different from that of operating system and application stack changes.

 It is also important to recognise that manual configuration of distributed systems is time-consuming and error-prone, and can lead to inconsistently-configured systems. Therefore, the ability to automate, monitor, and track configuration changes is a key component of any configuration management solution.

 The services that customers should consider using in particular are:
+  [Service Catalog](https://aws.amazon.com/servicecatalog/) enables customer cloud administrators to make available an approved set of AWS services and associated configurations to be consumed. This is a preventative control to help avoid introducing security vulnerabilities through insecure deployment of services not approved for organisational use by certain stakeholder groups.
+  [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) enables AWS resources to be described in declarative code form known as a template, with an associated development, testing, deployment, and retirement lifecycle, this simplifies the process of creating secure infrastructure by preventing security misconfigurations arising from manual actions, and ensuring consistent, repeatable deployment of initial resources and subsequent updates. This service supports the principle of immutable infrastructure, in which deployed resources are replaced with newer versions rather than updated, which benefits from security reviews built into the template development lifecycle.

 **Applicable risk classes:** All

****
 The Service User should maintain an accurate inventory of the assets which make up the service, along with their configurations and dependencies.

 AWS recommends using the following combination of configuration management tools to maintain an accurate inventory of services:
+  [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) with AWS Config Rules or an AWS Config Partner to provide a detailed, visual, and searchable inventory of AWS resources, configuration history, and resource configuration compliance.
+  [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or a third-party AWS–resource orchestration tool to manage AWS resource provisioning, update, and termination.
+  [AWS OpsWorks](https://docs.aws.amazon.com/opsworks/latest/userguide/welcome.html) or a third-party server configuration management tool to manage operating system and application stack configuration changes (preferably abiding by the principle of infrastructure as code).

 For more detailed guidance and resources, see [Infrastructure Configuration Management](https://d1.awsstatic.com/aws-answers/AWS_Infrastructure_Configuration_Management.pdf) on the AWS Answers site.

****
 The Service User should ensure changes to the service are assessed for potential security impact, and the implementation of changes are managed and tracked through to completion.

 Customer can conduct a security impact assessment in much the same way as for existing infrastructure. With AWS though, the application of automation should reduce the time and effort to conduct this assessment.

 There are two elements to this assessment:
+  The security impact of changes to the AWS environment, including the AWS services and resources used in the solution. AWS recommends adopting a Security by Design (SbD) approach to operating the environment, as described in the [https://d0.awsstatic.com/whitepapers/compliance/Intro_to_Security_by_Design.pdf](https://d0.awsstatic.com/whitepapers/compliance/Intro_to_Security_by_Design.pdf) whitepaper. The result is an automated environment enabling assurance, governance, security, and compliance capabilities. This provides a reliable implementation of what was previously written in policies, standards and regulations. It minimises the effort involved in carrying out a security impact assessment, as the majority of resources will be deployed with a known, and minimised, security impact.
+  The security of hosts and applications, such as operating systems, databases, and applications. The impact assessments already used today can be applied when using AWS. AWS also provides [Amazon Inspector](https://aws.amazon.com/inspector/), which is an automated security assessment service that helps improve the security and compliance of applications deployed on Amazon EC2.

   Amazon Inspector automatically assesses applications for vulnerabilities or deviations from best practices. After performing an assessment, it produces a detailed list of security findings prioritised by level of severity. These findings can be reviewed directly or as part of detailed assessment reports which are available via the Amazon Inspector console or API. This makes it easy to build these into a DevOps process, decentralising and automating vulnerability assessments, and empowering development and operations teams to make security assessment an integral part of the deployment process.

## Section 5.2: Vulnerability management
<a name="section-5.2-vulnerability-management"></a>

 *You should identify and mitigate security issues in constituent components.*

 **Applicable risk classes:** All

****
 The Service User should undertake patching or vulnerability management for the guest operating system and application components, within the NCSC best practice timescales set out below:
 a. ‘Critical’ patches should be deployed within 24 hours.
 b. ‘Important’ patches should be deployed within 2 weeks of a patch becoming available.
 c. ‘Other’ patches deployed within 8 weeks of a patch becoming available.

 AWS provides facilities to patch the operating systems that customers run in their AWS environments. Where applicable, AWS will also undertake patch management on the customer’s behalf for certain managed services.

 [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html) automates the process of patching managed EC2 instances with security-related updates. Patches for non-security updates can also be deployed to Linux-based instances. Fleets of EC2 instances and on-premises servers and virtual machines (VMs) can also be patched using this service. Applicable operating systems include supported versions of Microsoft Windows, Ubuntu Server, Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), Amazon Linux, and Amazon Linux 2. Instances can be scanned to establish which patches are missing, if any, and optionally, all missing patches can then be automatically installed.

 While customer-operated applications deployed to AWS can be patched and updated using a conventional manual approach, there are additional benefits to automation, such as the ability to perform blue/green deployments for greater application availability during patching as well as upgrades. Customers can choose to host patching solutions provided by AWS Partners and third-party solutions with which they are already familiar. Some customers establish repositories within their AWS environment that automatically fetch patches from software vendors; this limits the number of internal instances (and other servers) connecting to external repositories.

 Note that for both EC2 and application-patching AWS recommends testing the patches in a separate test environment, and also putting mechanisms in place to roll back patches in the event that they cause issues with the system being updated.

 The recommended approach from AWS to patching for maximum security risk control is to make use of the principle of immutable infrastructure: namely, that instead of patching running EC2 instances, customers should launch replacement instances from Amazon Machine Images (AMIs) to which the required patches have already been deployed, and destroy the unpatched ones. This minimised the probability of “configuration drift” and deviation from desired patch status.

 AWS offers a substantial and growing number of services for which the line of security responsibility with the customer is drawn at a higher level than the hypervisor. [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) is one example of such a service. AWS performs automated patching of the database engine, underlying operating system, and certain plugins. Customers configure a time window in which the RDS service can take the database offline, perform the update, then bring it back online. This reduces the required customer effort for managing the security of their databases.

 Another example is [AWS Lambda](https://aws.amazon.com/lambda/), a service that enables customers to deploy very granular application functions comprising microservices architectures or other application capabilities to the cloud: not only does AWS carry out regular automated patching of the operating system, but also the containers in which the functions run and the language runtimes they use.

 In this case, customer patching responsibility covers any third-party libraries used in the code for their Lambda functions. An additional security benefit of using Lambda to run code is that functions have a finite maximum lifetime (15 minutes at the time of writing), so even if a function is compromised during run, the window of opportunity for an attacker to exploit this is greatly reduced.

 **Applicable risk classes:** III-V

****
 The Service User should undertake regular (minimum yearly) penetration testing.
 The Service User should ensure that the penetration test is well scoped such that ‘security vulnerabilities in the Operating system and components above’ are fully tested.

 Penetration testing can be performed as it would on systems deployed to non-AWS environments, such as customers’ own premises. Note, however that the [AWS Acceptable Use Policy](https://aws.amazon.com/aup/) describes permitted and prohibited behaviour on AWS and includes descriptions of prohibited security violations and network abuse. Because penetration testing and other simulated events are frequently indistinguishable from these activities, AWS has established a [security testing policy](https://aws.amazon.com/security/penetration-testing/) that customers need to abide by when conducting penetration tests and vulnerability scans to or originating from the AWS environment.

## Section 5.3: Protective monitoring
<a name="section-5.3-protective-monitoring"></a>

 *You should put measures in place to detect attacks and unauthorised activity on the service.*

 **Applicable risk classes:** III-V

****
 The Service User should put in place monitoring solutions to identify attacks against their applications or software.

 AWS provides services that provide monitoring of resources deployed to customer AWS environments and service usage to help identify attacks against applications. Attacks may come from either external or internal sources and may be malicious or accidental.

 Attacks from external sources come in forms such as Distributed Denial of Service (DDoS). AWS provides flexible infrastructure and services that help customers implement strong DDoS mitigations and create highly available application architectures that follow [AWS Best Practices for DDoS Resiliency](https://d1.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf). These include services such as [Amazon Route 53](https://aws.amazon.com/route53/), [Amazon CloudFront](https://aws.amazon.com/cloudfront/), [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/), and [AWS WAF](https://aws.amazon.com/waf/) to control and absorb traffic, and deflect unwanted requests. These services integrate with [AWS Shield](https://aws.amazon.com/shield/), a managed DDoS protection service that provides always-on detection and automatic inline mitigations to safeguard web applications running on AWS. For more details, see the [https://aws.amazon.com/answers/networking/aws-ddos-attack-mitigation/](https://aws.amazon.com/answers/networking/aws-ddos-attack-mitigation/) whitepaper.

 AWS also provides attack identification with [Amazon GuardDuty](https://aws.amazon.com/guardduty/), a managed threat detection service that continuously monitors for malicious or unauthorised behavior to help customers protect their AWS accounts and workloads. It monitors for activity such as unusual API calls or potentially unauthorised deployments that indicate a possible account compromise. GuardDuty also detects potentially compromised instances or reconnaissance by attackers.

 Customer can also deploy some or all of their existing attack detection tools into AWS or purchase new solutions from the AWS Marketplace or Amazon Partner Network.

 An advantage of the cloud is that if an attack is detected, automated action can be taken to reduce or mitigate the impact. For example, if a virus is detected on an EC2 instance, response code can be automatically run that quarantines the affected instance for forensic analysis and sets up a clean one in its place to ensure continuity of operations.

## Section 5.4: Incident management
<a name="section-5.4-incident-management"></a>

 *Ensure you can respond to incidents and recover a secure, available service.*

 **Applicable risk classes:** III-V

****
 The Service User should put in place monitoring solutions to identify attacks against their applications or software.

 See [Section 5.3: Protective monitoring](#section-5.3-protective-monitoring).

 **Applicable risk classes:** III-V

****
 The Service User should have an incident management process to rapidly respond to attacks.

 An incident is an unplanned interruption to an IT service or reduction in the quality of an IT service. Through tools such as [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), [AWS Config](https://aws.amazon.com/config/), and [AWS Config Rules](https://aws.amazon.com/blogs/aws/aws-config-rules-dynamic-compliance-checking-for-cloud-resources/), customers can track, monitor, analyse, and audit events. Customers may also want to bring existing, application-specific event monitoring tools already familiar to them. Finally, AWS provides a [Service Health Dashboard](https://status.aws.amazon.com/) that allows customers to subscribe to an RSS feed and be notified of interruptions to each individual service.

 If these tools identify an event, which is analysed and qualified as an incident, that “qualifying event” will raise an incident and trigger the incident management process and any appropriate response actions necessary to mitigate the incident. These qualifying events will need to be integrated into existing incident management processes.

 Should customers detect a vulnerability or have a security concern regarding AWS, they may want to report it as part of their incident management process. For details, see [Vulnerability Reporting](https://aws.amazon.com/security/vulnerability-reporting/).

 For further guidance, see [Building a cloud-specific incident response plan](https://aws.amazon.com/blogs/publicsector/building-a-cloud-specific-incident-response-plan/) on the AWS Government, Education, and Nonprofits Blog.
