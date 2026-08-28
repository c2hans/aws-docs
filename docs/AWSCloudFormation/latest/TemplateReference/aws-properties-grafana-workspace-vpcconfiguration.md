---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-grafana-workspace-vpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Grafana::Workspace VpcConfiguration
<a name="aws-properties-grafana-workspace-vpcconfiguration"></a>

The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.

**Note**
Provided `securityGroupIds` and `subnetIds` must be part of the same VPC.
Connecting to a private VPC is not yet available in the Asia Pacific (Seoul) Region (ap-northeast-2).

## Syntax
<a name="aws-properties-grafana-workspace-vpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-grafana-workspace-vpcconfiguration-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-grafana-workspace-vpcconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-grafana-workspace-vpcconfiguration-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-grafana-workspace-vpcconfiguration-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-grafana-workspace-vpcconfiguration-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-grafana-workspace-vpcconfiguration-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-grafana-workspace-vpcconfiguration-properties"></a>

`SecurityGroupIds`  <a name="cfn-grafana-workspace-vpcconfiguration-securitygroupids"></a>
The list of Amazon EC2 security group IDs attached to the Amazon VPC for your Grafana workspace to connect. Duplicates not allowed.
*Array Members*: Minimum number of 1 items. Maximum number of 5 items.
*Length*: Minimum length of 0. Maximum length of 255.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-grafana-workspace-vpcconfiguration-subnetids"></a>
The list of Amazon EC2 subnet IDs created in the Amazon VPC for your Grafana workspace to connect. Duplicates not allowed.
*Array Members*: Minimum number of 2 items. Maximum number of 6 items.
*Length*: Minimum length of 0. Maximum length of 255.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 2`
*Maximum*: `255 | 6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
