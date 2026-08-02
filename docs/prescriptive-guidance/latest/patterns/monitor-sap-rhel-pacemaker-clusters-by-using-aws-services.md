---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-sap-rhel-pacemaker-clusters-by-using-aws-services.html
---

# Monitor SAP RHEL Pacemaker clusters by using AWS services
<a name="monitor-sap-rhel-pacemaker-clusters-by-using-aws-services"></a>

*Harsh Thoria, Randy Germann, and RAVEENDRA Voore, Amazon Web Services*

## Summary
<a name="monitor-sap-rhel-pacemaker-clusters-by-using-aws-services-summary"></a>

This pattern outlines the steps for monitoring and configuring alerts for a Red Hat Enterprise Linux (RHEL) Pacemaker cluster for SAP applications and SAP HANA database services by using Amazon CloudWatch and Amazon Simple Notification Service (Amazon SNS).

The configuration enables you to monitor SAP SCS or ASCS, Enqueue Replication Server (ERS), and SAP HANA cluster resources when they are in a "stopped" state with the help of CloudWatch log streams, metric filters, and alarms. Amazon SNS sends an email to the infrastructure or SAP Basis team about the stopped cluster status.

You can create the AWS resources for this pattern by using AWS CloudFormation scripts or the AWS service consoles. This pattern assumes that you're using the consoles; it doesn't provide CloudFormation scripts or cover infrastructure deployment for CloudWatch and Amazon SNS. Pacemaker commands are used to set the cluster alerting configuration.

## Prerequisites and limitations
<a name="monitor-sap-rhel-pacemaker-clusters-by-using-aws-services-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ Amazon SNS set up to send email or mobile notifications.
+ An SAP ASCS/ERS for ABAP or SCS/ERS for Java, and SAP HANA Database RHEL Pacemaker cluster. For instructions, see the following:
  + [SAP HANA cluster setup](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-on-aws-manual-deployment-of-sap-hana-on-aws-with-high-availability-clusters.html)
  + [SAP Netweaver ABAP/Java cluster setup](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sap-netweaver-ha-configuration-guide.html)

**Limitations**
+ This solution currently works for RHEL version 7.3 and later Pacemaker-based clusters. It hasn’t been tested on SUSE operating systems.

**Product versions**
+ RHEL 7.3 and later

## Architecture
<a name="monitor-sap-rhel-pacemaker-clusters-by-using-aws-services-architecture"></a>

**Target technology stack **
+ RHEL Pacemaker alert event-driven agent
+ Amazon Elastic Compute Cloud (Amazon EC2)
+ CloudWatch alarm
+ CloudWatch log group and metric filter
+ Amazon SNS

**Target architecture **

The following diagram illustrates the components and workflows for this solution.

![Architecture for monitoring SAP RHEL Pacemaker clusters](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/ca4d282e-eadd-43fd-8506-3dbeb43e4db6/images/bfc96678-1fd3-47b6-8f09-bf7cf7c4a92c.png)

**Automation and scale**
+ You can automate the creation of AWS resources by using CloudFormation scripts. You can also use additional metric filters to scale and cover multiple clusters.

## Tools
<a name="monitor-sap-rhel-pacemaker-clusters-by-using-aws-services-tools"></a>

**AWS services**
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+  [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.

**Tools**
+ CloudWatch agent (unified) is a tool that collects system-level metrics, logs, and traces from EC2 instances, and retrieves custom metrics from your applications.
+ Pacemaker alert agent (for RHEL 7.3 and later) is a tool that initiates an action when there's a change, such as when a resource stops or restarts, in a Pacemaker cluster.

## Best practices
<a name="monitor-sap-rhel-pacemaker-clusters-by-using-aws-services-best-practices"></a>
+ For best practices for using SAP workloads on AWS, see the [SAP Lens](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/sap-lens.html) for the AWS Well-Architected Framework.
+ Consider the costs involved in setting up CloudWatch monitoring for SAP HANA clusters. For more information, see the [CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_billing.html).
+ Consider using a pager or ticketing mechanism for Amazon SNS alerts.
+ Always check for RHEL high availability (HA) versions of the RPM package for **pcs**, Pacemaker, and the AWS fencing agent.

## Epics
<a name="monitor-sap-rhel-pacemaker-clusters-by-using-aws-services-epics"></a>

### Set up Amazon SNS
<a name="set-up-sns"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an SNS topic. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-sap-rhel-pacemaker-clusters-by-using-aws-services.html) | AWS administrator |
| Modify the access policy for the SNS topic. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-sap-rhel-pacemaker-clusters-by-using-aws-services.html) | AWS systems administrator |
| Subscribe to the SNS topic. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-sap-rhel-pacemaker-clusters-by-using-aws-services.html)Your web browser displays a confirmation response from Amazon SNS. | AWS systems administrator |

### Confirm the setup of the cluster
<a name="confirm-the-setup-of-the-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Check cluster status. | Use the **pcs status** command to confirm that the resources are online. | SAP Basis administrator |

