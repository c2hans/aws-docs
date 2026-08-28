---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-sagemakerrunconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource SageMakerRunConfigurationInput
<a name="aws-properties-datazone-datasource-sagemakerrunconfigurationinput"></a>

The Amazon SageMaker run configuration.

## Syntax
<a name="aws-properties-datazone-datasource-sagemakerrunconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-sagemakerrunconfigurationinput-syntax.json"></a>

```
{
  "[TrackingAssets](#cfn-datazone-datasource-sagemakerrunconfigurationinput-trackingassets)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-sagemakerrunconfigurationinput-syntax.yaml"></a>

```
  [TrackingAssets](#cfn-datazone-datasource-sagemakerrunconfigurationinput-trackingassets): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-datazone-datasource-sagemakerrunconfigurationinput-properties"></a>

`TrackingAssets`  <a name="cfn-datazone-datasource-sagemakerrunconfigurationinput-trackingassets"></a>
The tracking assets of the Amazon SageMaker run.
*Required*: Yes
*Type*: Object of Array
*Pattern*: `^.{1,64}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
