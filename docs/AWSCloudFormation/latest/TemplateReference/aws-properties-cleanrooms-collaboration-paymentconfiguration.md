---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-collaboration-paymentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Collaboration PaymentConfiguration
<a name="aws-properties-cleanrooms-collaboration-paymentconfiguration"></a>

An object representing the collaboration member's payment responsibilities set by the collaboration creator.

## Syntax
<a name="aws-properties-cleanrooms-collaboration-paymentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-collaboration-paymentconfiguration-syntax.json"></a>

```
{
  "[JobCompute](#cfn-cleanrooms-collaboration-paymentconfiguration-jobcompute)" : {{JobComputePaymentConfig}},
  "[MachineLearning](#cfn-cleanrooms-collaboration-paymentconfiguration-machinelearning)" : {{MLPaymentConfig}},
  "[QueryCompute](#cfn-cleanrooms-collaboration-paymentconfiguration-querycompute)" : {{QueryComputePaymentConfig}}
}
```

### YAML
<a name="aws-properties-cleanrooms-collaboration-paymentconfiguration-syntax.yaml"></a>

```
  [JobCompute](#cfn-cleanrooms-collaboration-paymentconfiguration-jobcompute): {{
    JobComputePaymentConfig}}
  [MachineLearning](#cfn-cleanrooms-collaboration-paymentconfiguration-machinelearning): {{
    MLPaymentConfig}}
  [QueryCompute](#cfn-cleanrooms-collaboration-paymentconfiguration-querycompute): {{
    QueryComputePaymentConfig}}
```

## Properties
<a name="aws-properties-cleanrooms-collaboration-paymentconfiguration-properties"></a>

`JobCompute`  <a name="cfn-cleanrooms-collaboration-paymentconfiguration-jobcompute"></a>
 The compute configuration for the job.
*Required*: No
*Type*: [JobComputePaymentConfig](aws-properties-cleanrooms-collaboration-jobcomputepaymentconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MachineLearning`  <a name="cfn-cleanrooms-collaboration-paymentconfiguration-machinelearning"></a>
An object representing the collaboration member's machine learning payment responsibilities set by the collaboration creator.
*Required*: No
*Type*: [MLPaymentConfig](aws-properties-cleanrooms-collaboration-mlpaymentconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueryCompute`  <a name="cfn-cleanrooms-collaboration-paymentconfiguration-querycompute"></a>
The collaboration member's payment responsibilities set by the collaboration creator for query compute costs.
*Required*: Yes
*Type*: [QueryComputePaymentConfig](aws-properties-cleanrooms-collaboration-querycomputepaymentconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
