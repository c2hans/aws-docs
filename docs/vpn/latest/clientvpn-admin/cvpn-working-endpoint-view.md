---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-view.html
---

# View AWS Client VPN endpoints
<a name="cvpn-working-endpoint-view"></a>

You can view information about Client VPN endpoints by using the Amazon VPC Console or the AWS CLI.

**To view Client VPN endpoints (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to view.

1. Use the **Details**, **Target network associations**, **Security groups**, **Authorization rules**, **Route table**, **Connections** and **Tags** tabs to view information about existing Client VPN endpoints.

   You can also use filters to help refine your search.

**To view Client VPN endpoints (AWS CLI)**
Use the [describe-client-vpn-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-endpoints.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
