---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic.html
---

# Use Network Firewall to capture the DNS domain names from the Server Name Indication for outbound traffic
<a name="use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic"></a>

*Kirankumar Chandrashekar, Amazon Web Services*

## Summary
<a name="use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic-summary"></a>

This pattern shows you how to use AWS Network Firewall to collect the DNS domain names that are provided by the Server Name Indication (SNI) in the HTTPS header of your outbound network traffic. Network Firewall is a managed service that makes it easy to deploy critical network protections for Amazon Virtual Private Cloud (Amazon VPC), including the ability to secure outbound traffic with a firewall that blocks packets that fail to meet certain security requirements. Securing outbound traffic to specific DNS domain names is called egress filtering, which is the practice of monitoring and potentially restricting the flow of outbound information from one network to another.

After you capture the SNI data that passes through Network Firewall, you can use Amazon CloudWatch Logs and AWS Lambda to publish the data to an Amazon Simple Notification Service (Amazon SNS) topic that generates email notifications. The email notifications include the server name and other relevant SNI information. Additionally, you can use the output of this pattern to allow or restrict outbound traffic by domain name in the SNI by using firewall rules. For more information, see [Working with stateful rule groups in AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-ips.html) in the Network Firewall documentation.

## Prerequisites and limitations
<a name="use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) version 2, installed and configured on Linux, macOS, or Windows.
+ [Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/getting-started.html), set up and configured in Amazon VPC and in use for inspecting outbound traffic. You can configure Network Firewall to use any of the following VPC configurations:
  + [Simple single zone architecture with an internet gateway](https://docs.aws.amazon.com/network-firewall/latest/developerguide/arch-single-zone-igw.html)
  + [Multi zone architecture with an internet gateway](https://docs.aws.amazon.com/network-firewall/latest/developerguide/arch-two-zone-igw.html)
  + [Architecture with an internet gateway and a NAT gateway](https://docs.aws.amazon.com/network-firewall/latest/developerguide/arch-igw-ngw.html)

## Architecture
<a name="use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic-architecture"></a>

The following diagram shows how to use Network Firewall to collect SNI data from outbound network traffic, and then publish that data to an SNS topic by using CloudWatch Logs and Lambda.

![Workflow between Network Firewall, CloudWatch Logs, Lambda, and Amazon SNS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/9eb1e9e3-f459-4ea3-8e6d-60fec6b7ea98/images/1094b5f6-33e3-42bc-8fb8-7409b5b826b0.png)

The diagram shows the following workflow:

1. Network Firewall collects domain names from the SNI data in the HTTPS header of your outbound network traffic.

1. CloudWatch Logs monitors the SNI data and invokes a Lambda function whenever the outbound network traffic passes through Network Firewall.

1. The Lambda function reads the SNI data captured by CloudWatch Logs and then publishes that data to an SNS topic.

1. The SNS topic sends you an email notification that includes the SNI data.

**Automation and scale**
+ You can use [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) to create this pattern by using [infrastructure as code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html).

**Technology stack**
+ Amazon CloudWatch Logs
+ Amazon SNS
+ Amazon VPC
+ AWS Lambda
+ AWS Network Firewall

## Tools
<a name="use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic-tools"></a>

**AWS services**
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) – You can use Amazon CloudWatch Logs to monitor, store, and access your log files from Amazon Elastic Compute Cloud (Amazon EC2) instances, AWS CloudTrail, Amazon Route 53, and other sources.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon Simple Notification Service (Amazon SNS) is a managed service that provides message delivery from publishers to subscribers (also known as producers and consumers).
+ [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) – Amazon Virtual Private Cloud (Amazon VPC) provisions a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – AWS Lambda is a compute service that lets you run code without provisioning or managing servers.
+ [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) – AWS Network Firewall is a managed service that makes it easy to deploy essential network protections for all of your Amazon VPCs.

## Epics
<a name="use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic-epics"></a>

### Create a CloudWatch log group for Network Firewall
<a name="create-a-cloudwatch-log-group-for-network-firewall"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a CloudWatch log group. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic.html)For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the CloudWatch documentation. | Cloud administrator |

### Create an SNS topic and subscription
<a name="create-an-sns-topic-and-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an SNS topic. | To create an SNS topic, follow the instructions in the [Amazon SNS documentation](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html#create-topic-aws-console). | Cloud administrator |
| Subscribe an endpoint to the SNS topic. | To subscribe an email address as an endpoint to the SNS topic that you created, follow the instructions in the [Amazon SNS documentation](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html). For **Protocol**, choose [Email/Email-JSON](https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html). You can also choose a different endpoint based on your requirements. | Cloud administrator |

### Set up logging in Network Firewall
<a name="set-up-logging-in-network-firewall"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enable firewall logging. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic.html)For more information about using CloudWatch Logs as a log destination for Network Firewall, see [Amazon CloudWatch Logs](https://docs.aws.amazon.com/network-firewall/latest/developerguide/logging-cw-logs.html) in the Network Firewall documentation.  | Cloud administrator |

### Set up a stateful rule in Network Firewall
<a name="set-up-a-stateful-rule-in-network-firewall"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a stateful rule. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic.html) | Cloud administrator |
| Associate the stateful rule to Network Firewall. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic.html) | Cloud administrator |

