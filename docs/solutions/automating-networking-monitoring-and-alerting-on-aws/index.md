---
source_url: https://docs.aws.amazon.com/solutions/automating-networking-monitoring-and-alerting-on-aws/index.html
---

---
title: 'Guidance for Automating Networking Monitoring and Alerting on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/automating-networking-monitoring-and-alerting-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Automating Networking Monitoring and Alerting on AWS

## Overview

This Guidance demonstrates how to automate the setup of Amazon CloudWatch dashboards for monitoring and alerting network resources on AWS. It uses AWS tagging and API capabilities to efficiently gather the necessary information to configure the dashboards, including the ability to centralize monitoring across your AWS environment. This automated approach helps you save time and effort in establishing comprehensive network visibility while also making the process more adaptable to changes in your AWS infrastructure. There are three architecture diagrams: the first illustrates the high-level automation process of deploying CloudWatch dashboards. The second diagram shows detailed information when configuring monitoring. The last diagram shows the flow of events when a CloudWatch alarm is triggered.

## How it works

### Overview

This architecture diagram illustrates the high-level automation process of deploying Amazon CloudWatch dashboards for network monitoring and alerting. The subsequent slides provide more detailed information on the configuration of monitoring (slide 2) and alerting (slide 3).

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automating-networking-monitoring-and-alerting-on-aws.pdf#page=1)Step 1A group of AWS Cloud resources continuously store related metrics in the Amazon CloudWatch data store.Step 2The user initiates the Guidance Resource Collector script that uses the config file.Step 3The Guidance Resource Collector fetches resources matching the config file from the AWS Resource Groups Tagging API Reference.Step 4The Guidance Resource Collector saves resource data in a JSON file.Step 5The user initiates the AWS Cloud Development Kit (AWS CDK) to synthesize an AWS CloudFormation template. The CloudFormation template is using AWS monitoring best practices.Step 6The user is asked for confirmation to deploy the template. Upon confirmation, the AWS CDK deploys the synthesized template containing CloudWatch dashboards.### Monitoring

This architecture diagram shows how to generate and deploy the "Event Forwarder Stack," which is required for configuring the AWS accounts where the resources being monitored reside. These are the accounts that need to be configured to forward the CloudWatch alarm events to the central "monitoring" account.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automating-networking-monitoring-and-alerting-on-aws.pdf#page=2)Step 1The user runs the `cdk deploy` command to generate the CloudFormation template and deploy the infrastructure within the designated "monitoring" account.Step 2The user records the output of the deployment, which contains the Amazon Resource Names (ARNs) of the central custom Amazon EventBridge event bus and the AWS Lambda function execution role.Step 3The user provides the ARNs obtained from the previous step to generate the CloudFormation template for the "Event Forwarder Stack," which is required for configuring the source accounts.Step 4The user deploys the CloudFormation template for the "Event Forwarder Stack" to the intended source accounts, either individually or across multiple accounts and Regions, using CloudFormation StackSets.### Alerting

This architecture diagram shows the flow of events when a CloudWatch alarm is triggered. The alarm event is forwarded to an Amazon EventBridge event bus and processed by an AWS Lambda function. The ‘view’ and ‘list’ Lambda functions retrieve and render the alarm data in the CloudWatch dashboard.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automating-networking-monitoring-and-alerting-on-aws.pdf#page=3)Step 1An AWS Cloud resource sends a metric that breaches a threshold defined in a CloudWatch alarm.Step 2When the alarm is triggered, CloudWatch emits a "CloudWatch Alarm State Change" event on the EventBridge default bus within the respective account.Step 3An EventBridge Rule on the default bus forwards the event to the central custom EventBridge event bus.Step 4An EventBridge Rule defined within the central event bus dispatches the event to the "Event Handler" Lambda function that analyzes the event.Step 5The "Event Handler" Lambda function assumes an AWS Identity and Access Management (IAM) role that has been deployed by the "Event Forwarder" CloudFormation stack set in the source account. It then queries the monitored resource and the CloudWatch alarm for additional details.Step 6The "Event Handler" Lambda function consolidates the additional details with the event and stores the combined information in an Amazon DynamoDB alarms table.Step 7The CloudWatch dashboard, which includes custom CloudWatch widgets, triggers the execution of two Lambda functions—"View" and "List" —upon each dashboard refresh.Step 8The "View" and "List" Lambda functions retrieve and filter the alarm data, then generate HTML code for rendering within the respective CloudWatch custom widgets.Step 9The "View" and "List" Lambda functions return the HTML code to the CloudWatch widgets, which then render the code, including the relevant metrics, on the CloudWatch user interface.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/networking/automating-networking-monitoring-and-alerting-on-aws.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-automating-network-monitoring-and-alerting-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudWatch, Lambda, DynamoDB, and the AWS Systems Manager Parameter Store are used to automate the deployment and management of this Guidance. Specifically, CloudWatch is used for metrics storage, monitoring, and visualization, while Lambda handles event processing and alarm visualization. DynamoDB stores event data, and the Parameter Store manages metrics and the dashboard configuration. Collectively, these services support the manageability, monitoring, and automation of applications across Regions in a cost-effective manner. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM is used to control access to the resources deployed in this Guidance, with roles and policies scoped to minimum permissions. Lambda functions run with least privilege, and EventBridge has resource-based policies to prevent unauthorized access. These security measures align with AWS best practices, protecting resources and data by limiting access and reducing the risk of unauthorized activities. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The use of serverless Lambda functions, the reliable and scalable capabilities of DynamoDB, and the monitoring and alerting capabilities of CloudWatch enhance the overall reliability of this Guidance. Specifically, CloudWatch enables quick detection and response to issues, while Lambda and DynamoDB store and visualize alarm data to improve monitoring across your environments. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

EventBridge is an AWS managed service that offers near real-time delivery of events to Lambda functions. Lambda is a serverless service that automatically scales in and out to meet the performance needs of the application. DynamoDB is used to enable fast querying of data while maintaining on-demand efficiency. Together, these services enable automated, on-demand performance optimization by connecting components, minimizing manual tasks, and providing observability through CloudWatch. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

DynamoDB offers cost-efficient storage of the data used within this Guidance, achieved through the application of an on-demand charging model. Lambda is billed based on invocations, aligning the costs with the actual usage. CloudWatch is used to effectively monitor and manage the resources. Furthermore, DynamoDB, Lambda, and CloudWatch are serverless services that inherently possess the capability of elasticity, enabling automatic scaling out and scaling in as required. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The DynamoDB serverless architecture facilitates the storage of only event-driven data, thereby conserving the resources required for data storage. Similarly, the serverless architecture of Lambda helps ensures the use of only the necessary compute resources, which are subsequently released upon completion of the tasks, reducing waste and promoting efficient resource utilization. Furthermore, the event monitoring capabilities of CloudWatch can be used to identify potential AWS "resource waste" and further promote efficient resource utilization. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
