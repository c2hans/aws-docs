---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-database-relationaldatabaseparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Database RelationalDatabaseParameter
<a name="aws-properties-lightsail-database-relationaldatabaseparameter"></a>

`RelationalDatabaseParameter` is a property of the [AWS::Lightsail::Database](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html) resource. It describes parameters for the database.

## Syntax
<a name="aws-properties-lightsail-database-relationaldatabaseparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-database-relationaldatabaseparameter-syntax.json"></a>

```
{
  "[AllowedValues](#cfn-lightsail-database-relationaldatabaseparameter-allowedvalues)" : {{String}},
  "[ApplyMethod](#cfn-lightsail-database-relationaldatabaseparameter-applymethod)" : {{String}},
  "[ApplyType](#cfn-lightsail-database-relationaldatabaseparameter-applytype)" : {{String}},
  "[DataType](#cfn-lightsail-database-relationaldatabaseparameter-datatype)" : {{String}},
  "[Description](#cfn-lightsail-database-relationaldatabaseparameter-description)" : {{String}},
  "[IsModifiable](#cfn-lightsail-database-relationaldatabaseparameter-ismodifiable)" : {{Boolean}},
  "[ParameterName](#cfn-lightsail-database-relationaldatabaseparameter-parametername)" : {{String}},
  "[ParameterValue](#cfn-lightsail-database-relationaldatabaseparameter-parametervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-database-relationaldatabaseparameter-syntax.yaml"></a>

```
  [AllowedValues](#cfn-lightsail-database-relationaldatabaseparameter-allowedvalues): {{String}}
  [ApplyMethod](#cfn-lightsail-database-relationaldatabaseparameter-applymethod): {{String}}
  [ApplyType](#cfn-lightsail-database-relationaldatabaseparameter-applytype): {{String}}
  [DataType](#cfn-lightsail-database-relationaldatabaseparameter-datatype): {{String}}
  [Description](#cfn-lightsail-database-relationaldatabaseparameter-description): {{String}}
  [IsModifiable](#cfn-lightsail-database-relationaldatabaseparameter-ismodifiable): {{Boolean}}
  [ParameterName](#cfn-lightsail-database-relationaldatabaseparameter-parametername): {{String}}
  [ParameterValue](#cfn-lightsail-database-relationaldatabaseparameter-parametervalue): {{String}}
```

## Properties
<a name="aws-properties-lightsail-database-relationaldatabaseparameter-properties"></a>

`AllowedValues`  <a name="cfn-lightsail-database-relationaldatabaseparameter-allowedvalues"></a>
The valid range of values for the parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplyMethod`  <a name="cfn-lightsail-database-relationaldatabaseparameter-applymethod"></a>
Indicates when parameter updates are applied.
Can be `immediate` or `pending-reboot`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplyType`  <a name="cfn-lightsail-database-relationaldatabaseparameter-applytype"></a>
Specifies the engine-specific parameter type.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataType`  <a name="cfn-lightsail-database-relationaldatabaseparameter-datatype"></a>
The valid data type of the parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-lightsail-database-relationaldatabaseparameter-description"></a>
A description of the parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsModifiable`  <a name="cfn-lightsail-database-relationaldatabaseparameter-ismodifiable"></a>
A Boolean value indicating whether the parameter can be modified.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterName`  <a name="cfn-lightsail-database-relationaldatabaseparameter-parametername"></a>
The name of the parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterValue`  <a name="cfn-lightsail-database-relationaldatabaseparameter-parametervalue"></a>
The value for the parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
