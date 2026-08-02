---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-flow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow
<a name="aws-resource-mediaconnect-flow"></a>

The `AWS::MediaConnect::Flow` resource defines a connection between one or more video sources and one or more outputs. For each flow, you specify the transport protocol to use, encryption information, and details for any outputs or entitlements that you want. AWS Elemental MediaConnect returns an ingest endpoint where you can send your live video as a single unicast stream. The service replicates and distributes the video to every output that you specify, whether inside or outside the AWS Cloud. You can also set up entitlements on a flow to allow other AWS accounts to access your content.

## Syntax
<a name="aws-resource-mediaconnect-flow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-flow-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConnect::Flow",
  "Properties" : {
      "[AvailabilityZone](#cfn-mediaconnect-flow-availabilityzone)" : {{String}},
      "[EncodingConfig](#cfn-mediaconnect-flow-encodingconfig)" : {{EncodingConfig}},
      "[FlowSize](#cfn-mediaconnect-flow-flowsize)" : {{String}},
      "[Maintenance](#cfn-mediaconnect-flow-maintenance)" : {{Maintenance}},
      "[MediaStreams](#cfn-mediaconnect-flow-mediastreams)" : {{[ MediaStream, ... ]}},
      "[Name](#cfn-mediaconnect-flow-name)" : {{String}},
      "[NdiConfig](#cfn-mediaconnect-flow-ndiconfig)" : {{NdiConfig}},
      "[Source](#cfn-mediaconnect-flow-source)" : {{Source}},
      "[SourceFailoverConfig](#cfn-mediaconnect-flow-sourcefailoverconfig)" : {{FailoverConfig}},
      "[SourceMonitoringConfig](#cfn-mediaconnect-flow-sourcemonitoringconfig)" : {{SourceMonitoringConfig}},
      "[Tags](#cfn-mediaconnect-flow-tags)" : {{[ Tag, ... ]}},
      "[VpcInterfaces](#cfn-mediaconnect-flow-vpcinterfaces)" : {{[ VpcInterface, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediaconnect-flow-syntax.yaml"></a>

```
Type: AWS::MediaConnect::Flow
Properties:
  [AvailabilityZone](#cfn-mediaconnect-flow-availabilityzone): {{String}}
  [EncodingConfig](#cfn-mediaconnect-flow-encodingconfig): {{
    EncodingConfig}}
  [FlowSize](#cfn-mediaconnect-flow-flowsize): {{String}}
  [Maintenance](#cfn-mediaconnect-flow-maintenance): {{
    Maintenance}}
  [MediaStreams](#cfn-mediaconnect-flow-mediastreams): {{
    - MediaStream}}
  [Name](#cfn-mediaconnect-flow-name): {{String}}
  [NdiConfig](#cfn-mediaconnect-flow-ndiconfig): {{
    NdiConfig}}
  [Source](#cfn-mediaconnect-flow-source): {{
    Source}}
  [SourceFailoverConfig](#cfn-mediaconnect-flow-sourcefailoverconfig): {{
    FailoverConfig}}
  [SourceMonitoringConfig](#cfn-mediaconnect-flow-sourcemonitoringconfig): {{
    SourceMonitoringConfig}}
  [Tags](#cfn-mediaconnect-flow-tags): {{
    - Tag}}
  [VpcInterfaces](#cfn-mediaconnect-flow-vpcinterfaces): {{
    - VpcInterface}}
```

## Properties
<a name="aws-resource-mediaconnect-flow-properties"></a>

`AvailabilityZone`  <a name="cfn-mediaconnect-flow-availabilityzone"></a>
 The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS Region.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncodingConfig`  <a name="cfn-mediaconnect-flow-encodingconfig"></a>
 The encoding configuration to apply to the NDI® source when transcoding it to a transport stream for downstream distribution.
*Required*: No
*Type*: [EncodingConfig](aws-properties-mediaconnect-flow-encodingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowSize`  <a name="cfn-mediaconnect-flow-flowsize"></a>
 Determines the processing capacity and feature set of the flow.
*Required*: No
*Type*: String
*Allowed values*: `MEDIUM | LARGE | LARGE_4X`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Maintenance`  <a name="cfn-mediaconnect-flow-maintenance"></a>
The maintenance settings you want to use for the flow.
*Required*: No
*Type*: [Maintenance](aws-properties-mediaconnect-flow-maintenance.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaStreams`  <a name="cfn-mediaconnect-flow-mediastreams"></a>
 The media streams that are associated with the flow. After you associate a media stream with a source, you can also associate it with outputs on the flow.
*Required*: No
*Type*: Array of [MediaStream](aws-properties-mediaconnect-flow-mediastream.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediaconnect-flow-name"></a>
 The name of the flow.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NdiConfig`  <a name="cfn-mediaconnect-flow-ndiconfig"></a>
Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output.
*Required*: No
*Type*: [NdiConfig](aws-properties-mediaconnect-flow-ndiconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-mediaconnect-flow-source"></a>
 The settings for the source that you want to use for the new flow.
*Required*: Yes
*Type*: [Source](aws-properties-mediaconnect-flow-source.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceFailoverConfig`  <a name="cfn-mediaconnect-flow-sourcefailoverconfig"></a>
 The settings for source failover.
*Required*: No
*Type*: [FailoverConfig](aws-properties-mediaconnect-flow-failoverconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceMonitoringConfig`  <a name="cfn-mediaconnect-flow-sourcemonitoringconfig"></a>
The settings for source monitoring.
*Required*: No
*Type*: [SourceMonitoringConfig](aws-properties-mediaconnect-flow-sourcemonitoringconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediaconnect-flow-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediaconnect-flow-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcInterfaces`  <a name="cfn-mediaconnect-flow-vpcinterfaces"></a>
 The VPC Interfaces for this flow.
*Required*: No
*Type*: Array of [VpcInterface](aws-properties-mediaconnect-flow-vpcinterface.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediaconnect-flow-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-flow-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the flow ARN. For example:

 `{ "Ref": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mediaconnect-flow-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mediaconnect-flow-return-values-fn--getatt-fn--getatt"></a>

`EgressIp`  <a name="EgressIp-fn::getatt"></a>
 The IP address from which video will be sent to output destinations.

`FlowArn`  <a name="FlowArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the flow.

`FlowAvailabilityZone`  <a name="FlowAvailabilityZone-fn::getatt"></a>
The Availability Zone that the flow was created in. These options are limited to the Availability Zones within the current AWS Region.

`FlowNdiMachineName`  <a name="FlowNdiMachineName-fn::getatt"></a>
 This read-only value represents the NDI machine name that MediaConnect automatically generated for this flow. These NDI machine names are only generated when you don't specify your own custom name.

`Source.IngestIp`  <a name="Source.IngestIp-fn::getatt"></a>
The IP address that the flow listens on for incoming content.

`Source.SourceArn`  <a name="Source.SourceArn-fn::getatt"></a>
The ARN of the source.

`Source.SourceIngestPort`  <a name="Source.SourceIngestPort-fn::getatt"></a>
The port that the flow listens on for incoming content. If the protocol of the source is Zixi, the port must be set to 2088.

## Examples
<a name="aws-resource-mediaconnect-flow--examples"></a>

**Topics**
+ [Enabling thumbnails](#aws-resource-mediaconnect-flow--examples--Enabling_thumbnails)
+ [Disabling thumbnails](#aws-resource-mediaconnect-flow--examples--Disabling_thumbnails)
+ [Setting a thumbnail state to `None`](#aws-resource-mediaconnect-flow--examples--Setting_a_thumbnail_state_to_None)

### Enabling thumbnails
<a name="aws-resource-mediaconnect-flow--examples--Enabling_thumbnails"></a>

This example demonstrates a flow that sets the thumbnail state to `ENABLED`. You can verify the thumbnail state using the `DescribeFlow` API operation.

#### JSON
<a name="aws-resource-mediaconnect-flow--examples--Enabling_thumbnails--json"></a>

```
{
  "Parameters": {
    "Name": {
      "Type": "String"
    }
  },
  "Resources": {
    "TestFlow": {
      "Type": "AWS::MediaConnect::Flow",
      "Properties": {
        "Name": {
          "Ref": "Name"
        },
        "Source": {
          "Name": "testSource",
          "Protocol": "rtp",
          "IngestPort": 1234,
          "Description": "CFN test Source",
          "WhitelistCidr": "0.0.0.0/0"
        },
        "Maintenance": {
          "MaintenanceDay": "Tuesday",
          "MaintenanceStartHour": "02:00"
        },
        "SourceMonitoringConfig": {
          "ThumbnailState": "ENABLED"
        }
      }
    }
  },
  "Outputs": {
    "FlowArn": {
      "Value": {
        "Ref": "TestFlow"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-mediaconnect-flow--examples--Enabling_thumbnails--yaml"></a>

```
Parameters:
  Name:
    Type: String

Resources:
  TestFlow:
    Type: AWS::MediaConnect::Flow
    Properties:
      Name: !Ref Name
      Source:
        Name: testSource
        Protocol: rtp
        IngestPort: 1234
        Description: CFN test Source
        WhitelistCidr: 0.0.0.0/0
      Maintenance:
        MaintenanceDay: Tuesday
        MaintenanceStartHour: 02:00
      SourceMonitoringConfig:
        ThumbnailState: ENABLED

Outputs:
  FlowArn:
    Value: !Ref TestFlow
```

### Disabling thumbnails
<a name="aws-resource-mediaconnect-flow--examples--Disabling_thumbnails"></a>

This example demonstrates a flow that sets the thumbnail state to `DISABLED`. You can verify the thumbnail state using the `DescribeFlow` API operation.

#### JSON
<a name="aws-resource-mediaconnect-flow--examples--Disabling_thumbnails--json"></a>

```
{
  "Parameters": {
    "Name": {
      "Type": "String"
    }
  },
  "Resources": {
    "TestFlow": {
      "Type": "AWS::MediaConnect::Flow",
      "Properties": {
        "Name": {
          "Ref": "Name"
        },
        "Source": {
          "Name": "testSource",
          "Protocol": "rtp",
          "IngestPort": 1234,
          "Description": "CFN test Source",
          "WhitelistCidr": "0.0.0.0/0"
        },
        "Maintenance": {
          "MaintenanceDay": "Tuesday",
          "MaintenanceStartHour": "02:00"
        },
        "SourceMonitoringConfig": {
          "ThumbnailState": "DISABLED"
        }
      }
    }
  },
  "Outputs": {
    "FlowArn": {
      "Value": {
        "Ref": "TestFlow"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-mediaconnect-flow--examples--Disabling_thumbnails--yaml"></a>

```
Parameters:
  Name:
    Type: String

Resources:
  TestFlow:
    Type: AWS::MediaConnect::Flow
    Properties:
      Name: !Ref Name
      Source:
        Name: testSource
        Protocol: rtp
        IngestPort: 1234
        Description: CFN test Source
        WhitelistCidr: 0.0.0.0/0
      Maintenance:
        MaintenanceDay: Tuesday
        MaintenanceStartHour: 02:00
      SourceMonitoringConfig:
        ThumbnailState: DISABLED

Outputs:
  FlowArn:
    Value: !Ref TestFlow
```

### Setting a thumbnail state to `None`
<a name="aws-resource-mediaconnect-flow--examples--Setting_a_thumbnail_state_to_None"></a>

If you don't specify a thumbnail state, it affects new and existing flows differently. Here's how it works in each scenario.

 **Creating a flow**

When you create a new flow without specifying a thumbnail state, no state has been set yet. After you create your flow in this way, the `DescribeFlow` API operation shows the thumbnail state as `NONE`.

 **Updating an existing flow**

When you update an existing flow and remove its thumbnail state (previously set to either `ENABLED` or `DISABLED`), you're altering a previously set state. In this case, the state doesn't become `NONE`. Instead, it defaults to `DISABLED`. This happens because after you've specified a state for an existing flow, it can't revert to `NONE`. The `NONE` state only applies when no state has been set before. After you update your flow in this way, the `DescribeFlow` API operation shows the thumbnail state as `DISABLED`, not `NONE`.

#### JSON
<a name="aws-resource-mediaconnect-flow--examples--Setting_a_thumbnail_state_to_None--json"></a>

```
{
  "Parameters": {
    "Name": {
      "Type": "String"
    }
  },
  "Resources": {
    "TestFlow": {
      "Type": "AWS::MediaConnect::Flow",
      "Properties": {
        "Name": {
          "Ref": "Name"
        },
        "Source": {
          "Name": "testSource",
          "Protocol": "rtp",
          "IngestPort": 1234,
          "Description": "CFN test Source",
          "WhitelistCidr": "0.0.0.0/0"
        },
        "Maintenance": {
          "MaintenanceDay": "Tuesday",
          "MaintenanceStartHour": "02:00"
        }
      }
    }
  },
  "Outputs": {
    "FlowArn": {
      "Value": {
        "Ref": "TestFlow"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-mediaconnect-flow--examples--Setting_a_thumbnail_state_to_None--yaml"></a>

```
Parameters:
  Name:
    Type: String

Resources:
  TestFlow:
    Type: AWS::MediaConnect::Flow
    Properties:
      Name: !Ref Name
      Source:
        Name: testSource
        Protocol: rtp
        IngestPort: 1234
        Description: CFN test Source
        WhitelistCidr: 0.0.0.0/0
      Maintenance:
        MaintenanceDay: Tuesday
        MaintenanceStartHour: 02:00

Outputs:
  FlowArn:
    Value: !Ref TestFlow
```
