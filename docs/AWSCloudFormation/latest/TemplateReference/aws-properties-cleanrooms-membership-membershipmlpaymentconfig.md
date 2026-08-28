---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-membership-membershipmlpaymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership MembershipMLPaymentConfig
<a name="aws-properties-cleanrooms-membership-membershipmlpaymentconfig"></a>

An object representing the collaboration member's machine learning payment responsibilities set by the collaboration creator.

## Syntax
<a name="aws-properties-cleanrooms-membership-membershipmlpaymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-membership-membershipmlpaymentconfig-syntax.json"></a>

```
{
  "[ModelInference](#cfn-cleanrooms-membership-membershipmlpaymentconfig-modelinference)" : {{MembershipModelInferencePaymentConfig}},
  "[ModelTraining](#cfn-cleanrooms-membership-membershipmlpaymentconfig-modeltraining)" : {{MembershipModelTrainingPaymentConfig}},
  "[SyntheticDataGeneration](#cfn-cleanrooms-membership-membershipmlpaymentconfig-syntheticdatageneration)" : {{MembershipSyntheticDataGenerationPaymentConfig}}
}
```

### YAML
<a name="aws-properties-cleanrooms-membership-membershipmlpaymentconfig-syntax.yaml"></a>

```
  [ModelInference](#cfn-cleanrooms-membership-membershipmlpaymentconfig-modelinference): {{
    MembershipModelInferencePaymentConfig}}
  [ModelTraining](#cfn-cleanrooms-membership-membershipmlpaymentconfig-modeltraining): {{
    MembershipModelTrainingPaymentConfig}}
  [SyntheticDataGeneration](#cfn-cleanrooms-membership-membershipmlpaymentconfig-syntheticdatageneration): {{
    MembershipSyntheticDataGenerationPaymentConfig}}
```

## Properties
<a name="aws-properties-cleanrooms-membership-membershipmlpaymentconfig-properties"></a>

`ModelInference`  <a name="cfn-cleanrooms-membership-membershipmlpaymentconfig-modelinference"></a>
The payment responsibilities accepted by the member for model inference.
*Required*: No
*Type*: [MembershipModelInferencePaymentConfig](aws-properties-cleanrooms-membership-membershipmodelinferencepaymentconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelTraining`  <a name="cfn-cleanrooms-membership-membershipmlpaymentconfig-modeltraining"></a>
The payment responsibilities accepted by the member for model training.
*Required*: No
*Type*: [MembershipModelTrainingPaymentConfig](aws-properties-cleanrooms-membership-membershipmodeltrainingpaymentconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SyntheticDataGeneration`  <a name="cfn-cleanrooms-membership-membershipmlpaymentconfig-syntheticdatageneration"></a>
The payment configuration for synthetic data generation for this machine learning membership.
*Required*: No
*Type*: [MembershipSyntheticDataGenerationPaymentConfig](aws-properties-cleanrooms-membership-membershipsyntheticdatagenerationpaymentconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
