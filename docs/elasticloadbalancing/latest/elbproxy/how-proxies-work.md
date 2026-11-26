---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/how-proxies-work.html
---

# How proxies work

A proxy is the single point of contact for clients. It runs the Envoy configuration that you provide. ELB for Envoy gives the proxy a unique DNS name that points to IP addresses in your VPC. The proxy is secured by the security groups you choose and uses the IP addressing you choose. The proxy runs on ELB for Envoy nodes that AWS manages. ELB for Envoy keeps the proxy highly available and scales it as traffic changes.

This section explains the networking, state, and addressing concepts behind a proxy. For the steps to create, update, or delete a proxy, see [Create a proxy](create-proxy.md), [Update proxy network settings](update-network-settings.md), and [Delete a proxy](delete-proxy.md).

## Architecture
<a name="how-proxies-work-architecture"></a>

Elastic Load Balancing for Envoy (ELB for Envoy) runs and operates the Envoy fleet, while the proxy's network interfaces and your targets live in your own account.

![Diagram titled Control plane vs. data plane. An AWS Region contains the AWS-owned ELB account with the AWS control plane, which handles lifecycle, scaling, and static configuration. Below it, your account and VPC span three Availability Zone subnets (us-east-1a, us-east-1b, us-east-1c). Each subnet holds one ELB for Envoy network interface in your subnet, inside a security group for the Envoy nodes; each network interface sends traffic to your applications, EKS pods and EC2 instances, inside a security group for the applications. The AWS control plane connects down to each network interface. On the left, three ways to supply configuration: the console or AWS CLI (static config through the API); your own xDS server, which Envoy connects to directly for routes and endpoints; and Envoy Gateway in your EKS cluster, whose controller calls the AWS API to create the proxy with configuration delivered over xDS. AWS runs the fleet, and your control plane talks to Envoy directly.](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/images/architecture.png)

Managed by AWS
AWS runs and operates the compute that serves your proxy configuration.

Your account and VPC
This account contains the proxy's data-plane network interfaces (ENIs) in your subnets and security groups, and your targets (such as Amazon EKS pods, Amazon EC2 instances, or target groups). It also contains your chosen control plane input: the Kubernetes Gateway API through the elb-envoy-remote-infra-provider controller, or the console, AWS CLI, or CloudFormation. Observability stays in your account: proxy logs in CloudWatch Logs under the log group `/aws/elb-proxy/{{proxy-name}}`, proxy metrics in CloudWatch, and AWS Health notices.

How traffic flows:

1. Clients connect to the proxy's DNS name from the internet or within your VPC.

1. Traffic enters through the data-plane ENIs in your subnets, subject to your security groups and, optionally, an AWS WAF web ACL.

1. The proxy runs your Envoy configuration and sends traffic to your targets.

### Ways to configure a proxy
<a name="how-proxies-work-config-options"></a>

You supply your proxy's Envoy configuration in one of three ways. All three run on the same ELB for Envoy fleet; they differ in where your configuration comes from.

Console, AWS CLI, or CloudFormation
You provide a static Envoy bootstrap configuration through the API, and you change it by updating the proxy. See [Create a proxy](create-proxy.md) and [Envoy configuration for ELB for Envoy](envoy-configuration.md).

