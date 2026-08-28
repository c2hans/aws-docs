---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-session-sessioncommand.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Session SessionCommand
<a name="aws-properties-glue-session-sessioncommand"></a>

The `SessionCommand` that runs the job.

## Syntax
<a name="aws-properties-glue-session-sessioncommand-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-session-sessioncommand-syntax.json"></a>

```
{
  "[Name](#cfn-glue-session-sessioncommand-name)" : {{String}},
  "[PythonVersion](#cfn-glue-session-sessioncommand-pythonversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-session-sessioncommand-syntax.yaml"></a>

```
  [Name](#cfn-glue-session-sessioncommand-name): {{String}}
  [PythonVersion](#cfn-glue-session-sessioncommand-pythonversion): {{String}}
```

## Properties
<a name="aws-properties-glue-session-sessioncommand-properties"></a>

`Name`  <a name="cfn-glue-session-sessioncommand-name"></a>
Specifies the name of the SessionCommand. Can be 'glueetl' or 'gluestreaming'.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PythonVersion`  <a name="cfn-glue-session-sessioncommand-pythonversion"></a>
Specifies the Python version. The Python version indicates the version supported for jobs of type Spark.
*Required*: No
*Type*: String
*Pattern*: `^([2-3]|3[.]9)$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
