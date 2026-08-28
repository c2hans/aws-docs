---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-policy-staticpolicydefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::Policy StaticPolicyDefinition
<a name="aws-properties-verifiedpermissions-policy-staticpolicydefinition"></a>

A structure that defines a static policy.

## Syntax
<a name="aws-properties-verifiedpermissions-policy-staticpolicydefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-policy-staticpolicydefinition-syntax.json"></a>

```
{
  "[Description](#cfn-verifiedpermissions-policy-staticpolicydefinition-description)" : {{String}},
  "[Statement](#cfn-verifiedpermissions-policy-staticpolicydefinition-statement)" : {{String}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-policy-staticpolicydefinition-syntax.yaml"></a>

```
  [Description](#cfn-verifiedpermissions-policy-staticpolicydefinition-description): {{String}}
  [Statement](#cfn-verifiedpermissions-policy-staticpolicydefinition-statement): {{String}}
```

## Properties
<a name="aws-properties-verifiedpermissions-policy-staticpolicydefinition-properties"></a>

`Description`  <a name="cfn-verifiedpermissions-policy-staticpolicydefinition-description"></a>
The description of the static policy.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Statement`  <a name="cfn-verifiedpermissions-policy-staticpolicydefinition-statement"></a>
The policy content of the static policy, written in the Cedar policy language.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
