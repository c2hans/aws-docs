---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Multiplexprogram MultiplexProgramPacketIdentifiersMap
<a name="aws-properties-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap"></a>

Packet identifiers map for a given Multiplex program.

## Syntax
<a name="aws-properties-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-syntax.json"></a>

```
{
  "[AudioPids](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-audiopids)" : {{[ Integer, ... ]}},
  "[DvbSubPids](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-dvbsubpids)" : {{[ Integer, ... ]}},
  "[DvbTeletextPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-dvbteletextpid)" : {{Integer}},
  "[EtvPlatformPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-etvplatformpid)" : {{Integer}},
  "[EtvSignalPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-etvsignalpid)" : {{Integer}},
  "[KlvDataPids](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-klvdatapids)" : {{[ Integer, ... ]}},
  "[PcrPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-pcrpid)" : {{Integer}},
  "[PmtPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-pmtpid)" : {{Integer}},
  "[PrivateMetadataPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-privatemetadatapid)" : {{Integer}},
  "[Scte27Pids](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-scte27pids)" : {{[ Integer, ... ]}},
  "[Scte35Pid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-scte35pid)" : {{Integer}},
  "[TimedMetadataPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-timedmetadatapid)" : {{Integer}},
  "[VideoPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-videopid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-syntax.yaml"></a>

```
  [AudioPids](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-audiopids): {{
    - Integer}}
  [DvbSubPids](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-dvbsubpids): {{
    - Integer}}
  [DvbTeletextPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-dvbteletextpid): {{Integer}}
  [EtvPlatformPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-etvplatformpid): {{Integer}}
  [EtvSignalPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-etvsignalpid): {{Integer}}
  [KlvDataPids](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-klvdatapids): {{
    - Integer}}
  [PcrPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-pcrpid): {{Integer}}
  [PmtPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-pmtpid): {{Integer}}
  [PrivateMetadataPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-privatemetadatapid): {{Integer}}
  [Scte27Pids](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-scte27pids): {{
    - Integer}}
  [Scte35Pid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-scte35pid): {{Integer}}
  [TimedMetadataPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-timedmetadatapid): {{Integer}}
  [VideoPid](#cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-videopid): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-properties"></a>

`AudioPids`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-audiopids"></a>
Property description not available.
*Required*: No
*Type*: Array of Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DvbSubPids`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-dvbsubpids"></a>
Property description not available.
*Required*: No
*Type*: Array of Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DvbTeletextPid`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-dvbteletextpid"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EtvPlatformPid`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-etvplatformpid"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EtvSignalPid`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-etvsignalpid"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KlvDataPids`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-klvdatapids"></a>
Property description not available.
*Required*: No
*Type*: Array of Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PcrPid`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-pcrpid"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PmtPid`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-pmtpid"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateMetadataPid`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-privatemetadatapid"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scte27Pids`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-scte27pids"></a>
Property description not available.
*Required*: No
*Type*: Array of Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scte35Pid`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-scte35pid"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimedMetadataPid`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-timedmetadatapid"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoPid`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampacketidentifiersmap-videopid"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
