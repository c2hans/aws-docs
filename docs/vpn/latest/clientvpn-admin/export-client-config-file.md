---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/export-client-config-file.html
---

# Export the AWS Client VPN client configuration file
<a name="export-client-config-file"></a>

You can export the Client VPN client configuration by using the console or the AWS CLI.

**To export client configuration (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to download the client configuration and choose **Download Client Configuration**.

**To export client configuration (AWS CLI)**
Use the [export-client-vpn-client-configuration](https://docs.aws.amazon.com/cli/latest/reference/ec2/export-client-vpn-client-configuration.html) command and specify the output file name.

```
$ aws ec2 export-client-vpn-client-configuration --client-vpn-endpoint-id {{endpoint_id}} --output text>{{config_filename}}.ovpn
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
