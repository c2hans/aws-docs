---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/auto-scaling.html
---

# Example: Auto scaling SAP applications
<a name="auto-scaling"></a>

You can automate *SAP application auto scaling*, which automatically detects SAP application server demand and scales up or scales down Amazon EC2 instances accordingly. This capability can adapt to spikes and dips for concurrent user logins, month-end close, payment runs, and a variety of both predictable and unpredictable workloads. The capability can horizontally scale up (start new compute services as application servers) and scale down (stop existing compute services). The following are the benefits of this automation:
+ Dynamic adjusting of application server capacity based on user demand
+ Running minimal baseline EC2 instances at the application layer
+ Reducing costs
+ Maintaining increased and scalable performance service level agreements (SLAs) for the business

The following image and process describe how you can automate scaling of the resources that support your SAP applications:

1. A time-based event, typically scheduled for every 2 minutes, causes Amazon EventBridge to start a Lambda function.

1. The Lambda function collects the required statistical information from Amazon DynamoDB and its local environment variables, such as hostname and threshold values.

1. If demand is above or below the threshold, the Lambda function directs AWS Systems Manager to start or stop additional EC2 instances to support the SAP applications.

![Architecture diagram showing how you can automate starting or stopping EC2 instances to support the demand for your SAP applications.](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/images/guide-img/029e7e61-9fe5-41b5-83f4-177d03384b91/images/529bd45f-fb29-4598-b42c-4f9a3f0f6cea.png)
