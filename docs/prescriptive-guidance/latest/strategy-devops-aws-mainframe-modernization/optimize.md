---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-devops-aws-mainframe-modernization/optimize.html
---

# Optimize
<a name="optimize"></a>

The optimize phase is the commitment to perpetual enhancement and the key to sustaining the benefits of mainframe modernization on AWS. The optimize phase is about continuous improvement of people, process, and technology. This phase represents the ongoing efforts to enhance and refine the modernized mainframe applications hosted on AWS. To ensure the health, security, and efficiency of the application environment, the optimize phase is based on continuous monitoring, including real-time visibility and proactive management.

This phase enables your organization to respond swiftly to emerging issues, maintain compliance with industry regulations, and optimize resource utilization for cost-effectiveness. It promotes a culture of continuous improvement and knowledge sharing within cross-functional teams, helping to ensure that DevOps practices remain aligned with evolving business needs.

## Continuous monitoring for observability and optimization
<a name="monitoring-and-optimization"></a>

Continuous monitoring is the real-time observation and analysis of telemetry data to help optimize system performance. It encompasses alert configuration to notify teams of potential issues. The alerting promotes rapid response. Post-event investigations provide valuable insights to continuously optimize the monitoring process.

Continuous monitoring includes the following areas:
+ **Real-time visibility** – Continuous monitoring provides real-time visibility into the performance and security of applications, so your organization can identify and address issues promptly. Services such as Amazon CloudWatch can help in collecting application logs, creating alarms and dashboards by providing real-time visibility into the status of the application health.
+ **Security and compliance** – Continuous monitoring helps your organization detect and respond to security threats. Rapid detection and response help ensure that that modernized applications remain compliant with industry regulations and security best practices. In a modernized environment, mainframe applications can use AWS services such as Amazon GuardDuty and AWS Security Hub CSPM in tandem to provide nearly continuous visibility, compliance, and threat detection for refactored (re-architected) and replatformed mainframe workloads.
+ **Alerting and notification** – Monitoring solutions send alerts and notifications to relevant teams when predefined thresholds or anomalies are detected. Alerts help teams to rapidly respond to issues. Services such as CloudWatch help to generate alarms for critical events in the application. These alarms can be configured to send notifications by using Amazon Simple Notification Service (Amazon SNS) to necessary stakeholders.
+ **Resource use** – Organizations use monitoring data to analyze resource utilization and make informed decisions about scaling resources up or down as needed to meet application demands. You can use CloudWatch metrics for Amazon Elastic Compute Cloud (Amazon EC2) to determine to  the number of EC2 instances based on a predefined threshold. An example threshold is more than 75 percent of CPU utilization and more than 70 percent of disk utilization.
+ **Log and event management** – Centralized logging and event-management solutions help your organization to maintain visibility into application logs and to track events for troubleshooting and compliance purposes. CloudWatch helps with log management for refactored and replatformed mainframe workloads by aggregating the logs from applications in single log group.
+ **Cost optimization** – Continuous monitoring helps teams to analyze the usage and costs of AWS resources and services. Teams can look for opportunities to reduce unnecessary spending while maintaining performance and functionality. AWS Cost Explorer provides a holistic view of resources used and the corresponding cost of usage by the AWS Mainframe Modernization service. Services such as AWS Compute Optimizer can provide recommendations for optimizing the AWS resource usage and efficiency to achieve more efficient use of resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
