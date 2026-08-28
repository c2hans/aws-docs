---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-x12codelistvalidationrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer X12CodeListValidationRule
<a name="aws-properties-b2bi-transformer-x12codelistvalidationrule"></a>

Code list validation rule configuration.

## Syntax
<a name="aws-properties-b2bi-transformer-x12codelistvalidationrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-x12codelistvalidationrule-syntax.json"></a>

```
{
  "[CodesToAdd](#cfn-b2bi-transformer-x12codelistvalidationrule-codestoadd)" : {{[ String, ... ]}},
  "[CodesToRemove](#cfn-b2bi-transformer-x12codelistvalidationrule-codestoremove)" : {{[ String, ... ]}},
  "[ElementId](#cfn-b2bi-transformer-x12codelistvalidationrule-elementid)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-x12codelistvalidationrule-syntax.yaml"></a>

```
  [CodesToAdd](#cfn-b2bi-transformer-x12codelistvalidationrule-codestoadd): {{
    - String}}
  [CodesToRemove](#cfn-b2bi-transformer-x12codelistvalidationrule-codestoremove): {{
    - String}}
  [ElementId](#cfn-b2bi-transformer-x12codelistvalidationrule-elementid): {{String}}
```

## Properties
<a name="aws-properties-b2bi-transformer-x12codelistvalidationrule-properties"></a>

`CodesToAdd`  <a name="cfn-b2bi-transformer-x12codelistvalidationrule-codestoadd"></a>
Specifies a list of code values to add to the element's allowed values. These codes will be considered valid for the specified element in addition to the standard codes defined by the X12 specification.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodesToRemove`  <a name="cfn-b2bi-transformer-x12codelistvalidationrule-codestoremove"></a>
Specifies a list of code values to remove from the element's allowed values. These codes will be considered invalid for the specified element, even if they are part of the standard codes defined by the X12 specification.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ElementId`  <a name="cfn-b2bi-transformer-x12codelistvalidationrule-elementid"></a>
Specifies the four-digit element ID to which the code list modifications apply. This identifies which X12 element will have its allowed code values modified.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{4}$`
*Minimum*: `4`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
