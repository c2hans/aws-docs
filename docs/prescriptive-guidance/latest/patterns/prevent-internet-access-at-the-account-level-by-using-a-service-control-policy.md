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
| Create the SCP. | 1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in to the organization’s management account.<br />2. In the left pane, choose **Policies**.<br />3. On the policies page, choose **Service control policies**.<br />4. On the **Service control policies** page, choose **Create policy**.<br />5. On the **Create new service control policy** page, enter a **Policy name** and an optional **Policy description**.<br />6. (Optional) Add [AWS tags](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) to your policy.<br />7. In the JSON editor, delete the placeholder policy.<br />8. Paste the following policy into the JSON editor.<pre>{<br />  "Version": "2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "ec2:AttachInternetGateway",<br />        "ec2:CreateInternetGateway",        <br />        "ec2:CreateVpcPeeringConnection",<br />        "ec2:AcceptVpcPeeringConnection",<br />        "ec2:CreateEgressOnlyInternetGateway"<br />      ],<br />      "Resource": "*",<br />      "Effect": "Deny"<br />    },<br />    {<br />      "Action": [<br />        "globalaccelerator:Create*",<br />        "globalaccelerator:Update*"<br />      ],<br />      "Resource": "*",<br />      "Effect": "Deny"<br />    }<br />  ]<br />}</pre><br />9. Choose **Create policy**. | AWS administrator |
| Attach the SCP. | 1. On the **Service control policies** page, choose the policy you created.<br />2. On the **Targets** tab, choose **Attach**.<br />3. Select the OU or account that you want to attach the policy to. You might have to expand the OUs to find the OU or account that you want.<br />4. Choose **Attach policy**. | AWS administrator |

## Related resources
<a name="prevent-internet-access-at-the-account-level-by-using-a-service-control-policy-resources"></a>
+ [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
+ [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
+ [Centralized inspection architecture with AWS Gateway Load Balancer and AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-inspection-architecture-with-aws-gateway-load-balancer-and-aws-transit-gateway/) (AWS blog post)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
