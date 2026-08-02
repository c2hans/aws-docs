---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-aggregatorv2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AggregatorV2
<a name="aws-resource-securityhub-aggregatorv2"></a>

Enables aggregation across AWS Regions.

## Syntax
<a name="aws-resource-securityhub-aggregatorv2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-aggregatorv2-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::AggregatorV2",
  "Properties" : {
      "[LinkedRegions](#cfn-securityhub-aggregatorv2-linkedregions)" : {{[ String, ... ]}},
      "[RegionLinkingMode](#cfn-securityhub-aggregatorv2-regionlinkingmode)" : {{String}},
      "[Tags](#cfn-securityhub-aggregatorv2-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-aggregatorv2-syntax.yaml"></a>

```
Type: AWS::SecurityHub::AggregatorV2
Properties:
  [LinkedRegions](#cfn-securityhub-aggregatorv2-linkedregions): {{
    - String}}
  [RegionLinkingMode](#cfn-securityhub-aggregatorv2-regionlinkingmode): {{String}}
  [Tags](#cfn-securityhub-aggregatorv2-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-securityhub-aggregatorv2-properties"></a>

`LinkedRegions`  <a name="cfn-securityhub-aggregatorv2-linkedregions"></a>
The list of Regions that are linked to the aggregation Region.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionLinkingMode`  <a name="cfn-securityhub-aggregatorv2-regionlinkingmode"></a>
Determines how Regions are linked to an Aggregator V2.
*Required*: Yes
*Type*: String
*Allowed values*: `SPECIFIED_REGIONS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-securityhub-aggregatorv2-tags"></a>
A list of key-value pairs to be applied to the AggregatorV2.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityhub-aggregatorv2-return-values"></a>

### Ref
<a name="aws-resource-securityhub-aggregatorv2-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `AggregatorV2ARN` for the `AggregatorV2` created: `arn:aws:securityhub:region:123456789012:aggregatorv2/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityhub-aggregatorv2-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityhub-aggregatorv2-return-values-fn--getatt-fn--getatt"></a>

`AggregationRegion`  <a name="AggregationRegion-fn::getatt"></a>
The AWS Region where data is aggregated.

`AggregatorV2Arn`  <a name="AggregatorV2Arn-fn::getatt"></a>
The ARN of the AggregatorV2.
