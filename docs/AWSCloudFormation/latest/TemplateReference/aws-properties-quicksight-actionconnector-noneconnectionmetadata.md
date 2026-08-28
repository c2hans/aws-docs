---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-actionconnector-noneconnectionmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector NoneConnectionMetadata
<a name="aws-properties-quicksight-actionconnector-noneconnectionmetadata"></a>

Authentication metadata for connections that do not require authentication credentials.

## Syntax
<a name="aws-properties-quicksight-actionconnector-noneconnectionmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-actionconnector-noneconnectionmetadata-syntax.json"></a>

```
{
  "[BaseEndpoint](#cfn-quicksight-actionconnector-noneconnectionmetadata-baseendpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-actionconnector-noneconnectionmetadata-syntax.yaml"></a>

```
  [BaseEndpoint](#cfn-quicksight-actionconnector-noneconnectionmetadata-baseendpoint): {{String}}
```

## Properties
<a name="aws-properties-quicksight-actionconnector-noneconnectionmetadata-properties"></a>

`BaseEndpoint`  <a name="cfn-quicksight-actionconnector-noneconnectionmetadata-baseendpoint"></a>
The base endpoint URL for connections that do not require authentication.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*`
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
