---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-create.html
---

# Create an AWS Client VPN endpoint
<a name="cvpn-working-endpoint-create"></a>

Create a AWS Client VPN endpoint to enable your clients to establish a VPN session using either the Amazon VPC Console or the AWS CLI.Client VPN supports all combinations of endpoint type (split-tunnel and full-tunnel) with traffic type (IPv4, IPv6, and dual-stack) during initial creation.

Before creating an endpoint, familiarize yourself with the requirements. For more information, see [Requirements for creating Client VPN endpoints](cvpn-working-endpoints.md#cvpn-working-create-req).

**To create a Client VPN endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints** and then choose **Create Client VPN Endpoint**.

1. Under "Choose setup method", select one of the following:
   + Quickstart - Create an endpoint with AWS-recommended defaults
   + Standard - Manually configure all settings for the endpoint

**Quickstart setup:**

1. For "Choose setup method", select Quickstart.

1.  For "Client IPv4 CIDR", enter the IP address range from which to assign client IP addresses. AWS recommends using a /22 CIDR block (for example, 10.0.0.0/22).

1.  For "VPC", select the VPC to associate with the Client VPN endpoint.

1.  For "Subnets", select one or more subnets in the VPC. These subnets will be used for target network associations.

1.  For Server certificate ARN, specify the ARN for the TLS certificate to be used by the server. Clients use the server certificate to authenticate the Client VPN endpoint to which they are connecting.

1.  Choose "Create Client VPN endpoint".

AWS automatically creates the following resources:
+ Authorization rule allowing all users to access the VPC CIDR
+ Target network association with the selected VPC subnets
+ Route table entries for the VPC CIDR

 After the endpoint is created, you can download the client configuration file from the endpoint details page and distribute it to your users along with the client certificate and key.

**Standard setup:**

1. For "Choose setup method", select Standard.

1. (Optional) Provide a name tag and description for the Client VPN endpoint.

1. For **Endpoint IP address type**, choose the IP address type for the endpoint:
   + **IPv4**: The endpoint uses IPv4 addresses for outer VPN tunnel traffic.
   + **IPv6**: The endpoint uses IPv6 addresses for outer VPN tunnel traffic.
   + **Dual-stack**: The endpoint uses both IPv4 and IPv6 addresses for outer VPN tunnel traffic.

1. For **Traffic IP address type**, choose the IP address type for traffic flowing through the endpoint:
   + **IPv4**: The endpoint supports IPv4 traffic only.
   + **IPv6**: The endpoint supports IPv6 traffic only.
   + **Dual-stack**: The endpoint supports both IPv4 and IPv6 traffic.

1. For **Client IPv4 CIDR**, specify an IP address range, in CIDR notation, from which to assign client IP addresses. For example, `10.0.0.0/22`. This is required if you selected IPv4 or Dual-stack for the Traffic IP address type.
**Note**
The address range cannot overlap with the target network address range, the VPC address range or any of the routes that will be associated with the Client VPN endpoint. The client address range must be at minimum /22 and not greater than /12 CIDR block size. You cannot change the client address range after you create the Client VPN endpoint.
When you select IPv6 as the endpoint IP address type, the Client IPv4 CIDR field is disabled. The Client VPN endpoint allocates client IPv6 addresses from an associated subnet, and you can associate the subnet after creating the endpoint.
**Note**
For IPv6 traffic, you do not need to specify a client CIDR range. Amazon automatically assigns IPv6 CIDR ranges for clients.

1. For **Server certificate ARN**, specify the ARN for the TLS certificate to be used by the server. Clients use the server certificate to authenticate the Client VPN endpoint to which they are connecting.
**Note**
The server certificate must be present in AWS Certificate Manager (ACM) in the region you are creating the Client VPN endpoint. The certificate can either be provisioned with ACM or imported into ACM.
For the steps to provision or import a certificate into ACM, see [AWS Certificate Manager Certificates](https://docs.aws.amazon.com/acm/latest/userguide/gs.html) in the *AWS Certificate Manager User Guide*.

1. Specify the authentication method to be used to authenticate clients when they establish a VPN connection. You must select an authentication method.
   + To use user-based authentication, select **Use user-based authentication**, and then choose one of the following:
     + **Active Directory authentication**: Choose this option for Active Directory authentication. For **Directory ID**, specify the ID of the Active Directory to use.
     + **Federated authentication**: Choose this option for SAML-based federated authentication.

       For **SAML provider ARN**, specify the ARN of the IAM SAML identity provider.

       (Optional) For **Self-service SAML provider ARN**, specify the ARN of the IAM SAML identity provider that you created to [support the self-service portal](federated-authentication.md#saml-self-service-support), if applicable.
   + To use mutual certificate authentication, select **Use mutual authentication**, and then for **Client certificate ARN**, specify the ARN of the client certificate that's provisioned in AWS Certificate Manager (ACM).
**Note**
If the server and client certificates have been issued by the same Certificate Authority (CA), you can use the server certificate ARN for both server and client. If the client certificate was issued by a different CA, then the client certificate ARN should be specified.

1. (Optional) For **Connection logging**, specify whether to log data about client connections using Amazon CloudWatch Logs. Turn on **Enable log details on client connections**. For **CloudWatch Logs log group name**, enter the name of the log group to use. For **CloudWatch Logs log stream name**, enter the name of the log stream to use, or leave this option blank to let us create a log stream for you.

1. (Optional) For **Client Connect Handler**, turn on **Enable client connect handler** to run custom code that allows or denies a new connection to the Client VPN endpoint. For **Client Connect Handler ARN**, specify the Amazon Resource Name (ARN) of the Lambda function that contains the logic that allows or denies connections.

1. (Optional) Specify which DNS servers to use for DNS resolution. To use custom DNS servers, for **DNS Server 1 IP address** and **DNS Server 2 IP address**, specify the IPv4 addresses of the DNS servers to use. For IPv6 or dual-stack endpoints, you can also specify **DNS Server IPv6 1** and **DNS Server IPv6 2** addresses. To use VPC DNS server, for either **DNS Server 1 IP address** or **DNS Server 2 IP address**, specify the IP addresses, and add the VPC DNS server IP address.
**Note**
Verify that the DNS servers can be reached by clients.

1. (Optional) By default, the Client VPN endpoint uses the `UDP` transport protocol. To use the `TCP` transport protocol instead, for **Transport Protocol**, select **TCP**.
**Note**
UDP typically offers better performance than TCP. You cannot change the transport protocol after you create the Client VPN endpoint.

1. (Optional) To have the endpoint be a split-tunnel Client VPN endpoint, turn on **Enable split-tunnel**. By default, split-tunnel on a Client VPN endpoint is disabled.

1. (Optional) For **VPC ID**, choose the VPC to associate with the Client VPN endpoint. For **Security Group IDs**, choose one or more of the VPC's security groups to apply to the Client VPN endpoint.

1. (Optional) For **VPN port**, choose the VPN port number. The default is 443.

1. (Optional) To generate a [self-service portal URL](cvpn-self-service-portal.md) for clients, turn on **Enable self-service portal**.

1. (Optional) For **Session timeout hours**, choose the desired maximum VPN session duration time in hours from the available options, or leave set to default of 24 hours.

1. (Optional) For **Disconnect on session timeout**, choose if you want to terminate the session when the maximum session time is reached. Choosing this option requires that users reconnect manually to the endpoint when the session times out; otherwise, Client VPN will automatically try to reconnect.

1. (Optional) Specify whether to enable client login banner text. Turn on **Enable client login banner**. For **Client login banner text**, enter the text that will be displayed in a banner on AWS provided clients when a VPN session is established. UTF-8 encoded characters only. Maximum of 1400 characters.

1. Choose **Create Client VPN endpoint**.

After you create the Client VPN endpoint, do the following to complete the configuration and enable clients to connect:
+ The initial state of the Client VPN endpoint is `pending-associate`. Clients can only connect to the Client VPN endpoint after you associate the first [target network](cvpn-working-target-associate.md).
+ Create an [authorization rule](cvpn-working-rules.md) to specify which clients have access to the network.
+ Download and prepare the Client VPN endpoint [configuration file](cvpn-working-endpoint-export.md) to distribute to your clients.
+ Instruct your clients to use the AWS provided client or another OpenVPN-based client application to connect to the Client VPN endpoint. For more information, see the [AWS Client VPN User Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/).

**To create a Client VPN endpoint using the AWS CLI**
Use the [create-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-client-vpn-endpoint.html) command.

Example for creating an IPv4 endpoint:

```
aws ec2 create-client-vpn-endpoint \
  --client-cidr-block "172.31.0.0/16" \
  --server-certificate-arn arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
  --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE} \
  --connection-log-options Enabled=false
```

Example for creating an IPv6 endpoint:

```
aws ec2 create-client-vpn-endpoint \
  --endpoint-ip-address-type "ipv6" \
  --traffic-ip-address-type "ipv6" \
  --server-certificate-arn arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
  --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE} \
  --connection-log-options Enabled=false
```

Example for creating a dual-stack endpoint:

```
aws ec2 create-client-vpn-endpoint \
  --endpoint-ip-address-type "dual-stack" \
  --traffic-ip-address-type "dual-stack" \
  --client-cidr-block "172.31.0.0/16" \
  --server-certificate-arn arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
  --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE} \
  --connection-log-options Enabled=false
```
