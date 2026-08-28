---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-computenodegroup-spotoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::ComputeNodeGroup SpotOptions
<a name="aws-properties-pcs-computenodegroup-spotoptions"></a>

Additional configuration when you specify `SPOT` as the `purchaseOption` for the `CreateComputeNodeGroup` API action.

## Syntax
<a name="aws-properties-pcs-computenodegroup-spotoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-computenodegroup-spotoptions-syntax.json"></a>

```
{
  "[AllocationStrategy](#cfn-pcs-computenodegroup-spotoptions-allocationstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-computenodegroup-spotoptions-syntax.yaml"></a>

```
  [AllocationStrategy](#cfn-pcs-computenodegroup-spotoptions-allocationstrategy): {{String}}
```

## Properties
<a name="aws-properties-pcs-computenodegroup-spotoptions-properties"></a>

`AllocationStrategy`  <a name="cfn-pcs-computenodegroup-spotoptions-allocationstrategy"></a>
The Amazon EC2 allocation strategy AWS PCS uses to provision EC2 instances. AWS PCS supports **lowest price**, **capacity optimized**, and **price capacity optimized**. For more information, see [Use allocation strategies to determine how EC2 Fleet or Spot Fleet fulfills Spot and On-Demand capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-allocation-strategy.html) in the *Amazon Elastic Compute Cloud User Guide*. If you don't provide this option, it defaults to **price capacity optimized**.
*Required*: No
*Type*: String
*Allowed values*: `lowest-price | capacity-optimized | price-capacity-optimized`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
