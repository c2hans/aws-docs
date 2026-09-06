---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about migrating your SSIS ETL jobs to AWS.

## Should I enhance SSIS jobs during migration?
<a name="q1"></a>

Yes. Implement any important enhancements or bug fixes in both existing and new jobs at the same time. Low-priority changes can be implemented after migration.

## How can I monitor jobs on AWS?
<a name="q2"></a>

You can use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to monitor jobs and to send rule-based alerts.

## When can I decommission my on-premises SSIS jobs?
<a name="q3"></a>

We recommend that you maintain old and new jobs in parallel for a period of time until the performance, accuracy, and completeness of data are the same in both environments. You can also replicate reporting systems to connect and compare reports from both environments. You can decommission your SSIS jobs when the reports are identical.
