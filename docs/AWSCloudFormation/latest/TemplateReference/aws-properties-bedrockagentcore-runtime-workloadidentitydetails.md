---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-workloadidentitydetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime WorkloadIdentityDetails
<a name="aws-properties-bedrockagentcore-runtime-workloadidentitydetails"></a>

The workload identity details for the AgentCore Runtime.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-workloadidentitydetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-workloadidentitydetails-syntax.json"></a>

```
{
  "[WorkloadIdentityArn](#cfn-bedrockagentcore-runtime-workloadidentitydetails-workloadidentityarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-workloadidentitydetails-syntax.yaml"></a>

```
  [WorkloadIdentityArn](#cfn-bedrockagentcore-runtime-workloadidentitydetails-workloadidentityarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-workloadidentitydetails-properties"></a>

`WorkloadIdentityArn`  <a name="cfn-bedrockagentcore-runtime-workloadidentitydetails-workloadidentityarn"></a>
The Amazon Resource Name (ARN) of the workload identity.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