Your own xDS control plane
You run an xDS control plane, and the proxy connects to it to receive listeners, routes, clusters, and endpoints at runtime, without a restart. See [Dynamic configuration (xDS)](how-envoy-runs.md#how-envoy-runs-xds).

Envoy Gateway on Amazon EKS
You manage your Gateways with the Kubernetes Gateway API. The elb-envoy-remote-infra-provider controller calls the ELB for Envoy API to create the proxy, and your configuration flows to it over xDS. See [Use ELB for Envoy with Kubernetes](kubernetes.md).

## Availability Zones and subnets
<a name="how-proxies-work-azs"></a>

ELB for Envoy deploys your proxy across the Availability Zones that correspond to the subnets you provide. You must specify at least two subnets in different Availability Zones for high availability. All subnets must belong to the same VPC.

When you use IPv6 or dualstack addressing, your subnets must have an IPv6 CIDR block associated. You can verify this by checking the `ipv6CidrBlockAssociationSet` field on your subnet with **aws ec2 describe-subnets**. For IPv6-only configurations (IPv4 set to `off`), you must use `ipv6Native` subnets. All other configurations require non-`ipv6Native` subnets.

You can update subnets after proxy creation. For instructions, see [Update proxy network settings](update-network-settings.md).

## Security groups
<a name="how-proxies-work-security-groups"></a>

You must provide at least one security group in the same VPC as your subnets. Security group rules control what traffic can reach your proxy and what traffic your proxy can send.

For IPv4 configurations, your security groups need inbound rules that allow IPv4 traffic on the ports your proxy listens on. For IPv6 or dualstack configurations, you also need inbound rules that allow IPv6 traffic. For example, use a `::/0` source for an internet-facing proxy, or your VPC's IPv6 CIDR for an internal proxy.

You can update security groups after proxy creation. For instructions, see [Update proxy network settings](update-network-settings.md).

## Proxy states
<a name="how-proxies-work-states"></a>

A proxy transitions through several states during its lifecycle. You can check the current state with **aws elb-proxy get-proxy** or **aws elb-proxy list-proxies**.

| State | Description |
| --- | --- |
| create-in-progress | The proxy is being provisioned. Networking is being configured. |
| active | The proxy is fully provisioned and serving traffic. |
| action-required | The proxy requires customer intervention. Check the status.reasons field for details. |
| create-failed | Proxy creation failed. Check the status.reasons field for details. |
| delete-in-progress | The proxy is being deleted. Resources are being cleaned up. |
| deleted | The proxy has been fully deleted. |

### action-required reasons
<a name="how-proxies-work-action-required"></a>

When a proxy is in the `action-required` state, read the `status.reasons` field (**aws elb-proxy get-proxy**) and match the reason to the following table.

| Reason | Cause | Fix |
| --- | --- | --- |
| `InvalidCustomerConfigurationContents` | ELB for Envoy (Envoy) rejected the configuration you submitted. The previous configuration keeps serving traffic. | Fix the configuration and submit it again. If you use a configuration archive, make sure bundled files are referenced by paths relative to the archive root. For more information, see [Configuration validation](how-envoy-runs.md#how-envoy-runs-validation). |
| `CustomerKmsKeyInaccessible` | ELB for Envoy can't use the customer managed key that encrypts the proxy's configuration, because the key is disabled, pending deletion, or its key policy no longer grants the service. | Re-enable the key or restore its key policy. For more information, see [When ELB for Envoy can't use your key](proxy-encryption.md#proxy-encryption-key-inaccessible). |
| `InsufficientFreeAddressesInSubnet` | A subnet the proxy uses doesn't have enough free IP addresses for new nodes. | Free up addresses in that subnet, or move the proxy to subnets in the same VPC that have more free addresses with [Update proxy network settings](update-network-settings.md). |
| `SecurityGroupsPerInterfaceLimitExceeded` | The proxy has more security groups than Amazon VPC allows per network interface. | Specify fewer security groups with [Update proxy network settings](update-network-settings.md), or request a quota increase. See [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). |
| `SecurityGroupRulesPerInterfaceLimitExceeded` | The proxy's security groups together have more rules than Amazon VPC allows on one network interface. | Remove rules from the security groups, or specify fewer security groups with [Update proxy network settings](update-network-settings.md). See [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). |
| `InvalidSubnetID.NotFound` | A subnet the proxy uses no longer exists. | Replace the deleted subnet with an existing subnet in the same VPC with [Update proxy network settings](update-network-settings.md). |
| `InvalidSecurityGroupID.NotFound` and `InvalidGroup.NotFound` | A security group the proxy uses no longer exists. | Specify existing security groups with [Update proxy network settings](update-network-settings.md). |
| `Gateway.NotAttached` | The proxy's VPC has no internet gateway, so ELB for Envoy can't assign public IP addresses to an internet-facing proxy. | Attach an internet gateway to the VPC and add a route to it in the proxy's subnets. See [Enable internet access for a VPC using an internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html). |
| `InvalidVpcID.NotFound` | The proxy's VPC no longer exists. | You can't move a proxy to another VPC. Delete the proxy with [Delete a proxy](delete-proxy.md), and create a new one in an existing VPC with [Create a proxy](create-proxy.md). |

For the Amazon EC2 provisioning reasons, the `message` is the Amazon EC2 error message, prefixed with the reason code in brackets (for example, `[InsufficientFreeAddressesInSubnet]`). ELB for Envoy retries provisioning automatically, and these reasons clear once a retry succeeds.

After you fix the cause, the proxy clears the `action-required` state automatically. Run **aws elb-proxy get-proxy** again to confirm the state is `active`.

## IP address types
<a name="how-proxies-work-ip-address-types"></a>

Each proxy is configured with an IPv4 and an IPv6 addressability setting. Each setting can be `off`, `internet-facing`, or `internal`. This determines how the proxy is reachable and what DNS records are published.
+ `internet-facing`: The proxy is reachable from the public internet over the given protocol.
+ `internal`: The proxy is reachable only from within the VPC over the given protocol.
+ `off`: The protocol is disabled.

IPv4 and IPv6 cannot both be `off` at the same time. Mixing `internet-facing` and `internal` across IPv4 and IPv6 is not supported.

The IP addressing configuration is immutable after proxy creation. To change it, you must create a new proxy.

The following table shows the DNS names that are published for each combination of IPv4 and IPv6 addressability, and whether the combination is valid. In the table, `A` is an IPv4 DNS record, `AAAA` is an IPv6 DNS record, and `A` \+ `AAAA` is both. `my-proxy` represents the proxy's `dnsName` returned by the API.

| IPv4 \\ IPv6 | OFF | INTERNAL | INTERNET-FACING |
| --- | --- | --- | --- |
| OFF | Not allowed | `internal-my-proxy` (`AAAA`)<br />`dualstack.internal-my-proxy` (`AAAA`) | `dualstack.my-proxy` (`AAAA`)<br />`my-proxy` (`AAAA`) |
| INTERNAL | `internal-my-proxy` (`A`)<br />`dualstack.internal-my-proxy` (`A`) | `internal-my-proxy` (`A` \+ `AAAA`)<br />`dualstack.internal-my-proxy` (`A` \+ `AAAA`) | Not allowed |
| INTERNET-FACING | `internal-my-proxy` (`A`)<br />`dualstack.my-proxy` (`A`)<br />`my-proxy` (`A`) | Not allowed | `internal-my-proxy` (`A`)<br />`dualstack.my-proxy` (`A` \+ `AAAA`)<br />`my-proxy` (`A` \+ `AAAA`) |

## IP address management
<a name="how-proxies-work-ip-management"></a>

ELB for Envoy manages IP addresses for your proxies based on your IP addressing configuration:
+ For IPv4 configurations, proxies receive private IPv4 addresses allocated from the subnet's primary CIDR block. Internet-facing proxies also receive a public IPv4 address.
+ For IPv6 configurations, proxies receive IPv6 addresses allocated from the subnet's IPv6 CIDR block. ELB for Envoy manages whether the address is publicly reachable or kept private, based on your addressability setting.
+ For dualstack configurations, both IPv4 and IPv6 addresses are allocated.

ELB for Envoy publishes these addresses to DNS.

## DNS names
<a name="how-proxies-work-dns"></a>

Each proxy receives a dedicated DNS name when you create it, returned in the `dnsName` field of the API response. This is the primary endpoint clients use to send traffic to your proxy.

Depending on the IP addressing configuration, ELB for Envoy can publish additional DNS name variants:
+ `dualstack.{{dnsName}}`: A variant that can resolve to `A` records, `AAAA` records, or both, depending on the IP addressing configuration.
+ `internal-{{dnsName}}`: Published for any configuration that includes IPv4, or when IPv6 is set to `internal`. For internal proxies, this is the primary DNS name. For internet-facing IPv4 proxies, this is an additional DNS name that lets clients within the VPC reach the proxy over private IPv4 addresses without routing through the public internet.

For the full mapping of configurations to DNS names and record types, see the table in [IP address types](#how-proxies-work-ip-address-types).

You can use **dig** to verify that your proxy's DNS names resolve. Run the following commands, and replace {{dnsName}} with the value from the `dnsName` field.

```bash
# Resolve IPv4 addresses (A records)
dig A <dnsName>

# Resolve IPv6 addresses (AAAA records)
dig AAAA <dnsName>
```

Replace {{dnsName}} with the DNS name returned in the `dnsName` field of the API response.

## Connection tracking timeouts
<a name="how-proxies-work-timeouts"></a>

Some network configurations that the service applies to your proxy limit the values that take effect in Envoy. The following timeouts apply to any connection or flow that requires Amazon EC2 security group connection tracking. These values are not configurable.

| Timeout | Value | Applies to |
| --- | --- | --- |
| TCP established connection idle timeout | 4,000 seconds | Any connection that requires Amazon EC2 security group connection tracking. You can set TCP connection timeouts in Envoy, but this service limit can prevent very high values from taking effect. |
| UDP timeout | 30 seconds | Any single-direction or single request-response flow that requires Amazon EC2 security group connection tracking. |
| UDP stream timeout | 60 seconds | Any flow that requires Amazon EC2 security group connection tracking. You can set the UDP idle\_timeout in Envoy, but this service limit can prevent an increased value from taking effect. |
