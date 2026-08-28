---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-channel-destinationtable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Channel DestinationTable
<a name="aws-properties-msk-channel-destinationtable"></a>

<a name="aws-properties-msk-channel-destinationtable-description"></a>The `DestinationTable` property type specifies Property description not available. for an [AWS::MSK::Channel](aws-resource-msk-channel.md).

## Syntax
<a name="aws-properties-msk-channel-destinationtable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-channel-destinationtable-syntax.json"></a>

```
{
  "[DestinationDatabaseName](#cfn-msk-channel-destinationtable-destinationdatabasename)" : {{String}},
  "[DestinationTableName](#cfn-msk-channel-destinationtable-destinationtablename)" : {{String}},
  "[PartitionSpec](#cfn-msk-channel-destinationtable-partitionspec)" : {{PartitionSpec}}
}
```

### YAML
<a name="aws-properties-msk-channel-destinationtable-syntax.yaml"></a>

```
  [DestinationDatabaseName](#cfn-msk-channel-destinationtable-destinationdatabasename): {{String}}
  [DestinationTableName](#cfn-msk-channel-destinationtable-destinationtablename): {{String}}
  [PartitionSpec](#cfn-msk-channel-destinationtable-partitionspec): {{
    PartitionSpec}}
```

## Properties
<a name="aws-properties-msk-channel-destinationtable-properties"></a>

`DestinationDatabaseName`  <a name="cfn-msk-channel-destinationtable-destinationdatabasename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DestinationTableName`  <a name="cfn-msk-channel-destinationtable-destinationtablename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PartitionSpec`  <a name="cfn-msk-channel-destinationtable-partitionspec"></a>
Property description not available.
*Required*: No
*Type*: [PartitionSpec](aws-properties-msk-channel-partitionspec.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