### Create a Lambda function to read the logs
<a name="create-a-lambda-function-to-read-the-logs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the code for the Lambda function. | In an integrated development environment (IDE) that can read the CloudWatch Logs event from Network Firewall for outbound traffic, paste in the following Python 3 code and replace `<SNS-topic-ARN>` with your value:<pre>import json<br />import gzip<br />import base64<br />import boto3<br />sns_client = boto3.client('sns')<br />def lambda_handler(event, context):<br />    decoded_event = json.loads(gzip.decompress(base64.b64decode(event['awslogs']['data'])))<br />    body = '''<br />    {filtermatch}<br />    '''.format(<br />        loggroup=decoded_event['logGroup'],<br />        logstream=decoded_event['logStream'],<br />        filtermatch=decoded_event['logEvents'][0]['message'],<br />    )<br />    print(body)<br />    filterMatch = json.loads(body)<br />    data = []<br />    if 'http' in filterMatch['event']:<br />        data.append(filterMatch['event']['http']['hostname'])<br />    elif 'tls' in filterMatch['event']:<br />        data.append(filterMatch['event']['tls']['sni'])<br />    result = 'Domain accessed ' + 1*' ' + (data[0]) + 1*' ' 'via AWS Network Firewall ' + 1*' '  + (filterMatch['firewall_name'])<br />    print(result)<br />    message = {'ServerName': result}<br />    send_to_sns = sns_client.publish(<br />        TargetArn=<SNS-topic-ARN>,          #Replace with the SNS topic ARN<br />        Message=json.dumps({'default': json.dumps(message),<br />                        'sms': json.dumps(message),<br />                        'email': json.dumps(message)}),<br />        Subject='Server Name passed through the Network Firewall',<br />        MessageStructure='json'<br />    )</pre><br />This code sample parses the CloudWatch Logs content and captures the server name provided by the SNI in the HTTPS header. | App developer |
| Create the Lambda function. | To create the Lambda function, follow the instructions in the [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html#getting-started-create-function) and choose **Python 3.9** for **Runtime**. | Cloud administrator |
| Add the code to the Lambda function. | To add your Python code to the Lambda function that you created earlier, follow the instructions in the [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-zip.html#configuration-function-update). | Cloud administrator |
| Add CloudWatch Logs as a trigger to the Lambda function. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic.html)For more information, see [Using Lambda with CloudWatch Logs](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchlogs.html) in the Lambda documentation. | Cloud administrator |
| Add SNS publish permissions. | Add the **sns:Publish** permission to the Lambda execution role, so that Lambda can make API calls to publish messages to SNS.  [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic.html)<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Sid": "AllowSNSPublish",<br />            "Effect": "Allow",<br />            "Action": [<br />                "sns:GetTopicAttributes",<br />                "sns:Subscribe",<br />                "sns:Unsubscribe",<br />                "sns:Publish"<br />            ],<br />            "Resource": "*"<br />        }<br />    ]<br />}</pre> | Cloud administrator |

### Test the functionality of your SNS notification
<a name="test-the-functionality-of-your-sns-notification"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Send traffic through Network Firewall. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-network-firewall-to-capture-the-dns-domain-names-from-the-server-name-indication-sni-for-outbound-traffic.html)<pre>{<br />    "Type": "Notification",<br />    "MessageId": "<messageID>",<br />    "TopicArn": "arn:aws:sns:us-west-2:123456789:testSNSTopic",<br />    "Subject": "Server Name passed through the Network Firewall",<br />    "Message": "{\"ServerName\": \"Domain 'aws.amazon.com' accessed via AWS Network Firewall 'AWS-Network-Firewall-Multi-AZ-firewall\"}",<br />    "Timestamp": "2022-03-22T04:10:04.217Z",<br />    "SignatureVersion": "1",<br />    "Signature": "<Signature>",<br />    "SigningCertURL": "<SigningCertUrl>",<br />    "UnsubscribeURL": "<UnsubscribeURL>"<br />}</pre>Then, check the Network Firewall alert log in Amazon CloudWatch by following the instructions in the [Amazon CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SearchDataFilterPattern.html). The alert log shows the following output:<pre>{<br />    "firewall_name": "AWS-Network-Firewall-Multi-AZ-firewall",<br />    "availability_zone": "us-east-2b",<br />    "event_timestamp": "<event timestamp>",<br />    "event": {<br />        "timestamp": "2021-03-22T04:10:04.214222+0000",<br />        "flow_id": <flow ID>,<br />        "event_type": "alert",<br />        "src_ip": "10.1.3.76",<br />        "src_port": 22761,<br />        "dest_ip": "99.86.59.73",<br />        "dest_port": 443,<br />        "proto": "TCP",<br />        "alert": {<br />            "action": "allowed",<br />            "signature_id": 2,<br />            "rev": 0,<br />            "signature": "",<br />            "category": "",<br />            "severity": 3<br />        },<br />        "tls": {<br />            "subject": "CN=aws.amazon.com",<br />            "issuerdn": "C=US, O=Amazon, OU=Server CA 1B, CN=Amazon",<br />            "serial": "<serial number>",<br />            "fingerprint": "<fingerprint ID>",<br />            "sni": "aws.amazon.com",<br />            "version": "TLS 1.2",<br />            "notbefore": "2020-09-30T00:00:00",<br />            "notafter": "2021-09-23T12:00:00",<br />            "ja3": {},<br />            "ja3s": {}<br />        },<br />        "app_proto": "tls"<br />    }<br />}</pre> | Test engineer |
