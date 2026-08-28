---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/join-the-ecs-instance-host-to-the-domain.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Join the ECS instance (host) to the domain
<a name="join-the-ecs-instance-host-to-the-domain"></a>

 There are many ways to join the ECS instance to an Active Directory domain. It can be done manually (by connecting to the instance through RDP) or automatically. AWS enables you to save costs by automatically reducing compute capacity in times of low demand, and provision more capacity when demand increases. To take advantage of this elasticity, a best practice is to use Auto Scaling groups for provisioning ECS instances.

 The User Data section in the launch template/configuration that is used with the Auto Scaling group can include domain join commands. If your Active Directory domain is based on AWS Directory Service or you use AD Connector to connect to an on-premises Active Directory domain, you can use [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html) and run the [AWS-JoinDirectoryServiceDomain](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-systems-manager-dx-domain/) document. There are two prerequisites to using this approach that are described as follows.

1.  If the ECS instances and the Active Directory domain are provisioned in different VPCs, make sure they that the VPCs can communicate through [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) or [transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

1.  The ECS instances need permissions (through IAM policies) to communicate to the Systems Manager and Directory Service APIs. AWS recommends creating custom policies that take into account your system needs and security requirements. However, as a starting point, you can use the [following policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html):
   +  `AmazonSSMManagedInstanceCore` — This AWS managed policy enables an instance to use Systems Manager service core functionality.
   +  `AmazonSSMDirectoryServiceAccess` — This AWS managed policy allows AWS Systems Manager Agent (SSM Agent) to access AWS Directory Service on your behalf for requests to join the Active Directory domain by the managed instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
