---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-hlsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration HlsConfiguration
<a name="aws-properties-mediatailor-playbackconfiguration-hlsconfiguration"></a>

The configuration for HLS content.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-hlsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-hlsconfiguration-syntax.json"></a>

```
{
  "[ManifestEndpointPrefix](#cfn-mediatailor-playbackconfiguration-hlsconfiguration-manifestendpointprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-hlsconfiguration-syntax.yaml"></a>

```
  [ManifestEndpointPrefix](#cfn-mediatailor-playbackconfiguration-hlsconfiguration-manifestendpointprefix): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-hlsconfiguration-properties"></a>

`ManifestEndpointPrefix`  <a name="cfn-mediatailor-playbackconfiguration-hlsconfiguration-manifestendpointprefix"></a>
The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
