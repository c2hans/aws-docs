---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-usageprofile-configurationobject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::UsageProfile ConfigurationObject
<a name="aws-properties-glue-usageprofile-configurationobject"></a>

Specifies the values that an admin sets for each job or session parameter configured in a AWS Glue usage profile.

## Syntax
<a name="aws-properties-glue-usageprofile-configurationobject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-usageprofile-configurationobject-syntax.json"></a>

```
{
  "[AllowedValues](#cfn-glue-usageprofile-configurationobject-allowedvalues)" : {{[ String, ... ]}},
  "[DefaultValue](#cfn-glue-usageprofile-configurationobject-defaultvalue)" : {{String}},
  "[MaxValue](#cfn-glue-usageprofile-configurationobject-maxvalue)" : {{String}},
  "[MinValue](#cfn-glue-usageprofile-configurationobject-minvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-usageprofile-configurationobject-syntax.yaml"></a>

```
  [AllowedValues](#cfn-glue-usageprofile-configurationobject-allowedvalues): {{
    - String}}
  [DefaultValue](#cfn-glue-usageprofile-configurationobject-defaultvalue): {{String}}
  [MaxValue](#cfn-glue-usageprofile-configurationobject-maxvalue): {{String}}
  [MinValue](#cfn-glue-usageprofile-configurationobject-minvalue): {{String}}
```

## Properties
<a name="aws-properties-glue-usageprofile-configurationobject-properties"></a>

`AllowedValues`  <a name="cfn-glue-usageprofile-configurationobject-allowedvalues"></a>
A list of allowed values for the parameter.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultValue`  <a name="cfn-glue-usageprofile-configurationobject-defaultvalue"></a>
A default value for the parameter.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_.-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxValue`  <a name="cfn-glue-usageprofile-configurationobject-maxvalue"></a>
A maximum allowed value for the parameter.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_.-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinValue`  <a name="cfn-glue-usageprofile-configurationobject-minvalue"></a>
A minimum allowed value for the parameter.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_.-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
