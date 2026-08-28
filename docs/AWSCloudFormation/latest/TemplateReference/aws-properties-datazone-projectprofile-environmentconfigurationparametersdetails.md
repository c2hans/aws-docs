---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-projectprofile-environmentconfigurationparametersdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::ProjectProfile EnvironmentConfigurationParametersDetails
<a name="aws-properties-datazone-projectprofile-environmentconfigurationparametersdetails"></a>

The details of the environment configuration parameter.

## Syntax
<a name="aws-properties-datazone-projectprofile-environmentconfigurationparametersdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-projectprofile-environmentconfigurationparametersdetails-syntax.json"></a>

```
{
  "[ParameterOverrides](#cfn-datazone-projectprofile-environmentconfigurationparametersdetails-parameteroverrides)" : {{[ EnvironmentConfigurationParameter, ... ]}},
  "[ResolvedParameters](#cfn-datazone-projectprofile-environmentconfigurationparametersdetails-resolvedparameters)" : {{[ EnvironmentConfigurationParameter, ... ]}},
  "[SsmPath](#cfn-datazone-projectprofile-environmentconfigurationparametersdetails-ssmpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-projectprofile-environmentconfigurationparametersdetails-syntax.yaml"></a>

```
  [ParameterOverrides](#cfn-datazone-projectprofile-environmentconfigurationparametersdetails-parameteroverrides): {{
    - EnvironmentConfigurationParameter}}
  [ResolvedParameters](#cfn-datazone-projectprofile-environmentconfigurationparametersdetails-resolvedparameters): {{
    - EnvironmentConfigurationParameter}}
  [SsmPath](#cfn-datazone-projectprofile-environmentconfigurationparametersdetails-ssmpath): {{String}}
```

## Properties
<a name="aws-properties-datazone-projectprofile-environmentconfigurationparametersdetails-properties"></a>

`ParameterOverrides`  <a name="cfn-datazone-projectprofile-environmentconfigurationparametersdetails-parameteroverrides"></a>
The parameter overrides.
*Required*: No
*Type*: Array of [EnvironmentConfigurationParameter](aws-properties-datazone-projectprofile-environmentconfigurationparameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResolvedParameters`  <a name="cfn-datazone-projectprofile-environmentconfigurationparametersdetails-resolvedparameters"></a>
The resolved environment configuration parameters.
*Required*: No
*Type*: Array of [EnvironmentConfigurationParameter](aws-properties-datazone-projectprofile-environmentconfigurationparameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SsmPath`  <a name="cfn-datazone-projectprofile-environmentconfigurationparametersdetails-ssmpath"></a>
Ssm path environment configuration parameters.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
