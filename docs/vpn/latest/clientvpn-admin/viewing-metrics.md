---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/viewing-metrics.html
---

# View Client VPN endpoint metrics in Amazon CloudWatch
<a name="viewing-metrics"></a>

You can view the metrics for your Client VPN endpoint as follows.

**To view metrics using the CloudWatch console**

Metrics are grouped first by the service namespace, and then by the various dimension combinations within each namespace.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Under **All metrics**, choose the **ClientVPN** metric namespace.

1. To view the metrics, select the metric dimension **by endpoint**.

**To view metrics using the AWS CLI**
At a command prompt, use the following command to list the metrics that are available for the Client VPN

```
aws cloudwatch list-metrics --namespace "AWS/ClientVPN"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
