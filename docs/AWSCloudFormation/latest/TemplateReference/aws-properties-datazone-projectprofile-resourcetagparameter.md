---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-projectprofile-resourcetagparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::ProjectProfile ResourceTagParameter
<a name="aws-properties-datazone-projectprofile-resourcetagparameter"></a>

The resource tag parameter of the project profile.

## Syntax
<a name="aws-properties-datazone-projectprofile-resourcetagparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-projectprofile-resourcetagparameter-syntax.json"></a>

```
{
  "[IsValueEditable](#cfn-datazone-projectprofile-resourcetagparameter-isvalueeditable)" : {{Boolean}},
  "[Key](#cfn-datazone-projectprofile-resourcetagparameter-key)" : {{String}},
  "[Value](#cfn-datazone-projectprofile-resourcetagparameter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-projectprofile-resourcetagparameter-syntax.yaml"></a>

```
  [IsValueEditable](#cfn-datazone-projectprofile-resourcetagparameter-isvalueeditable): {{Boolean}}
  [Key](#cfn-datazone-projectprofile-resourcetagparameter-key): {{String}}
  [Value](#cfn-datazone-projectprofile-resourcetagparameter-value): {{String}}
```

## Properties
<a name="aws-properties-datazone-projectprofile-resourcetagparameter-properties"></a>

`IsValueEditable`  <a name="cfn-datazone-projectprofile-resourcetagparameter-isvalueeditable"></a>
Specifies whether the value of the resource tag parameter of the project profile is editable at the project level.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-datazone-projectprofile-resourcetagparameter-key"></a>
The key of the resource tag parameter of the project profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w \.:/=+@-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-datazone-projectprofile-resourcetagparameter-value"></a>
The value of the resource tag parameter key of the project profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w \.:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
