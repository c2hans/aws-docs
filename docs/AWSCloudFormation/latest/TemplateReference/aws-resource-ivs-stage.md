---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ivs-stage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Stage
<a name="aws-resource-ivs-stage"></a>

The `AWS::IVS::Stage` resource specifies an Amazon IVS stage. A stage is a virtual space where participants can exchange video in real time. For more information, see [CreateStage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateStage.html) in the *Amazon IVS Real-Time Streaming API Reference*.

## Syntax
<a name="aws-resource-ivs-stage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ivs-stage-syntax.json"></a>

```
{
  "Type" : "AWS::IVS::Stage",
  "Properties" : {
      "[AutoParticipantRecordingConfiguration](#cfn-ivs-stage-autoparticipantrecordingconfiguration)" : {{AutoParticipantRecordingConfiguration}},
      "[Name](#cfn-ivs-stage-name)" : {{String}},
      "[Tags](#cfn-ivs-stage-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ivs-stage-syntax.yaml"></a>

```
Type: AWS::IVS::Stage
Properties:
  [AutoParticipantRecordingConfiguration](#cfn-ivs-stage-autoparticipantrecordingconfiguration): {{
    AutoParticipantRecordingConfiguration}}
  [Name](#cfn-ivs-stage-name): {{String}}
  [Tags](#cfn-ivs-stage-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ivs-stage-properties"></a>

`AutoParticipantRecordingConfiguration`  <a name="cfn-ivs-stage-autoparticipantrecordingconfiguration"></a>
Configuration object for individual participant recording.
*Required*: No
*Type*: [AutoParticipantRecordingConfiguration](aws-properties-ivs-stage-autoparticipantrecordingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ivs-stage-name"></a>
Stage name.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]*$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ivs-stage-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-stage-tag.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-ivs-stage-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ivs-stage-return-values"></a>

### Ref
<a name="aws-resource-ivs-stage-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the stage ARN. For example:

 `{ "Ref": "myStage" }`

For the Amazon IVS stage `myStage`, `Ref` returns the stage ARN.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ivs-stage-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ivs-stage-return-values-fn--getatt-fn--getatt"></a>

`ActiveSessionId`  <a name="ActiveSessionId-fn::getatt"></a>
ID of the active session within the stage. For example: `st-a1b2c3d4e5f6g`

`Arn`  <a name="Arn-fn::getatt"></a>
The stage ARN. For example: `arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`

## Examples
<a name="aws-resource-ivs-stage--examples"></a>

### Stage Template Examples
<a name="aws-resource-ivs-stage--examples--Stage_Template_Examples"></a>

The following examples specify an Amazon IVS stage.

#### JSON
<a name="aws-resource-ivs-stage--examples--Stage_Template_Examples--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "StorageConfiguration": {
            "Type": "AWS::IVS::StorageConfiguration",
            "Properties": {
                "Name": "myStorageConfiguration",
                "S3": { "BucketName": "my-bucket" },
                "Tags": [
                    {
                        "Key": "MyKey",
                        "Value": "MyValue"
                    }
                ]
            }
        },
        "Stage": {
            "Type": "AWS::IVS::Stage",
            "Properties": {
                "Name": "myStage",
                "AutoParticipantRecordingConfiguration": {
                    "StorageConfigurationArn": {
                        "Ref": "StorageConfiguration"
                    },
                    "MediaTypes": [
                        "AUDIO_VIDEO"
                    ],
                    "HlsConfiguration": {
                        "ParticipantRecordingHlsConfiguration": {
                            "TargetSegmentDurationSeconds": 5
                        }
                    },
                    "RecordingReconnectWindowSeconds": 30,
                    "ThumbnailConfiguration": {
                        "ParticipantThumbnailConfiguration": {
                            "RecordingMode": "INTERVAL",
                            "TargetIntervalSeconds": 2,
                            "Storage": [
                                "SEQUENTIAL",
                                "LATEST"
                            ]
                        }
                    }
                },
                "Tags": [
                    {
                        "Key": "MyKey",
                        "Value": "MyValue"
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ivs-stage--examples--Stage_Template_Examples--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  StorageConfiguration:
    Type: AWS::IVS::StorageConfiguration
    Properties:
      Name: myStorageConfiguration
      S3:
        BucketName: my-bucket
      Tags:
        - Key: myKey
          Value: myValue
  Stage:
    Type: AWS::IVS::Stage
    Properties:
      Name: myStage
      AutoParticipantRecordingConfiguration:
        HlsConfiguration:
          ParticipantRecordingHlsConfiguration:
            TargetSegmentDurationSeconds: 5
        MediaTypes:
          - AUDIO_VIDEO
        RecordingReconnectWindowSeconds: 30
        StorageConfigurationArn: !Ref StorageConfiguration
        ThumbnailConfiguration:
          ParticipantThumbnailConfiguration:
            RecordingMode: INTERVAL
            TargetIntervalSeconds: 2
            Storage:
              - SEQUENTIAL
              - LATEST
      Tags:
        - Key: myKey
          Value: myValue
```

## See also
<a name="aws-resource-ivs-stage--seealso"></a>
+  [Getting Started with IVS Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started.html)
+ [Stage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Stage.html) data type
+ [CreateStage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateStage.html) API endpoint