### Configure Pacemaker alerts
<a name="configure-pacemaker-alerts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the Pacemaker alert agent on the primary cluster instance. | Log in to the EC2 instance in the pimary cluster and run the following commands:<pre>install --mode=0755 /usr/share/pacemaker/alerts/alert_file.sh.sample<br />touch /var/lib/pacemaker/alert_file.sh<br />touch /var/log/pcmk_alert_file.log<br />chown hacluster:haclient /var/log/pcmk_alert_file.log<br />chmod 600 /var/log/pcmk_alert_file.log<br />pcs alert create id=alert_file description="Log events to a file." path=/var/lib/pacemaker/alert_file.sh<br />pcs alert recipient add alert_file id=my-alert_logfile value=/var/log/pcmk_alert_file.log</pre> | SAP Basis administrator |
| Configure the Pacemaker alert agent on the secondary cluster instance. | Log in to the secondary cluster EC2 instance in the secondary cluster and run the following commands:<pre>install --mode=0755 /usr/share/pacemaker/alerts/alert_file.sh.sample<br />touch /var/lib/pacemaker/alert_file.sh<br />touch /var/log/pcmk_alert_file.log<br />chown hacluster:haclient /var/log/pcmk_alert_file.log<br />chmod 600 /var/log/pcmk_alert_file.log</pre> | SAP Basis administrator |
| Confirm that the RHEL alert resource was created. | Use the following command to confirm that the alert resource was created:<pre>pcs alert</pre><br />The output of the command will look like this:<pre>[root@xxxxxxx ~]# pcs alert <br />Alerts:<br /> Alert: alert_file (path=/var/lib/pacemaker/alert_file.sh)<br />  Description: Log events to a file.<br />  Recipients:<br />   Recipient: my-alert_logfile (value=/var/log/pcmk_alert_file.log)</pre> | SAP Basis administrator |

### Configure the CloudWatch agent
<a name="configure-the-cw-agent"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the CloudWatch agent. | There are several ways to install the CloudWatch agent on an EC2 instance. To use the command line:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-sap-rhel-pacemaker-clusters-by-using-aws-services.html)<br />For more information, see the [CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html). | AWS systems administrator |
| Attach an IAM role to the EC2 instance. | To enable the CloudWatch agent to send data from the instances, you must attach the IAM **CloudWatchAgentServerRole** role to each  instance. Or, you can add a policy for the CloudWatch agent to your existing IAM role. For more information, see the [CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent-commandline.html). | AWS administrator |
| Configure the CloudWatch agent to monitor the Pacemaker alert agent log file on the primary cluster instance. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-sap-rhel-pacemaker-clusters-by-using-aws-services.html) | AWS administrator |
| Start the CloudWatch agent on the primary and secondary cluster instances. | To start the agent, run the following command on the EC2 instances in the primary and secondary clusters:<pre>sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m<br />ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json</pre> | AWS administrator |

### Set up CloudWatch resources
<a name="set-up-cw-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up CloudWatch log groups. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-sap-rhel-pacemaker-clusters-by-using-aws-services.html)The CloudWatch agent will transfer the Pacemaker alert file to the CloudWatch log group as a log stream. | AWS administrator |
| Set up CloudWatch metric filters. | Metric filters help you search for a pattern such as `stop <cluster-resource-name>` in the CloudWatch log streams. When this pattern is identified, the metric filter updates a custom metric.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-sap-rhel-pacemaker-clusters-by-using-aws-services.html)<br />When the metric filter identifies the pattern in step 4, it updates the value of the CloudWatch custom metric `sapcluster_abc` to **1**.<br />The CloudWatch alarm `SAP-Cluster-QA1-ABC` monitors the metric `sapcluster_abc` and sends out an SNS notification when the value of the metric changes to **1**. This indicates that the cluster resource has stopped and action needs to be taken. | AWS administrator, SAP Basis administrator |
| Set up a CloudWatch metric alarm for the SAP ASCS/SCS and ERS metric. | To create an alarm based on a single metric:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-sap-rhel-pacemaker-clusters-by-using-aws-services.html) | AWS administrator |
| Set up a CloudWatch metric alarm for the SAP HANA metric. | Repeat the steps for setting up a CloudWatch metric alarm from the previous task, with these changes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-sap-rhel-pacemaker-clusters-by-using-aws-services.html) | AWS administrator |

## Related resources
<a name="monitor-sap-rhel-pacemaker-clusters-by-using-aws-services-resources"></a>
+ [Triggering Scripts for Cluster Events](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/high_availability_add-on_reference/index#ch-alertscripts-HAAR) (RHEL documentation)
+ [Create the CloudWatch agent configuration file with the wizard ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.html)(CloudWatch documentation)
+ [Installing and running the CloudWatch agent on your servers ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-commandline-fleet.html)(CloudWatch documentation)
+ [Create a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) (CloudWatch documentation)
+ [Manual deployment of SAP HANA on AWS with high availability clusters](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-on-aws-manual-deployment-of-sap-hana-on-aws-with-high-availability-clusters.html) (SAP documentation on the AWS website)
+ [SAP NetWeaver guides ](https://docs.aws.amazon.com/sap/latest/sap-netweaver/welcome.html)(SAP documentation on the AWS website)

## Attachments
<a name="attachments-ca4d282e-eadd-43fd-8506-3dbeb43e4db6"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/ca4d282e-eadd-43fd-8506-3dbeb43e4db6/attachments/attachment.zip)
