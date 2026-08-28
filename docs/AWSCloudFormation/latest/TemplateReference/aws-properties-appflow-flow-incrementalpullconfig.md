---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-incrementalpullconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow IncrementalPullConfig
<a name="aws-properties-appflow-flow-incrementalpullconfig"></a>

 Specifies the configuration used when importing incremental records from the source.

## Syntax
<a name="aws-properties-appflow-flow-incrementalpullconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-incrementalpullconfig-syntax.json"></a>

```
{
  "[DatetimeTypeFieldName](#cfn-appflow-flow-incrementalpullconfig-datetimetypefieldname)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-incrementalpullconfig-syntax.yaml"></a>

```
  [DatetimeTypeFieldName](#cfn-appflow-flow-incrementalpullconfig-datetimetypefieldname): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-incrementalpullconfig-properties"></a>

`DatetimeTypeFieldName`  <a name="cfn-appflow-flow-incrementalpullconfig-datetimetypefieldname"></a>
 A field that specifies the date time or timestamp field as the criteria to use when importing incremental records from the source.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
