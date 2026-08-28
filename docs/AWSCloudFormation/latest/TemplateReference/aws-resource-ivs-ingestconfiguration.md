---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ivs-ingestconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::IngestConfiguration
<a name="aws-resource-ivs-ingestconfiguration"></a>

The `AWS::IVS::IngestConfiguration` resource specifies an ingest protocol to be used for a stage. For more information, see [Stream Ingest](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html) in the *Amazon IVS Real-Time Streaming User Guide*.

## Syntax
<a name="aws-resource-ivs-ingestconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ivs-ingestconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::IVS::IngestConfiguration",
  "Properties" : {
      "[IngestProtocol](#cfn-ivs-ingestconfiguration-ingestprotocol)" : {{String}},
      "[InsecureIngest](#cfn-ivs-ingestconfiguration-insecureingest)" : {{Boolean}},
      "[Name](#cfn-ivs-ingestconfiguration-name)" : {{String}},
      "[StageArn](#cfn-ivs-ingestconfiguration-stagearn)" : {{String}},
      "[Tags](#cfn-ivs-ingestconfiguration-tags)" : {{[ Tag, ... ]}},
      "[UserId](#cfn-ivs-ingestconfiguration-userid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ivs-ingestconfiguration-syntax.yaml"></a>

```
Type: AWS::IVS::IngestConfiguration
Properties:
  [IngestProtocol](#cfn-ivs-ingestconfiguration-ingestprotocol): {{String}}
  [InsecureIngest](#cfn-ivs-ingestconfiguration-insecureingest): {{Boolean}}
  [Name](#cfn-ivs-ingestconfiguration-name): {{String}}
  [StageArn](#cfn-ivs-ingestconfiguration-stagearn): {{String}}
  [Tags](#cfn-ivs-ingestconfiguration-tags): {{
    - Tag}}
  [UserId](#cfn-ivs-ingestconfiguration-userid): {{String}}
```

## Properties
<a name="aws-resource-ivs-ingestconfiguration-properties"></a>

`IngestProtocol`  <a name="cfn-ivs-ingestconfiguration-ingestprotocol"></a>
Type of ingest protocol that the user employs for broadcasting.
*Required*: No
*Type*: String
*Allowed values*: `RTMP | RTMPS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InsecureIngest`  <a name="cfn-ivs-ingestconfiguration-insecureingest"></a>
Whether the channel allows insecure RTMP ingest. Default: `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-ivs-ingestconfiguration-name"></a>
Ingest name.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]*$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StageArn`  <a name="cfn-ivs-ingestconfiguration-stagearn"></a>
ARN of the stage with which the IngestConfiguration is associated.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ivs-ingestconfiguration-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-ivs-ingestconfiguration-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserId`  <a name="cfn-ivs-ingestconfiguration-userid"></a>
Customer-assigned name to help identify the participant using the IngestConfiguration; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ivs-ingestconfiguration-return-values"></a>

### Ref
<a name="aws-resource-ivs-ingestconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ingest configuration ARN. For example:

 `{ "Ref": "myIngestConfiguration" }`

For the Amazon IVS ingest configuration `myIngestConfiguration`, `Ref` returns the ingest configuration ARN.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ivs-ingestconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ivs-ingestconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ingest-configuration ARN. For example: `arn:aws:ivs:us-west-2:123456789012:ingest-configuration/abcdABCDefgh`

`ParticipantId`  <a name="ParticipantId-fn::getatt"></a>
ID of the participant within the stage. For example: `abCDEf12GHIj`

`State`  <a name="State-fn::getatt"></a>
State of the ingest configuration. It is `ACTIVE` if a publisher currently is publishing to the stage associated with the ingest configuration. Valid values: `ACTIVE` \| `INACTIVE`.

`StreamKey`  <a name="StreamKey-fn::getatt"></a>
Ingest-key value for the RTMP(S) protocol. For example: `skSKABCDefgh`

## Examples
<a name="aws-resource-ivs-ingestconfiguration--examples"></a>

### Ingest Configuration Template Examples
<a name="aws-resource-ivs-ingestconfiguration--examples--Ingest_Configuration_Template_Examples"></a>

The following examples specify an Amazon IVS ingest configuration.

#### JSON
<a name="aws-resource-ivs-ingestconfiguration--examples--Ingest_Configuration_Template_Examples--json"></a>

```
{
     "AWSTemplateFormatVersion": "2010-09-09",
     "Resources": {
         "Stage": {
             "Type": "AWS::IVS::Stage",
             "Properties": {
                 "Name": "myStage",
                 "Tags": [
                     {
                         "Key": "MyKey",
                         "Value": "MyValue"
                     }
                 ]
             }
         },
         "IngestConfiguration": {
             "Type": "AWS::IVS::IngestConfiguration",
             "Properties": {
                 "Name": "myIngest",
                 "StageArn": {"Ref": "Stage"},
                 "IngestProtocol": "RTMPS",
                 "InsecureIngest": false,
                 "UserId": "myUser",
                 "Tags": [
                     {
                         "Key": "MyKey",
                         "Value": "MyValue"
                     }
                 ]
             }
         }
     },
     "Outputs": {
         "IngestConfigurationArn": {
             "Value": {"Ref": "IngestConfiguration"}
         },
         "IngestConfigurationState": {
             "Value": {
                 "Fn::GetAtt": [
                     "IngestConfiguration",
                     "State"
                 ]
             }
         },
         "IngestConfigurationStreamKey": {
             "Value": {
                 "Fn::GetAtt": [
                     "IngestConfiguration",
                     "StreamKey"
                 ]
             }
         },
         "IngestConfigurationParticipantId": {
             "Value": {
                 "Fn::GetAtt": [
                     "IngestConfiguration",
                     "ParticipantId"
                 ]
			 }
         }
     }
 }
```

#### YAML
<a name="aws-resource-ivs-ingestconfiguration--examples--Ingest_Configuration_Template_Examples--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  Stage:
    Type: AWS::IVS::Stage
    Properties:
      Name: MyStage
      Tags:
        - Key: MyKey
          Value: MyValue

  IngestConfiguration:
    Type: AWS::IVS::IngestConfiguration
    Properties:
      Name: myIngestName
      IngestProtocol: RTMPS
      InsecureIngest: false
      UserId: myUser
      StageArn: !Ref Stage
      Tags:
        - Key: MyKey
          Value: MyValue

Outputs:
  IngestConfigurationArn:
    Value: !Ref IngestConfiguration

  IngestConfigurationState:
    Value: !GetAtt IngestConfiguration.State

  IngestConfigurationStreamKey:
    Value: !GetAtt IngestConfiguration.StreamKey

  IngestConfigurationParticipantId:
    Value: !GetAtt IngestConfiguration.ParticipantId
```

## See also
<a name="aws-resource-ivs-ingestconfiguration--seealso"></a>
+  [IVS Stream Ingest](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html)
+ [IngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_IngestConfiguration.html) data type
+ [CreateIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateIngestConfiguration.html) API endpoint
+ [DeleteIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeleteIngestConfiguration.html) API endpoint
+ [GetIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetIngestConfiguration.html) API endpoint
+ [ListIngestConfigurations](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListIngestConfigurations.html) API endpoint
+ [UpdateIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_UpdateIngestConfiguration.html) API endpoint

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
