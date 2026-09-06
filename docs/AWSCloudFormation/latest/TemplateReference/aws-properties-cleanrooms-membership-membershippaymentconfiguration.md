---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-membership-membershippaymentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership MembershipPaymentConfiguration
<a name="aws-properties-cleanrooms-membership-membershippaymentconfiguration"></a>

An object representing the payment responsibilities accepted by the collaboration member.

## Syntax
<a name="aws-properties-cleanrooms-membership-membershippaymentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-membership-membershippaymentconfiguration-syntax.json"></a>

```
{
  "[JobCompute](#cfn-cleanrooms-membership-membershippaymentconfiguration-jobcompute)" : {{MembershipJobComputePaymentConfig}},
  "[MachineLearning](#cfn-cleanrooms-membership-membershippaymentconfiguration-machinelearning)" : {{MembershipMLPaymentConfig}},
  "[QueryCompute](#cfn-cleanrooms-membership-membershippaymentconfiguration-querycompute)" : {{MembershipQueryComputePaymentConfig}}
}
```

### YAML
<a name="aws-properties-cleanrooms-membership-membershippaymentconfiguration-syntax.yaml"></a>

```
  [JobCompute](#cfn-cleanrooms-membership-membershippaymentconfiguration-jobcompute): {{
    MembershipJobComputePaymentConfig}}
  [MachineLearning](#cfn-cleanrooms-membership-membershippaymentconfiguration-machinelearning): {{
    MembershipMLPaymentConfig}}
  [QueryCompute](#cfn-cleanrooms-membership-membershippaymentconfiguration-querycompute): {{
    MembershipQueryComputePaymentConfig}}
```

## Properties
<a name="aws-properties-cleanrooms-membership-membershippaymentconfiguration-properties"></a>

`JobCompute`  <a name="cfn-cleanrooms-membership-membershippaymentconfiguration-jobcompute"></a>
The payment responsibilities accepted by the collaboration member for job compute costs.
*Required*: No
*Type*: [MembershipJobComputePaymentConfig](aws-properties-cleanrooms-membership-membershipjobcomputepaymentconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MachineLearning`  <a name="cfn-cleanrooms-membership-membershippaymentconfiguration-machinelearning"></a>
The payment responsibilities accepted by the collaboration member for machine learning costs.
*Required*: No
*Type*: [MembershipMLPaymentConfig](aws-properties-cleanrooms-membership-membershipmlpaymentconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryCompute`  <a name="cfn-cleanrooms-membership-membershippaymentconfiguration-querycompute"></a>
The payment responsibilities accepted by the collaboration member for query compute costs.
*Required*: Yes
*Type*: [MembershipQueryComputePaymentConfig](aws-properties-cleanrooms-membership-membershipquerycomputepaymentconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
