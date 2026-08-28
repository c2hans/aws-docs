---
source_url: https://docs.aws.amazon.com/ses/latest/dg/monitor-sender-reputation.html
---

# Monitoring your Amazon SES sender reputation
<a name="monitor-sender-reputation"></a>

Amazon SES actively tracks several metrics that may cause your reputation as a sender to be damaged, or that could cause your email delivery rates to decline. Two important metrics that we consider in this process are the bounce and complaint rates for your account. If the bounce or complaint rates for your account are too high, we might place your account under review or pause your account's ability to send email.

Because your bounce and complaint rate are so important to the health of your account, Amazon SES includes a reputation metrics page in the Amazon SES console that you can use to track these metrics. Reputation metrics can also display information about factors unrelated to bounces or complaints that could damage your sender reputation. For example, if you send email to a known [spamtrap](https://en.wikipedia.org/wiki/Spamtrap), you will see a message on this dashboard.

This section contains information about accessing reputation metrics, interpreting the information it contains, and setting up systems to actively notify you of factors that could impact your sender reputation.

**Topics**
+ [Using reputation metrics to track bounce and complaint rates](reputation-dashboard-dg.md)
+ [Reputation metrics messages](reputationdashboardmessages.md)
+ [Creating reputation monitoring alarms using CloudWatch](reputationdashboard-cloudwatch-alarm.md)
+ [SNDS metrics for dedicated IPs](snds-metrics-dedicated-ips.md)
+ [Automatically pausing email sending](monitoring-sender-reputation-pausing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
