---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-findingaggregator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::FindingAggregator
<a name="aws-resource-securityhub-findingaggregator"></a>

The `AWS::SecurityHub::FindingAggregator` resource enables cross-Region aggregation. When cross-Region aggregation is enabled, you can aggregate findings, finding updates, insights, control compliance statuses, and security scores from one or more linked Regions to a single aggregation Region. You can then view and manage all of this data from the aggregation Region. For more details about cross-Region aggregation, see [Cross-Region aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html) in the *AWS Security Hub CSPM User Guide*

This resource must be created in the Region that you want to designate as your aggregation Region.

Cross-Region aggregation is also a prerequisite for using [central configuration](https://docs.aws.amazon.com/securityhub/latest/userguide/central-configuration-intro.html) in Security Hub CSPM.

## Syntax
<a name="aws-resource-securityhub-findingaggregator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-findingaggregator-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::FindingAggregator",
  "Properties" : {
      "[RegionLinkingMode](#cfn-securityhub-findingaggregator-regionlinkingmode)" : {{String}},
      "[Regions](#cfn-securityhub-findingaggregator-regions)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-findingaggregator-syntax.yaml"></a>

```
Type: AWS::SecurityHub::FindingAggregator
Properties:
  [RegionLinkingMode](#cfn-securityhub-findingaggregator-regionlinkingmode): {{String}}
  [Regions](#cfn-securityhub-findingaggregator-regions): {{
    - String}}
```

## Properties
<a name="aws-resource-securityhub-findingaggregator-properties"></a>

`RegionLinkingMode`  <a name="cfn-securityhub-findingaggregator-regionlinkingmode"></a>
Indicates whether to aggregate findings from all of the available Regions in the current partition. Also determines whether to automatically aggregate findings from new Regions as Security Hub supports them and you opt into them.
The selected option also determines how to use the Regions provided in the Regions list.
In CloudFormation, the options for this property are as follows:
+ `ALL_REGIONS` - Indicates to aggregate findings from all of the Regions where Security Hub is enabled. When you choose this option, Security Hub also automatically aggregates findings from new Regions as Security Hub supports them and you opt into them.
+ `ALL_REGIONS_EXCEPT_SPECIFIED` - Indicates to aggregate findings from all of the Regions where Security Hub is enabled, except for the Regions listed in the `Regions` parameter. When you choose this option, Security Hub also automatically aggregates findings from new Regions as Security Hub supports them and you opt into them.
+ `SPECIFIED_REGIONS` - Indicates to aggregate findings only from the Regions listed in the `Regions` parameter. Security Hub does not automatically aggregate findings from new Regions.
*Required*: Yes
*Type*: String
*Allowed values*: `ALL_REGIONS | ALL_REGIONS_EXCEPT_SPECIFIED | SPECIFIED_REGIONS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regions`  <a name="cfn-securityhub-findingaggregator-regions"></a>
If `RegionLinkingMode` is `ALL_REGIONS_EXCEPT_SPECIFIED`, then this is a space-separated list of Regions that do not aggregate findings to the aggregation Region.
If `RegionLinkingMode` is `SPECIFIED_REGIONS`, then this is a space-separated list of Regions that do aggregate findings to the aggregation Region.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityhub-findingaggregator-return-values"></a>

### Ref
<a name="aws-resource-securityhub-findingaggregator-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the finding aggregator. For example, `arn:aws:securityhub:us-east-1:123456789012:finding-aggregator/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityhub-findingaggregator-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityhub-findingaggregator-return-values-fn--getatt-fn--getatt"></a>

`FindingAggregationRegion`  <a name="FindingAggregationRegion-fn::getatt"></a>
The home Region. Findings generated in linked Regions are replicated and sent to the home Region.

`FindingAggregatorArn`  <a name="FindingAggregatorArn-fn::getatt"></a>
The ARN of the finding aggregator. You use the finding aggregator ARN to retrieve details for, update, and delete the finding aggregator.

## Examples
<a name="aws-resource-securityhub-findingaggregator--examples"></a>

### Configuring Security Hub CSPM cross-Region aggregation
<a name="aws-resource-securityhub-findingaggregator--examples--Configuring_cross-Region_aggregation"></a>

The following example configures cross-Region aggregation. The region in which the resource is created is the aggregation Region. In this example, `us-east-2` and `us-west-1` contribute data to the aggregation Region.

#### JSON
<a name="aws-resource-securityhub-findingaggregator--examples--Configuring_cross-Region_aggregation--json"></a>

```
{
	"Description": "Example template to configure Security Hub cross-Region aggregation",
	"Resources": {
		"SecurityHubFindingAggregator": {
			"Type": "AWS::SecurityHub::FindingAggregator",
			"Properties": {
				"RegionLinkingMode": "SPECIFIED_REGIONS",
				"Regions": ["us-west-1", "us-east-2"]
			}
		}
	}
}
```

#### YAML
<a name="aws-resource-securityhub-findingaggregator--examples--Configuring_cross-Region_aggregation--yaml"></a>

```
Description: Example template to configure Security Hub cross-Region aggregation
Resources:
  SecurityHubFindingAggregator:
    Type: 'AWS::SecurityHub::FindingAggregator'
    Properties:
      RegionLinkingMode: 'SPECIFIED_REGIONS'
      Regions:
        - "us-west-1"
        - "us-east-2"
```
