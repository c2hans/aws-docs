---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-modify.html
---

# Modify an AWS Client VPN endpoint
<a name="cvpn-working-endpoint-modify"></a>

You can modify a Client VPN endpoint by using the Amazon VPC Console or the AWS CLI. For more information about the fields you can Client VPN fields you can modify, see [Endpoint modification](cvpn-working-endpoints.md#cvpn-endpoints-modify-req).

## Limitations
<a name="endpoints-limits"></a>

The following limitations apply when modifying an endpoint
+  Modifications to Client VPN endpoints, including Certificate Revocation List (CRL) changes, will take effect up to 4 hours after a request is accepted by the Client VPN service.
+ You cannot modify the client IPv4 CIDR range, authentication options, client certificate or transport protocol after the Client VPN endpoint has been created.
+ You can modify existing IPv4 endpoints to dual-stack for both endpoint IP and traffic IP types. If you need IPv6-only for endpoint IP and traffic IP, you must create a new endpoint.
+ Client VPN does not support modification of endpoint type (IPv4, IPv6, dual-stack) or traffic type (IPv4, IPv6, dual-stack) after creation.
+ Modifying a Client VPN with a specific combination of endpoint type and traffic type is not supported. You cannot change to any other combination. The endpoint must be deleted and recreated with the desired configuration.
+ Client-to-client communication for IPv6 traffic is not supported.

## Modify a Client VPN endpoint
<a name="endpoint-modify"></a>

You can modify a Client VPN endpoint using either the console or the AWS CLI.

**To modify a Client VPN endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to modify, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. For **Description**, enter a brief description for the Client VPN endpoint.

1. For **Endpoint IP address type**, you can modify an existing IPv4 endpoint to dual-stack. This option is only available for IPv4 endpoints.

1. For **Traffic IP address type**, you can modify an existing IPv4 endpoint to dual-stack. This option is only available for IPv4 endpoints.

1. For **Server certificate ARN**, specify the ARN for the TLS certificate to be used by the server. Clients use the server certificate to authenticate the Client VPN endpoint to which they are connecting.
**Note**
The server certificate must be present in AWS Certificate Manager (ACM) in the region you are creating the Client VPN endpoint. The certificate can either be provisioned with ACM or imported into ACM.

1. Specify whether to log data about client connections using Amazon CloudWatch Logs. For **Enable log details on client connections**, do one of the following:
   + To activate client connection logging, turn on **Enable log details on client connections**. For **CloudWatch Logs log group name**, select the name of the log group to use. For **CloudWatch Logs log stream name**, select the name of the log stream to use, or leave this option blank to let us create a log stream for you.
   + To deactivate client connection logging, turn off **Enable log details on client connections**.

1. For **Client connect handler**, to activate the [client connect handler](connection-authorization.md) turn on **Enable client connect handler**. For **Client Connect Handler ARN**, specify the Amazon Resource Name (ARN) of the Lambda function that contains the logic that allows or denies connections.

1. Turn on or off **Enable DNS servers**. To use custom DNS servers, for **DNS Server 1 IP address** and **DNS Server 2 IP address**, specify the IPv4 addresses of the DNS servers to use. For IPv6 or dual-stack endpoints, you can also specify **DNS Server IPv6 1** and **DNS Server IPv6 2** addresses. To use VPC DNS server, for either **DNS Server 1 IP address** or **DNS Server 2 IP address**, specify the IP addresses, and add the VPC DNS server IP address.
**Note**
Verify that the DNS servers can be reached by clients.

1. Turn on or off **Enable split-tunnel**. By default, split-tunnel on a VPN endpoint is off.

1. For **VPC ID**, choose the VPC to associate with the Client VPN endpoint. For **Security Group IDs**, choose one or more of the VPC's security groups to apply to the Client VPN endpoint.

1. For **VPN port**, choose the VPN port number. The default is 443.

1. To generate a [self-service portal URL](cvpn-self-service-portal.md) for clients, turn on **Enable self-service portal**.

1. For **Session timeout hours**, choose the desired maximum VPN session duration time in hours from the available options, or leave set to default of 24 hours.

1. For **Disconnect on session timeout**, choose if you want to terminate the session when the maximum session time is reached. Choosing this option requires that users reconnect manually to the endpoint when the session times out; otherwise, Client VPN will automatically try to reconnect.

1. Turn on or off **Enable client login banner**. If you want to use the client login banner, enter the text that will be displayed in a banner on AWS provided clients when a VPN session is established. UTF-8 encoded characters only. Maximum of 1400 characters.

1. Choose **Modify Client VPN endpoint**.

**To modify a Client VPN endpoint using the AWS CLI**
Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.

Example for modifying an IPv4 endpoint to dual-stack:

```
aws ec2 modify-client-vpn-endpoint \
  --client-vpn-endpoint-id cvpn-endpoint-123456789123abcde \
  --endpoint-ip-address-type "dual-stack" \
  --traffic-ip-address-type "dual-stack" \
  --client-cidr-block "172.31.0.0/16"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
