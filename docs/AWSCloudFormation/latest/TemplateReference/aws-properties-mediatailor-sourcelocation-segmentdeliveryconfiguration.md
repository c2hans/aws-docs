---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::SourceLocation SegmentDeliveryConfiguration
<a name="aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration"></a>

The segment delivery configuration settings.

## Syntax
<a name="aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration-syntax.json"></a>

```
{
  "[BaseUrl](#cfn-mediatailor-sourcelocation-segmentdeliveryconfiguration-baseurl)" : {{String}},
  "[Name](#cfn-mediatailor-sourcelocation-segmentdeliveryconfiguration-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration-syntax.yaml"></a>

```
  [BaseUrl](#cfn-mediatailor-sourcelocation-segmentdeliveryconfiguration-baseurl): {{String}}
  [Name](#cfn-mediatailor-sourcelocation-segmentdeliveryconfiguration-name): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration-properties"></a>

`BaseUrl`  <a name="cfn-mediatailor-sourcelocation-segmentdeliveryconfiguration-baseurl"></a>
The base URL of the host or path of the segment delivery server that you're using to serve segments. This is typically a content delivery network (CDN). The URL can be absolute or relative. To use an absolute URL include the protocol, such as `https://example.com/some/path`. To use a relative URL specify the relative path, such as `/some/path*`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediatailor-sourcelocation-segmentdeliveryconfiguration-name"></a>
A unique identifier used to distinguish between multiple segment delivery configurations in a source location.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
