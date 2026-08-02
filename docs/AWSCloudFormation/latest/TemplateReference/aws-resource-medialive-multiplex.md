---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-multiplex.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Multiplex
<a name="aws-resource-medialive-multiplex"></a>

The multiplex object.

## Syntax
<a name="aws-resource-medialive-multiplex-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-multiplex-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::Multiplex",
  "Properties" : {
      "[AvailabilityZones](#cfn-medialive-multiplex-availabilityzones)" : {{[ String, ... ]}},
      "[Destinations](#cfn-medialive-multiplex-destinations)" : {{[ MultiplexOutputDestination, ... ]}},
      "[MultiplexSettings](#cfn-medialive-multiplex-multiplexsettings)" : {{MultiplexSettings}},
      "[Name](#cfn-medialive-multiplex-name)" : {{String}},
      "[Tags](#cfn-medialive-multiplex-tags)" : {{[ Tags, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-medialive-multiplex-syntax.yaml"></a>

```
Type: AWS::MediaLive::Multiplex
Properties:
  [AvailabilityZones](#cfn-medialive-multiplex-availabilityzones): {{
    - String}}
  [Destinations](#cfn-medialive-multiplex-destinations): {{
    - MultiplexOutputDestination}}
  [MultiplexSettings](#cfn-medialive-multiplex-multiplexsettings): {{
    MultiplexSettings}}
  [Name](#cfn-medialive-multiplex-name): {{String}}
  [Tags](#cfn-medialive-multiplex-tags): {{
    - Tags}}
```

## Properties
<a name="aws-resource-medialive-multiplex-properties"></a>

`AvailabilityZones`  <a name="cfn-medialive-multiplex-availabilityzones"></a>
A list of availability zones for the multiplex.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Destinations`  <a name="cfn-medialive-multiplex-destinations"></a>
A list of the multiplex output destinations.
*Required*: No
*Type*: Array of [MultiplexOutputDestination](aws-properties-medialive-multiplex-multiplexoutputdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiplexSettings`  <a name="cfn-medialive-multiplex-multiplexsettings"></a>
Configuration for a multiplex event.
*Required*: Yes
*Type*: [MultiplexSettings](aws-properties-medialive-multiplex-multiplexsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-multiplex-name"></a>
The name of the multiplex.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-medialive-multiplex-tags"></a>
A collection of key-value pairs.
*Required*: No
*Type*: [Array](aws-properties-medialive-multiplex-tags.md) of [Tags](aws-properties-medialive-multiplex-tags.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-medialive-multiplex-return-values"></a>

### Ref
<a name="aws-resource-medialive-multiplex-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-medialive-multiplex-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-multiplex-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The unique arn of the multiplex.

`Id`  <a name="Id-fn::getatt"></a>
The unique id of the multiplex.

`PipelinesRunningCount`  <a name="PipelinesRunningCount-fn::getatt"></a>
The number of currently healthy pipelines.

`ProgramCount`  <a name="ProgramCount-fn::getatt"></a>
The number of programs in the multiplex.

`State`  <a name="State-fn::getatt"></a>
The current state of the multiplex.
