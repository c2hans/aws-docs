---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-dataprotectionsettings-redactionplaceholder.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::DataProtectionSettings RedactionPlaceHolder
<a name="aws-properties-workspacesweb-dataprotectionsettings-redactionplaceholder"></a>

The redaction placeholder that will replace the redacted text in session.

## Syntax
<a name="aws-properties-workspacesweb-dataprotectionsettings-redactionplaceholder-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-dataprotectionsettings-redactionplaceholder-syntax.json"></a>

```
{
  "[RedactionPlaceHolderText](#cfn-workspacesweb-dataprotectionsettings-redactionplaceholder-redactionplaceholdertext)" : {{String}},
  "[RedactionPlaceHolderType](#cfn-workspacesweb-dataprotectionsettings-redactionplaceholder-redactionplaceholdertype)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspacesweb-dataprotectionsettings-redactionplaceholder-syntax.yaml"></a>

```
  [RedactionPlaceHolderText](#cfn-workspacesweb-dataprotectionsettings-redactionplaceholder-redactionplaceholdertext): {{String}}
  [RedactionPlaceHolderType](#cfn-workspacesweb-dataprotectionsettings-redactionplaceholder-redactionplaceholdertype): {{String}}
```

## Properties
<a name="aws-properties-workspacesweb-dataprotectionsettings-redactionplaceholder-properties"></a>

`RedactionPlaceHolderText`  <a name="cfn-workspacesweb-dataprotectionsettings-redactionplaceholder-redactionplaceholdertext"></a>
The redaction placeholder text that will replace the redacted text in session for the custom text redaction placeholder type.
*Required*: No
*Type*: String
*Pattern*: `^[*_\-\d\w]+$`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedactionPlaceHolderType`  <a name="cfn-workspacesweb-dataprotectionsettings-redactionplaceholder-redactionplaceholdertype"></a>
The redaction placeholder type that will replace the redacted text in session.
*Required*: Yes
*Type*: String
*Allowed values*: `CustomText`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
