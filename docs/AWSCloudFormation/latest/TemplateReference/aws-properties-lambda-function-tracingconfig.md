---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-tracingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function TracingConfig
<a name="aws-properties-lambda-function-tracingconfig"></a>

The function's [AWS X-Ray](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html) tracing configuration. To sample and record incoming requests, set `Mode` to `Active`.

## Syntax
<a name="aws-properties-lambda-function-tracingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-tracingconfig-syntax.json"></a>

```
{
  "[Mode](#cfn-lambda-function-tracingconfig-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-function-tracingconfig-syntax.yaml"></a>

```
  [Mode](#cfn-lambda-function-tracingconfig-mode): {{String}}
```

## Properties
<a name="aws-properties-lambda-function-tracingconfig-properties"></a>

`Mode`  <a name="cfn-lambda-function-tracingconfig-mode"></a>
The tracing mode.
*Required*: No
*Type*: String
*Allowed values*: `Active | PassThrough`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-lambda-function-tracingconfig--examples"></a>

### Tracing Configuration
<a name="aws-properties-lambda-function-tracingconfig--examples--Tracing_Configuration"></a>

Enable active tracing on a function.

#### YAML
<a name="aws-properties-lambda-function-tracingconfig--examples--Tracing_Configuration--yaml"></a>

```
      TracingConfig:
        Mode: Active
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
