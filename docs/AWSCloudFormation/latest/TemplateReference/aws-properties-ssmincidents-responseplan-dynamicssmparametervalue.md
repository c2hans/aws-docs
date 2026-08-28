---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmincidents-responseplan-dynamicssmparametervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ResponsePlan DynamicSsmParameterValue
<a name="aws-properties-ssmincidents-responseplan-dynamicssmparametervalue"></a>

The dynamic parameter value.

## Syntax
<a name="aws-properties-ssmincidents-responseplan-dynamicssmparametervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmincidents-responseplan-dynamicssmparametervalue-syntax.json"></a>

```
{
  "[Variable](#cfn-ssmincidents-responseplan-dynamicssmparametervalue-variable)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmincidents-responseplan-dynamicssmparametervalue-syntax.yaml"></a>

```
  [Variable](#cfn-ssmincidents-responseplan-dynamicssmparametervalue-variable): {{String}}
```

## Properties
<a name="aws-properties-ssmincidents-responseplan-dynamicssmparametervalue-properties"></a>

`Variable`  <a name="cfn-ssmincidents-responseplan-dynamicssmparametervalue-variable"></a>
Variable dynamic parameters. A parameter value is determined when an incident is created.
*Required*: No
*Type*: String
*Allowed values*: `INCIDENT_RECORD_ARN | INVOLVED_RESOURCES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
