---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/publish-amazon-cloudwatch-metrics-to-a-csv-file.html
---

# Publish Amazon CloudWatch metrics to a CSV file
<a name="publish-amazon-cloudwatch-metrics-to-a-csv-file"></a>

*Abdullahi Olaoye, Amazon Web Services*

## Summary
<a name="publish-amazon-cloudwatch-metrics-to-a-csv-file-summary"></a>

This pattern uses a Python script to retrieve Amazon CloudWatch metrics and to convert the metrics information into a comma-separated values (CSV) file for improved readability. The script takes the AWS service whose metrics should be retrieved as a required argument. You can specify the AWS Region and AWS credential profile as optional arguments. If you don’t specify those arguments, the script uses the default Region and profile that are configured for the workstation where the script is run. After the script runs, it generates and stores a CSV file in the same directory.

See the *Attachments* section for the script and associated files provided with this pattern.

## Prerequisites and limitations
<a name="publish-amazon-cloudwatch-metrics-to-a-csv-file-prereqs"></a>

**Prerequisites **
+ Python 3.x
+ AWS Command Line Interface (AWS CLI)

**Limitations **

The script currently supports the following AWS services:
+ AWS Lambda
+ Amazon Elastic Compute Cloud (Amazon EC2)
  + By default, the script doesn’t collect Amazon Elastic Block Store (Amazon EBS) volume metrics. To collect Amazon EBS metrics, you must modify the attached `metrics.yaml` file.
+ Amazon Relational Database Service (Amazon RDS)
  + However, the script doesn't support Amazon Aurora.
+ Application Load Balancer
+ Network Load Balancer
+ Amazon API Gateway

## Tools
<a name="publish-amazon-cloudwatch-metrics-to-a-csv-file-tools"></a>
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) is a monitoring service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers. CloudWatch provides data and actionable insights to help you monitor your applications, respond to systemwide performance changes, optimize resource utilization, and get a unified view of operational health. CloudWatch collects monitoring and operational data in the form of logs, metrics, and events, and provides a unified view of AWS resources, applications, and services that run on AWS and on-premises servers.

## Epics
<a name="publish-amazon-cloudwatch-metrics-to-a-csv-file-epics"></a>

### Install and configure the prerequisites
<a name="install-and-configure-the-prerequisites"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the prerequisites. | Run the following command:<pre>$ pip3 install -r requirements.txt</pre> | Developer |
| Configure the AWS CLI. | Run the following command: <pre>$ aws configure</pre> | Developer |

### Configure the Python script
<a name="configure-the-python-script"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Open the script. | To change the default configuration of the script, open `metrics.yaml`. | Developer |
| Set the period for the script. | This is the time period to fetch. The default period is 5 minutes (300 seconds). You can change the time period, but note the following limitations: + If the hours value that you specify is between 3 hours and 15 days ago, use a multiple of 60 seconds (1 minute) for the period. <br />+ If the hours value that you specify is between 15 hours and 63 days ago, use a multiple of 300 seconds (5 minutes) for the period. <br />+ If the hours value that you specify is greater than 63 days ago, use a multiple of 3,600 seconds (1 hour) for the period.<br />Otherwise, the API operation won't return any data points. | Developer |
| Set the hours for the script. | This value specifies how many hours of metrics you want to fetch. The default is 1 hour. To retrieve multiple days of metrics, provide the value in hours. For example, for 2 days, specify 48. | Developer |
| Change statistics values for the script.  | (Optional) The global statistics value is `Average`, which is used when fetching metrics that do not have a specific statistics value assigned. The script supports the statistics values `Maximum`, `SampleCount`, and `Sum`. | Developer |

### Run the Python script
<a name="run-the-python-script"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the script. | Use the following command: <pre>$ python3 cwreport.py <service> </pre><br />To see a list of service values and the optional `region `and `profile `parameters, run the following command:<pre> $ python3 cwreport.py -h</pre><br />For more information about the optional parameters, see the *Additional information* section. | Developer |

## Related resources
<a name="publish-amazon-cloudwatch-metrics-to-a-csv-file-resources"></a>
+ [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
+ [Amazon CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ [EC2 CloudWatch Metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html#ec2-cloudwatch-metrics)
+ [AWS Lambda Metrics](https://docs.aws.amazon.com/lambda/latest/operatorguide/logging-metrics.html)
+ [Amazon RDS Metrics](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html#rds-cw-metrics-instance)
+ [Application Load Balancer Metrics](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html)
+ [Network Load Balancer Metrics](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-cloudwatch-metrics.html)
+ [Amazon API Gateway Metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html)

## Additional information
<a name="publish-amazon-cloudwatch-metrics-to-a-csv-file-additional"></a>

**Script usage**

```
$ python3 cwreport.py -h
```

**Example syntax**

```
python3 cwreport.py <service> <--region=Optional Region> <--profile=Optional credential profile>
```

**Parameters**
+ **service (required)** ‒ The service you want to run the script against. The script currently supports these services: AWS Lambda, Amazon EC2, Amazon RDS, Application Load Balancer, Network Load Balancer, and API Gateway.
+ **region (optional)** ‒ The AWS Region to fetch metrics from. The default Region is `ap-southeast-1`.
+ **profile (optional)** ‒ The AWS CLI named profile to use. If this parameter isn’t specified, the default configured credential profile is used.

**Examples**
+ To use the default Region `ap-southeast-1` and default configured credentials to fetch Amazon EC2 metrics: `$ python3 cwreport.py ec2`
+ To specify a Region and fetch API Gateway metrics: `$ python3 cwreport.py apigateway --region us-east-1`
+ To specify an AWS profile and fetch Amazon EC2 metrics: `$ python3 cwreport.py ec2 --profile testprofile`
+ To specify both Region and profile to fetch Amazon EC2 metrics: `$ python3 cwreport.py ec2 --region us-east-1 --profile testprofile`

## Attachments
<a name="attachments-0a915a9d-2eef-4da1-8283-3cf4a115b3b2"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/0a915a9d-2eef-4da1-8283-3cf4a115b3b2/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
