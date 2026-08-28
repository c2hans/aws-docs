---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging-destinations.html
---

# AWS Network Firewall logging destinations
<a name="firewall-logging-destinations"></a>

This section describes the logging destinations that you can choose from for your Network Firewall logs. Each section provides guidance for configuring logging for the destination type and information about any behavior that's specific to the destination type. After you've configured your logging destination, you can provide its specifications to the firewall logging configuration to start logging to it.

For information about how to update the logging destination for an existing logging configuration, see [Updating a firewall's logging configuration](firewall-update-logging-configuration.md).

**Topics**
+ [Sending AWS Network Firewall logs to Amazon Simple Storage Service](logging-s3.md)
+ [Sending AWS Network Firewall logs to Amazon CloudWatch Logs](logging-cw-logs.md)
+ [Sending AWS Network Firewall logs to Amazon Data Firehose](logging-kinesis.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
