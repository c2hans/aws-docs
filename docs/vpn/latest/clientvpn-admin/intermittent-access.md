---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/intermittent-access.html
---

# Troubleshooting AWS Client VPN: Access to a peered VPC, Amazon S3, or the internet is intermittent
<a name="intermittent-access"></a>

**Problem**
I have intermittent connectivity issues when connecting to a peered VPC, Amazon S3, or the internet, but access to associated subnets is unaffected. I need to disconnect and reconnect in order to resolve the connectivity issues.

**Cause**
Clients connect to a Client VPN endpoint based on the DNS round-robin algorithm. This means that their traffic can be routed through any of the associated subnets when they establish a connection. Therefore, they might experience connectivity issues if they land on an associated subnet that does not have the required route entries.

**Solution**
Verify that the Client VPN endpoint has the same route entries with targets for each associated network. This ensures that clients have access to all routes regardless of the associated subnet through which their traffic is routed.

For example, say that your Client VPN endpoint has three associated subnets (Subnet A, B, and C), and you want to enable internet access for your clients. To do this, you must add three `0.0.0.0/0` routes - one that targets each associated subnet:
+ Route 1: `0.0.0.0/0` for Subnet A
+ Route 2: `0.0.0.0/0` for Subnet B
+ Route 3: `0.0.0.0/0` for Subnet C
