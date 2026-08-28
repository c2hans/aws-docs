---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-identitypoolroleattachment-mappingrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::IdentityPoolRoleAttachment MappingRule
<a name="aws-properties-cognito-identitypoolroleattachment-mappingrule"></a>

Defines how to map a claim to a role ARN.

## Syntax
<a name="aws-properties-cognito-identitypoolroleattachment-mappingrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-identitypoolroleattachment-mappingrule-syntax.json"></a>

```
{
  "[Claim](#cfn-cognito-identitypoolroleattachment-mappingrule-claim)" : {{String}},
  "[MatchType](#cfn-cognito-identitypoolroleattachment-mappingrule-matchtype)" : {{String}},
  "[RoleARN](#cfn-cognito-identitypoolroleattachment-mappingrule-rolearn)" : {{String}},
  "[Value](#cfn-cognito-identitypoolroleattachment-mappingrule-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-identitypoolroleattachment-mappingrule-syntax.yaml"></a>

```
  [Claim](#cfn-cognito-identitypoolroleattachment-mappingrule-claim): {{String}}
  [MatchType](#cfn-cognito-identitypoolroleattachment-mappingrule-matchtype): {{String}}
  [RoleARN](#cfn-cognito-identitypoolroleattachment-mappingrule-rolearn): {{String}}
  [Value](#cfn-cognito-identitypoolroleattachment-mappingrule-value): {{String}}
```

## Properties
<a name="aws-properties-cognito-identitypoolroleattachment-mappingrule-properties"></a>

`Claim`  <a name="cfn-cognito-identitypoolroleattachment-mappingrule-claim"></a>
The claim name that must be present in the token. For example: "isAdmin" or "paid".
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchType`  <a name="cfn-cognito-identitypoolroleattachment-mappingrule-matchtype"></a>
The match condition that specifies how closely the claim value in the IdP token must match `Value`.
Valid values are: `Equals`, `Contains`, `StartsWith`, and `NotEqual`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleARN`  <a name="cfn-cognito-identitypoolroleattachment-mappingrule-rolearn"></a>
The Amazon Resource Name (ARN) of the role.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cognito-identitypoolroleattachment-mappingrule-value"></a>
A brief string that the claim must match. For example, "paid" or "yes".
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
