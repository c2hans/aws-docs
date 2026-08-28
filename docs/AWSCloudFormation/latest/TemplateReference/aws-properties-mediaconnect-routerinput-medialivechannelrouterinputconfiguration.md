---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-medialivechannelrouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput MediaLiveChannelRouterInputConfiguration
<a name="aws-properties-mediaconnect-routerinput-medialivechannelrouterinputconfiguration"></a>

Configuration settings for connecting a router input to a MediaLive channel output.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-syntax.json"></a>

```
{
  "[MediaLiveChannelArn](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivechannelarn)" : {{String}},
  "[MediaLiveChannelOutputName](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivechanneloutputname)" : {{String}},
  "[MediaLivePipelineId](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivepipelineid)" : {{String}},
  "[SourceTransitDecryption](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-sourcetransitdecryption)" : {{MediaLiveTransitEncryption}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-syntax.yaml"></a>

```
  [MediaLiveChannelArn](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivechannelarn): {{String}}
  [MediaLiveChannelOutputName](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivechanneloutputname): {{String}}
  [MediaLivePipelineId](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivepipelineid): {{String}}
  [SourceTransitDecryption](#cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-sourcetransitdecryption): {{
    MediaLiveTransitEncryption}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-properties"></a>

`MediaLiveChannelArn`  <a name="cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivechannelarn"></a>
The ARN of the MediaLive channel to connect to this router input.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):medialive:[a-z0-9-]+:[0-9]{12}:channel:[a-zA-Z0-9]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaLiveChannelOutputName`  <a name="cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivechanneloutputname"></a>
The name of the MediaLive channel output to connect to this router input.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaLivePipelineId`  <a name="cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-medialivepipelineid"></a>
The index of the MediaLive pipeline to connect to this router input.
*Required*: No
*Type*: String
*Allowed values*: `PIPELINE_0 | PIPELINE_1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceTransitDecryption`  <a name="cfn-mediaconnect-routerinput-medialivechannelrouterinputconfiguration-sourcetransitdecryption"></a>
The decryption configuration for the MediaLive channel source when connected to this router input.
*Required*: Yes
*Type*: [MediaLiveTransitEncryption](aws-properties-mediaconnect-routerinput-medialivetransitencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
