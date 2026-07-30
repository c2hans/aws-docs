---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-collaboration-mlpaymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Collaboration MLPaymentConfig
<a name="aws-properties-cleanrooms-collaboration-mlpaymentconfig"></a>

An object representing the collaboration member's machine learning payment responsibilities set by the collaboration creator.

## Syntax
<a name="aws-properties-cleanrooms-collaboration-mlpaymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-collaboration-mlpaymentconfig-syntax.json"></a>

```
{
  "[ModelInference](#cfn-cleanrooms-collaboration-mlpaymentconfig-modelinference)" : {{ModelInferencePaymentConfig}},
  "[ModelTraining](#cfn-cleanrooms-collaboration-mlpaymentconfig-modeltraining)" : {{ModelTrainingPaymentConfig}},
  "[SyntheticDataGeneration](#cfn-cleanrooms-collaboration-mlpaymentconfig-syntheticdatageneration)" : {{SyntheticDataGenerationPaymentConfig}}
}
```

### YAML
<a name="aws-properties-cleanrooms-collaboration-mlpaymentconfig-syntax.yaml"></a>

```
  [ModelInference](#cfn-cleanrooms-collaboration-mlpaymentconfig-modelinference): {{
    ModelInferencePaymentConfig}}
  [ModelTraining](#cfn-cleanrooms-collaboration-mlpaymentconfig-modeltraining): {{
    ModelTrainingPaymentConfig}}
  [SyntheticDataGeneration](#cfn-cleanrooms-collaboration-mlpaymentconfig-syntheticdatageneration): {{
    SyntheticDataGenerationPaymentConfig}}
```

## Properties
<a name="aws-properties-cleanrooms-collaboration-mlpaymentconfig-properties"></a>

`ModelInference`  <a name="cfn-cleanrooms-collaboration-mlpaymentconfig-modelinference"></a>
The payment responsibilities accepted by the member for model inference.
*Required*: No
*Type*: [ModelInferencePaymentConfig](aws-properties-cleanrooms-collaboration-modelinferencepaymentconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelTraining`  <a name="cfn-cleanrooms-collaboration-mlpaymentconfig-modeltraining"></a>
The payment responsibilities accepted by the member for model training.
*Required*: No
*Type*: [ModelTrainingPaymentConfig](aws-properties-cleanrooms-collaboration-modeltrainingpaymentconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SyntheticDataGeneration`  <a name="cfn-cleanrooms-collaboration-mlpaymentconfig-syntheticdatageneration"></a>
The payment configuration for machine learning synthetic data generation.
*Required*: No
*Type*: [SyntheticDataGenerationPaymentConfig](aws-properties-cleanrooms-collaboration-syntheticdatagenerationpaymentconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
