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

![Architecture for monitoring SAP RHEL Pacemaker clusters](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/ca4d282e-eadd-43fd-8506-3dbeb43e4db6/images/bfc96678-1fd3-47b6-8f09-bf7cf7c4a92c.png)

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
| Create an SNS topic. | 1. Sign in to the AWS Management Console and open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).<br />2. On the Amazon SNS dashboard, under **Common actions**, choose **Create Topic**. <br />3. In the **Create new topic** dialog box, for **Type**, choose **Standard**.<br />4. For **Topic name**, enter a name for the topic (for example, `my-topic`).<br />5. Choose **Create topic**.<br />This creates an SNS topic with a resource policy that lets you publish notifications.<br />6. Copy the **Topic ARN** (for example, `arn:aws:sns:us-east-1:111122223333:my-topic`). You will use this ARN in a later step. | AWS administrator |
| Modify the access policy for the SNS topic. | 1. On the Amazon SNS console, in the navigation pane, choose **Topics**, and then choose the topic you created. <br />2. Choose **Edit** and go to the **Access policy** section.<br />3. Make sure that the access policy includes CloudWatch as one of the service principals that are allowed to publish to this topic. For example:<pre>   { <br />      "Sid": "Allow AWS CloudWatch to Publish to this SNS topic",<br />      "Effect": "Allow",<br />      "Principal": {<br />        "Service": [<br />          "cloudwatch.amazonaws.com"<br />        ]<br />      },<br />      "Action": "SNS:Publish",<br />      "Resource": "arn:aws:sns:us-east-1:111122223333:my-topic"<br />    }</pre><br />4. Choose **Save changes**. | AWS systems administrator |
| Subscribe to the SNS topic. | 1. On the Amazon SNS console, in the navigation pane, choose **Subscriptions**, **Create subscription**.<br />2. For **Topic ARN**, paste the ARN that you created in the first task.<br />3. For **Protocol**, choose **Email**.<br />4. For **Endpoint**, enter an email address for the person or team that is responsible for the SAP Pacemaker cluster and should receive notifications. For example, this can be the email address for the SAP Basis or infrastructure team's distribution list.<br />5. Choose **Create subscription**.<br />6. From your email application, open the message from AWS Notifications and confirm your subscription.Your web browser displays a confirmation response from Amazon SNS. | AWS systems administrator |

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
| Install the CloudWatch agent. | There are several ways to install the CloudWatch agent on an EC2 instance. To use the command line:1. Download the CloudWatch agent package: <pre>wget https://s3.<region>.amazonaws.com/amazoncloudwatch-agent-region/redhat/amd64/latest/amazon-cloudwatch-agent.rpm</pre><br />where `<region>` is the AWS Region where the EC2 instance is located (for example, `us-west-2`).<br />2. Optional) Verify the package signature. For instructions, see [Verifying the signature of the CloudWatch agent package](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/verify-CloudWatch-Agent-Package-Signature.html) in the CloudWatch documentation.<br />3. Install the package on the first instance:<pre>sudo rpm -U ./amazon-cloudwatch-agent.rpm</pre><br />4. Repeat for the secondary instance.<br />For more information, see the [CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html). | AWS systems administrator |
| Attach an IAM role to the EC2 instance. | To enable the CloudWatch agent to send data from the instances, you must attach the IAM **CloudWatchAgentServerRole** role to each  instance. Or, you can add a policy for the CloudWatch agent to your existing IAM role. For more information, see the [CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent-commandline.html). | AWS administrator |
| Configure the CloudWatch agent to monitor the Pacemaker alert agent log file on the primary cluster instance. | 1. Configure the primary cluster instance by running the command:<pre>sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard</pre><br />2. Choose **1** for Linux, and then select the options  for your monitoring strategy.<br />3. For the question **"Do you want to monitor any log files,"** choose **Yes** and provide the path of the Pacemaker log file from the **pcs alert** command. In our case, it is `var/log/pcmk_alert_file.log`.<br />4. Provide the name of the log group and log stream. If you don't specify a log stream, the AWS instance ID is used as the default.<br />5. Repeat steps 1-4 for the secondary cluster instance. | AWS administrator |
| Start the CloudWatch agent on the primary and secondary cluster instances. | To start the agent, run the following command on the EC2 instances in the primary and secondary clusters:<pre>sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m<br />ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json</pre> | AWS administrator |

