---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-customerprofiles-calculatedattributedefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::CalculatedAttributeDefinition
<a name="aws-resource-customerprofiles-calculatedattributedefinition"></a>

A calculated attribute definition for Customer Profiles.

## Syntax
<a name="aws-resource-customerprofiles-calculatedattributedefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-customerprofiles-calculatedattributedefinition-syntax.json"></a>

```
{
  "Type" : "AWS::CustomerProfiles::CalculatedAttributeDefinition",
  "Properties" : {
      "[AttributeDetails](#cfn-customerprofiles-calculatedattributedefinition-attributedetails)" : {{AttributeDetails}},
      "[CalculatedAttributeName](#cfn-customerprofiles-calculatedattributedefinition-calculatedattributename)" : {{String}},
      "[Conditions](#cfn-customerprofiles-calculatedattributedefinition-conditions)" : {{Conditions}},
      "[Description](#cfn-customerprofiles-calculatedattributedefinition-description)" : {{String}},
      "[DisplayName](#cfn-customerprofiles-calculatedattributedefinition-displayname)" : {{String}},
      "[DomainName](#cfn-customerprofiles-calculatedattributedefinition-domainname)" : {{String}},
      "[Statistic](#cfn-customerprofiles-calculatedattributedefinition-statistic)" : {{String}},
      "[Tags](#cfn-customerprofiles-calculatedattributedefinition-tags)" : {{[ Tag, ... ]}},
      "[UseHistoricalData](#cfn-customerprofiles-calculatedattributedefinition-usehistoricaldata)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-customerprofiles-calculatedattributedefinition-syntax.yaml"></a>

```
Type: AWS::CustomerProfiles::CalculatedAttributeDefinition
Properties:
  [AttributeDetails](#cfn-customerprofiles-calculatedattributedefinition-attributedetails): {{
    AttributeDetails}}
  [CalculatedAttributeName](#cfn-customerprofiles-calculatedattributedefinition-calculatedattributename): {{String}}
  [Conditions](#cfn-customerprofiles-calculatedattributedefinition-conditions): {{
    Conditions}}
  [Description](#cfn-customerprofiles-calculatedattributedefinition-description): {{String}}
  [DisplayName](#cfn-customerprofiles-calculatedattributedefinition-displayname): {{String}}
  [DomainName](#cfn-customerprofiles-calculatedattributedefinition-domainname): {{String}}
  [Statistic](#cfn-customerprofiles-calculatedattributedefinition-statistic): {{String}}
  [Tags](#cfn-customerprofiles-calculatedattributedefinition-tags): {{
    - Tag}}
  [UseHistoricalData](#cfn-customerprofiles-calculatedattributedefinition-usehistoricaldata): {{Boolean}}
```

## Properties
<a name="aws-resource-customerprofiles-calculatedattributedefinition-properties"></a>

`AttributeDetails`  <a name="cfn-customerprofiles-calculatedattributedefinition-attributedetails"></a>
Mathematical expression and a list of attribute items specified in that expression.
*Required*: Yes
*Type*: [AttributeDetails](aws-properties-customerprofiles-calculatedattributedefinition-attributedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CalculatedAttributeName`  <a name="cfn-customerprofiles-calculatedattributedefinition-calculatedattributename"></a>
The name of an attribute defined in a profile object type.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Conditions`  <a name="cfn-customerprofiles-calculatedattributedefinition-conditions"></a>
The conditions including range, object count, and threshold for the calculated attribute.
*Required*: No
*Type*: [Conditions](aws-properties-customerprofiles-calculatedattributedefinition-conditions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-customerprofiles-calculatedattributedefinition-description"></a>
The description of the calculated attribute.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-customerprofiles-calculatedattributedefinition-displayname"></a>
The display name of the calculated attribute.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z_][a-zA-Z_0-9-\s]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-customerprofiles-calculatedattributedefinition-domainname"></a>
The unique name of the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Statistic`  <a name="cfn-customerprofiles-calculatedattributedefinition-statistic"></a>
The aggregation operation to perform for the calculated attribute.
*Required*: Yes
*Type*: String
*Allowed values*: `FIRST_OCCURRENCE | LAST_OCCURRENCE | COUNT | SUM | MINIMUM | MAXIMUM | AVERAGE | MAX_OCCURRENCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-customerprofiles-calculatedattributedefinition-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-customerprofiles-calculatedattributedefinition-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseHistoricalData`  <a name="cfn-customerprofiles-calculatedattributedefinition-usehistoricaldata"></a>
Whether historical data ingested before the Calculated Attribute was created should be included in calculations.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-customerprofiles-calculatedattributedefinition-return-values"></a>

### Ref
<a name="aws-resource-customerprofiles-calculatedattributedefinition-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-customerprofiles-calculatedattributedefinition-return-values-fn--getatt"></a>

####
<a name="aws-resource-customerprofiles-calculatedattributedefinition-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the calculated attribute definition was created.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp of when the calculated attribute definition was most recently edited.

`Status`  <a name="Status-fn::getatt"></a>
Status of the Calculated Attribute creation (whether all historical data has been indexed.)
