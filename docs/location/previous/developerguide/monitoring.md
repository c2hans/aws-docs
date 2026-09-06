---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/monitoring.html
---

# Monitor Amazon Location Service
<a name="monitoring"></a>

When using Amazon Location Service, you can monitor your usage and resources over time by using:
+ **Amazon CloudWatch**. Monitors your Amazon Location Service resources, and provides metrics with statistics in near-real time.
+ **AWS CloudTrail**. Provides event tracking of all calls to Amazon Location Service APIs.

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon Location Service and your AWS solutions. We recommend that you collect monitoring data from the resources that make up your AWS solution so that you can more easily debug a multi-point failure if one occurs. Before you start monitoring Amazon Location Service, however, you should create a monitoring plan that includes answers to the following questions:
+ What are your monitoring goals?
+ What resources will you monitor?
+ How often will you monitor these resources?
+ What monitoring tools will you use?
+ Who will perform the monitoring tasks?
+ Who should be notified when something goes wrong?

This section provides information about using these services.

**Topics**
+ [Monitor Amazon Location Service with Amazon CloudWatch](monitoring-using-cloudwatch.md)
+ [Log and monitor with AWS CloudTrail](logging-using-cloudtrail.md)
