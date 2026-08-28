---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/create-connection-log-existing.html
---

# Enable connection logging for an existing AWS Client VPN endpoint
<a name="create-connection-log-existing"></a>

You can enable connection logging for an existing Client VPN endpoint by using the console or the command line.

**To enable connection logging for an existing Client VPN endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. Under **Connection logging**, turn on **Enable log details on client connections**.

1. For **CloudWatch Logs log group name**, choose the name of the CloudWatch Logs log group.

1. (Optional) For **CloudWatch Logs log stream name**, choose the name of the CloudWatch Logs log stream.

1. Choose **Modify Client VPN endpoint**.

**To enable connection logging for an existing Client VPN endpoint using the AWS CLI**
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command and specify the `--connection-log-options` parameter. You can specify the connection logs information in JSON format, as shown in the following example.

```
{
    "Enabled": true,
    "CloudwatchLogGroup": "ClientVpnConnectionLogs",
    "CloudwatchLogStream": "NewYorkOfficeVPN"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
