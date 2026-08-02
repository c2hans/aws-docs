---
source_url: https://docs.aws.amazon.com/whitepapers/latest/swift-customer-security-controls-framework-2021/detect-anomalous-activity.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Requirement 6 - Detect anomalous activity
<a name="detect-anomalous-activity"></a>

## Malware protection
<a name="malware-protection"></a>

 AWS is responsible for the deployment and management of antivirus and anti-malware solutions on AWS managed services such as Amazon RDS, Amazon ECS, and [AWS Fargate](https://aws.amazon.com/fargate/). Customers inherit the security and compliance for AWS managed operating systems. You are responsible for configuring and running appropriate antivirus software on any applicable EC2 instance in which you have access to and responsibility for the underlying operating system. The [AWS Marketplace](https://aws.amazon.com/marketplace) offers numerous products.

## Software integrity
<a name="software-integrity"></a>

 Software integrity checks are generally embedded in SWIFT software components (AMH, SAA, SAG, SNL). If additional software and components are required to run in the SWIFT secure zone, consider getting a third-party file integrity monitoring tool in the AWS Marketplace.

 The immutable infrastructure mentioned in the [Security updates](reduce-attack-surface-and-vulnerabilities.md#security-updates) section of this document also plays a part in this security control objective. In an immutable infrastructure environment setup, no individuals should be allowed to perform any software changes or modification directly on the live SWIFT system.

## Database integrity
<a name="database-integrity"></a>

 Similar to the software integrity requirement, database integrity checks are enabled for SWIFT software components (AMH, SAA, SAG).

 From the environment perspective, use a dedicated database instance for SWIFT connectivity purposes. The database should be encrypted with KMS keys. You should have designated users and roles for ensuring separation of duty for the database tables and schemas. Use AWS Secrets Manager to store the password for the database user login, and use the password rotation capability to rotate the database password periodically. You can implement detective controls for password checkout from AWS Secrets Manager.

 Regarding database integrity, Amazon RDS creates and saves automated backups of your database (DB) instance during the backup window of your DB instance. Amazon RDS snapshots are automatically encrypted with the same encryption key that was used to encrypt the source Amazon RDS database. For the IAM permission aspect, grant least-privileged IAM policy to authorized roles that are required to perform infrastructure operations on the database instances. For details, refer to [Identity-based policy examples for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_id-based-policy-examples.html).

## Logging and monitoring
<a name="logging-and-monitoring"></a>

 The overall goal is to capture security-related logs, configure alarms for suspicious events, and establish a plan to remediate the incident. Per SWIFT CSP implementation guidelines, enable logging on jump servers, firewall logs, databases, messaging interfaces, and command line history.

 GuardDuty can help you detect unauthorized and unexpected activity in your AWS environment. You can use it to analyze and process data from AWS CloudTrail event logs, VPC Flow Logs, and DNS logs to detect anomalies involving the following AWS resource types:
+  EC2 instances
+  S3 buckets

 From the application and middleware components perspective, this control objective can be covered by configuring logging and monitoring for different services in the SWIFT secure zone.

 Amazon GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts, workloads, and data stored in Amazon S3. It also uses integrated threat intelligence such as known malicious IP addresses, anomaly detection, and machine learning (ML) to identify threats more accurately.

 Logging in SWIFT secure zone by component:
+  **Amazon RDS Oracle** — Alert logs, trace log, audit logs, trace files, listener logs, and Oracle Management Agent logs. Refer to [Oracle database log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.Oracle.html).
+  **Amazon MQ** — General logging and audit logging. Refer to [Configuring ActiveMQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-logging-monitoring-activemq.html#security-logging-monitoring-configure-cloudwatch-troubleshoot) [logs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-logging-monitoring-activemq.html#security-logging-monitoring-configure-cloudwatch-troubleshoot).
+  **AWS Systems Manager Session Manager** — SSM Session Manager Session activity. Refer to [Logging session activity](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-logging.html).
+  **VPC Flow Log** — Capture information about the IP traffic going to and from network interfaces in your VPC. Refer to [Log and View Network Traffic Flows](https://aws.amazon.com/blogs/aws/vpc-flow-logs-log-and-view-network-traffic-flows/).
+  **AWS CloudTrail** — Log account activity-related action across the AWS infrastructure. Refer to [Turning on CloudTrail in Additional Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/turn-on-cloudtrail-in-additional-accounts.html).
+  **SWIFT Application Logs** — AMH, SAA and SAG / SNL logs.

 All logging mechanisms have integration with [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html), which can be used to store, access, and monitor the behavior in the SWIFT secure zone. You can leverage [create metrics from log events using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) to be alerted for suspicious activities. If you want to perform analytics on the logs generated, you can use Amazon [CloudWatch Logs Insights](https://docs.amazonaws.cn/en_us/kinesisanalytics/latest/java/cloudwatch-logs-reading.html), [Amazon Athena](https://aws.amazon.com/athena/), or [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/). You can choose to integrate all AWS logs into your existing security information and event management (SIEM) and log archival solutions.

## Intrusion detection
<a name="intrusion-detection"></a>

 Amazon GuardDuty (described in the [Logging and monitoring](#logging-and-monitoring) section of this document) can be leveraged to help you meet this control objective. This can not only detect anomalies in the networking traffic that is happening in the VPC, but can also detect suspicious activities on the AWS account level.

 [AWS Network Firewall](https://aws.amazon.com/network-firewall/) can also be used to act as a network intrusion prevention system/intrusion detection system (IPS / IDS) within AWS as well as other IPS / IDS offerings from the AWS Marketplace.
