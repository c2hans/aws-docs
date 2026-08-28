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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
