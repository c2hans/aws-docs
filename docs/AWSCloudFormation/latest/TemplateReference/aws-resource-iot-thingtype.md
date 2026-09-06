---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-thingtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::ThingType
<a name="aws-resource-iot-thingtype"></a>

Creates a new thing type.

## Syntax
<a name="aws-resource-iot-thingtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-thingtype-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::ThingType",
  "Properties" : {
      "[DeprecateThingType](#cfn-iot-thingtype-deprecatethingtype)" : {{Boolean}},
      "[Tags](#cfn-iot-thingtype-tags)" : {{[ Tag, ... ]}},
      "[ThingTypeName](#cfn-iot-thingtype-thingtypename)" : {{String}},
      "[ThingTypeProperties](#cfn-iot-thingtype-thingtypeproperties)" : {{ThingTypeProperties}}
    }
}
```

### YAML
<a name="aws-resource-iot-thingtype-syntax.yaml"></a>

```
Type: AWS::IoT::ThingType
Properties:
  [DeprecateThingType](#cfn-iot-thingtype-deprecatethingtype): {{Boolean}}
  [Tags](#cfn-iot-thingtype-tags): {{
    - Tag}}
  [ThingTypeName](#cfn-iot-thingtype-thingtypename): {{String}}
  [ThingTypeProperties](#cfn-iot-thingtype-thingtypeproperties): {{
    ThingTypeProperties}}
```

## Properties
<a name="aws-resource-iot-thingtype-properties"></a>

`DeprecateThingType`  <a name="cfn-iot-thingtype-deprecatethingtype"></a>
Deprecates a thing type. You can not associate new things with deprecated thing type.
Requires permission to access the [DeprecateThingType](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iot-thingtype-tags"></a>
Metadata which can be used to manage the thing type.
*Required*: No
*Type*: Array of [Tag](aws-properties-iot-thingtype-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThingTypeName`  <a name="cfn-iot-thingtype-thingtypename"></a>
The name of the thing type.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9:_-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ThingTypeProperties`  <a name="cfn-iot-thingtype-thingtypeproperties"></a>
The thing type properties for the thing type to create. It contains information about the new thing type including a description, a list of searchable thing attribute names, and a list of propagating attributes. After a thing type is created, you can only update `Mqtt5Configuration`.
*Required*: No
*Type*: [ThingTypeProperties](aws-properties-iot-thingtype-thingtypeproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iot-thingtype-return-values"></a>

### Ref
<a name="aws-resource-iot-thingtype-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the thing type id.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iot-thingtype-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iot-thingtype-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The thing type arn.

`Id`  <a name="Id-fn::getatt"></a>
The thing type id.
