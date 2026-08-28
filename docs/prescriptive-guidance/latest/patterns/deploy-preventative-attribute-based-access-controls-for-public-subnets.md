---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-preventative-attribute-based-access-controls-for-public-subnets.html
---

# Deploy preventative attribute-based access controls for public subnets
<a name="deploy-preventative-attribute-based-access-controls-for-public-subnets"></a>

*Joel Alfredo Nunez Gonzalez and Samuel Ortega Sancho, Amazon Web Services*

## Summary
<a name="deploy-preventative-attribute-based-access-controls-for-public-subnets-summary"></a>

In centralized network architectures, inspection and edge virtual private clouds (VPCs) concentrate all inbound and outbound traffic, such as traffic to and from the internet. However, this can create bottlenecks or result in reaching the limits of AWS service quotas. Deploying network edge security alongside the workloads in their VPCs provides unprecedented scalability in comparison to the more common, centralized approach. This is called a *distributed edge* architecture.

Although deploying public subnets in workload accounts can provide benefits, it also introduces new security risks because it increases the attack surface. We recommend that you deploy only Elastic Load Balancing (ELB) resources, such as Application Load Balancers, or NAT gateways in the public subnets of these VPCs. Using load balancers and NAT gateways in dedicated public subnets helps you implement fine-grained control for inbound and outbound traffic.

