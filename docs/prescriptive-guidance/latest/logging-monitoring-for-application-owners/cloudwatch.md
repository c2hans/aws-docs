---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/cloudwatch.html
---

# Amazon CloudWatch
<a name="cloudwatch"></a>

[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) monitors your AWS resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track *metrics*, which are variables you can measure for your resources and applications.

## Using CloudWatch
<a name="using-cloudwatch"></a>

CloudWatch is, essentially, a metrics repository. An AWS service, such as Amazon EC2, puts metrics into the repository, and you retrieve statistics based on those metrics. If you put your own custom metrics into the repository, you can also retrieve statistics on these metrics. For more information, see [Using CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) (CloudWatch documentation).

You can also configure *alarms*, which automatically initiate actions on your behalf. An alarm watches a single metric over a specified time period and performs one or more specified actions, based on the value of the metric relative to a threshold over time. For example, the alarm might send a notification to an Amazon Simple Notification Service (Amazon SNS) topic. You can also add alarms to dashboards. For more information, see [Using CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) (CloudWatch documentation).

The CloudWatch console automatically displays metrics about every AWS service you use. You can create additional, custom dashboards to display metrics and alarms for your applications. For more information, see [Using CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) (CloudWatch documentation).

CloudWatch automatically supports cross-Region functionality. You do not need to take any extra steps to display metrics from different AWS Regions in a single account on the same graph or dashboard. You can achieve cross-account functionality by implementing [cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) (CloudWatch documentation).

For more information and detailed guidance about using CloudWatch to log and monitor workloads in the AWS Cloud, see [Designing and implementing logging and monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/welcome.html) (AWS Prescriptive Guidance).

## Use cases for CloudWatch
<a name="cloudwatch-use-cases"></a>
+ **Application health monitoring** – CloudWatch ServiceLens enhances the observability of your services and applications by enabling you to integrate traces, metrics, logs, alarms, and other resource health information into one place. ServiceLens integrates CloudWatch with AWS X-Ray to provide an end-to-end view of your application to help you more efficiently pinpoint performance bottlenecks and identify impacted users. For more information, see [Using ServiceLens to monitor the health of your applications](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceLens.html) (CloudWatch documentation).
+ **Synthetic monitoring** – You can use CloudWatch Synthetics to create canaries, configurable scripts that run on a schedule, to monitor your endpoints and APIs. Canaries follow the same routes and perform the same actions as a customer, which makes it possible for you to continually verify your customer experience even when you don't have any customer traffic on your applications. Canaries check the availability and latency of your endpoints and can store load time data and screenshots of the UI. They monitor your REST APIs, URLs, and website content, and they can check for unauthorized changes from phishing, code injection, and cross-site scripting. For more information, see [Using synthetic monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) (CloudWatch documentation).
+ **User monitoring** – With CloudWatch RUM, you can perform real user monitoring to collect and view client-side data about your web application performance. The data includes page load times, client-side errors, and user behavior. You can use the collected data to quickly identify and debug client-side performance issues. For more information, see [Using CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) (CloudWatch documentation).
+ **Anomalous behavior detection** – When you enable *anomaly detection* for a metric, CloudWatch applies statistical and machine learning algorithms. These algorithms continuously analyze metrics of systems and applications, determine normal baselines, and surface anomalies. For more information, see [Using CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) (CloudWatch documentation).
+ **Feature validation and A/B experiments** – You can use Amazon CloudWatch Evidently to safely validate new features by serving them to a specified percentage of your users while you roll out the feature. You can also conduct A/B experiments to make feature design decisions based on evidence and data. For more information, see [Perform launches and A/B experiments with CloudWatch Evidently](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently.html) (CloudWatch documentation).
