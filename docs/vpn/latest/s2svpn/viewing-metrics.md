---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/viewing-metrics.html
---

# View Amazon CloudWatch Logs metrics for AWS Site-to-Site VPN
<a name="viewing-metrics"></a>

When you create a Site-to-Site VPN connection, the VPN service sends metrics about your VPN connection to CloudWatch, as they become available. You can view the metrics for your VPN connection as follows.

**To view metrics using the CloudWatch console**

Metrics are grouped first by the service namespace, and then by the various dimension combinations within each namespace.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Under **All metrics**, choose the **VPN** metric namespace.

1. Select the metric dimension to view the metrics— for example, **VPN Tunnel Metrics**.

**Note**
The VPN namespace will not appear in the CloudWatch console until after a Site-to-Site VPN connection has been created in the AWS region you are viewing.

**To view metrics using the AWS CLI**
At a command prompt, use the following command:

```
aws cloudwatch list-metrics --namespace "AWS/VPN"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
