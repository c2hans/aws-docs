---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-membership-membershipsyntheticdatagenerationpaymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership MembershipSyntheticDataGenerationPaymentConfig
<a name="aws-properties-cleanrooms-membership-membershipsyntheticdatagenerationpaymentconfig"></a>

Configuration for payment for synthetic data generation in a membership.

## Syntax
<a name="aws-properties-cleanrooms-membership-membershipsyntheticdatagenerationpaymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-membership-membershipsyntheticdatagenerationpaymentconfig-syntax.json"></a>

```
{
  "[IsResponsible](#cfn-cleanrooms-membership-membershipsyntheticdatagenerationpaymentconfig-isresponsible)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-membership-membershipsyntheticdatagenerationpaymentconfig-syntax.yaml"></a>

```
  [IsResponsible](#cfn-cleanrooms-membership-membershipsyntheticdatagenerationpaymentconfig-isresponsible): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-membership-membershipsyntheticdatagenerationpaymentconfig-properties"></a>

`IsResponsible`  <a name="cfn-cleanrooms-membership-membershipsyntheticdatagenerationpaymentconfig-isresponsible"></a>
Indicates if this membership is responsible for paying for synthetic data generation.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
