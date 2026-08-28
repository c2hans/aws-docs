---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-dimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective Dimension
<a name="aws-properties-applicationsignals-servicelevelobjective-dimension"></a>

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-dimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-dimension-syntax.json"></a>

```
{
  "[Name](#cfn-applicationsignals-servicelevelobjective-dimension-name)" : {{String}},
  "[Value](#cfn-applicationsignals-servicelevelobjective-dimension-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-dimension-syntax.yaml"></a>

```
  [Name](#cfn-applicationsignals-servicelevelobjective-dimension-name): {{String}}
  [Value](#cfn-applicationsignals-servicelevelobjective-dimension-value): {{String}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-dimension-properties"></a>

`Name`  <a name="cfn-applicationsignals-servicelevelobjective-dimension-name"></a>
The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:`). ASCII control characters are not supported as part of dimension names.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-applicationsignals-servicelevelobjective-dimension-value"></a>
The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
