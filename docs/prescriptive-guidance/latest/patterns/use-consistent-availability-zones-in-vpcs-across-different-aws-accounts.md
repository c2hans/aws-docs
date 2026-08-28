---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-consistent-availability-zones-in-vpcs-across-different-aws-accounts.html
---

# Use consistent Availability Zones in VPCs across different AWS accounts
<a name="use-consistent-availability-zones-in-vpcs-across-different-aws-accounts"></a>

*Adam Spicer, Amazon Web Services*

## Summary
<a name="use-consistent-availability-zones-in-vpcs-across-different-aws-accounts-summary"></a>

On the Amazon Web Services (AWS) Cloud, an Availability Zone has a name that can vary between your AWS accounts and an [Availability Zone ID (AZ ID) ](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html)that identifies its location. If you use AWS CloudFormation to create virtual private clouds (VPCs), you must specify the Availability Zone's name or ID when creating the subnets. If you create VPCs in multiple accounts, the Availability Zone name is randomized, which means that subnets use different Availability Zones in each account.

To use the same Availability Zone across your accounts, you must map the Availability Zone name in each account to the same AZ ID. For example, the following diagram shows that the `use1-az6` AZ ID is named `us-east-1a` in AWS account A and `us-east-1c` in AWS account Z.

![The use1-az6 AZ ID is named us-east-1a in AWS account A and us-east-1c in AWS account Z.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/9954e7f9-d6ce-44bd-af99-0c6bb7cd3cb0/images/23c8a37b-2408-4534-a1e0-bccfa4d7fbe3.png)

This pattern helps ensure zonal consistency by providing a cross-account, scalable solution for using the same Availability Zones in your subnets. Zonal consistency ensures that your cross-account network traffic avoids cross-Availability Zone network paths, which helps reduce data transfer costs and lower network latency between your workloads.

This pattern is an alternative approach to the AWS CloudFormation [AvailabilityZoneId property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-availabilityzoneid).

## Prerequisites and limitations
<a name="use-consistent-availability-zones-in-vpcs-across-different-aws-accounts-prereqs"></a>

