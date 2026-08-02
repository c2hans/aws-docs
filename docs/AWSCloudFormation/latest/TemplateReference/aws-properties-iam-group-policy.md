---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iam-group-policy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IAM::Group Policy
<a name="aws-properties-iam-group-policy"></a>

Contains information about an attached policy.

An attached policy is a managed policy that has been attached to a user, group, or role.

For more information about managed policies, see [Managed Policies and Inline Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.

## Syntax
<a name="aws-properties-iam-group-policy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iam-group-policy-syntax.json"></a>

```
{
  "[PolicyDocument](#cfn-iam-group-policy-policydocument)" : {{Json}},
  "[PolicyName](#cfn-iam-group-policy-policyname)" : {{String}}
}
```

### YAML
<a name="aws-properties-iam-group-policy-syntax.yaml"></a>

```
  [PolicyDocument](#cfn-iam-group-policy-policydocument): {{Json}}
  [PolicyName](#cfn-iam-group-policy-policyname): {{String}}
```

## Properties
<a name="aws-properties-iam-group-policy-properties"></a>

`PolicyDocument`  <a name="cfn-iam-group-policy-policydocument"></a>
The policy document.
*Required*: Yes
*Type*: Json
*Pattern*: `[\u0009\u000A\u000D\u0020-\u00FF]+`
*Minimum*: `1`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyName`  <a name="cfn-iam-group-policy-policyname"></a>
The friendly name (not ARN) identifying the policy.
*Required*: Yes
*Type*: String
*Pattern*: `[\w+=,.@-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-iam-group-policy--seealso"></a>
+ [PolicyDetail](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PolicyDetail.html) in the *AWS Identity and Access Management API Reference*
