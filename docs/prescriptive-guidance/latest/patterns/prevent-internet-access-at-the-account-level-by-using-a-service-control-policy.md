---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/prevent-internet-access-at-the-account-level-by-using-a-service-control-policy.html
---

# Prevent internet access at the account level by using a service control policy
<a name="prevent-internet-access-at-the-account-level-by-using-a-service-control-policy"></a>

*Sergiy Shevchenko, Sean O'Sullivan, and Victor Mazeo Whitaker, Amazon Web Services*

## Summary
<a name="prevent-internet-access-at-the-account-level-by-using-a-service-control-policy-summary"></a>

Organizations frequently want to limit internet access for account resources that should remain private. In these accounts, the resources in virtual private clouds (VPCs) should not access the internet by any means. Many organizations choose a [centralized inspection architecture](https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-inspection-architecture-with-aws-gateway-load-balancer-and-aws-transit-gateway/). For the east-west (VPC-to-VPC) traffic in a centralized inspection architecture, you need to make sure that the spoke accounts and their resources do not have access to the internet. For north-south (internet egress and on-premises) traffic, you want to allow internet access only through the inspection VPC.

This pattern uses a [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to help prevent internet access. You can apply this SCP at the account or organizational unit (OU) level. The SCP limits internet connectivity by preventing the following:
+ Creating or attaching an IPv4 or IPv6 [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) that allows direct internet access to the VPC
+ Creating or accepting a [VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) that might allow indirect internet access through another VPC
+ Creating or updating an [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) configuration that might allow direct internet access to VPC resources

## Prerequisites and limitations
<a name="prevent-internet-access-at-the-account-level-by-using-a-service-control-policy-prereqs"></a>

**Prerequisites**
+ One or multiple AWS accounts managed as an organization in AWS Organizations.
+ [All features are enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in AWS Organizations.
+ [SCPs are enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_enable-disable.html) in the organization.
+ Permissions to:
  + Access the organization's management account.
  + Create SCPs. For more information about the minimum permissions, see [Creating an SCP](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_create.html#create-an-scp).
  + Attach the SCP to the target accounts or organizational units (OUs). For more information about the minimum permissions, see [Attaching and detaching service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_attach.html).

**Limitations**
+ SCPs don't affect users or roles in the management account. They affect only the member accounts in your organization.
+ SCPs affect only AWS Identity and Access Management (IAM) users and roles that are managed by accounts that are part of the organization. For more information, see [SCP effects on permissions](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html#scp-effects-on-permissions).

## Tools
<a name="prevent-internet-access-at-the-account-level-by-using-a-service-control-policy-tools"></a>

**AWS services**
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage. In this pattern, you use [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in AWS Organizations.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

## Best practices
<a name="prevent-internet-access-at-the-account-level-by-using-a-service-control-policy-best-practices"></a>

After establishing this SCP in your organization, make sure to update it frequently to address any new AWS services or features that might affect internet access.

## Epics
<a name="prevent-internet-access-at-the-account-level-by-using-a-service-control-policy-epics"></a>

### Create and attach the SCP
<a name="create-and-attach-the-scp"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the SCP. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/prevent-internet-access-at-the-account-level-by-using-a-service-control-policy.html) | AWS administrator |
| Attach the SCP. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/prevent-internet-access-at-the-account-level-by-using-a-service-control-policy.html) | AWS administrator |

## Related resources
<a name="prevent-internet-access-at-the-account-level-by-using-a-service-control-policy-resources"></a>
+ [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
+ [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
+ [Centralized inspection architecture with AWS Gateway Load Balancer and AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-inspection-architecture-with-aws-gateway-load-balancer-and-aws-transit-gateway/) (AWS blog post)