*Attribute-based access control* (ABAC) is the practice of creating fine-grained permissions based on user attributes, such as department, job role, and team name. For more information, see [ABAC for AWS](https://aws.amazon.com/identity/attribute-based-access-control/). ABAC can provide guardrails for public subnets in workload accounts. This helps application teams be agile, without compromising the security of the infrastructure.

This pattern describes how to help secure public subnets by implementing ABAC through a [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in AWS Organizations and [policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in AWS Identity and Access Management (IAM). You apply the SCP to either a member account of an organization or to an organizational unit (OU). These ABAC policies permit users to deploy NAT gateways in the target subnets and prevent them from deploying other Amazon Elastic Compute Cloud (Amazon EC2) resources, such as EC2 instances and elastic network interfaces.

## Prerequisites and limitations
<a name="deploy-preventative-attribute-based-access-controls-for-public-subnets-prereqs"></a>

**Prerequisites**
+ An organization in AWS Organizations
+ Administrative access to the AWS Organizations root account
+ In the organization, an active member account or OU for testing the SCP

**Limitations**
+ The SCP in this solution doesn’t prevent AWS services that use a service-linked role from deploying resources in the target subnets. Examples of these services are Elastic Load Balancing (ELB), Amazon Elastic Container Service (Amazon ECS), and Amazon Relational Database Service (Amazon RDS). For more information, see [SCP effects on permissions](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html#scp-effects-on-permissions) in the AWS Organizations documentation. Implement security controls to detect these exceptions.

## Architecture
<a name="deploy-preventative-attribute-based-access-controls-for-public-subnets-architecture"></a>

**Target technology stack**
+ SCP applied to an AWS account or OU in AWS Organizations
+ The following IAM roles:
  + `AutomationAdminRole` – Used to modify subnet tags and create VPC resources after implementing the SCP
  + `TestAdminRole` – Used to test whether the SCP is preventing other IAM principals, including those with administrative access, from performing the actions reserved for the `AutomationAdminRole`

**Target architecture**

![The tags prevent users from deploying resources other than NAT gateways in public subnets](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/25f22f67-5bb6-42ac-8fd6-836e00c436f1/images/b8345c8c-0fc5-46a3-be60-c171979cf979.png)

1. You create the `AutomationAdminRole` IAM role in the target account. This role has permissions to manage networking resources. Note the following permissions that are exclusive to this role:
   + This role can create VPCs and public subnets.
   + This role can modify the tag assignments for the target subnets.
   + This role can manage its own permissions.

1. In AWS Organizations, you apply the SCP to the target AWS account or OU. For a sample policy, see [Additional information](#deploy-preventative-attribute-based-access-controls-for-public-subnets-additional) in this pattern.

1. A user or a tool in the CI/CD pipeline can assume the `AutomationAdminRole` role to apply the `SubnetType` tag to the target subnets.

1. By assuming other IAM roles, authorized IAM principals in your organization can manage NAT gateways in the target subnets and other permitted networking resources in the AWS account, such as route tables. Use IAM policies to grant these permissions. For more information, see [Identity and access management for Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html).

**Automation and scale**

To help protect public subnets, the corresponding [AWS tags](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) must be applied. After applying the SCP, NAT gateways are the only kind of Amazon EC2 resource that authorized users can create in subnets that have the `SubnetType:IFA` tag. (`IFA` means *internet-facing assets*.) The SCP prevents the creation of other Amazon EC2 resources, such as instances and elastic network interfaces. We recommend that you use a CI/CD pipeline that assumes the `AutomationAdminRole` role to create VPC resources so that these tags are properly applied to public subnets.

## Tools
<a name="deploy-preventative-attribute-based-access-controls-for-public-subnets-tools"></a>

**AWS services**
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage. In AWS Organizations, you can implement [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), which are a type of policy that you can use to manage permissions in your organization.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

## Epics
<a name="deploy-preventative-attribute-based-access-controls-for-public-subnets-epics"></a>

### Apply the SCP
<a name="apply-the-scp"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a test admin role.  | Create an IAM role named `TestAdminRole` in the target AWS account. Attach the **AdministratorAccess** AWS managed IAM policy to the new role. For instructions, see [Creating a role to delegate permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the IAM documentation. | AWS administrator |
| Create the automation admin role. | 1. Create an IAM role named `AutomationAdminRole` in the target AWS account.<br />2. Attach the **AdministratorAccess** AWS managed IAM policy to the new role.The following is an example of a trust policy that you could use to test the role from the `111122223333` account.<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Principal": {<br />                "AWS": [<br />                    "arn:aws:iam::111122223333:root"<br />                ]<br />            },<br />            "Action": "sts:AssumeRole",<br />            "Condition": {}<br />        }<br />    ]<br />}</pre> | AWS administrator |
| Create and attach the SCP. | 1. Using the sample code provided in the [Additional information](#deploy-preventative-attribute-based-access-controls-for-public-subnets-additional) section, create a security control policy. For instructions, see [Creating an SCP](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_create.html#create-an-scp) in the AWS Organizations documentation.<br />2. Attach the SCP to the target AWS account or OU. For instructions, see [Attaching and detaching service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_attach.html) in the AWS Organizations documentation. | AWS administrator |

### Test the SCP
<a name="test-the-scp"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC or subnet. | 1. Assume the `TestAdminRole` role in the target AWS account.<br />2. Try to create a VPC or a new public subnet in an existing VPC. For instructions, see [Create a VPC, subnets, and other VPC resources](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#create-vpc-and-other-resources) in the Amazon VPC documentation. You shouldn't be able to create these resources.<br />3. Assume the `AutomationAdminRole` role, and retry the previous step. Now, you should be able to create the networking resources. | AWS administrator |
| Manage tags. | 1. Assume the `TestAdminRole` role in the target AWS account.<br />2. Add a `SubnetType:IFA` tag to an available public subnet. You should be able to add this tag. For instructions about how to add tags through the AWS Command Line Interface (AWS CLI), see [create-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html) in the *AWS CLI Command Reference*.<br />3. Without changing your credentials, attempt to modify the `SubnetType:IFA` tag assigned to this subnet. You shouldn’t be able to modify this tag.<br />4. Assume the `AutomationAdminRole` role, and retry the previous steps. This role should be able to add and modify this tag. | AWS administrator |
| Deploy resources in the target subnets. | 1. Assume the `TestAdminRole` role.<br />2. For a public subnet that has the `SubnetType:IFA` tag, try to create an EC2 instance. For instructions, see [Launch an instance](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html) in the Amazon EC2 documentation. In this subnet, you shouldn’t be able to create, modify, or delete any Amazon EC2 resources except NAT gateways.<br />3. In the same subnet, create a NAT gateway. For instructions, see [Create a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating) in the Amazon VPC documentation. You should be able to create, modify, or delete NAT gateways in this subnet. | AWS administrator |
| Manage the AutomationAdminRole role. | 1. Assume the `TestAdminRole` role.<br />2. Try to modify the `AutomationAdminRole` role. For instructions, see [Modifying a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html) in the IAM documentation. You shouldn't be able to modify this role.<br />3. Assume the `AutomationAdminRole` role, and retry the previous step. Now, you should be able to modify the role. | AWS administrator |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up deployed resources. | 1. Detach the SCP from the AWS account or OU. For instructions, see [Detaching an SCP](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_attach.html#detach_policy) in the AWS Organizations documentation.<br />2. Delete the SCP. For instructions, see [Deleting an SCP](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_create.html#delete_policy) (AWS Organizations documentation).<br />3. Delete the `AutomationAdminRole` role and the `TestAdminRole` role. For instructions, see [Deleting roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html) in the IAM documentation.<br />4. Delete all networking resources, such as VPCs and subnets, that you created for this solution. | AWS administrator |

## Related resources
<a name="deploy-preventative-attribute-based-access-controls-for-public-subnets-resources"></a>

**AWS documentation**
+ [Attaching and detaching SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_attach.html)
+ [Creating, updating, and deleting SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_create.html)
+ [Deploy detective attribute-based access controls for public subnets by using AWS Config](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config.html)
+ [Detective controls](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/detective-controls.html)
+ [Service authorization reference](https://docs.aws.amazon.com/service-authorization/latest/reference/reference.html)
+ [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
+ [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html)

**Additional AWS references**
+ [Securing resource tags used for authorization using a Service Control Policy in AWS Organizations](https://aws.amazon.com/es/blogs/security/securing-resource-tags-used-for-authorization-using-service-control-policy-in-aws-organizations/) (AWS blog post)

## Additional information
<a name="deploy-preventative-attribute-based-access-controls-for-public-subnets-additional"></a>

The following service control policy is an example that you can use to test this approach in your organization.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyVPCActions",
      "Effect": "Deny",
      "Action": [
        "ec2:CreateVPC",
        "ec2:CreateRoute",
        "ec2:CreateSubnet",
        "ec2:CreateInternetGateway",
        "ec2:DeleteVPC",
        "ec2:DeleteRoute",
        "ec2:DeleteSubnet",
        "ec2:DeleteInternetGateway"
      ],
      "Resource": [
        "arn:aws:ec2:*:*:*"
      ],
      "Condition": {
        "StringNotLike": {
          "aws:PrincipalARN": ["arn:aws:iam::*:role/AutomationAdminRole"]
        }
      }
    },
    {
      "Sid": "AllowNATGWOnIFASubnet",
      "Effect": "Deny",
      "NotAction": [
        "ec2:CreateNatGateway",
        "ec2:DeleteNatGateway"
      ],
      "Resource": [
        "arn:aws:ec2:*:*:subnet/*"
      ],
      "Condition": {
        "ForAnyValue:StringEqualsIfExists": {
          "aws:ResourceTag/SubnetType": "IFA"
        },
        "StringNotLike": {
          "aws:PrincipalARN": ["arn:aws:iam::*:role/AutomationAdminRole"]
        }
      }
    },
    {
      "Sid": "DenyChangesToAdminRole",
      "Effect": "Deny",
      "NotAction": [
        "iam:GetContextKeysForPrincipalPolicy",
        "iam:GetRole",
        "iam:GetRolePolicy",
        "iam:ListAttachedRolePolicies",
        "iam:ListInstanceProfilesForRole",
        "iam:ListRolePolicies",
        "iam:ListRoleTags"
      ],
      "Resource": [
        "arn:aws:iam::*:role/AutomationAdminRole"
      ],
      "Condition": {
        "StringNotLike": {
          "aws:PrincipalARN": ["arn:aws:iam::*:role/AutomationAdminRole"]
        }
      }
    }
  ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
