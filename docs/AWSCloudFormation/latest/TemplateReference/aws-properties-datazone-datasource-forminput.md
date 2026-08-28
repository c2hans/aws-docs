---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-forminput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource FormInput
<a name="aws-properties-datazone-datasource-forminput"></a>

The details of a metadata form.

## Syntax
<a name="aws-properties-datazone-datasource-forminput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-forminput-syntax.json"></a>

```
{
  "[Content](#cfn-datazone-datasource-forminput-content)" : {{String}},
  "[FormName](#cfn-datazone-datasource-forminput-formname)" : {{String}},
  "[TypeIdentifier](#cfn-datazone-datasource-forminput-typeidentifier)" : {{String}},
  "[TypeRevision](#cfn-datazone-datasource-forminput-typerevision)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-forminput-syntax.yaml"></a>

```
  [Content](#cfn-datazone-datasource-forminput-content): {{String}}
  [FormName](#cfn-datazone-datasource-forminput-formname): {{String}}
  [TypeIdentifier](#cfn-datazone-datasource-forminput-typeidentifier): {{String}}
  [TypeRevision](#cfn-datazone-datasource-forminput-typerevision): {{String}}
```

## Properties
<a name="aws-properties-datazone-datasource-forminput-properties"></a>

`Content`  <a name="cfn-datazone-datasource-forminput-content"></a>
The content of the metadata form.
*Required*: No
*Type*: String
*Maximum*: `75000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FormName`  <a name="cfn-datazone-datasource-forminput-formname"></a>
The name of the metadata form.
*Required*: Yes
*Type*: String
*Pattern*: `^(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TypeIdentifier`  <a name="cfn-datazone-datasource-forminput-typeidentifier"></a>
The ID of the metadata form type.
*Required*: No
*Type*: String
*Pattern*: `^(?!\.)[\w\.]*\w$`
*Minimum*: `1`
*Maximum*: `385`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TypeRevision`  <a name="cfn-datazone-datasource-forminput-typerevision"></a>
The revision of the metadata form type.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
