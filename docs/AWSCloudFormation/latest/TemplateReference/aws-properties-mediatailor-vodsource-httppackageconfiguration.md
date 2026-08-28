---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-vodsource-httppackageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::VodSource HttpPackageConfiguration
<a name="aws-properties-mediatailor-vodsource-httppackageconfiguration"></a>

The HTTP package configuration properties for the requested VOD source.

## Syntax
<a name="aws-properties-mediatailor-vodsource-httppackageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-vodsource-httppackageconfiguration-syntax.json"></a>

```
{
  "[Path](#cfn-mediatailor-vodsource-httppackageconfiguration-path)" : {{String}},
  "[SourceGroup](#cfn-mediatailor-vodsource-httppackageconfiguration-sourcegroup)" : {{String}},
  "[Type](#cfn-mediatailor-vodsource-httppackageconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-vodsource-httppackageconfiguration-syntax.yaml"></a>

```
  [Path](#cfn-mediatailor-vodsource-httppackageconfiguration-path): {{String}}
  [SourceGroup](#cfn-mediatailor-vodsource-httppackageconfiguration-sourcegroup): {{String}}
  [Type](#cfn-mediatailor-vodsource-httppackageconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-vodsource-httppackageconfiguration-properties"></a>

`Path`  <a name="cfn-mediatailor-vodsource-httppackageconfiguration-path"></a>
The relative path to the URL for this VOD source. This is combined with `SourceLocation::HttpConfiguration::BaseUrl` to form a valid URL.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceGroup`  <a name="cfn-mediatailor-vodsource-httppackageconfiguration-sourcegroup"></a>
The name of the source group. This has to match one of the `Channel::Outputs::SourceGroup`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-mediatailor-vodsource-httppackageconfiguration-type"></a>
The streaming protocol for this package configuration. Supported values are `HLS` and `DASH`.
*Required*: Yes
*Type*: String
*Allowed values*: `DASH | HLS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
