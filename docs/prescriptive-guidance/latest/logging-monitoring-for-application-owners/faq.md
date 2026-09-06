---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/faq.html
---

# FAQ
<a name="faq"></a>

## Can I use my current monitoring service?
<a name="faq1"></a>

[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), IT managers, and application owners. It provides data and actionable insights to help you monitor your applications, respond to system-wide performance changes, and optimize resource utilization. However, if you have an established monitoring service in place, you do not need to replace it.

## How do I stop the log files from being tampered with?
<a name="faq2"></a>

You can enable log file integrity validation. It is good practice to manage and store your logs in a dedicated AWS account and restrict access to that account. For more information, see [Using AWS CloudTrail](cloudtrail.md#using-cloudtrail) in this guide.

## Do I have to maintain separate log files for each application?
<a name="faq3"></a>

No, you can consolidate the log data from multiple applications into the same log file. However, make sure that a unique identifier for each application is recorded in the log stream.
