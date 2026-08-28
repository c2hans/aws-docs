---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancefleetconfig-spotresizingspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceFleetConfig SpotResizingSpecification
<a name="aws-properties-emr-instancefleetconfig-spotresizingspecification"></a>

The resize specification for Spot Instances in the instance fleet, which contains the resize timeout period.

## Syntax
<a name="aws-properties-emr-instancefleetconfig-spotresizingspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancefleetconfig-spotresizingspecification-syntax.json"></a>

```
{
  "[AllocationStrategy](#cfn-emr-instancefleetconfig-spotresizingspecification-allocationstrategy)" : {{String}},
  "[TimeoutDurationMinutes](#cfn-emr-instancefleetconfig-spotresizingspecification-timeoutdurationminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emr-instancefleetconfig-spotresizingspecification-syntax.yaml"></a>

```
  [AllocationStrategy](#cfn-emr-instancefleetconfig-spotresizingspecification-allocationstrategy): {{String}}
  [TimeoutDurationMinutes](#cfn-emr-instancefleetconfig-spotresizingspecification-timeoutdurationminutes): {{Integer}}
```

## Properties
<a name="aws-properties-emr-instancefleetconfig-spotresizingspecification-properties"></a>

`AllocationStrategy`  <a name="cfn-emr-instancefleetconfig-spotresizingspecification-allocationstrategy"></a>
Specifies the allocation strategy to use to launch Spot instances during a resize. If you run Amazon EMR releases 6.9.0 or higher, the default is `price-capacity-optimized`. If you run Amazon EMR releases 6.8.0 or lower, the default is `capacity-optimized`.
*Required*: No
*Type*: String
*Allowed values*: `capacity-optimized | price-capacity-optimized | lowest-price | diversified | capacity-optimized-prioritized`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutDurationMinutes`  <a name="cfn-emr-instancefleetconfig-spotresizingspecification-timeoutdurationminutes"></a>
Spot resize timeout in minutes. If Spot Instances are not provisioned within this time, the resize workflow will stop provisioning of Spot instances. Minimum value is 5 minutes and maximum value is 10,080 minutes (7 days). The timeout applies to all resize workflows on the Instance Fleet. The resize could be triggered by Amazon EMR Managed Scaling or by the customer (via Amazon EMR Console, Amazon EMR CLI modify-instance-fleet or Amazon EMR SDK ModifyInstanceFleet API) or by Amazon EMR due to Amazon EC2 Spot Reclamation.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
