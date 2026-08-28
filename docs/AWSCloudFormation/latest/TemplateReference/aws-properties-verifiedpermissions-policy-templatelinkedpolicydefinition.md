---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::Policy TemplateLinkedPolicyDefinition
<a name="aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition"></a>

A structure that describes a policy created by instantiating a policy template.

**Note**
You can't directly update a template-linked policy. You must update the associated policy template instead.

## Syntax
<a name="aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition-syntax.json"></a>

```
{
  "[PolicyTemplateId](#cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-policytemplateid)" : {{String}},
  "[Principal](#cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-principal)" : {{EntityIdentifier}},
  "[Resource](#cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-resource)" : {{EntityIdentifier}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition-syntax.yaml"></a>

```
  [PolicyTemplateId](#cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-policytemplateid): {{String}}
  [Principal](#cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-principal): {{
    EntityIdentifier}}
  [Resource](#cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-resource): {{
    EntityIdentifier}}
```

## Properties
<a name="aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition-properties"></a>

`PolicyTemplateId`  <a name="cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-policytemplateid"></a>
The unique identifier of the policy template used to create this policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: Updates are not supported.

`Principal`  <a name="cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-principal"></a>
The principal associated with this template-linked policy. Verified Permissions substitutes this principal for the `?principal` placeholder in the policy template when it evaluates an authorization request.
*Required*: No
*Type*: [EntityIdentifier](aws-properties-verifiedpermissions-policy-entityidentifier.md)
*Update requires*: Updates are not supported.

`Resource`  <a name="cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-resource"></a>
The resource associated with this template-linked policy. Verified Permissions substitutes this resource for the `?resource` placeholder in the policy template when it evaluates an authorization request.
*Required*: No
*Type*: [EntityIdentifier](aws-properties-verifiedpermissions-policy-entityidentifier.md)
*Update requires*: Updates are not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
