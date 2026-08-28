---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-environment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function Environment
<a name="aws-properties-lambda-function-environment"></a>

A function's environment variable settings. You can use environment variables to adjust your function's behavior without updating code. An environment variable is a pair of strings that are stored in a function's version-specific configuration.

## Syntax
<a name="aws-properties-lambda-function-environment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-environment-syntax.json"></a>

```
{
  "[Variables](#cfn-lambda-function-environment-variables)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-lambda-function-environment-syntax.yaml"></a>

```
  [Variables](#cfn-lambda-function-environment-variables): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-lambda-function-environment-properties"></a>

`Variables`  <a name="cfn-lambda-function-environment-variables"></a>
Environment variable key-value pairs. For more information, see [Using Lambda environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html).
If the value of the environment variable is a time or a duration, enclose the value in quotes.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z][a-zA-Z0-9_]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-lambda-function-environment--examples"></a>

### Environment Variables
<a name="aws-properties-lambda-function-environment--examples--Environment_Variables"></a>

Add environment variables to a function. Each variable is a key-value pair. This example specifies values for a `databaseName` and a `databaseUser`.

#### YAML
<a name="aws-properties-lambda-function-environment--examples--Environment_Variables--yaml"></a>

```
      Environment:
        Variables:
          databaseName: lambdadb
          databaseUser: admin
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
