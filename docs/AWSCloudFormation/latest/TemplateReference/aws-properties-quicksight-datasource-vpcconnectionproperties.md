---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-vpcconnectionproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource VpcConnectionProperties
<a name="aws-properties-quicksight-datasource-vpcconnectionproperties"></a>

VPC connection properties.

## Syntax
<a name="aws-properties-quicksight-datasource-vpcconnectionproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-vpcconnectionproperties-syntax.json"></a>

```
{
  "[VpcConnectionArn](#cfn-quicksight-datasource-vpcconnectionproperties-vpcconnectionarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-vpcconnectionproperties-syntax.yaml"></a>

```
  [VpcConnectionArn](#cfn-quicksight-datasource-vpcconnectionproperties-vpcconnectionarn): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-vpcconnectionproperties-properties"></a>

`VpcConnectionArn`  <a name="cfn-quicksight-datasource-vpcconnectionproperties-vpcconnectionarn"></a>
The Amazon Resource Name (ARN) for the VPC connection.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
