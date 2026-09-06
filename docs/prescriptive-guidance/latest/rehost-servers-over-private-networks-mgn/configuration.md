---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/configuration.html
---

# Configuration best practices
<a name="configuration"></a>

This section describes the configuration for the most restrictive scenario (replication over private networks only), as shown in the first diagram, based on the considerations discussed earlier. You can configure both hybrid scenarios by skipping parts of the most restrictive configuration:
+ For the hybrid scenario that supports public HTTPS egress at the source and private staging area resources, the Amazon S3 interface VPC endpoint is not required.
+ For the hybrid scenario that supports public HTTPS egress at the source and public staging area resources, no VPC endpoints in the staging area subnet are required.

The following sections assume that the initial AWS Transform MGN configuration is already complete, as described in the blog posts [Accelerate your Migration with AWS Transform MGN](https://aws.amazon.com/blogs/mt/accelerate-your-migration-with-aws-application-migration-service/) and [How to Use the New AWS Transform MGN for Lift-and-Shift Migrations](https://aws.amazon.com/blogs/aws/how-to-use-the-new-aws-application-migration-service-for-lift-and-shift-migrations/)). This discussion focuses on components that are specific to the restrictive scenario, and assumes a private staging subnet that has no connectivity to the internet.

## Subnets and routing configurations
<a name="subnets"></a>

For the restrictive scenario, you configure the required AWS resources in the private subnet of a staging VPC. This subnet has no connectivity to the internet (there's no internet gateway attached to the routing table as a default route). Instead, it uses either a virtual gateway associated with an [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html) gateway (connected through an IPsec tunnel to an on-premises gateway), or it's connected to a transfer gateway or to AWS Direct Connect services to provide private interconnectivity to the on-premises data centers.

You will use that private subnet as a staging subnet for replication-related resources managed by MGN, and you'll configure all required network access through this subnet by using VPC endpoints, as discussed in the next section.

## VPC endpoints configuration
<a name="vpc-endpoints"></a>

You now need to create VPC endpoints in the staging subnet to provide connectivity for the replication servers and MGN Agents from on-premises subnets.

Here's a full list of VPC endpoints you need:
+ MGN and Amazon EC2 interface endpoints, which provide their own elastic network interfaces with private IP addresses and private DNS names to be used by both replication servers and Agents. (Agents will use only the MGN endpoint.)
+ Amazon S3 gateway endpoint that provides a specific route in the subnet route table (though a prefix list). This will be used by replication servers.
+ Amazon S3 interface endpoint that provides a specific elastic network interface with a dedicated private IP address in the private subnet. MGN Agents will use this address through a specific DNS name.

The next sections go into more detail about how VPC endpoints work. The following table lists all the endpoints created for the staging private subnet. (Note that the Amazon S3 gateway endpoint has no network interfaces provisioned but does have specific prefix lists provisioned into the subnet's route table, as will be described later in this guide.)

|
|
| AWS service | VPC endpoint type | Private DNS | Related subnet |
| --- |--- |--- |--- |
| **Amazon EC2** | Interface | Enabled | Staging private subnet |
| **AWS Transform MGN** | Interface | Enabled | Staging private subnet |
| **Amazon S3** | Interface | Not available | Staging private subnet |
| **Amazon S3** | Gateway | Not available | Connect to route table of the staging private subnet |

You can create optional VPC endpoints to enable access to Amazon EC2 instances on private isolated subnets through AWS Systems Manager, as discussed in [Creating VPC endpoints](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html#sysman-setting-up-vpc-create) in the Systems Manager documentation.

|
|
| AWS service | VPC endpoint type | Private DNS | Related subnet |
| --- |--- |--- |--- |
| **Systems Manager** | Interface | Enabled | Staging private subnet |
| **ssmmessages** | Interface | Enabled | Staging private subnet |
| **ec2messages** | Interface | Enabled | Staging private subnet |
| **AWS Key Management Service (AWS KMS)** | Interface | Enabled | Staging private subnet |
| **Logs** | Interface | Enabled | Staging private subnet |

## VPC interface endpoints
<a name="vpc-interface-endpoints"></a>

Creating an interface endpoint also creates a specific elastic network interface for each subnet that the given interface endpoint is provisioned for. For example, the MGN interface endpoint is provisioned in a private subnet in the staging VPC with an elastic network interface that is associated with the IP address inside that subnet, and it also has three DNS names resolvable from the subnet to this IP address:
+ A private DNS name, `mgn.<region>.amazonaws.com`
+ Two DNS names that are based on the endpoint ID (`vpce-xxx`), with and without the Region included in the name: `vpce-xxx-<region>.<service-name>` and `vpce-xxx.<service-name>`

This allows any instance running in the subnet that is using the default [Dynamic Host Configuration Protocol (DHCP) option set](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) configuration in the VPC, and has both [DNS attributes](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support) `enableDnsHostnames` and `enableDnsSupport` enabled, to:
+ Resolve the DNS name of MGN (`mgn.<region>.amazonaws.com`) to a private IP address assigned to the elastic network interface.
+ Connect to MGN by using the local network only.

That fixes connectivity for any instances running in the staging subnet (such as the MGN replication server or conversion server) for any AWS service that has interface endpoints provisioned in the subnet (such as Amazon EC2, MGN, Systems Manager, AWS KMS, and so on).

## VPC gateway endpoints
<a name="vpc-gateway-endpoints"></a>

For services such as Amazon S3 there's no fixed DNS name that can be provisioned, because each bucket has its own DNS name. For this scenario you will use VPC gateway endpoints.

Creating an Amazon S3 gateway endpoint also creates a specific prefix list object with a list of subnet destinations (in CIDR notation), which can be added in the subnet route table. Thus, DNS names of Amazon S3 buckets resolved to IP addresses included in this list would be accessible through internal connectivity.

When you provision an Amazon S3 gateway endpoint, you can specify the subnets in the route tables that should include that prefix list ID (`PL-<id>`). The resulting route table for the staging private subnet must include that prefix list ID, as in this example route table:

|
|
| Destination | Target |
| --- |--- |
| `pl-<id>` | `vpce-<id-of-S3-Gateway-VPC-endpoint>` |
| Any other routes (for example, source subnet CIDRs) | Any targets such as virtual gateway IDs |
| Local CIDR | `"local"` |

## DNS resolver inbound endpoints
<a name="dns-resolver-endpoints"></a>

The configuration described in the previous section is sufficient for instances that are running inside the AWS subnets, because they are already configured to use internal Amazon Route 53 DNS servers. However, on-premises source servers require additional steps to be able to communicate with AWS services privately. In particular, MGN Agent has to download the installer from Amazon S3 and then communicate with MGN by using DNS names provided in the [documentation](https://docs.aws.amazon.com/mgn/latest/ug/Network-Requirements.html#TCP-443). On-premises servers use their default DNS servers to resolve these DNS names, resulting in public IP addresses. Communications with these addresses over HTTPS/TCP port 443 are eventually blocked by corporate firewalls.

To prevent this, you need to configure source servers or their default DNS servers to use [Amazon Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) for resolution of these specific DNS names or a subdomain zone (that is, the full `*.<region>.amazonaws.com` zone) . This can be configured by creating a [Route 53 Resolver inbound endpoint](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html#resolver-overview-forward-network-to-vpc), which, like a VPC interface endpoint, has a dedicated elastic network interface created in the dedicated private subnet on AWS, and is thus able to forward DNS requests to Amazon Route 53 Resolver.

## Elastic network interface security groups
<a name="eni-security-groups"></a>

Each elastic network interface has a dedicated security group associated with it, which must permit traffic that's expected for this elastic network interface and corresponding endpoint. Thus, the DNS resolver endpoint's security group should permit inbound UDP port 53 (and sometimes TCP port 53) for DNS requests, and the endpoint security groups for most other services (MGN, Amazon EC2, Systems Manager, and so on) need inbound HTTPS/TCP port 443 enabled.

## Installing MGN Agent on source servers
<a name="installing-agent"></a>

To install MGN Agent on source servers, you need to supply the DNS names of the MGN and Amazon S3 interface endpoints to the Agent's command line parameters (see [Installing the Agent on a secured network](https://docs.aws.amazon.com/mgn/latest/ug/installing-agent-blocked.html) in the MGN documentation).

For the MGN endpoint, you can use any of the DNS names associated with it―a "Private DNS" field (`mgn.<region>.amazonaws.com`) or a VPC-specific DNS name (`vpce-<VPC-id>-<suffix>.mgn.<region>.vpce.amazonaws.com`)―and supply an argument: `--endpoint <FQDN>`. In fact, if you skip this argument, the Agent uses the specified AWS Region to reconstruct the default DNS FQDN (`mgn.<region>.amazonaws.com`) and uses the FQDN to access the MGN control plane. In most cases, that default behavior should suffice, as long as that FQDN resolves from the source server correctly to the private IP address of the elastic network interface for the MGN VPC endpoint created in the staging subnet.

The Amazon S3 interface endpoint won't have a single private DNS name (because each bucket will have its own), so that option isn't supported. However, an Amazon S3 interface endpoint still has an elastic network interface associated with it. It also has a specific private IP and wildcard DNS names (in the format `.vpce-<VPC-ID>-<suffix>.s3.<region>.vpce.amazonaws.com` or Region-specific .`vpce-<VPC-ID>-<suffix>-<region>.s3.<region>.vpce.amazonaws.com`) that are resolvable to this private IP.

That wildcard DNS name can be used for the `--s3-endpoint` argument, as in the following:

```
aws-replication-installer-init.py --region <region> --aws-access-key-id <MGN_IAM_ACCESS_KEY>  --aws-secret-access-key <MGN_IAM_SECRET> --no-prompt \
--endpoint vpce-<VPC-id>-<suffix>.mgn.<region>.vpce.amazonaws.com --s3-endpoint vpce-<VPC-ID>-<suffix>-<region>.s3.<region>.vpce.amazonaws.com
```

The next section provides an example of configuring MGN, including all required VPC endpoints, and deploying the Agents by using VPC endpoints on Windows and Linux source servers. The section covers both manual and automated deployment.
