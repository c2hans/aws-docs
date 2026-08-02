---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-addecisionserverconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration AdDecisionServerConfiguration
<a name="aws-properties-mediatailor-playbackconfiguration-addecisionserverconfiguration"></a>

Configuration parameters for customizing HTTP requests sent to the ad decision server (ADS). This allows you to specify the HTTP method, headers, request body, and compression settings for ADS requests.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-addecisionserverconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-addecisionserverconfiguration-syntax.json"></a>

```
{
  "[HttpRequest](#cfn-mediatailor-playbackconfiguration-addecisionserverconfiguration-httprequest)" : {{HttpRequest}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-addecisionserverconfiguration-syntax.yaml"></a>

```
  [HttpRequest](#cfn-mediatailor-playbackconfiguration-addecisionserverconfiguration-httprequest): {{
    HttpRequest}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-addecisionserverconfiguration-properties"></a>

`HttpRequest`  <a name="cfn-mediatailor-playbackconfiguration-addecisionserverconfiguration-httprequest"></a>
The HTTP request configuration parameters for the ad decision server.
*Required*: Yes
*Type*: [HttpRequest](aws-properties-mediatailor-playbackconfiguration-httprequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
