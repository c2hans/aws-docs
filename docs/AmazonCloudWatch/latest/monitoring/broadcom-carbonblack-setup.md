---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/broadcom-carbonblack-setup.html
---

# Broadcom Carbon Black integration configuration
<a name="broadcom-carbonblack-setup"></a>

[Broadcom Carbon Black](https://www.broadcom.com/products/carbon-black/threat-prevention/carbon-black-cloud) is a cloud-native endpoint protection platform (EPP) that combines next-generation antivirus (NGAV), behavioral detection, and endpoint detection and response (EDR). It provides continuous monitoring of endpoints and workloads from a single console to detect and stop ransomware, malware, and fileless attacks.

The Carbon Black [Data Forwarder](https://developer.carbonblack.com/reference/carbon-black-cloud/integrations/data-forwarder/) is a high-volume data streaming service designed to send alerts, endpoint events, watchlist hits, authentication events, auditlog events, and livequery results to Amazon S3.

Data Forwarder can be configured to forward events for one of the following types:
+ alert 2.1.0
+ auth.event 1.0.0
+ endpoint.event 1.2.0
+ watchlist.hit 1.0.0
+ auditlog 1.0.0
+ livequery 1.0.0

**Topics**
+ [Source configuration for Broadcom Carbon Black](broadcom-carbonblack-source-config.md)
+ [CloudWatch pipelines configuration for Broadcom Carbon Black](broadcom-carbonblack-pipeline-setup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
