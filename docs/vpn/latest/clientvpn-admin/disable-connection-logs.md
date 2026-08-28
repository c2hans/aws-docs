---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/disable-connection-logs.html
---

# Turn off AWS Client VPN connection logging
<a name="disable-connection-logs"></a>

You can turn off connection logging for a Client VPN endpoint by using the console or the command line. When you turn off connection logging, existing connection logs in CloudWatch Logs are not deleted.

**To turn off connection logging using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. Under **Connection logging**, turn off **Enable log details on client connections**.

1. Choose **Modify Client VPN endpoint**.

**To turn off connection logging using the AWS CLI**
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command, and specify the `--connection-log-options` parameter. Ensure that `Enabled` is set to `false`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
