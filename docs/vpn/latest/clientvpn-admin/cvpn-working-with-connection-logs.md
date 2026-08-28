---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-with-connection-logs.html
---

# AWS Client VPN connection logs
<a name="cvpn-working-with-connection-logs"></a>

You can enable connection logging for a new or existing Client VPN endpoint, and start capturing connection logs. Connection logs show the sequence of log events for the Client VPN endpoint. When you enable connection logging, you can specify the name of a log stream in the log group. If you do not specify a log stream, the Client VPN service creates one for you. Connection logging then logs the following information: client connection requests, client connection results (successful or unsuccessful), reasons for unsuccessful connection results, and the client termination time from the endpoint.

Before you begin, you must have a CloudWatch Logs log group in your account. For more information, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*. Charges apply for using CloudWatch Logs. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

Client VPN connection logs can be created using either the Amazon VPC Console or the AWS CLI.

**Topics**
+ [Enable connection logging for a new endpoint](create-connection-log-new.md)
+ [Enable connection logging for an existing endpoint](create-connection-log-existing.md)
+ [View connection logs](view-connection-logs.md)
+ [Turn off connection logging](disable-connection-logs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
