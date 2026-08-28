---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-capacityprovider-vpcconfig.html
---

# VpcConfig
<a name="sam-property-capacityprovider-vpcconfig"></a>

Configures the VPC settings for a capacity provider, including the subnets and security groups where EC2 instances will be launched.

## Syntax
<a name="sam-property-capacityprovider-vpcconfig-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-capacityprovider-vpcconfig-syntax.yaml"></a>

```
[SubnetIds](#sam-capacityprovider-vpcconfig-subnetids): {{List}}
[SecurityGroupIds](#sam-capacityprovider-vpcconfig-securitygroupids): {{List}}
```

## Properties
<a name="sam-property-capacityprovider-vpcconfig-properties"></a>

 `SubnetIds`   <a name="sam-capacityprovider-vpcconfig-subnetids"></a>
A list of subnet IDs where EC2 instances will be launched. At least one subnet must be specified.
*Type*: List
*Required*: Yes
*CloudFormation compatibility*: This property is passed directly to the `[SubnetIds](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-capacityprovider-capacityprovidervpcconfig.html#cfn-lambda-capacityprovider-capacityprovidervpcconfig-subnetids)` property of `[VpcConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-vpcconfig) ` of an `AWS::Lambda::CapacityProvider` resource.

 `SecurityGroupIds`   <a name="sam-capacityprovider-vpcconfig-securitygroupids"></a>
A list of security group IDs to associate with the EC2 instances. If not specified, the default security group for the VPC will be used.
*Type*: List
*Required*: No
*CloudFormation compatibility*: This property is passed directly to the `[SecurityGroupIds](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-capacityprovider-capacityprovidervpcconfig.html#cfn-lambda-capacityprovider-capacityprovidervpcconfig-securitygroupids)` property of `[VpcConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-vpcconfig)` property of an `AWS::Lambda::CapacityProvider` resource.

## Examples
<a name="sam-property-capacityprovider-vpcconfig-examples"></a>

### VPC configuration
<a name="sam-property-capacityprovider-vpcconfig-examples-basic"></a>

The following example shows a VPC configuration with multiple subnets and security groups.

```
VpcConfig:
  SubnetIds:
    - {{subnet-12345678}}
    - {{subnet-87654321}}
  SecurityGroupIds:
    - {{sg-12345678}}
    - {{sg-87654321}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
