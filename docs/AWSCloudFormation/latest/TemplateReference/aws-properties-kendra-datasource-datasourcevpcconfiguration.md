---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-datasourcevpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource DataSourceVpcConfiguration
<a name="aws-properties-kendra-datasource-datasourcevpcconfiguration"></a>

Provides the configuration information to connect to an Amazon VPC.

## Syntax
<a name="aws-properties-kendra-datasource-datasourcevpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-datasourcevpcconfiguration-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-kendra-datasource-datasourcevpcconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-kendra-datasource-datasourcevpcconfiguration-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-datasourcevpcconfiguration-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-kendra-datasource-datasourcevpcconfiguration-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-kendra-datasource-datasourcevpcconfiguration-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-kendra-datasource-datasourcevpcconfiguration-properties"></a>

`SecurityGroupIds`  <a name="cfn-kendra-datasource-datasourcevpcconfiguration-securitygroupids"></a>
A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `200 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-kendra-datasource-datasourcevpcconfiguration-subnetids"></a>
A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `200 | 6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
