---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/create-connection-log-new.html
---

# Enable connection logging for a new AWS Client VPN endpoint
<a name="create-connection-log-new"></a>

You can enable connection logging when you create a new Client VPN endpoint by using the console or the command line.

**To enable connection logging for a new Client VPN endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**, and then choose **Create Client VPN endpoint.**

1. Complete the options until you reach the **Connection Logging** section. For more information about the options, see [Create an AWS Client VPN endpoint](cvpn-working-endpoint-create.md).

1. Under **Connection logging**, turn on **Enable log details on client connections**.

1. For **CloudWatch Logs log group name**, choose the name of the CloudWatch Logs log group.

1. (Optional) For **CloudWatch Logs log stream name**, choose the name of the CloudWatch Logs log stream.

1. Choose **Create Client VPN endpoint**.

**To enable connection logging for a new Client VPN endpoint using the AWS CLI**
Use the [create-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-client-vpn-endpoint.html) command, and specify the `--connection-log-options` parameter. You can specify the connection logs information in JSON format, as shown in the following example.

```
{
    "Enabled": true,
    "CloudwatchLogGroup": "ClientVpnConnectionLogs",
    "CloudwatchLogStream": "NewYorkOfficeVPN"
}
```
