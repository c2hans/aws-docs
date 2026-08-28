---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-sourcelocation-httpconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::SourceLocation HttpConfiguration
<a name="aws-properties-mediatailor-sourcelocation-httpconfiguration"></a>

The HTTP configuration for the source location.

## Syntax
<a name="aws-properties-mediatailor-sourcelocation-httpconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-sourcelocation-httpconfiguration-syntax.json"></a>

```
{
  "[BaseUrl](#cfn-mediatailor-sourcelocation-httpconfiguration-baseurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-sourcelocation-httpconfiguration-syntax.yaml"></a>

```
  [BaseUrl](#cfn-mediatailor-sourcelocation-httpconfiguration-baseurl): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-sourcelocation-httpconfiguration-properties"></a>

`BaseUrl`  <a name="cfn-mediatailor-sourcelocation-httpconfiguration-baseurl"></a>
The base URL for the source location host server. This string must include the protocol, such as **https://**.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
