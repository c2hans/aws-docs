---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-experimentdefinition-treatment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::ExperimentDefinition Treatment
<a name="aws-properties-appconfig-experimentdefinition-treatment"></a>

Describes a treatment in an experiment, including its traffic allocation weight and feature flag value.

## Syntax
<a name="aws-properties-appconfig-experimentdefinition-treatment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appconfig-experimentdefinition-treatment-syntax.json"></a>

```
{
  "[AttributeValues](#cfn-appconfig-experimentdefinition-treatment-attributevalues)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Description](#cfn-appconfig-experimentdefinition-treatment-description)" : {{String}},
  "[Enabled](#cfn-appconfig-experimentdefinition-treatment-enabled)" : {{Boolean}},
  "[Key](#cfn-appconfig-experimentdefinition-treatment-key)" : {{String}},
  "[Weight](#cfn-appconfig-experimentdefinition-treatment-weight)" : {{Number}}
}
```

### YAML
<a name="aws-properties-appconfig-experimentdefinition-treatment-syntax.yaml"></a>

```
  [AttributeValues](#cfn-appconfig-experimentdefinition-treatment-attributevalues): {{
    {{Key}}: {{Value}}}}
  [Description](#cfn-appconfig-experimentdefinition-treatment-description): {{String}}
  [Enabled](#cfn-appconfig-experimentdefinition-treatment-enabled): {{Boolean}}
  [Key](#cfn-appconfig-experimentdefinition-treatment-key): {{String}}
  [Weight](#cfn-appconfig-experimentdefinition-treatment-weight): {{Number}}
```

## Properties
<a name="aws-properties-appconfig-experimentdefinition-treatment-properties"></a>

`AttributeValues`  <a name="cfn-appconfig-experimentdefinition-treatment-attributevalues"></a>
Property description not available.
*Required*: No
*Type*: Object of [AttributeValue](aws-properties-appconfig-experimentdefinition-attributevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-appconfig-experimentdefinition-treatment-description"></a>
A description of the treatment.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-appconfig-experimentdefinition-treatment-enabled"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-appconfig-experimentdefinition-treatment-key"></a>
The unique key that identifies this treatment.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]{1,8}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-appconfig-experimentdefinition-treatment-weight"></a>
The traffic allocation weight for this treatment.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
