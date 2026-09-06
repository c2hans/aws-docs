---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-membership-membershipmodeltrainingpaymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership MembershipModelTrainingPaymentConfig
<a name="aws-properties-cleanrooms-membership-membershipmodeltrainingpaymentconfig"></a>

An object representing the collaboration member's model training payment responsibilities set by the collaboration creator.

## Syntax
<a name="aws-properties-cleanrooms-membership-membershipmodeltrainingpaymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-membership-membershipmodeltrainingpaymentconfig-syntax.json"></a>

```
{
  "[IsResponsible](#cfn-cleanrooms-membership-membershipmodeltrainingpaymentconfig-isresponsible)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-membership-membershipmodeltrainingpaymentconfig-syntax.yaml"></a>

```
  [IsResponsible](#cfn-cleanrooms-membership-membershipmodeltrainingpaymentconfig-isresponsible): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-membership-membershipmodeltrainingpaymentconfig-properties"></a>

`IsResponsible`  <a name="cfn-cleanrooms-membership-membershipmodeltrainingpaymentconfig-isresponsible"></a>
Indicates whether the collaboration member has accepted to pay for model training costs (`TRUE`) or has not accepted to pay for model training costs (`FALSE`).
If the collaboration creator has not specified anyone to pay for model training costs, then the member who can query is the default payer.
An error message is returned for the following reasons:
+ If you set the value to `FALSE` but you are responsible to pay for model training costs.
+ If you set the value to `TRUE` but you are not responsible to pay for model training costs.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
