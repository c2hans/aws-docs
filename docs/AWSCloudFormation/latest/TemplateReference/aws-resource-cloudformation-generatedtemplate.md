---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-generatedtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::GeneratedTemplate
<a name="aws-resource-cloudformation-generatedtemplate"></a>

Creates a template from existing resources that are not already managed with CloudFormation. You can check the status of the template generation using the `DescribeGeneratedTemplate` API action.

## Syntax
<a name="aws-resource-cloudformation-generatedtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-generatedtemplate-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::GeneratedTemplate",
  "Properties" : {
      "[GeneratedTemplateName](#cfn-cloudformation-generatedtemplate-generatedtemplatename)" : {{String}},
      "[TemplateConfiguration](#cfn-cloudformation-generatedtemplate-templateconfiguration)" : {{TemplateConfiguration}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-generatedtemplate-syntax.yaml"></a>

```
Type: AWS::CloudFormation::GeneratedTemplate
Properties:
  [GeneratedTemplateName](#cfn-cloudformation-generatedtemplate-generatedtemplatename): {{String}}
  [TemplateConfiguration](#cfn-cloudformation-generatedtemplate-templateconfiguration): {{
    TemplateConfiguration}}
```

## Properties
<a name="aws-resource-cloudformation-generatedtemplate-properties"></a>

`GeneratedTemplateName`  <a name="cfn-cloudformation-generatedtemplate-generatedtemplatename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateConfiguration`  <a name="cfn-cloudformation-generatedtemplate-templateconfiguration"></a>
The configuration details of a generated template.
*Required*: No
*Type*: [TemplateConfiguration](aws-properties-cloudformation-generatedtemplate-templateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudformation-generatedtemplate-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-generatedtemplate-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudformation-generatedtemplate-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudformation-generatedtemplate-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Property description not available.

`GeneratedTemplateId`  <a name="GeneratedTemplateId-fn::getatt"></a>
Property description not available.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`TotalWarnings`  <a name="TotalWarnings-fn::getatt"></a>
Contains any warnings returned by the `GetTemplateSummary` API action.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
