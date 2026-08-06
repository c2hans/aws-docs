---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/view-aws-network-firewall-logs-and-metrics-by-using-splunk.html
---

# View AWS Network Firewall logs and metrics by using Splunk
<a name="view-aws-network-firewall-logs-and-metrics-by-using-splunk"></a>

*Ivo Pinto, Amazon Web Services*

## Summary
<a name="view-aws-network-firewall-logs-and-metrics-by-using-splunk-summary"></a>

Many organizations use [Splunk Enterprise](https://www.splunk.com/en_us/products/splunk-enterprise.html) as a centralized aggregation and visualization tool for logs and metrics from different sources. This pattern helps you configure Splunk to fetch [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) logs and metrics from [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) by using the Splunk Add-On for AWS.

To achieve this, you create a read-only AWS Identity and Access Management (IAM) role. Splunk Add-On for AWS uses this role to access CloudWatch. You configure the Splunk Add-On for AWS to fetch metrics and logs from CloudWatch. Finally, you create visualizations in Splunk from the retrieved log data and metrics.

## Prerequisites and limitations
<a name="view-aws-network-firewall-logs-and-metrics-by-using-splunk-prereqs"></a>

**Prerequisites**
+ A [Splunk](https://www.splunk.com/) account
+ A Splunk Enterprise instance, version 8.2.2 or later
+ An active AWS account
+ Network Firewall, [set up](https://docs.aws.amazon.com/network-firewall/latest/developerguide/getting-started.html) and [configured](https://docs.aws.amazon.com/network-firewall/latest/developerguide/logging-cw-logs.html) to send logs to CloudWatch Logs

**Limitations**
+ Splunk Enterprise must be deployed as a cluster of Amazon Elastic Compute Cloud (Amazon EC2) instances in the AWS Cloud.
+ Collecting data by using an automatically discovered IAM role for Amazon EC2 is not supported in the AWS China Regions.

## Architecture
<a name="view-aws-network-firewall-logs-and-metrics-by-using-splunk-architecture"></a>

![AWS Network Firewall and Splunk logging architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c6ce254a-841f-4bed-8f9f-b35e99f22e56/images/3dd420e9-70af-4a42-b24d-c54872c55e0b.png)

The diagram illustrates the following:

1. Network Firewall publishes logs to CloudWatch Logs.

1. Splunk Enterprise retrieves metrics and logs from CloudWatch.

To populate example metrics and logs in this architecture, a workload generates traffic that passes through the Network Firewall endpoint to go to the internet. This is achieved by the use of [route tables](https://docs.aws.amazon.com/network-firewall/latest/developerguide/vpc-config.html#vpc-config-route-tables). Although this pattern uses a single Amazon EC2 instance as the workload, this pattern can apply to any architecture as long as Network Firewall is configured to send logs to CloudWatch Logs.

This architecture also uses a Splunk Enterprise instance in another virtual private cloud (VPC). However, the Splunk instance can be in another location, such as in the same VPC as the workload, as long as it can reach the CloudWatch APIs.

## Tools
<a name="view-aws-network-firewall-logs-and-metrics-by-using-splunk-tools"></a>

**AWS services**
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) is a stateful, managed, network firewall and intrusion detection and prevention service for VPCs in the AWS Cloud.

**Other tools**
+ [Splunk](https://www.splunk.com/) helps you monitor, visualize, and analyze log data.

## Epics
<a name="view-aws-network-firewall-logs-and-metrics-by-using-splunk-epics"></a>

### Create an IAM role
<a name="create-an-iam-role"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the IAM policy. | Follow the instructions in [Creating policies using the JSON editor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-json-editor) to create the IAM policy that grants read-only access to the CloudWatch Logs data and CloudWatch metrics. Paste the following policy into the JSON editor.<pre>{<br />    "Statement": [<br />        {<br />            "Action": [<br />                "cloudwatch:List*",<br />                "cloudwatch:Get*",<br />                "network-firewall:List*",<br />                "logs:Describe*",<br />                "logs:Get*",<br />                "logs:List*",<br />                "logs:StartQuery",<br />                "logs:StopQuery",<br />                "logs:TestMetricFilter",<br />                "logs:FilterLogEvents",<br />                "network-firewall:Describe*"<br />            ],<br />            "Effect": "Allow",<br />            "Resource": "*"<br />        }<br />    ],<br />    "Version": "2012-10-17"<br />}</pre> | AWS administrator |
| Create a new IAM role. | Follow the instructions in [Creating a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) to create the IAM role that the Splunk Add-On for AWS uses to access CloudWatch. For **Permissions policies**, choose the policy that you created previously. | AWS administrator |
| Assign the IAM role to the EC2 instances in the Splunk cluster. | 1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/]().<br />2. In the navigation pane, choose **Instances**.<br />3. Select the EC2 instances in the Splunk cluster.<br />4. Choose **Actions**, **Security**, and then **Modify IAM role**.<br />5. Select the IAM role that you created previously, and then choose **Save**. | AWS administrator |

### Install the Splunk Add-On for AWS
<a name="install-the-splunk-add-on-for-aws"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the add-on. | 1. In the Splunk dashboard, navigate to **Splunk Apps**.<br />2. Search for **Splunk Add-on for Amazon Web Services**.<br />3. Choose **Install**.<br />4. Provide your Splunk credentials. | Splunk administrator |
| Configure the AWS credentials. | 1. In the Splunk dashboard, navigate to **Splunk Add-on for AWS**.<br />2. Choose **Configuration**.<br />3. In the **Autodiscovered IAM Role** column, select the IAM role that you created previously.For more information, see [Find an IAM role within your Splunk platform instance](https://splunk.github.io/splunk-add-on-for-amazon-web-services/#Find_an_IAM_role_within_your_Splunk_platform_instance) in the Splunk documentation. | Splunk administrator |

### Configure Splunk access to CloudWatch
<a name="configure-splunk-access-to-cloudwatch"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the retrieval of Network Firewall logs from CloudWatch Logs. | 1. In the Splunk dashboard, navigate to **Splunk Add-on for AWS**.<br />2. Choose **Input**.<br />3. Choose **Create New Input**.<br />4. In the list, choose **Custom Data Type**, and then choose **CloudWatch Logs**.<br />5. Provide the **Name**, **AWS Account**, **AWS Region**, and **Log Group **for your Network Firewall logs.<br />6. Choose **Save**.By default, Splunk fetches the log data every 10 minutes. This is a configurable parameter under **Advanced Settings**. For more information, see [Configure a CloudWatch Logs input using Splunk Web](https://splunk.github.io/splunk-add-on-for-amazon-web-services/#Configure_a_CloudWatch_Logs_input_using_Splunk_Web) in the Splunk documentation. | Splunk administrator |
| Configure the retrieval of Network Firewall metrics from CloudWatch. | 1. In the Splunk dashboard, navigate to **Splunk Add-on for AWS**.<br />2. Choose **Input**.<br />3. Choose **Create New Input**.<br />4. In the list, choose **CloudWatch**.<br />5. Provide the **Name**, **AWS Account**, and **AWS Region **for your Network Firewall metrics.<br />6. Next to **Metric Configuration**, choose **Edit in advanced mode**.<br />7. (Optional) Delete all preconfigured namespaces. <br />8. Choose **Add Namespace**, and then name it **AWS/NetworkFirewall**.<br />9. In **Dimension Value**, add the following.<pre>[{"AvailabilityZone":[".*"],"Engine":[".*"],"FirewallName":[".*"]}]</pre><br />10. For **Metrics**, choose **All**.<br />11. For **Metric Statistics**, choose **Sum**.<br />12. Choose **OK**.<br />13. Choose **Save**.By default, Splunk fetches the metric data every 5 minutes. This is a configurable parameter under **Advanced Settings**. For more information, see [Configure a CloudWatch input using Splunk Web](https://splunk.github.io/splunk-add-on-for-amazon-web-services/#Configure_a_CloudWatch_input_using_Splunk_Web) in the Splunk documentation. | Splunk administrator |

### Create Splunk visualizations by using queries
<a name="create-splunk-visualizations-by-using-queries"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| View the top source IP addresses. | 1. In the Splunk dashboard, navigate to **Search & Reporting**.<br />2. In the **enter search here **box, enter the following.<pre>sourcetype="aws:cloudwatchlogs" | top event.src_ip</pre><br />This query displays a table of the source IP addresses with the most traffic, in descending order.<br />3. For a graphical representation, choose **Visualization**. | Splunk administrator |
| View packet statistics. | 1. In the Splunk dashboard, navigate to **Search & Reporting**.<br />2. In the **enter search here **box, enter the following.<pre>sourcetype="aws:cloudwatch"| timechart sum(Sum) by metric_name</pre><br />This query displays a table of the metrics `DroppedPackets`, `PassedPackets`, and `ReceivedPackets` per minute.<br />3. For a graphical representation, choose **Visualization**. | Splunk administrator |
| View the most-used source ports. | 1. In the Splunk dashboard, navigate to **Search & Reporting**.<br />2. In the **enter search here **box, enter the following.<pre>sourcetype="aws:cloudwatchlogs" | top event.dest_port</pre><br />This query displays a table of the source ports with the most traffic, in descending order.<br />3. For a graphical representation, choose **Visualization**. | Splunk administrator |

## Related resources
<a name="view-aws-network-firewall-logs-and-metrics-by-using-splunk-resources"></a>

**AWS documentation**
+ [Creating a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) (IAM documentation)
+ [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-start) (IAM documentation)
+ [Logging and monitoring in AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/logging-monitoring.html) (Network Firewall documentation)
+ [Route table configurations for AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/route-tables.html) (Network Firewall documentation)

**AWS blog posts**
+ [AWS Network Firewall deployment models](https://aws.amazon.com/pt/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/)

**AWS Marketplace**
+ [Splunk Enterprise Amazon Machine Image (AMI)](https://aws.amazon.com/marketplace/pp/prodview-l6oos72bsyaks)
