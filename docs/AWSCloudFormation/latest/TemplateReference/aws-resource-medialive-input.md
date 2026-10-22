---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-input.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input
<a name="aws-resource-medialive-input"></a>

The AWS::MediaLive::Input resource is a MediaLive resource type that creates an input.

A MediaLive input holds information that describes how the MediaLive channel is connected to the upstream system that is providing the source content that is to be transcoded.

## Syntax
<a name="aws-resource-medialive-input-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-input-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::Input",
  "Properties" : {
      "[Destinations](#cfn-medialive-input-destinations)" : {{[ InputDestination, ... ]}},
      "[InputDevices](#cfn-medialive-input-inputdevices)" : {{[ InputDeviceSettings, ... ]}},
      "[InputNetworkLocation](#cfn-medialive-input-inputnetworklocation)" : {{String}},
      "[InputSecurityGroups](#cfn-medialive-input-inputsecuritygroups)" : {{[ String, ... ]}},
      "[MediaConnectFlows](#cfn-medialive-input-mediaconnectflows)" : {{[ MediaConnectFlow, ... ]}},
      "[MulticastSettings](#cfn-medialive-input-multicastsettings)" : {{MulticastSettings}},
      "[Name](#cfn-medialive-input-name)" : {{String}},
      "[RoleArn](#cfn-medialive-input-rolearn)" : {{String}},
      "[RouterSettings](#cfn-medialive-input-routersettings)" : {{RouterSettings}},
      "[SdiSources](#cfn-medialive-input-sdisources)" : {{[ String, ... ]}},
      "[Smpte2110ReceiverGroupSettings](#cfn-medialive-input-smpte2110receivergroupsettings)" : {{Smpte2110ReceiverGroupSettings}},
      "[Sources](#cfn-medialive-input-sources)" : {{[ InputSource, ... ]}},
      "[SrtSettings](#cfn-medialive-input-srtsettings)" : {{SrtSettings}},
      "[Tags](#cfn-medialive-input-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Type](#cfn-medialive-input-type)" : {{String}},
      "[Vpc](#cfn-medialive-input-vpc)" : {{InputVpcRequest}}
    }
}
```

### YAML
<a name="aws-resource-medialive-input-syntax.yaml"></a>

```
Type: AWS::MediaLive::Input
Properties:
  [Destinations](#cfn-medialive-input-destinations): {{
    - InputDestination}}
  [InputDevices](#cfn-medialive-input-inputdevices): {{
    - InputDeviceSettings}}
  [InputNetworkLocation](#cfn-medialive-input-inputnetworklocation): {{String}}
  [InputSecurityGroups](#cfn-medialive-input-inputsecuritygroups): {{
    - String}}
  [MediaConnectFlows](#cfn-medialive-input-mediaconnectflows): {{
    - MediaConnectFlow}}
  [MulticastSettings](#cfn-medialive-input-multicastsettings): {{
    MulticastSettings}}
  [Name](#cfn-medialive-input-name): {{String}}
  [RoleArn](#cfn-medialive-input-rolearn): {{String}}
  [RouterSettings](#cfn-medialive-input-routersettings): {{
    RouterSettings}}
  [SdiSources](#cfn-medialive-input-sdisources): {{
    - String}}
  [Smpte2110ReceiverGroupSettings](#cfn-medialive-input-smpte2110receivergroupsettings): {{
    Smpte2110ReceiverGroupSettings}}
  [Sources](#cfn-medialive-input-sources): {{
    - InputSource}}
  [SrtSettings](#cfn-medialive-input-srtsettings): {{
    SrtSettings}}
  [Tags](#cfn-medialive-input-tags): {{
    {{Key}}: {{Value}}}}
  [Type](#cfn-medialive-input-type): {{String}}
  [Vpc](#cfn-medialive-input-vpc): {{
    InputVpcRequest}}
