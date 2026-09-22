---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecyclepolicy-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecyclePolicy Filter
<a name="aws-properties-imagebuilder-lifecyclepolicy-filter"></a>

Defines filters that the lifecycle policy uses to determine impacted resource.

## Syntax
<a name="aws-properties-imagebuilder-lifecyclepolicy-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-lifecyclepolicy-filter-syntax.json"></a>

```
{
  "[RetainAtLeast](#cfn-imagebuilder-lifecyclepolicy-filter-retainatleast)" : {{Integer}},
  "[Type](#cfn-imagebuilder-lifecyclepolicy-filter-type)" : {{String}},
  "[Unit](#cfn-imagebuilder-lifecyclepolicy-filter-unit)" : {{String}},
  "[Value](#cfn-imagebuilder-lifecyclepolicy-filter-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-imagebuilder-lifecyclepolicy-filter-syntax.yaml"></a>

```
  [RetainAtLeast](#cfn-imagebuilder-lifecyclepolicy-filter-retainatleast): {{Integer}}
  [Type](#cfn-imagebuilder-lifecyclepolicy-filter-type): {{String}}
  [Unit](#cfn-imagebuilder-lifecyclepolicy-filter-unit): {{String}}
  [Value](#cfn-imagebuilder-lifecyclepolicy-filter-value): {{Integer}}
```

## Properties
<a name="aws-properties-imagebuilder-lifecyclepolicy-filter-properties"></a>

`RetainAtLeast`  <a name="cfn-imagebuilder-lifecyclepolicy-filter-retainatleast"></a>
For age-based filters, this is the number of resources to keep on hand after the lifecycle `DELETE` action is applied. Impacted resources are only deleted if you have more than this number of resources. If you have fewer resources than this number, the impacted resource is not deleted.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-imagebuilder-lifecyclepolicy-filter-type"></a>
Filter resources based on either `AGE` or `COUNT`. You can only use the count filter with the `DELETE` action type.
*Required*: Yes
*Type*: String
*Allowed values*: `AGE | COUNT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-imagebuilder-lifecyclepolicy-filter-unit"></a>
Defines the unit of time that the lifecycle policy uses to determine impacted resources. This is required for age-based rules.
*Required*: No
*Type*: String
*Allowed values*: `DAYS | WEEKS | MONTHS | YEARS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-imagebuilder-lifecyclepolicy-filter-value"></a>
The number of units for the time period or for the count. For example, a value of `6` might refer to six months or six AMIs.
For count-based filters, this value represents the minimum number of resources to keep on hand. If you have fewer resources than this number, the resource is excluded from lifecycle actions.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
