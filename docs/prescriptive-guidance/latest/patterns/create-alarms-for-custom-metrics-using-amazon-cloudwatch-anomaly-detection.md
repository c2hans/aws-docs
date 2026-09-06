---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-alarms-for-custom-metrics-using-amazon-cloudwatch-anomaly-detection.html
---

# Create alarms for custom metrics using Amazon CloudWatch anomaly detection
<a name="create-alarms-for-custom-metrics-using-amazon-cloudwatch-anomaly-detection"></a>

*Ram Kandaswamy and Raheem Jiwani, Amazon Web Services*

## Summary
<a name="create-alarms-for-custom-metrics-using-amazon-cloudwatch-anomaly-detection-summary"></a>

On the Amazon Web Services (AWS) Cloud, you can use Amazon CloudWatch to create alarms that monitor metrics and send notifications or automatically make changes if a threshold is breached.

To avoid being limited by [static thresholds](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html), you can create alarms based on past patterns and that notify you if specific metrics are outside the normal operating window. For example, you could monitor your API’s response times from Amazon API Gateway and receive notifications about anomalies that prevent you from meeting a service-level agreement (SLA).

This pattern describes how to use CloudWatch anomaly detection for custom metrics. The pattern shows you how to create a custom metric in Amazon CloudWatch Logs Insights or publish a custom metric with an AWS Lambda function, and then set up anomaly detection and create notifications using Amazon Simple Notification Service (Amazon SNS).

## Prerequisites and limitations
<a name="create-alarms-for-custom-metrics-using-amazon-cloudwatch-anomaly-detection-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An existing SNS topic, configured to send email notifications. For more information about this, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) in the Amazon SNS documentation.
+ An existing application, configured with [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_GettingStarted.html).

**Limitations **
+ CloudWatch metrics don't support millisecond time intervals. For more information about the granularity of regular and custom metrics, see the [Amazon CloudWatch FAQs](https://aws.amazon.com/cloudwatch/faqs/).

## Architecture
<a name="create-alarms-for-custom-metrics-using-amazon-cloudwatch-anomaly-detection-architecture"></a>

![CloudWatch using an Amazon SNS topic to send an email notification when an alarm initiates.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d47e6f7f-e469-4cb9-b34b-8c4b78d71820/images/49f30340-9552-430a-893a-d0608bb09e38.png)

 The diagram shows the following workflow:

1. Logs that use metrics created and updated by CloudWatch Logs are streamed to CloudWatch.

1. An alarm initiates based on thresholds and sends an alert to an SNS topic.

1. Amazon SNS sends you an email notification.

**Technology stack  **
+ CloudWatch
+ AWS Lambda
+ Amazon SNS

## Tools
<a name="create-alarms-for-custom-metrics-using-amazon-cloudwatch-anomaly-detection-tools"></a>
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) provides a reliable, scalable, and flexible monitoring solution.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without provisioning or managing  servers.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) is a managed service that provides message delivery from publishers to subscribers.

## Epics
<a name="create-alarms-for-custom-metrics-using-amazon-cloudwatch-anomaly-detection-epics"></a>

### Set up anomaly detection for a custom metric
<a name="set-up-anomaly-detection-for-a-custom-metric"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Option 1 - Create a custom metric with a Lambda function. | Download the `lambda_function.py` file (attached) and then replace the sample `lambda_function.py` file in the [aws-lambda-developer-guide](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-python/function) repository on the AWS Documentation GitHub. This provides you with a sample Lambda function that sends custom metrics to CloudWatch Logs. The Lambda function uses the Boto3 API to integrate with CloudWatch. <br />After you run the Lambda function, you can sign in to the AWS Management Console, open the CloudWatch console, and the published metric is available under your published namespace. | DevOps engineer, AWS DevOps |
| Option 2 – Create custom metrics from CloudWatch log groups.  | Sign in to the AWS Management Console, open the CloudWatch console, and then choose **Log groups**. Choose the log group that you want to create a metric for. <br />Choose **Actions **and then choose **Create metric filter**. For **Filter pattern**, enter the filter pattern that you want to use. For more information, see [Filter and pattern syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) in the CloudWatch documentation. <br />To test your filter pattern, enter one or more log events under **Test Pattern**. Each log event must be within one line, because line breaks are used to separate log events in the **Log event** messages box. After you test the pattern, you can enter a name and value for your metric under **Metric details**. <br />For more information and steps to create a custom metric, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the CloudWatch documentation. | DevOps engineer, AWS DevOps |
| Create an alarm for your custom metric. | On the CloudWatch console, choose **Alarms** and then choose **Create Alarm**. Choose **Select metric** and enter the name of the metric that you created earlier into the search box. Choose the **Graphed metrics** tab and configure the options according to your requirements.<br />Under **Conditions**, choose **Anomaly detection** instead of **Static thresholds**. This shows you a band based on two standard default deviations. You can set up thresholds and adjust them according to your requirements.<br />Choose **Next.**The band is dynamic and depends on the quality of the datapoints. When you begin aggregating more data, the band and thresholds are automatically updated.  | DevOps engineer, AWS DevOps |
| Set up SNS notifications. | Under **Notification**, choose the SNS topic to notify when the alarm is in `ALARM` state, `OK` state, or `INSUFFICIENT_DATA` state.<br />To have the alarm send multiple notifications for the same alarm state or for different alarm states, choose **Add notification**. Choose **Next**. Enter a name and description for the alarm. The name must only contain ASCII characters. Then choose **Next**.<br />Under **Preview and create**, confirm that the information and conditions are correct, and then choose **Create alarm**. | DevOps engineer, AWS DevOps |

## Related resources
<a name="create-alarms-for-custom-metrics-using-amazon-cloudwatch-anomaly-detection-resources"></a>
+ [Publishing custom metrics to CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
+ [Using CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
+ [Alarm events and Amazon EventBridge](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-and-eventbridge.html)
+ [What are the best practices to follow while pushing custom metrics to Cloud Watch?](https://www.youtube.com/watch?v=mVffHIzIL60) (video)
+ [Introduction to CloudWatch Application Insights ](https://www.youtube.com/watch?v=PBO636_t9n0)(video)
+ [Detect anomalies with CloudWatch ](https://www.youtube.com/watch?v=8umIX-pUy3k)(video)

## Attachments
<a name="attachments-d47e6f7f-e469-4cb9-b34b-8c4b78d71820"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/d47e6f7f-e469-4cb9-b34b-8c4b78d71820/attachments/attachment.zip)
