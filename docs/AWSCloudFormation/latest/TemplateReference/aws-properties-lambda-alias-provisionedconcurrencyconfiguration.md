---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-alias-provisionedconcurrencyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Alias ProvisionedConcurrencyConfiguration
<a name="aws-properties-lambda-alias-provisionedconcurrencyconfiguration"></a>

A provisioned concurrency configuration for a function's alias.

## Syntax
<a name="aws-properties-lambda-alias-provisionedconcurrencyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-alias-provisionedconcurrencyconfiguration-syntax.json"></a>

```
{
  "[ProvisionedConcurrentExecutions](#cfn-lambda-alias-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-alias-provisionedconcurrencyconfiguration-syntax.yaml"></a>

```
  [ProvisionedConcurrentExecutions](#cfn-lambda-alias-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-alias-provisionedconcurrencyconfiguration-properties"></a>

`ProvisionedConcurrentExecutions`  <a name="cfn-lambda-alias-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions"></a>
The amount of provisioned concurrency to allocate for the alias.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-lambda-alias-provisionedconcurrencyconfiguration--examples"></a>

### Provisioned Concurrency
<a name="aws-properties-lambda-alias-provisionedconcurrencyconfiguration--examples--Provisioned_Concurrency"></a>

An alias with 20 provisioned concurrency.

#### YAML
<a name="aws-properties-lambda-alias-provisionedconcurrencyconfiguration--examples--Provisioned_Concurrency--yaml"></a>

```
  alias:
    Type: AWS::Lambda::Alias
    Properties:
      FunctionName: !Ref function
      FunctionVersion: !GetAtt newVersion.Version
      Name: BLUE
      ProvisionedConcurrencyConfig:
        ProvisionedConcurrentExecutions: 20
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
