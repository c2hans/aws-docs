---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-document-documentrequires.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::Document DocumentRequires
<a name="aws-properties-ssm-document-documentrequires"></a>

An SSM document required by the current document.

## Syntax
<a name="aws-properties-ssm-document-documentrequires-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-document-documentrequires-syntax.json"></a>

```
{
  "[Name](#cfn-ssm-document-documentrequires-name)" : {{String}},
  "[Version](#cfn-ssm-document-documentrequires-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssm-document-documentrequires-syntax.yaml"></a>

```
  [Name](#cfn-ssm-document-documentrequires-name): {{String}}
  [Version](#cfn-ssm-document-documentrequires-version): {{String}}
```

## Properties
<a name="aws-properties-ssm-document-documentrequires-properties"></a>

`Name`  <a name="cfn-ssm-document-documentrequires-name"></a>
The name of the required SSM document. The name can be an Amazon Resource Name (ARN).
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-.:/]{3,200}$`
*Maximum*: `200`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Version`  <a name="cfn-ssm-document-documentrequires-version"></a>
The document version required by the current document.
*Required*: No
*Type*: String
*Pattern*: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
*Maximum*: `8`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
