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
