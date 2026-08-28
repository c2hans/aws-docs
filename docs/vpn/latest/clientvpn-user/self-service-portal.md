---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/self-service-portal.html
---

# Download the AWS Client VPN from the self-service portal
<a name="self-service-portal"></a>

The self-service portal is a web page that enables you to download the latest version of the AWS provided client and the latest versions of Client VPN endpoint configuration files. If your Client VPN endpoint administrator has preconfigured one or more configuration files for the Client VPN client, you can download and install that Client VPN application along with those configuration files, from this portal.

**Note**
If you're an administrator and want to configure the self-service portal, see [Client VPN endpoints](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html) in the *AWS Client VPN Administrator Guide*.

Before you begin, you must have the ID of each Client VPN endpoint you want to download Your Client VPN endpoint administrator can provide you with the ID, or can give you a self-service portal URL that includes the ID. For multiple endpoint connections you'll need the endpoint ID for each profile you want to connect to.

**To access the self-service portal**

1. Go to the self-service portal at [https://self-service.clientvpn.amazonaws.com/](https://self-service.clientvpn.amazonaws.com/), or use the URL that was provided to you by your administrator.

1. If required, enter the ID of the Client VPN endpoint, for example, `cvpn-endpoint-0123456abcd123456`. Choose **Next**.

1. Enter your user name and password and choose **Sign In**. This is the same user name and password that you use to connect to the Client VPN endpoint.

1. In the self-service portal, you can do the following:
   + Download the latest version of the client configuration file for the Client VPN endpoint. If you want to connect to multiple endpoints, you'll need to download the configuration file for each endpoint.
   + Download the latest version of the AWS provided client for your platform.

1. Repeat these steps for each endpoint configuration file you want to create a connection profile for.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
