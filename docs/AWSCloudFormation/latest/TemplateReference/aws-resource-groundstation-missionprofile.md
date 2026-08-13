---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-groundstation-missionprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::MissionProfile
<a name="aws-resource-groundstation-missionprofile"></a>

 Mission profiles specify parameters and provide references to config objects to define how Ground Station lists and executes contacts.

## Syntax
<a name="aws-resource-groundstation-missionprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-groundstation-missionprofile-syntax.json"></a>

```
{
  "Type" : "AWS::GroundStation::MissionProfile",
  "Properties" : {
      "[ContactPostPassDurationSeconds](#cfn-groundstation-missionprofile-contactpostpassdurationseconds)" : {{Integer}},
      "[ContactPrePassDurationSeconds](#cfn-groundstation-missionprofile-contactprepassdurationseconds)" : {{Integer}},
      "[DataflowEdges](#cfn-groundstation-missionprofile-dataflowedges)" : {{[ DataflowEdge, ... ]}},
      "[MinimumViableContactDurationSeconds](#cfn-groundstation-missionprofile-minimumviablecontactdurationseconds)" : {{Integer}},
      "[Name](#cfn-groundstation-missionprofile-name)" : {{String}},
      "[StreamsKmsKey](#cfn-groundstation-missionprofile-streamskmskey)" : {{StreamsKmsKey}},
      "[StreamsKmsRole](#cfn-groundstation-missionprofile-streamskmsrole)" : {{String}},
      "[Tags](#cfn-groundstation-missionprofile-tags)" : {{[ Tag, ... ]}},
      "[TelemetrySinkConfigArn](#cfn-groundstation-missionprofile-telemetrysinkconfigarn)" : {{String}},
      "[TrackingConfigArn](#cfn-groundstation-missionprofile-trackingconfigarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-groundstation-missionprofile-syntax.yaml"></a>

```
Type: AWS::GroundStation::MissionProfile
Properties:
  [ContactPostPassDurationSeconds](#cfn-groundstation-missionprofile-contactpostpassdurationseconds): {{Integer}}
  [ContactPrePassDurationSeconds](#cfn-groundstation-missionprofile-contactprepassdurationseconds): {{Integer}}
  [DataflowEdges](#cfn-groundstation-missionprofile-dataflowedges): {{
    - DataflowEdge}}
  [MinimumViableContactDurationSeconds](#cfn-groundstation-missionprofile-minimumviablecontactdurationseconds): {{Integer}}
  [Name](#cfn-groundstation-missionprofile-name): {{String}}
  [StreamsKmsKey](#cfn-groundstation-missionprofile-streamskmskey): {{
    StreamsKmsKey}}
  [StreamsKmsRole](#cfn-groundstation-missionprofile-streamskmsrole): {{String}}
  [Tags](#cfn-groundstation-missionprofile-tags): {{
    - Tag}}
  [TelemetrySinkConfigArn](#cfn-groundstation-missionprofile-telemetrysinkconfigarn): {{String}}
  [TrackingConfigArn](#cfn-groundstation-missionprofile-trackingconfigarn): {{String}}
```

## Properties
<a name="aws-resource-groundstation-missionprofile-properties"></a>

`ContactPostPassDurationSeconds`  <a name="cfn-groundstation-missionprofile-contactpostpassdurationseconds"></a>
 Amount of time in seconds after a contact ends that you’d like to receive a Ground Station Contact State Change indicating the pass has finished.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `21600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContactPrePassDurationSeconds`  <a name="cfn-groundstation-missionprofile-contactprepassdurationseconds"></a>
 Amount of time in seconds prior to contact start that you'd like to receive a Ground Station Contact State Change Event indicating an upcoming pass.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `21600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataflowEdges`  <a name="cfn-groundstation-missionprofile-dataflowedges"></a>
 A list containing lists of config ARNs. Each list of config ARNs is an edge, with a "from" config and a "to" config.
*Required*: Yes
*Type*: Array of [DataflowEdge](aws-properties-groundstation-missionprofile-dataflowedge.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumViableContactDurationSeconds`  <a name="cfn-groundstation-missionprofile-minimumviablecontactdurationseconds"></a>
 Minimum length of a contact in seconds that Ground Station will return when listing contacts. Ground Station will not return contacts shorter than this duration.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `21600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-groundstation-missionprofile-name"></a>
 The name of the mission profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[ a-zA-Z0-9_:-]{1,256}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamsKmsKey`  <a name="cfn-groundstation-missionprofile-streamskmskey"></a>
KMS key to use for encrypting streams.
*Required*: No
*Type*: [StreamsKmsKey](aws-properties-groundstation-missionprofile-streamskmskey.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamsKmsRole`  <a name="cfn-groundstation-missionprofile-streamskmsrole"></a>
Role to use for encrypting streams with KMS key.
*Required*: No
*Type*: String
*Pattern*: `arn:[a-z0-9-.]{1,63}:iam::[0-9]{12}:role/[\w+=,.@-]{1,64}`
*Minimum*: `30`
*Maximum*: `165`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-groundstation-missionprofile-tags"></a>
 Tags assigned to the mission profile.
*Required*: No
*Type*: Array of [Tag](aws-properties-groundstation-missionprofile-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TelemetrySinkConfigArn`  <a name="cfn-groundstation-missionprofile-telemetrysinkconfigarn"></a>
 The ARN of a TelemetrySinkConfig object that defines how to deliver telemetry data during a contact.
 When specified, telemetry data will be delivered to the configured sink (such as Amazon Kinesis Data Streams) according to the settings defined in the referenced TelemetrySinkConfig.
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrackingConfigArn`  <a name="cfn-groundstation-missionprofile-trackingconfigarn"></a>
 The ARN of a tracking config objects that defines how to track the satellite through the sky during a contact.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-groundstation-missionprofile-return-values"></a>

### Ref
<a name="aws-resource-groundstation-missionprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the mission profile. For example:

 `{ "Ref": "MissionProfile" }`

`Ref` returns the ARN of the mission profile.

### Fn::GetAtt
<a name="aws-resource-groundstation-missionprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-groundstation-missionprofile-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the mission profile, such as `arn:aws:groundstation:us-east-2:012345678910:mission-profile/9940bf3b-d2ba-427e-9906-842b5e5d2296`.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the mission profile, such as `9940bf3b-d2ba-427e-9906-842b5e5d2296`.

`Region`  <a name="Region-fn::getatt"></a>
 The region of the mission profile.

## Examples
<a name="aws-resource-groundstation-missionprofile--examples"></a>

### Mission Profile With Downlink And Uplink
<a name="aws-resource-groundstation-missionprofile--examples--Mission_Profile_With_Downlink_And_Uplink"></a>

 The following example shows how to create a mission profile that utilizes both downlink and uplink during a contact.

 The resulting mission profile will have a name of `My Mission Profile`. CloudWatch Events will be sent `120` seconds before the contact starts and `180` seconds after the contact completes. No contacts less than `300` seconds in duration will be returned when listing available contacts with this mission profile selected.

 The satellite will be tracked as it moves through the sky using the method specified by the referenced tracking config.

 The first dataflow edge in the list shows how to specify dataflow for a downlink contact. Data is delivered from the antenna to a dataflow endpoint. More specifically, data is flowed:
+ From the antenna using the parameters defined in this antenna downlink config:
  +  `arn:aws:groundstation:us-east-2:012345678910:config/antenna-downlink/11111111-1111-1111-1111-111111111111`
+ To the dataflow endpoint defined in this dataflow endpoint config:
  +  `arn:aws:groundstation:us-east-2:012345678910:config/dataflow-endpoint/22222222-2222-2222-2222-222222222222`

 The second dataflow edge in the list shows how to specify dataflow for an uplink contact. Data is delivered from a dataflow endpoint to the antenna for transmission to a satellite. More specifically, data is flowed:
+ From the dataflow endpoint defined in this dataflow endpoint config:
  +  `arn:aws:groundstation:us-east-2:012345678910:config/dataflow-endpoint/33333333-3333-3333-3333-333333333333`
+ To the antenna using the parameters defined in this antenna uplink config:
  +  `arn:aws:groundstation:us-east-2:012345678910:config/antenna-uplink/44444444-4444-4444-4444-444444444444`

#### JSON
<a name="aws-resource-groundstation-missionprofile--examples--Mission_Profile_With_Downlink_And_Uplink--json"></a>

```
{
  "Resources": {
    "MyMissionProfile": {
      "Type": "AWS::GroundStation::MissionProfile",
      "Properties": {
        "Name": "My Mission Profile",
        "ContactPrePassDurationSeconds": 120,
        "ContactPostPassDurationSeconds": 180,
        "MinimumViableContactDurationSeconds": 300,
        "TrackingConfigArn": "arn:aws:groundstation:us-east-2:012345678910:config/tracking/00000000-0000-0000-0000-000000000000",
        "TelemetrySinkConfigArn": "arn:aws:groundstation:us-east-2:012345678910:config/telemetry-sink/55555555-5555-5555-5555-555555555555",
        "DataflowEdges": [
          {
            "Source": "arn:aws:groundstation:us-east-2:012345678910:config/antenna-downlink/11111111-1111-1111-1111-111111111111",
            "Destination": "arn:aws:groundstation:us-east-2:012345678910:config/dataflow-endpoint/22222222-2222-2222-2222-222222222222"
          },
          {
            "Source": "arn:aws:groundstation:us-east-2:012345678910:config/dataflow-endpoint/33333333-3333-3333-3333-333333333333",
            "Destination": "arn:aws:groundstation:us-east-2:012345678910:config/antenna-uplink/44444444-4444-4444-4444-444444444444"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-groundstation-missionprofile--examples--Mission_Profile_With_Downlink_And_Uplink--yaml"></a>

```
Resources:
  MyMissionProfile:
    Type: AWS::GroundStation::MissionProfile
    Properties:
      Name: "Mission Profile"
      ContactPrePassDurationSeconds: 120
      ContactPostPassDurationSeconds: 180
      MinimumViableContactDurationSeconds: 300
      TrackingConfigArn: arn:aws:groundstation:us-east-2:012345678910:config/tracking/00000000-0000-0000-0000-000000000000
      TelemetrySinkConfigArn: arn:aws:groundstation:us-east-2:012345678910:config/telemetry-sink/55555555-5555-5555-5555-555555555555
      DataflowEdges:
        - Source: arn:aws:groundstation:us-east-2:012345678910:config/antenna-downlink/11111111-1111-1111-1111-111111111111
          Destination: arn:aws:groundstation:us-east-2:012345678910:config/dataflow-endpoint/22222222-2222-2222-2222-222222222222
        - Source: arn:aws:groundstation:us-east-2:012345678910:config/dataflow-endpoint/33333333-3333-3333-3333-333333333333
          Destination: arn:aws:groundstation:us-east-2:012345678910:config/antenna-uplink/44444444-4444-4444-4444-444444444444
```