**Prerequisites**
+ At least two active AWS accounts in the same AWS Region.
+ Evaluate how many Availability Zones are needed to support your VPC requirements in the Region.
+ Identify and record the AZ ID for each Availability Zone that you need to support. For more information about this, see [Availability Zone IDs for your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html) in the AWS Resource Access Manager documentation.
+ An ordered, comma-separated list of your AZ IDs. For example, the first Availability Zone on your list is mapped as `az1`, the second Availbility Zone is mapped as `az2`, and this mapping structure continues until your comma-separated list is fully mapped. There is no maximum number of AZ IDs that can be mapped.
+ The `az-mapping.yaml` file from the GitHub [Multi-account Availability Zone mapping](https://github.com/aws-samples/multi-account-az-mapping/) repository, copied to your local machine

## Architecture
<a name="use-consistent-availability-zones-in-vpcs-across-different-aws-accounts-architecture"></a>

The following diagram shows the architecture that is deployed in an account and that creates AWS Systems Manager Parameter Store values. These Parameter Store values are consumed when you create a VPC in the account.

![Workflow to create Systems Manager Parameter Store values for each AZ ID and store AZ name.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/9954e7f9-d6ce-44bd-af99-0c6bb7cd3cb0/images/f1168464-55f8-4efc-9b28-6a0cda668b9e.png)

The diagram shows the following workflow:

1. This pattern’s solution is deployed to all accounts that require zonal consistency for a VPC.

1. The solution creates Parameter Store values for each AZ ID and stores the new Availability Zone name.

1. The AWS CloudFormation template uses the Availability Zone name stored in each Parameter Store value and this ensures zonal consistency.

The following diagram shows the workflow for creating a VPC with this pattern's solution.

![Workflow submits CloudFormation template to create a VPC with correct AZ IDs.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/9954e7f9-d6ce-44bd-af99-0c6bb7cd3cb0/images/cd859430-ac25-479f-b56a-21da24cddf21.png)

The diagram shows the following workflow:

1. Submit a template for creating a VPC to AWS CloudFormation.

1. AWS CloudFormation resolves the Parameter Store values for each Availability Zone and returns the Availability Zone name for each AZ ID.

1. A VPC is created with the correct AZ IDs required for zonal consistency.

After you deploy this pattern’s solution, you can create subnets that reference the Parameter Store values. If you use AWS CloudFormation, you can reference the Availability Zone mapping parameter values from the following YAML-formatted sample code:

```
Resources:
    PrivateSubnet1AZ1:
        Type: AWS::EC2::Subnet
        Properties:
            VpcId: !Ref VPC
            CidrBlock: !Ref PrivateSubnetAZ1CIDR
            AvailabilityZone:
                !Join
                    - ''
                    - - '{{resolve:ssm:/az-mapping/az1:1}}'
```

This sample code is contained in the `vpc-example.yaml `file from the GitHub [Multi-account Availability Zone mapping](https://github.com/aws-samples/multi-account-az-mapping/) repository. It shows you how to create a VPC and subnets that align to the Parameter Store values for zonal consistency.

**Technology stack  **
+ AWS CloudFormation
+ AWS Lambda
+ AWS Systems Manager Parameter Store

**Automation and scale**

You can deploy this pattern to all your AWS accounts by using AWS CloudFormation StackSets or the Customizations for AWS Control Tower solution. For more information, see [Working with AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) in the AWS Cloudformation documentation and [Customizations for AWS Control Tower](https://aws.amazon.com/solutions/implementations/customizations-for-aws-control-tower/) in the AWS Solutions Library.

After you deploy the AWS CloudFormation template, you can update it to use the Parameter Store values and deploy your VPCs in pipelines or according to your requirements.

## Tools
<a name="use-consistent-availability-zones-in-vpcs-across-different-aws-accounts-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you model and set up your AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle. You can use a template to describe your resources and their dependencies, and launch and configure them together as a stack, instead of managing resources individually. You can manage and provision stacks across multiple AWS accounts and AWS Regions.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time that you consume—there is no charge when your code is not running.
+ [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) is a capability of AWS Systems Manager. It provides secure, hierarchical storage for configuration data management and secrets management.

**Code**

The code for this pattern is provided in the GitHub [Multi-account Availability Zone mapping](https://github.com/aws-samples/multi-account-az-mapping/) repository.

## Epics
<a name="use-consistent-availability-zones-in-vpcs-across-different-aws-accounts-epics"></a>

### Deploy the az-mapping.yaml file
<a name="deploy-the-az-mapping-yaml-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Determine the required Availability Zones for the Region. | 1. Determine the AZ IDs that must be consistently used in your Region. <br />2. Record these AZ IDs in a comma-separated list and in the order that you want them applied in. For example, the first Availability Zone on your list is mapped as `az1` and the second is mapped as `az2`. There is no maximum number of AZ IDs that can be mapped. | Cloud architect |
| Deploy the az-mapping.yaml file. | Use the `az-mapping.yaml` file to create an AWS CloudFormation stack in all required AWS accounts. In the `AZIds` parameter, use the comma-separated list that you created earlier. <br />We recommend that you use [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) or the [Customizations for AWS Control Tower Solution](https://aws.amazon.com/solutions/implementations/customizations-for-aws-control-tower/). | Cloud architect |

### Deploy the VPCs in your accounts
<a name="deploy-the-vpcs-in-your-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Customize the AWS CloudFormation templates. | When you create the subnets using AWS CloudFormation, customize the templates to use the Parameter Store values that you created earlier.<br />For a sample template, see the `vpc-example.yaml` file in the GitHub [Multi-account Availability Zone mapping](https://github.com/aws-samples/multi-account-az-mapping/) repository. | Cloud architect |
| Deploy the VPCs. | Deploy the customized AWS CloudFormation templates into your accounts. Each VPC in the Region then has zonal consistency in the Availability Zones used for the subnets | Cloud architect |

## Related resources
<a name="use-consistent-availability-zones-in-vpcs-across-different-aws-accounts-resources"></a>
+ [Availability Zone IDs for your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html) (AWS Resource Access Manager documentation)
+ [AWS::EC2::Subnet](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html) (AWS CloudFormation documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
