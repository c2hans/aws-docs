---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-multiplexprogram.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Multiplexprogram
<a name="aws-resource-medialive-multiplexprogram"></a>

Creates a multiplex program. A multiplex program specifies the settings for one channel in a multiplex.

## Syntax
<a name="aws-resource-medialive-multiplexprogram-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-multiplexprogram-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::Multiplexprogram",
  "Properties" : {
      "[MultiplexId](#cfn-medialive-multiplexprogram-multiplexid)" : {{String}},
      "[MultiplexProgramSettings](#cfn-medialive-multiplexprogram-multiplexprogramsettings)" : {{MultiplexProgramSettings}},
      "[PacketIdentifiersMap](#cfn-medialive-multiplexprogram-packetidentifiersmap)" : {{MultiplexProgramPacketIdentifiersMap}},
      "[PipelineDetails](#cfn-medialive-multiplexprogram-pipelinedetails)" : {{[ MultiplexProgramPipelineDetail, ... ]}},
      "[PreferredChannelPipeline](#cfn-medialive-multiplexprogram-preferredchannelpipeline)" : {{String}},
      "[ProgramName](#cfn-medialive-multiplexprogram-programname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-medialive-multiplexprogram-syntax.yaml"></a>

```
Type: AWS::MediaLive::Multiplexprogram
Properties:
  [MultiplexId](#cfn-medialive-multiplexprogram-multiplexid): {{String}}
  [MultiplexProgramSettings](#cfn-medialive-multiplexprogram-multiplexprogramsettings): {{
    MultiplexProgramSettings}}
  [PacketIdentifiersMap](#cfn-medialive-multiplexprogram-packetidentifiersmap): {{
    MultiplexProgramPacketIdentifiersMap}}
  [PipelineDetails](#cfn-medialive-multiplexprogram-pipelinedetails): {{
    - MultiplexProgramPipelineDetail}}
  [PreferredChannelPipeline](#cfn-medialive-multiplexprogram-preferredchannelpipeline): {{String}}
  [ProgramName](#cfn-medialive-multiplexprogram-programname): {{String}}
```

## Properties
<a name="aws-resource-medialive-multiplexprogram-properties"></a>

`MultiplexId`  <a name="cfn-medialive-multiplexprogram-multiplexid"></a>
The unique id of the multiplex.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MultiplexProgramSettings`  <a name="cfn-medialive-multiplexprogram-multiplexprogramsettings"></a>
Multiplex Program settings configuration.
*Required*: No
*Type*: [MultiplexProgramSettings](aws-properties-medialive-multiplexprogram-multiplexprogramsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PacketIdentifiersMap`  <a name="cfn-medialive-multiplexprogram-packetidentifiersmap"></a>
The packet identifier map for this multiplex program.
*Required*: No
*Type*: [MultiplexProgramPacketIdentifiersMap](aws-properties-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PipelineDetails`  <a name="cfn-medialive-multiplexprogram-pipelinedetails"></a>
Contains information about the current sources for the specified program in the specified multiplex.
*Required*: No
*Type*: Array of [MultiplexProgramPipelineDetail](aws-properties-medialive-multiplexprogram-multiplexprogrampipelinedetail.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreferredChannelPipeline`  <a name="cfn-medialive-multiplexprogram-preferredchannelpipeline"></a>
Indicates which pipeline is preferred by the multiplex for program ingest. If set to \\"PIPELINE\_0\\" or \\"PIPELINE\_1\\" and an unhealthy ingest causes the multiplex to switch to the non-preferred pipeline, it will switch back once that ingest is healthy again. If set to \\"CURRENTLY\_ACTIVE\\", it will not switch back to the other pipeline based on it recovering to a healthy state, it will only switch if the active pipeline becomes unhealthy.
*Required*: No
*Type*: String
*Allowed values*: `CURRENTLY_ACTIVE | PIPELINE_0 | PIPELINE_1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProgramName`  <a name="cfn-medialive-multiplexprogram-programname"></a>
The name of the multiplex program.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-medialive-multiplexprogram-return-values"></a>

### Ref
<a name="aws-resource-medialive-multiplexprogram-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-medialive-multiplexprogram-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-multiplexprogram-return-values-fn--getatt-fn--getatt"></a>

`ChannelId`  <a name="ChannelId-fn::getatt"></a>
The unique ID of the channel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
