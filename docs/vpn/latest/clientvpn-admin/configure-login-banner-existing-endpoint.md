---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/configure-login-banner-existing-endpoint.html
---

# Configure a client login banner for an existing AWS Client VPN endpoint
<a name="configure-login-banner-existing-endpoint"></a>

Use the following steps to configure a client login banner for an existing Client VPN endpoint.

**Enable client login banner on a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint that you want to modify, choose **Actions**, and then choose **Modify Client VPN Endpoint**.

1. Scroll down the page to the **Other parameters** section.

1. Turn on **Enable client login banner**.

1. For **Client login banner text**, enter the text that will be displayed in a banner on AWS provided clients when a VPN session is established. Use UTF-8 encoded characters only, with a maximum of 1400 characters allowed.

1. Choose **Modify Client VPN endpoint**.

**Enable client login banner on a Client VPN endpoint (AWS CLI)**
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
