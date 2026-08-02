---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/view-connection-logs.html
---

# View AWS Client VPN connection logs
<a name="view-connection-logs"></a>

You can view your Client VPN connection logs using the CloudWatch Logs console.

**To view your connection logs using the console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Log groups**, and select the log group that contains your connection logs.

1. Select the log stream for your Client VPN endpoint.
**Note**
The **Timestamp** column displays the time that the connection log was published to CloudWatch Logs, not the time of the connection.

For more information about searching log data, see [Search Log Data Using Filter Patterns](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SearchDataFilterPattern.html) in the *Amazon CloudWatch Logs User Guide*.
