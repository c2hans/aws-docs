---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-vpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application VpcConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-vpcconfiguration"></a>

Describes the parameters of a VPC used by the application.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-vpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-vpcconfiguration-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-kinesisanalyticsv2-application-vpcconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-kinesisanalyticsv2-application-vpcconfiguration-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-vpcconfiguration-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-kinesisanalyticsv2-application-vpcconfiguration-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-kinesisanalyticsv2-application-vpcconfiguration-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-vpcconfiguration-properties"></a>

`SecurityGroupIds`  <a name="cfn-kinesisanalyticsv2-application-vpcconfiguration-securitygroupids"></a>
The array of [SecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html) IDs used by the VPC configuration.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-kinesisanalyticsv2-application-vpcconfiguration-subnetids"></a>
The array of [Subnet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html) IDs used by the VPC configuration.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
