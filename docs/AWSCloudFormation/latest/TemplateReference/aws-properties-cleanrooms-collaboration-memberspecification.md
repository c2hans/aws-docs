---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-collaboration-memberspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Collaboration MemberSpecification
<a name="aws-properties-cleanrooms-collaboration-memberspecification"></a>

Basic metadata used to construct a new member.

## Syntax
<a name="aws-properties-cleanrooms-collaboration-memberspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-collaboration-memberspecification-syntax.json"></a>

```
{
  "[AccountId](#cfn-cleanrooms-collaboration-memberspecification-accountid)" : {{String}},
  "[DisplayName](#cfn-cleanrooms-collaboration-memberspecification-displayname)" : {{String}},
  "[MemberAbilities](#cfn-cleanrooms-collaboration-memberspecification-memberabilities)" : {{[ String, ... ]}},
  "[MLMemberAbilities](#cfn-cleanrooms-collaboration-memberspecification-mlmemberabilities)" : {{MLMemberAbilities}},
  "[PaymentConfiguration](#cfn-cleanrooms-collaboration-memberspecification-paymentconfiguration)" : {{PaymentConfiguration}}
}
```

### YAML
<a name="aws-properties-cleanrooms-collaboration-memberspecification-syntax.yaml"></a>

```
  [AccountId](#cfn-cleanrooms-collaboration-memberspecification-accountid): {{String}}
  [DisplayName](#cfn-cleanrooms-collaboration-memberspecification-displayname): {{String}}
  [MemberAbilities](#cfn-cleanrooms-collaboration-memberspecification-memberabilities): {{
    - String}}
  [MLMemberAbilities](#cfn-cleanrooms-collaboration-memberspecification-mlmemberabilities): {{
    MLMemberAbilities}}
  [PaymentConfiguration](#cfn-cleanrooms-collaboration-memberspecification-paymentconfiguration): {{
    PaymentConfiguration}}
```

## Properties
<a name="aws-properties-cleanrooms-collaboration-memberspecification-properties"></a>

`AccountId`  <a name="cfn-cleanrooms-collaboration-memberspecification-accountid"></a>
The identifier used to reference members of the collaboration. Currently only supports AWS account ID.
*Required*: Yes
*Type*: String
*Pattern*: `^\d+$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DisplayName`  <a name="cfn-cleanrooms-collaboration-memberspecification-displayname"></a>
The member's display name.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MemberAbilities`  <a name="cfn-cleanrooms-collaboration-memberspecification-memberabilities"></a>
The abilities granted to the collaboration member.
*Allowed Values*: `CAN_QUERY` \| `CAN_RECEIVE_RESULTS`
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MLMemberAbilities`  <a name="cfn-cleanrooms-collaboration-memberspecification-mlmemberabilities"></a>
The ML abilities granted to the collaboration member.
*Required*: No
*Type*: [MLMemberAbilities](aws-properties-cleanrooms-collaboration-mlmemberabilities.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PaymentConfiguration`  <a name="cfn-cleanrooms-collaboration-memberspecification-paymentconfiguration"></a>
The collaboration member's payment responsibilities set by the collaboration creator.
If the collaboration creator hasn't speciﬁed anyone as the member paying for query compute costs, then the member who can query is the default payer.
*Required*: No
*Type*: [PaymentConfiguration](aws-properties-cleanrooms-collaboration-paymentconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
