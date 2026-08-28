---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-capacityprovider-capacityprovidervpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::CapacityProvider CapacityProviderVpcConfig
<a name="aws-properties-lambda-capacityprovider-capacityprovidervpcconfig"></a>

VPC configuration that specifies the network settings for compute instances managed by the capacity provider.

## Syntax
<a name="aws-properties-lambda-capacityprovider-capacityprovidervpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-capacityprovider-capacityprovidervpcconfig-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-lambda-capacityprovider-capacityprovidervpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-lambda-capacityprovider-capacityprovidervpcconfig-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-lambda-capacityprovider-capacityprovidervpcconfig-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-lambda-capacityprovider-capacityprovidervpcconfig-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-lambda-capacityprovider-capacityprovidervpcconfig-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-lambda-capacityprovider-capacityprovidervpcconfig-properties"></a>

`SecurityGroupIds`  <a name="cfn-lambda-capacityprovider-capacityprovidervpcconfig-securitygroupids"></a>
A list of security group IDs that control network access for compute instances managed by the capacity provider.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `1024 | 5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-lambda-capacityprovider-capacityprovidervpcconfig-subnetids"></a>
A list of subnet IDs where the capacity provider launches compute instances.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0 | 1`
*Maximum*: `1024 | 16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
