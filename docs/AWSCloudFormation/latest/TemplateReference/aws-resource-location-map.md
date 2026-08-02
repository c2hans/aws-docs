---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-map.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::Map
<a name="aws-resource-location-map"></a>

The `AWS::Location::Map` resource specifies a map resource in your AWS account, which provides map tiles of different styles sourced from global location data providers.

## Syntax
<a name="aws-resource-location-map-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-location-map-syntax.json"></a>

```
{
  "Type" : "AWS::Location::Map",
  "Properties" : {
      "[Configuration](#cfn-location-map-configuration)" : {{MapConfiguration}},
      "[Description](#cfn-location-map-description)" : {{String}},
      "[MapName](#cfn-location-map-mapname)" : {{String}},
      "[PricingPlan](#cfn-location-map-pricingplan)" : {{String}},
      "[Tags](#cfn-location-map-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-location-map-syntax.yaml"></a>

```
Type: AWS::Location::Map
Properties:
  [Configuration](#cfn-location-map-configuration): {{
    MapConfiguration}}
  [Description](#cfn-location-map-description): {{String}}
  [MapName](#cfn-location-map-mapname): {{String}}
  [PricingPlan](#cfn-location-map-pricingplan): {{String}}
  [Tags](#cfn-location-map-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-location-map-properties"></a>

`Configuration`  <a name="cfn-location-map-configuration"></a>
Specifies the `MapConfiguration`, including the map style, for the map resource that you create. The map style defines the look of maps and the data provider for your map resource.
*Required*: Yes
*Type*: [MapConfiguration](aws-properties-location-map-mapconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-location-map-description"></a>
An optional description for the map resource.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MapName`  <a name="cfn-location-map-mapname"></a>
The name for the map resource.
Requirements:
+ Must contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (\_).
+ Must be a unique map resource name.
+ No spaces allowed. For example, `ExampleMap`.
*Required*: Yes
*Type*: String
*Pattern*: `^[-._\w]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PricingPlan`  <a name="cfn-location-map-pricingplan"></a>
No longer used. If included, the only allowed value is `RequestBasedUsage`.
*Allowed Values*: `RequestBasedUsage`
*Required*: No
*Type*: String
*Allowed values*: `RequestBasedUsage`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-location-map-tags"></a>
Applies one or more tags to the map resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.
Format: `"key" : "value"`
Restrictions:
+ Maximum 50 tags per resource
+ Each resource tag must be unique with a maximum of one value.
+ Maximum key length: 128 Unicode characters in UTF-8
+ Maximum value length: 256 Unicode characters in UTF-8
+ Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: \+ - = . \_ : / @.
+ Cannot use "aws:" as a prefix for a key.
*Required*: No
*Type*: Array of [Tag](aws-properties-location-map-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-location-map-return-values"></a>

### Ref
<a name="aws-resource-location-map-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `Map` name.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-location-map-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-location-map-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the map resource. Used to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:maps/ExampleMap`

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
The timestamp for when the map resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.

`MapArn`  <a name="MapArn-fn::getatt"></a>
Synonym for `Arn`. The Amazon Resource Name (ARN) for the map resource. Used to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:maps/ExampleMap`

`UpdateTime`  <a name="UpdateTime-fn::getatt"></a>
The timestamp for when the map resource was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
