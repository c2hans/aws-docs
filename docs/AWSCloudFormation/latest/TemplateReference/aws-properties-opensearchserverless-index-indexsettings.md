---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-index-indexsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::Index IndexSettings
<a name="aws-properties-opensearchserverless-index-indexsettings"></a>

Index settings for the OpenSearch Serverless index.

## Syntax
<a name="aws-properties-opensearchserverless-index-indexsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-index-indexsettings-syntax.json"></a>

```
{
  "[Analysis](#cfn-opensearchserverless-index-indexsettings-analysis)" : {{Analysis}},
  "[Index](#cfn-opensearchserverless-index-indexsettings-index)" : {{Index}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-index-indexsettings-syntax.yaml"></a>

```
  [Analysis](#cfn-opensearchserverless-index-indexsettings-analysis): {{
    Analysis}}
  [Index](#cfn-opensearchserverless-index-indexsettings-index): {{
    Index}}
```

## Properties
<a name="aws-properties-opensearchserverless-index-indexsettings-properties"></a>

`Analysis`  <a name="cfn-opensearchserverless-index-indexsettings-analysis"></a>
Property description not available.
*Required*: No
*Type*: [Analysis](aws-properties-opensearchserverless-index-analysis.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Index`  <a name="cfn-opensearchserverless-index-indexsettings-index"></a>
Index settings.
*Required*: No
*Type*: [Index](aws-properties-opensearchserverless-index-index.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
