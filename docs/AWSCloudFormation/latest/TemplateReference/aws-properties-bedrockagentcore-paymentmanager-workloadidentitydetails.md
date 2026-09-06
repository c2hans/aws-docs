---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentmanager-workloadidentitydetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentManager WorkloadIdentityDetails
<a name="aws-properties-bedrockagentcore-paymentmanager-workloadidentitydetails"></a>

Details about the workload identity associated with the payment manager.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentmanager-workloadidentitydetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentmanager-workloadidentitydetails-syntax.json"></a>

```
{
  "[WorkloadIdentityArn](#cfn-bedrockagentcore-paymentmanager-workloadidentitydetails-workloadidentityarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentmanager-workloadidentitydetails-syntax.yaml"></a>

```
  [WorkloadIdentityArn](#cfn-bedrockagentcore-paymentmanager-workloadidentitydetails-workloadidentityarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentmanager-workloadidentitydetails-properties"></a>

`WorkloadIdentityArn`  <a name="cfn-bedrockagentcore-paymentmanager-workloadidentitydetails-workloadidentityarn"></a>
The Amazon Resource Name (ARN) of the workload identity associated with the payment manager.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
