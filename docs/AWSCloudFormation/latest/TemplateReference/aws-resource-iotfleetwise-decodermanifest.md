---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotfleetwise-decodermanifest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::DecoderManifest
<a name="aws-resource-iotfleetwise-decodermanifest"></a>

Creates the decoder manifest associated with a model manifest. To create a decoder manifest, the following must be true:
+ Every signal decoder has a unique name.
+ Each signal decoder is associated with a network interface.
+ Each network interface has a unique ID.
+ The signal decoders are specified in the model manifest.

For more information, see [Decoder manifests](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/decoder-manifests.html) in the *AWS IoT FleetWise Developer Guide*.

**Important**
Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability ](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html) in the *AWS IoT FleetWise Developer Guide*.

## Syntax
<a name="aws-resource-iotfleetwise-decodermanifest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotfleetwise-decodermanifest-syntax.json"></a>

```
{
  "Type" : "AWS::IoTFleetWise::DecoderManifest",
  "Properties" : {
      "[DefaultForUnmappedSignals](#cfn-iotfleetwise-decodermanifest-defaultforunmappedsignals)" : {{String}},
      "[Description](#cfn-iotfleetwise-decodermanifest-description)" : {{String}},
      "[ModelManifestArn](#cfn-iotfleetwise-decodermanifest-modelmanifestarn)" : {{String}},
      "[Name](#cfn-iotfleetwise-decodermanifest-name)" : {{String}},
      "[NetworkInterfaces](#cfn-iotfleetwise-decodermanifest-networkinterfaces)" : {{[ NetworkInterfacesItems, ... ]}},
      "[SignalDecoders](#cfn-iotfleetwise-decodermanifest-signaldecoders)" : {{[ SignalDecodersItems, ... ]}},
      "[Status](#cfn-iotfleetwise-decodermanifest-status)" : {{String}},
      "[Tags](#cfn-iotfleetwise-decodermanifest-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotfleetwise-decodermanifest-syntax.yaml"></a>

```
Type: AWS::IoTFleetWise::DecoderManifest
Properties:
  [DefaultForUnmappedSignals](#cfn-iotfleetwise-decodermanifest-defaultforunmappedsignals): {{String}}
  [Description](#cfn-iotfleetwise-decodermanifest-description): {{String}}
  [ModelManifestArn](#cfn-iotfleetwise-decodermanifest-modelmanifestarn): {{String}}
  [Name](#cfn-iotfleetwise-decodermanifest-name): {{String}}
  [NetworkInterfaces](#cfn-iotfleetwise-decodermanifest-networkinterfaces): {{
    - NetworkInterfacesItems}}
  [SignalDecoders](#cfn-iotfleetwise-decodermanifest-signaldecoders): {{
    - SignalDecodersItems}}
  [Status](#cfn-iotfleetwise-decodermanifest-status): {{String}}
  [Tags](#cfn-iotfleetwise-decodermanifest-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iotfleetwise-decodermanifest-properties"></a>

`DefaultForUnmappedSignals`  <a name="cfn-iotfleetwise-decodermanifest-defaultforunmappedsignals"></a>
Use default decoders for all unmapped signals in the model. You don't need to provide any detailed decoding information.
*Required*: No
*Type*: String
*Allowed values*: `CUSTOM_DECODING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iotfleetwise-decodermanifest-description"></a>
 A brief description of the decoder manifest.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u001F\u007F]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelManifestArn`  <a name="cfn-iotfleetwise-decodermanifest-modelmanifestarn"></a>
The Amazon Resource Name (ARN) of a vehicle model (model manifest) associated with the decoder manifest.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-iotfleetwise-decodermanifest-name"></a>
The name of the decoder manifest.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z\d\-_:]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkInterfaces`  <a name="cfn-iotfleetwise-decodermanifest-networkinterfaces"></a>
 A list of information about available network interfaces.
*Required*: No
*Type*: Array of [NetworkInterfacesItems](aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.md)
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SignalDecoders`  <a name="cfn-iotfleetwise-decodermanifest-signaldecoders"></a>
 A list of information about signal decoders.
*Required*: No
*Type*: Array of [SignalDecodersItems](aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.md)
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-iotfleetwise-decodermanifest-status"></a>
 The state of the decoder manifest. If the status is `ACTIVE`, the decoder manifest can't be edited. If the status is marked `DRAFT`, you can edit the decoder manifest.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE | DRAFT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iotfleetwise-decodermanifest-tags"></a>
 Metadata that can be used to manage the decoder manifest.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotfleetwise-decodermanifest-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotfleetwise-decodermanifest-return-values"></a>

### Ref
<a name="aws-resource-iotfleetwise-decodermanifest-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iotfleetwise-decodermanifest-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotfleetwise-decodermanifest-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the decoder manifest.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time the decoder manifest was created in seconds since epoch (January 1, 1970 at midnight UTC time).

`LastModificationTime`  <a name="LastModificationTime-fn::getatt"></a>
The time the decoder manifest was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).
