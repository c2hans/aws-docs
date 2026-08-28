---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datapipeline-pipeline-parametervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataPipeline::Pipeline ParameterValue
<a name="aws-properties-datapipeline-pipeline-parametervalue"></a>

A value or list of parameter values.

## Syntax
<a name="aws-properties-datapipeline-pipeline-parametervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datapipeline-pipeline-parametervalue-syntax.json"></a>

```
{
  "[Id](#cfn-datapipeline-pipeline-parametervalue-id)" : {{String}},
  "[StringValue](#cfn-datapipeline-pipeline-parametervalue-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-datapipeline-pipeline-parametervalue-syntax.yaml"></a>

```
  [Id](#cfn-datapipeline-pipeline-parametervalue-id): {{String}}
  [StringValue](#cfn-datapipeline-pipeline-parametervalue-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-datapipeline-pipeline-parametervalue-properties"></a>

`Id`  <a name="cfn-datapipeline-pipeline-parametervalue-id"></a>
The ID of the parameter value.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-datapipeline-pipeline-parametervalue-stringvalue"></a>
The field value, expressed as a String.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
