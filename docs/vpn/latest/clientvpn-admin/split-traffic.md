---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-traffic.html
---

# Troubleshooting AWS Client VPN: Traffic is not being split between subnets
<a name="split-traffic"></a>

**Problem**
I am trying to split network traffic between two subnets. Private traffic should be routed through a private subnet, while internet traffic should be routed through a public subnet. However, only one route is being used even though I have added both routes to the Client VPN endpoint route table.

**Cause**
You can associate multiple subnets with a Client VPN endpoint, but you can associate only one subnet per Availability Zone. The purpose of multiple subnet association is to provide high availability and Availability Zone redundancy for clients. However, Client VPN does not enable you to selectively split traffic between the subnets that are associated with the Client VPN endpoint.

Clients connect to a Client VPN endpoint based on the DNS round-robin algorithm. This means that their traffic can be routed through any of the associated subnets when they establish a connection. Therefore, they might experience connectivity issues if they land on an associated subnet that does not have the required route entries.

For example, say that you configure the following subnet associations and routes:
+ Subnet associations
  + Association 1: Subnet-A (us-east-1a)
  + Association 2: Subnet-B (us-east-1b)
+ Routes
  + Route 1: 10.0.0.0/16 routed to Subnet-A
  + Route 2: 172.31.0.0/16 routed to Subnet-B

In this example, clients that land on Subnet-A when they connect cannot access Route 2, while clients that land on Subnet-B when they connect cannot access Route 1.

**Solution**
Verify that the Client VPN endpoint has the same route entries with targets for each associated network. This ensures that clients have access to all routes regardless of the subnet through which their traffic is routed.
