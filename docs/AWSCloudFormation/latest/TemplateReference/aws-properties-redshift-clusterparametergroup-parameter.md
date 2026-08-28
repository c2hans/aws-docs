---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-clusterparametergroup-parameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::ClusterParameterGroup Parameter
<a name="aws-properties-redshift-clusterparametergroup-parameter"></a>

Describes a parameter in a cluster parameter group.

## Syntax
<a name="aws-properties-redshift-clusterparametergroup-parameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-clusterparametergroup-parameter-syntax.json"></a>

```
{
  "[ParameterName](#cfn-redshift-clusterparametergroup-parameter-parametername)" : {{String}},
  "[ParameterValue](#cfn-redshift-clusterparametergroup-parameter-parametervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-clusterparametergroup-parameter-syntax.yaml"></a>

```
  [ParameterName](#cfn-redshift-clusterparametergroup-parameter-parametername): {{String}}
  [ParameterValue](#cfn-redshift-clusterparametergroup-parameter-parametervalue): {{String}}
```

## Properties
<a name="aws-properties-redshift-clusterparametergroup-parameter-properties"></a>

`ParameterName`  <a name="cfn-redshift-clusterparametergroup-parameter-parametername"></a>
The name of the parameter.
*Required*: Yes
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterValue`  <a name="cfn-redshift-clusterparametergroup-parameter-parametervalue"></a>
The value of the parameter. If `ParameterName` is `wlm_json_configuration`, then the maximum size of `ParameterValue` is 8000 characters.
*Required*: Yes
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
