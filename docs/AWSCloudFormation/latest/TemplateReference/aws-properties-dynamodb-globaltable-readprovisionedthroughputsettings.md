---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable ReadProvisionedThroughputSettings
<a name="aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings"></a>

Allows you to specify the read capacity settings for a replica table or a replica global secondary index when the `BillingMode` is set to `PROVISIONED`. You must specify a value for either `ReadCapacityUnits` or `ReadCapacityAutoScalingSettings`, but not both. You can switch between fixed capacity and auto scaling.

## Syntax
<a name="aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings-syntax.json"></a>

```
{
  "[ReadCapacityAutoScalingSettings](#cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityautoscalingsettings)" : {{CapacityAutoScalingSettings}},
  "[ReadCapacityUnits](#cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityunits)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings-syntax.yaml"></a>

```
  [ReadCapacityAutoScalingSettings](#cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityautoscalingsettings): {{
    CapacityAutoScalingSettings}}
  [ReadCapacityUnits](#cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityunits): {{Integer}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings-properties"></a>

`ReadCapacityAutoScalingSettings`  <a name="cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityautoscalingsettings"></a>
Specifies auto scaling settings for the replica table or global secondary index.
*Required*: No
*Type*: [CapacityAutoScalingSettings](aws-properties-dynamodb-globaltable-capacityautoscalingsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadCapacityUnits`  <a name="cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityunits"></a>
Specifies a fixed read capacity for the replica table or global secondary index.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
