---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/ug/access-management-overview.html
---

# Manage access to VPC Lattice services
<a name="access-management-overview"></a>

VPC Lattice is secure by default because you must be explicit about which services and resource configurations to provide access to and with which VPCs. You can access services through a VPC association or a VPC endpoint of type service network. For multi-account scenarios, you can use [AWS Resource Access Manager](sharing.md) to share services, resource configurations, and service networks across account boundaries.

 VPC Lattice provides a framework that lets you implement a defense-in-depth strategy at multiple layers of the network.
+ **First layer** – The service, resource, VPC, and VPC endpoint association with a service network. A VPC may be connected to a service network either though an association or through a VPC endpoint. If a VPC is not connected to a service network, clients in the VPC cannot access the service and resource configurations that are associated with the service network.
+ **Second layer** – Optional network-level security protections for the service network, such as security groups and network ACLs. By using these, you can allow access to specific groups of clients in a VPC instead of all clients in the VPC.
+ **Third layer** – Optional VPC Lattice auth policy. You can apply an auth policy to service networks and individual services. Typically, the auth policy on the service network is operated by the network or cloud administrator, and they implement coarse-grained authorization. For example, allowing only authenticated requests from a specific organization in AWS Organizations. For an auth policy at the service level, typically the service owner sets fine-grained controls, which might be more restrictive than the coarse-grained authorization applied at the service network level.
**Note**
The auth policy on the service network doesn’t apply to resource configurations in the service network.

**Methods of access control**
+ [Auth policies](auth-policies.md)
+ [Security groups](security-groups.md)
+ [Network ACLs](network-acls.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
