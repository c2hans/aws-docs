---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/bring-your-own-vpc.html
---

# Bring your own VPC
<a name="bring-your-own-vpc"></a>

By default, Spatial Data Management on AWS creates a new Amazon Virtual Private Cloud (Amazon VPC) with all required subnets, NAT gateways, and VPC endpoints. If your organization already has a VPC, you can deploy the solution into it instead.

For full requirements and deployment instructions, see [Reuse existing networking infrastructure](reuse-existing-networking.md).

 **Key considerations when planning a deployment with an existing VPC:**
+ Your VPC must have DNS hostnames and DNS support enabled.
+ Your VPC must have isolated subnets (no internet route) and private subnets (NAT gateway route), each spanning at least 2 Availability Zones.
+ You must provide subnet IDs explicitly and pre-create all required VPC endpoints before deploying. The solution validates that they exist but does not create them.
+ The choice to use an existing VPC is permanent for the lifetime of the stack. Plan your networking configuration before the initial deployment.
+ The solution never modifies your existing VPC resources. It only creates new solution-owned security groups inside your VPC.
