---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/operationalize.html
---

# Operationalize: Preparing your organization for a mature cloud security posture
<a name="operationalize"></a>

In order to move forward with the process of deploying operational loads into the cloud, it is important to focus on the alignment of people, process, and technology. This is particularly crucial in the cloud environment because processes and skills likely differ from on-premises operations. In this section, you use a framework to align your people, processes, and technology, and then you confirm that the framework has helped you achieve your expected outcomes.

## AWS Cloud Adoption Framework
<a name="aws-cloud-adoption-framework"></a>

The [AWS Cloud Adoption Framework (AWS CAF)](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html) helps you accelerate your business outcomes through innovative use of AWS services and features. AWS CAF identifies six specific organizational perspectives that underpin successful cloud transformations: Business, People, Governance, Platform, Security, and Operations. Each perspective contains capabilities that can improve your cloud readiness and help you accelerate your cloud transformation journey.

The following image shows the six perspectives in the AWS CAF and the capabilities in each perspective. For more information, see [Foundational capabilities](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html) in *An Overview of the AWS Cloud Adoption Framework*.

![The six perspectives in AWS CAF and the perspectives in each.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/images/guide-img/2162f372-44e6-4f4b-80cc-427f9fca7a33/images/dc28632c-7a07-422f-a3ad-07f2811f64ac.png)

## Expected outcomes
<a name="expected-outcomes"></a>

When you use the AWS CAF to align your people, processes, and technology, you can expect to achieve the following outcomes:
+ **DevSecOps pipeline and process** – Implementing a DevOps pipeline with integrated security tools can help you more securely deploy infrastructure as a code (IaC). You can implement code-scanning and security checks in the pipeline process, such as [cfn\_nag](https://github.com/cdklabs/cdk-nag#readme) (GitHub), which is an open source static code analyzer.
+ **Tagging and asset management** – Tags can help you more efficiently and consistently manage resources in the cloud. For more information, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html). It's important to develop a dynamic asset management strategy that can adapt to the constantly changing nature of the cloud. [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) helps you assign tags so that you can quickly search, manage, and identify your resources.
+ **Monitoring and detective integration** – It is crucial to establish a method for sending alerts from the cloud to on-premises security operations centers (SOCs) and security information and event management (SIEM) systems. [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) is a continuous security monitoring service that analyzes and processes logs to identify unexpected and potentially unauthorized activity in your AWS environment. It also integrates with many third-party tools.
+ **Cloud incident response plan and program** – It is important to make sure that the personnel responsible for handling the cloud alerts are familiar with the process of ingesting those alerts and know how to respond to cloud alerts, as compared to on-premises alerts. To improve incident response capabilities, train personnel to use Amazon Detective for log analysis. [Amazon Detective](https://docs.aws.amazon.com/detective/latest/adminguide/what-is-detective.html) helps you analyze, investigate, and identify the root cause of security findings or suspicious activities. Amazon Detective should be part of an incident response plan.
+ **Cloud vulnerability management** – The process of managing vulnerabilities in the cloud differs from on-premises environments. In addition to traditional vulnerability management, you also must assess the infrastructure code layer. [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) is an automated vulnerability management service that continually evaluates your resources for vulnerabilities and unintended network exposure.
+ **Cloud posture management** – Cloud posture management, as described in the [Assess](assess.md) section, is an important aspect of cloud security. You can use AWS Security Hub CSPM to automate security best practice checks and evaluate your overall cloud posture across all of your AWS accounts.
+ **Cloud security training **– It is essential to provide appropriate training to employees so they become proficient in cloud security. This includes providing access to resources and allocating time for employees to acquire the necessary knowledge and skills. AWS provides many training resources to upskill and educate, such as [AWS Skill Builder](https://skillbuilder.aws/).