```

## Properties
<a name="aws-resource-medialive-input-properties"></a>

`Destinations`  <a name="cfn-medialive-input-destinations"></a>
Settings that apply only if the input is a push type of input.
*Required*: No
*Type*: Array of [InputDestination](aws-properties-medialive-input-inputdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputDevices`  <a name="cfn-medialive-input-inputdevices"></a>
Settings that apply only if the input is an Elemental Link input.
*Required*: No
*Type*: Array of [InputDeviceSettings](aws-properties-medialive-input-inputdevicesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputNetworkLocation`  <a name="cfn-medialive-input-inputnetworklocation"></a>
The location of this input. AWS, for an input existing in the AWS Cloud, On-Prem for an input in a customer network.
*Required*: No
*Type*: String
*Allowed values*: `AWS | ON_PREMISES`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputSecurityGroups`  <a name="cfn-medialive-input-inputsecuritygroups"></a>
The list of input security groups (referenced by IDs) to attach to the input if the input is a push type.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaConnectFlows`  <a name="cfn-medialive-input-mediaconnectflows"></a>
Settings that apply only if the input is a MediaConnect input.
*Required*: No
*Type*: Array of [MediaConnectFlow](aws-properties-medialive-input-mediaconnectflow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MulticastSettings`  <a name="cfn-medialive-input-multicastsettings"></a>
Multicast input settings.
*Required*: No
*Type*: [MulticastSettings](aws-properties-medialive-input-multicastsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-input-name"></a>
A name for the input.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-medialive-input-rolearn"></a>
The IAM role for MediaLive to assume when creating a MediaConnect input or Amazon VPC input. This doesn't apply to other types of inputs. The role is identified by its ARN.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RouterSettings`  <a name="cfn-medialive-input-routersettings"></a>
Settings that apply only if the input is a MEDIACONNECT\_ROUTER type of input. Specifies the configuration for MediaConnect router-based content delivery.
*Required*: No
*Type*: [RouterSettings](aws-properties-medialive-input-routersettings.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SdiSources`  <a name="cfn-medialive-input-sdisources"></a>
SDI sources for this input.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Smpte2110ReceiverGroupSettings`  <a name="cfn-medialive-input-smpte2110receivergroupsettings"></a>
Include this parameter if the input is a SMPTE 2110 input, to identify the stream sources for this input.
*Required*: No
*Type*: [Smpte2110ReceiverGroupSettings](aws-properties-medialive-input-smpte2110receivergroupsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sources`  <a name="cfn-medialive-input-sources"></a>
Settings that apply only if the input is a pull type of input.
*Required*: No
*Type*: Array of [InputSource](aws-properties-medialive-input-inputsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtSettings`  <a name="cfn-medialive-input-srtsettings"></a>
The settings associated with an SRT input.
*Required*: No
*Type*: [SrtSettings](aws-properties-medialive-input-srtsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-medialive-input-tags"></a>
A collection of tags for this input. Each tag is a key-value pair.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-medialive-input-type"></a>
The type for this input.
*Required*: No
*Type*: String
*Allowed values*: `UDP_PUSH | RTP_PUSH | RTMP_PUSH | RTMP_PULL | URL_PULL | MP4_FILE | MEDIACONNECT | INPUT_DEVICE | AWS_CDI | TS_FILE | SRT_CALLER | MULTICAST | SMPTE_2110_RECEIVER_GROUP | SDI | MEDIACONNECT_ROUTER | SRT_LISTENER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Vpc`  <a name="cfn-medialive-input-vpc"></a>
Settings that apply only if the input is an push input where the source is on Amazon VPC.
*Required*: No
*Type*: [InputVpcRequest](aws-properties-medialive-input-inputvpcrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-medialive-input-return-values"></a>

### Ref
<a name="aws-resource-medialive-input-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the MediaLive id of the input.

For example: `{ "Ref": "myInput" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-medialive-input-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-input-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the MediaLive input. For example: arn:aws:medialive:us-west-1:111122223333:medialive:input:1234567. MediaLive creates this ARN when it creates the input.

`AttachedChannels`  <a name="AttachedChannels-fn::getatt"></a>
A list of channel IDs that that input is attached to (currently an input can only be attached to one channel).

`Destinations`  <a name="Destinations-fn::getatt"></a>
For a push input, the the destination or destinations for the input. The destinations are the URLs of locations on MediaLive where the upstream system pushes the content to, for this input. MediaLive creates these addresses when it creates the input.

`DestinationUrls`  <a name="DestinationUrls-fn::getatt"></a>
Property description not available.

`Id`  <a name="Id-fn::getatt"></a>
The unique ID for the device.

`InputClass`  <a name="InputClass-fn::getatt"></a>
STANDARD - MediaLive expects two sources to be connected to this input. If the channel is also STANDARD, both sources will be ingested. If the channel is SINGLE\_PIPELINE, only the first source will be ingested; the second source will always be ignored, even if the first source fails. SINGLE\_PIPELINE - You can connect only one source to this input. If the ChannelClass is also SINGLE\_PIPELINE, this value is valid. If the ChannelClass is STANDARD, this value is not valid because the channel requires two sources in the input.

`InputPartnerIds`  <a name="InputPartnerIds-fn::getatt"></a>
A list of IDs for all Inputs which are partners of this one.

`InputSourceType`  <a name="InputSourceType-fn::getatt"></a>
Certain pull input sources can be dynamic, meaning that they can have their URL's dynamically changes during input switch actions. Presently, this functionality only works with MP4\_FILE and TS\_FILE inputs.

`SecurityGroups`  <a name="SecurityGroups-fn::getatt"></a>
A list of IDs for all the Input Security Groups attached to the input.

`Sources`  <a name="Sources-fn::getatt"></a>
For a pull input, the source or sources for the input. The sources are the URLs of locations on the upstream system where MediaLive pulls the content from, for this input. You included these URLs in the create request.

`SourceUrls`  <a name="SourceUrls-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
Property description not available.

## Examples
<a name="aws-resource-medialive-input--examples"></a>

### Create a MEDIACONNECT\_ROUTER input
<a name="aws-resource-medialive-input--examples--Create_a_MEDIACONNECT_ROUTER_input"></a>

This example creates a standard (redundant) MediaLive input that uses MediaConnect as a router for content delivery, with automatic encryption.

#### JSON
<a name="aws-resource-medialive-input--examples--Create_a_MEDIACONNECT_ROUTER_input--json"></a>

```
{
  "Type": "AWS::MediaLive::Input",
  "Properties": {
    "Name": "my-router-input",
    "Type": "MEDIACONNECT_ROUTER",
    "RouterSettings": {
      "EncryptionType": "AUTOMATIC",
      "Destinations": [
        {
          "AvailabilityZoneName": "us-east-1a"
        },
        {
          "AvailabilityZoneName": "us-east-1b"
        }
      ]
    }
  }
}
```

#### YAML
<a name="aws-resource-medialive-input--examples--Create_a_MEDIACONNECT_ROUTER_input--yaml"></a>

```
Type: AWS::MediaLive::Input
Properties:
  Name: my-router-input
  Type: MEDIACONNECT_ROUTER
  RouterSettings:
    EncryptionType: AUTOMATIC
    Destinations:
      - AvailabilityZoneName: us-east-1a
      - AvailabilityZoneName: us-east-1b
```