### Set up CloudWatch resources
<a name="set-up-cw-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up CloudWatch log groups. | 1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/)<br />2. In the navigation pane, choose **Log groups,** **Create log group**.                <br />3. Enter a name for the log group,and then choose **Create log group**.The CloudWatch agent will transfer the Pacemaker alert file to the CloudWatch log group as a log stream. | AWS administrator |
| Set up CloudWatch metric filters. | Metric filters help you search for a pattern such as `stop <cluster-resource-name>` in the CloudWatch log streams. When this pattern is identified, the metric filter updates a custom metric.1. On the CloudWatch console, in the navigation pane, choose **Log groups**.<br />2. Choose the name of the log group you created in the previous task.<br />3. Choose **Actions**, **Create metric filter**.<br />4. For **Filter pattern**, enter the filter pattern to use, such as `stop ABC_scs`, to match the stop event for an SAP SCS cluster resource named `ABC_scs`.<br />For more information, see [Filter pattern syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) in the CloudWatch documentation.<br />5. (Optional) To test your filter pattern, under **Test Pattern**, enter one or more log events to use to test the pattern. Each log event must be specified on a separate line, because line breaks are used to separate log events in the **Log event messages** box.<br />6. Choose **Next**, and then enter a name for the filter.<br />7. Under **Metric details**, for **Metric namespace**, enter a name for the CloudWatch namespace where the metric will be published (for example, `sapcluster_monitoring`). If this namespace doesn't already exist, select **Create new**.<br />8. For **Metric name**, enter a name for the new metric (for example, `sapcluster_<sid>`, where `<sid>` is the SAP system identification name).<br />9. For **Metric value**, enter **1**. <br />Alternatively, you can enter a token such as `$size`. This increments the metric by the value of the number in the `size` field for every log event that contains a `size` field.<br />10. For **Default value**, enter **0**.<br />11. Choose **Create metric filter**.<br />When the metric filter identifies the pattern in step 4, it updates the value of the CloudWatch custom metric `sapcluster_abc` to **1**.<br />The CloudWatch alarm `SAP-Cluster-QA1-ABC` monitors the metric `sapcluster_abc` and sends out an SNS notification when the value of the metric changes to **1**. This indicates that the cluster resource has stopped and action needs to be taken. | AWS administrator, SAP Basis administrator |
| Set up a CloudWatch metric alarm for the SAP ASCS/SCS and ERS metric. | To create an alarm based on a single metric:1. On the CloudWatch console, in the navigation pane, choose **Alarms**, **All alarms**.<br />2. Choose **Create alarm**.<br />3. Choose **Select Metric**.<br />4. Search for the custom metric `sapcluster_monitoring` that was created in the previous task.<br />5. Choose the metric name for SAP SCS (for example, `sapcluster_<abc>`), which was also created in the previous task.<br />6. On the **Graphed metrics** tab, set the following:For **Statistic**, choose **Maximum**.For **Period**, choose **1 minute**.For **Threshold type**, choose **Static** and set the threshold for** **`sapcluster_<sid>`** **to a value that’s greater than or equal to 1.<br />7. Choose **Next**.<br />8. For **Notification**, select the SNS topic you created in the first epic.<br />9. For **Name** and **Description**, provide the alarm name and a brief description, and then choose **Next**.<br />10. Choose **Create Alarm**. | AWS administrator |
| Set up a CloudWatch metric alarm for the SAP HANA metric. | Repeat the steps for setting up a CloudWatch metric alarm from the previous task, with these changes:+ For step 5, choose  the metric name for SAP HANA (for example, `sapcluster_db_<abc>`).<br />+ For step 6, set the threshold for `sapcluster_<sid>`** **to a value that’s greater than  0. | AWS administrator |

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
