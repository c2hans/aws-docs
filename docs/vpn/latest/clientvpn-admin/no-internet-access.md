---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/no-internet-access.html
---

# Troubleshooting AWS Client VPN: Clients can't access a peered VPC, Amazon S3, or the internet
<a name="no-internet-access"></a>

**Problem**
I have properly configured my Client VPN endpoint routes, but my clients can't access a peered VPC, Amazon S3, or the internet.

**Solution**
The following flow chart contains the steps to diagnose internet, peered VPC, and Amazon S3 connectivity issues.

![Client VPN troubleshooting steps](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/cvpn-flow.png)

1. For access to the internet, add an authorization rule for `0.0.0.0/0`.

   For access to a peered VPC, add an authorization rule for the IPv4 CIDR range of the VPC.

   For access to S3, specify the IP address of the Amazon S3 endpoint.

1. Check whether you are able to resolve the DNS name.

   If you are unable to resolve the DNS name, verify that you have specified the DNS servers for the Client VPN endpoint. If you manage your own DNS server, specify its IP address. Verify that the DNS server is accessible from the VPC.

   If you're unsure about which IP address to specify for the DNS servers, specify the VPC DNS resolver at the .2 IP address in your VPC.

1. For internet access, check if you are able to ping a public IP address or a public website, for example, `amazon.com`. If you do not get a response, make sure that the route table for the associated subnets has a default route that targets either an internet gateway or a NAT gateway. If the route is in place, verify that the associated subnet does not have network access control list rules that block inbound and outbound traffic.

   If you are unable to reach a peered VPC, verify that the associated subnet's route table has a route entry for the peered VPC.

   If you are unable to reach Amazon S3, verify that the associated subnet's route table has a route entry for the gateway VPC endpoint.

1. Check whether you can ping a public IP address with a payload larger than 1400 bytes. Use one of the following commands:
   + Windows

     ```
     C:\> ping  8.8.8.8 -l 1480 -f
     ```
   + Linux

     ```
     $ ping -s 1480 8.8.8.8 -M do
     ```

   If you cannot ping an IP address with a payload larger than 1400 bytes, open the Client VPN endpoint `.ovpn` configuration file using your preferred text editor, and add the following.

   ```
   mssfix 1328
   ```
