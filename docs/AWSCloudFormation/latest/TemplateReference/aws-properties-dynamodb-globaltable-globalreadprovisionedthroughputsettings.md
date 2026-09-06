---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-globalreadprovisionedthroughputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable GlobalReadProvisionedThroughputSettings
<a name="aws-properties-dynamodb-globaltable-globalreadprovisionedthroughputsettings"></a>

Sets read capacity settings for the multi-account global table or its global secondary index.

## Syntax
<a name="aws-properties-dynamodb-globaltable-globalreadprovisionedthroughputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-globalreadprovisionedthroughputsettings-syntax.json"></a>

```
{
  "[ReadCapacityUnits](#cfn-dynamodb-globaltable-globalreadprovisionedthroughputsettings-readcapacityunits)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-globalreadprovisionedthroughputsettings-syntax.yaml"></a>

```
  [ReadCapacityUnits](#cfn-dynamodb-globaltable-globalreadprovisionedthroughputsettings-readcapacityunits): {{Integer}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-globalreadprovisionedthroughputsettings-properties"></a>

`ReadCapacityUnits`  <a name="cfn-dynamodb-globaltable-globalreadprovisionedthroughputsettings-readcapacityunits"></a>
Sets read capacity settings for the multi-account global table or its global secondary index.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
