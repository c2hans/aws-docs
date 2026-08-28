---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/automations.html
---

# AWS automations for SAP administration and operations
<a name="automations"></a>

Using AWS services and tools, you can choose which AWS automations to implement and customize for your specific requirements. The following are examples of AWS services and tools that you can use to automate SAP administration and operations:
+ Managing access using AWS IAM Identity Center (successor to AWS Single Sign-On)
+ System provisioning using AWS Launch Wizard
+ High availability and disaster recovery using AWS CloudFormation
+ Autoscaling AWS resources to support SAP applications by using AWS Auto Scaling
+ Managing SAP configuration with AWS Config
+ Copying serverless systems using AWS Lambda
+ Monitoring SAP systems with Amazon CloudWatch
+ Analyzing SAP data lakes with AWS Glue
+ Configuring Secure File Transfer Protocol (SFTP) with AWS Transfer Family
+ Starting and stopping SAP systems with AWS Systems Manager
+ Integrating email with Amazon Simple Email Service (Amazon SES)
+ Load balancing with Elastic Load Balancing (ELB)
+ Patching operating systems and SAP with Systems Manager
+ Backing up SAP with AWS Backup
+ Using the SAP HANA hardware and cloud measurement tool (HCMT) and hardware configuration check tool (HWCCT) with Systems Manager
+ Scheduling jobs with AWS Step Functions

The following sections describe some of these example automations in more detail. The SAP Global Specialty Practice team constantly innovates and drives new AWS automation capabilities, so the number of automations will continue to grow.

**See the following detailed examples of automations for SAP:**
+ [Example: Automating system provisioning](system-provisioning.md)
+ [Example: Monitoring SAP application clusters, SAP HANA clusters, and SAP application service](monitoring.md)
+ [Example: Automating SAP serverless refresh](serverless-refresh.md)
+ [Example: Automating startup and shutdown of SAP systems](system-start.md)
+ [Example: Auto scaling SAP applications](auto-scaling.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
