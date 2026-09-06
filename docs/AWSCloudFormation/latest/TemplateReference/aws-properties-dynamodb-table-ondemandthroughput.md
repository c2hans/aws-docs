---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-ondemandthroughput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Table OnDemandThroughput
<a name="aws-properties-dynamodb-table-ondemandthroughput"></a>

Sets the maximum number of read and write units for the specified on-demand table. If you use this property, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.

## Syntax
<a name="aws-properties-dynamodb-table-ondemandthroughput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-table-ondemandthroughput-syntax.json"></a>

```
{
  "[MaxReadRequestUnits](#cfn-dynamodb-table-ondemandthroughput-maxreadrequestunits)" : {{Integer}},
  "[MaxWriteRequestUnits](#cfn-dynamodb-table-ondemandthroughput-maxwriterequestunits)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-dynamodb-table-ondemandthroughput-syntax.yaml"></a>

```
  [MaxReadRequestUnits](#cfn-dynamodb-table-ondemandthroughput-maxreadrequestunits): {{Integer}}
  [MaxWriteRequestUnits](#cfn-dynamodb-table-ondemandthroughput-maxwriterequestunits): {{Integer}}
```

## Properties
<a name="aws-properties-dynamodb-table-ondemandthroughput-properties"></a>

`MaxReadRequestUnits`  <a name="cfn-dynamodb-table-ondemandthroughput-maxreadrequestunits"></a>
Maximum number of read request units for the specified table.
To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxReadRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxReadRequestUnits` to -1.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxWriteRequestUnits`  <a name="cfn-dynamodb-table-ondemandthroughput-maxwriterequestunits"></a>
Maximum number of write request units for the specified table.
To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxWriteRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxWriteRequestUnits` to -1.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
