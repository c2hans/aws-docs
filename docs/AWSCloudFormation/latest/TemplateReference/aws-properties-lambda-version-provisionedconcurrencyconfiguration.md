---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-version-provisionedconcurrencyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Version ProvisionedConcurrencyConfiguration
<a name="aws-properties-lambda-version-provisionedconcurrencyconfiguration"></a>

A [provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) configuration for a function's version.

## Syntax
<a name="aws-properties-lambda-version-provisionedconcurrencyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-version-provisionedconcurrencyconfiguration-syntax.json"></a>

```
{
  "[ProvisionedConcurrentExecutions](#cfn-lambda-version-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-version-provisionedconcurrencyconfiguration-syntax.yaml"></a>

```
  [ProvisionedConcurrentExecutions](#cfn-lambda-version-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-version-provisionedconcurrencyconfiguration-properties"></a>

`ProvisionedConcurrentExecutions`  <a name="cfn-lambda-version-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions"></a>
The amount of provisioned concurrency to allocate for the version.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Examples
<a name="aws-properties-lambda-version-provisionedconcurrencyconfiguration--examples"></a>

### Provisioned Concurrency Configuration
<a name="aws-properties-lambda-version-provisionedconcurrencyconfiguration--examples--Provisioned_Concurrency_Configuration"></a>

Allocate 20 provisioned concurrency for a version.

#### YAML
<a name="aws-properties-lambda-version-provisionedconcurrencyconfiguration--examples--Provisioned_Concurrency_Configuration--yaml"></a>

```
      ProvisionedConcurrencyConfig:
        ProvisionedConcurrentExecutions: 20
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
