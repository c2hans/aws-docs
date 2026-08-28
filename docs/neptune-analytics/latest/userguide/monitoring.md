---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/monitoring.html
---

# Monitoring Neptune Analytics
<a name="monitoring"></a>

 To ensure robust monitoring and analysis of Neptune Analytics usage, it is integrated with AWS CloudTrail, a service that records all API calls made to the Neptune Analytics service. By capturing these API calls, CloudTrail provides a detailed audit trail that can be used to understand who is accessing the service, what actions they are taking, and from where they are making those requests. This data can then be further analyzed using tools like Amazon CloudWatch and Amazon Athena to identify trends, anomalies, and other insights about the usage of Neptune Analytics within an organization.

**Topics**
+ [Neptune Analytics information in CloudTrail](monitoring-cloudtrail-info.md)
+ [Understanding Neptune Analytics log file entries](monitoring-cloudtrail-understanding.md)
+ [Monitoring your graphs](monitoring-cw.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
