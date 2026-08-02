---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch.html
---

# Monitor Oracle GoldenGate logs by using Amazon CloudWatch
<a name="monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch"></a>

*Chithra Krishnamurthy, Amazon Web Services*

## Summary
<a name="monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch-summary"></a>

Oracle GoldenGate provides real-time replication between Amazon Relational Database Service (Amazon RDS) for Oracle databases, or between Oracle databases hosted on Amazon Elastic Compute Cloud (Amazon EC2). It supports both unidirectional and bidirectional replication.

When you use GoldenGate for replication, monitoring is critical to verify that the GoldenGate process is up and running, to make sure that the source and target databases are in sync.

This pattern explains the steps to implement Amazon CloudWatch monitoring for a GoldenGate error log, and how to set alarms to send notifications for specific events such as `STOP` or `ABEND` so you can take appropriate actions to resume replication quickly.

## Prerequisites and limitations
<a name="monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch-prereqs"></a>

**Prerequisites **
+ GoldenGate installed and configured on an EC2 instance, so you can set up CloudWatch monitoring on those EC2 instances. If you want to monitor GoldenGate across AWS Regions for bidirectional replication, you must install the CloudWatch agent in each EC2 instance where the GoldenGate process is running.

**Limitations **
+ This pattern explains how to monitor the GoldenGate process by using CloudWatch. CloudWatch doesn’t monitor replication lag or data synchronization issues during replication. You must run separate SQL queries to monitor replication lag or data-related errors, as explained in the [GoldenGate documentation](https://docs.oracle.com/en/middleware/goldengate/core/19.1/index.html).

**Product versions**
+ This document is based on the implementation of Oracle GoldenGate 19.1.0.0.4 for Oracle on Linux x86-64. However, this solution is applicable to all major versions of GoldenGate.

## Architecture
<a name="monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch-architecture"></a>

**Target technology stack**
+ GoldenGate binaries for Oracle installed on an EC2 instance
+ Amazon CloudWatch
+ Amazon Simple Notification Service (Amazon SNS)

**Target architecture**

![Target architecture for monitoring GoldenGate logs on AWS](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/973a71d5-b6b3-4a2b-813e-cb4d8fd51ba5/images/1781aa9b-77b3-40c4-bc54-3cb91400899c.png)

## Tools
<a name="monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch-tools"></a>

**AWS services**
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) is a monitoring service that is used in this pattern to monitor GoldenGate error logs.
+ [Amazon SNS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_SetupSNS.html) is a message notification service that is used in this pattern to send email notifications.

**Other tools**
+ [Oracle GoldenGate ](https://docs.oracle.com/en/middleware/goldengate/core/19.1/index.html) is a data replication tool that you can use for Amazon RDS for Oracle databases or Oracle databases that are hosted on Amazon EC2.

**High-level implementation steps**

1. Create an AWS Identity and Access Management (IAM) role for the CloudWatch agent.

1. Attach the IAM role to the EC2 instance where GoldenGate error logs are generated.

1. Install the CloudWatch agent on the EC2 instance.

1. Configure the CloudWatch agent configuration files: `awscli.conf` and `awslogs.conf`.

1. Start the CloudWatch agent.

1. Create metric filters in the log group.

1. Set up Amazon SNS.

1. Create an alarm for the metric filters. Amazon SNS sends email alerts when those filters capture events.

For detailed instructions, see the next section.

## Epics
<a name="monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch-epics"></a>

### Step 1. Create an IAM role for the CloudWatch agent
<a name="step-1-create-an-iam-role-for-the-cloudwatch-agent"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the IAM role. | Access to AWS resources requires permissions, so you create IAM roles to include the permissions necessary for each server to run the CloudWatch agent.<br />To create the IAM role:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch.html) | AWS general |

### Step 2. Attach the IAM role to the GoldenGate EC2 instance
<a name="step-2-attach-the-iam-role-to-the-goldengate-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Attach the IAM role to the EC2 instance where GoldenGate error logs are generated. | The error logs generated by GoldenGate have to be populated to CloudWatch and monitored, so you need to attach the IAM role you created in step 1 to the EC2 instance where GoldenGate is running.<br />To attach an IAM role to an instance:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch.html) | AWS general |

### Steps 3-5. Install and configure the CloudWatch agent on the Goldengate EC2 instance
<a name="steps-3-5-install-and-configure-the-cloudwatch-agent-on-the-goldengate-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the CloudWatch agent on the GoldenGate EC2 instance. | To install the agent, run the command:<pre>sudo yum install -y awslogs</pre> | AWS general |
| Edit the agent configuration files. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch.html) | AWS general |
| Start the CloudWatch agent. | To start the agent, use the following command.<pre>$ sudo service awslogsd start</pre><br />After you start the agent, you can view the log group in the CloudWatch console. The log stream will have the contents of the file. | AWS general |

### Step 6. Create metric filters for the log group
<a name="step-6-create-metric-filters-for-the-log-group"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create metric filters for the keywords ABEND and STOPPED. | When you create metric filters for the log group, whenever the filters are identified in the error log, it starts an alarm and sends an email notification based on the Amazon SNS configuration.<br />To create metric filters:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch.html) | CloudWatch |

### Step 7. Set up Amazon SNS
<a name="step-7-set-up-amazon-sns"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an SNS topic. | In this step, you configure Amazon SNS to create alarms for the metric filters.<br />To create an SNS topic:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch.html) | Amazon SNS |
| Create a subscription. | To create a subscription to the topic:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch.html)<br />Amazon SNS opens your web browser and displays a subscription confirmation with your subscription ID. | Amazon SNS |

### Step 8. Create an alarm to send notifications for the metric filters
<a name="step-8-create-an-alarm-to-send-notifications-for-the-metric-filters"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an alarm for the SNS topic. | To create an alarm based on a log group-metric filter:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch.html)<br />After these steps, whenever these patterns are detected in the GoldenGate error log file (`ggserr.log`) that you are monitoring, you will get an email notification. | CloudWatch |

## Troubleshooting
<a name="monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The log stream from the GoldenGate error log doesn’t flow into CloudWatch. | Check the `/etc/awslogs/awslogs.conf` file to verify the file name, log group name, and the date/time format. You must specify the date/time to match the date format in `ggserror.log`. Otherwise, the log stream won’t flow into CloudWatch. |

## Related resources
<a name="monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch-resources"></a>
+ [Amazon CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ [Collecting metrics and logs with the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
+ [Amazon SNS documentation](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
