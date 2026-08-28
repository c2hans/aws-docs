---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput MediaLiveInputRouterOutputConfiguration
<a name="aws-properties-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration"></a>

Configuration settings for connecting a router output to a MediaLive input.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-syntax.json"></a>

```
{
  "[DestinationTransitEncryption](#cfn-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-destinationtransitencryption)" : {{MediaLiveTransitEncryption}},
  "[MediaLiveInputArn](#cfn-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-medialiveinputarn)" : {{String}},
  "[MediaLivePipelineId](#cfn-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-medialivepipelineid)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-syntax.yaml"></a>

```
  [DestinationTransitEncryption](#cfn-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-destinationtransitencryption): {{
    MediaLiveTransitEncryption}}
  [MediaLiveInputArn](#cfn-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-medialiveinputarn): {{String}}
  [MediaLivePipelineId](#cfn-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-medialivepipelineid): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-properties"></a>

`DestinationTransitEncryption`  <a name="cfn-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-destinationtransitencryption"></a>
The encryption configuration for the MediaLive input when connected to this router output.
*Required*: Yes
*Type*: [MediaLiveTransitEncryption](aws-properties-mediaconnect-routeroutput-medialivetransitencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaLiveInputArn`  <a name="cfn-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-medialiveinputarn"></a>
The ARN of the MediaLive input to connect to this router output.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):medialive:[a-z0-9-]+:[0-9]{12}:input:[a-zA-Z0-9]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaLivePipelineId`  <a name="cfn-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-medialivepipelineid"></a>
The index of the MediaLive pipeline to connect to this router output.
*Required*: No
*Type*: String
*Allowed values*: `PIPELINE_0 | PIPELINE_1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
