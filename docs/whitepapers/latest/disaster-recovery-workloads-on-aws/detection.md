---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/detection.html
---

# Detection
<a name="detection"></a>

 It is important to know as soon as possible that your workloads are not delivering the business outcomes that they should be delivering. In this way, you can quickly declare a disaster and recover from an incident. For aggressive recovery objectives, this response time coupled with appropriate information is critical in meeting recovery objectives. If your recovery time objective is one hour, then you need to detect the incident, notify appropriate personnel, engage your escalation processes, evaluate information (if you have any) on expected time to recovery (without executing the DR plan), declare a disaster and recover within an hour.

**Note**
If stakeholders decide not to invoke DR even though the RTO would be at risk, then re-evaluate DR plans and objectives. The decision not to invoke DR plans may be because the plans are inadequate or there is a lack of confidence in execution.

 It is critical to factor in incident detection, notification, escalation, discovery and declaration into your planning and objectives to provide realistic, achievable objectives that provide business value.

 AWS publishes our most up-to-the-minute information on service availability on the [Service Health Dashboard](https://status.aws.amazon.com/). Check at any time to get current status information, or subscribe to an RSS feed to be notified of interruptions to each individual service. If you are experiencing a real-time, operational issue with one of our services that is not shown on the Service Health Dashboard, you can create a [Support Request](https://console.aws.amazon.com/support/home#/case/create?issueType=technical).

 The [AWS Health Dashboard](https://phd.aws.amazon.com/phd/home#/) provides information about AWS Health events that can affect your account. The information is presented in two ways: a dashboard that shows recent and upcoming events organized by category, and a full event log that shows all events from the past 90 days.

 For the most stringent RTO requirements, you can implement automated failover based on [health checks.](https://aws.amazon.com/builders-library/implementing-health-checks/) Design health checks that are representative of user experience and based on Key Performance Indicators. Deep health checks exercise key functionality of your workload and go beyond shallow heartbeat checks. Use deep health checks based on multiple signals. Use caution with this approach so that you do not trigger false alarms because failing over when there is no need to can in itself introduce availability risks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
