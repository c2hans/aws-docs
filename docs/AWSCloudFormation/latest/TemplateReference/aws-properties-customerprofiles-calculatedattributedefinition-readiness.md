---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-calculatedattributedefinition-readiness.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::CalculatedAttributeDefinition Readiness
<a name="aws-properties-customerprofiles-calculatedattributedefinition-readiness"></a>

Information indicating if the Calculated Attribute is ready for use by confirming all historical data has been processed and reflected.

## Syntax
<a name="aws-properties-customerprofiles-calculatedattributedefinition-readiness-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-calculatedattributedefinition-readiness-syntax.json"></a>

```
{
  "[Message](#cfn-customerprofiles-calculatedattributedefinition-readiness-message)" : {{String}},
  "[ProgressPercentage](#cfn-customerprofiles-calculatedattributedefinition-readiness-progresspercentage)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-customerprofiles-calculatedattributedefinition-readiness-syntax.yaml"></a>

```
  [Message](#cfn-customerprofiles-calculatedattributedefinition-readiness-message): {{String}}
  [ProgressPercentage](#cfn-customerprofiles-calculatedattributedefinition-readiness-progresspercentage): {{Integer}}
```

## Properties
<a name="aws-properties-customerprofiles-calculatedattributedefinition-readiness-properties"></a>

`Message`  <a name="cfn-customerprofiles-calculatedattributedefinition-readiness-message"></a>
Any customer messaging.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProgressPercentage`  <a name="cfn-customerprofiles-calculatedattributedefinition-readiness-progresspercentage"></a>
Approximately how far the Calculated Attribute creation is from completion.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
