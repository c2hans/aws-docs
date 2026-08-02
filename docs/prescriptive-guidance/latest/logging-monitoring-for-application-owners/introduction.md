---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/introduction.html
---

# Logging and monitoring guide for application owners
<a name="introduction"></a>

*John Buckley, Amazon Web Services*

A *workload* is a collection of resources and code that delivers business value, such as a customer-facing application or a backend process. A workload might consist of a subset of resources in a single AWS account, or it might span multiple AWS accounts. In the cloud, an *application* is a type of workload. It might be deployed exclusively in the cloud environment, or it might be also be supported by local, on-premises hardware. Many publications focus on logging and monitoring cloud infrastructure and are intended for security teams. This guide is intended for application owners and focuses on effective and efficient approaches for logging and monitoring applications in the AWS Cloud.

This guide helps you set logging and monitoring at an appropriate level so that you can identify and respond to anomalies quickly. It also helps you make sure that your application logs support detailed analysis and resolution of any issues.

Although this guide is written with AWS Cloud deployments in mind, you can apply these principles to applications running on premises or on other cloud provider infrastructure.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

After reading this guide, you should be able to understand:
+ The types of events that are commonly logged for applications
+ The event attributes (such as the who, what, and when) that you should consider logging
+ The types of data that you should consider excluding from logs, such as data that might compromise your security posture or personally identifiable information
+ How to set logging and monitoring at an appropriate level for your application
+ Who should be able to manage and access your application logs
+ The AWS services and features that you can configure to monitor and log your applications in the AWS Cloud
+ How to use the log data from your application and AWS services and features to triage problems and diagnose issues
