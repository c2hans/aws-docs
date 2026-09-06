---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/amazon-cloudwatch.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon CloudWatch
<a name="amazon-cloudwatch"></a>

The cornerstone for monitoring applications running on AWS is [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), a group of services that can store log files, track metrics, send alarms, and execute automated actions when specific events are triggered.

Sending data to CloudWatch from Windows applications can be handled automatically using the Amazon CloudWatch agent, which runs as a Windows service to integrate with CloudWatch from .NET applications hosted on Amazon EC2, Amazon ECS, or Amazon EKS.

Amazon CloudWatch provides a number of key features. CloudWatch dashboards are customizable home pages in the CloudWatch console that can be used to monitor resources and view the metrics and alarms for your AWS resources. [CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) stores data about the performance of your systems, and allows publishing your own application metrics. [CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) can monitor one or more metrics, and can trigger a variety of actions, including automatic scaling, or sending a notification to an [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) topic.

[Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) stores and monitors log files, and can be used for centralized access to log files from a variety of applications, systems, and AWS services. Although logs can be sent from Windows using the CloudWatch agent, you can configure many [.NET logging libraries](https://github.com/aws/aws-logging-dotnet), including [Apache log4net](https://logging.apache.org/log4net/), [NLog](https://nlog-project.org/), [Serilog](https://serilog.net/), and [ASP.NET Core logging](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/logging/?view=aspnetcore-5.0), to send log entries to CloudWatch, and call CloudWatch directly using the AWS SDK for .NET. For .NET serverless functions running in AWS Lambda, you can send messages to CloudWatch Logs by either writing output to stdout or stderr using the Console class, or by using the ILambda Context object.

Once logs are stored, you can view the logs from multiple sources as a time-ordered flow of events, search the logs, and display them in custom dashboards. Although CloudWatch Logs provides a number of common logging features, sometimes there are use cases that fit more closely with other logging tools. Common tools used alongside or instead of CloudWatch Logs include [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/), [Splunk](https://www.splunk.com/en_us/download/splunk-enterprise.html), or [Loggly](https://www.loggly.com/lp-loggly-general/).

Amazon CloudWatch Events receives system events from AWS resources, and can be used to send notifications or run automated scripts when specific conditions are met. Rules are defined to match particular sets of events and conditions, and, once triggered, events can be routed to target actions, allowing notifications to be sent, or custom actions to execute. CloudWatch Events can also be run on a schedule, and provides a flexible tool to trigger various types of system automation.
