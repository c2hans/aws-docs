---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancefleetconfig-instancefleetresizingspecifications.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceFleetConfig InstanceFleetResizingSpecifications
<a name="aws-properties-emr-instancefleetconfig-instancefleetresizingspecifications"></a>

The resize specification for On-Demand and Spot Instances in the fleet.

## Syntax
<a name="aws-properties-emr-instancefleetconfig-instancefleetresizingspecifications-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancefleetconfig-instancefleetresizingspecifications-syntax.json"></a>

```
{
  "[OnDemandResizeSpecification](#cfn-emr-instancefleetconfig-instancefleetresizingspecifications-ondemandresizespecification)" : {{OnDemandResizingSpecification}},
  "[SpotResizeSpecification](#cfn-emr-instancefleetconfig-instancefleetresizingspecifications-spotresizespecification)" : {{SpotResizingSpecification}}
}
```

### YAML
<a name="aws-properties-emr-instancefleetconfig-instancefleetresizingspecifications-syntax.yaml"></a>

```
  [OnDemandResizeSpecification](#cfn-emr-instancefleetconfig-instancefleetresizingspecifications-ondemandresizespecification): {{
    OnDemandResizingSpecification}}
  [SpotResizeSpecification](#cfn-emr-instancefleetconfig-instancefleetresizingspecifications-spotresizespecification): {{
    SpotResizingSpecification}}
```

## Properties
<a name="aws-properties-emr-instancefleetconfig-instancefleetresizingspecifications-properties"></a>

`OnDemandResizeSpecification`  <a name="cfn-emr-instancefleetconfig-instancefleetresizingspecifications-ondemandresizespecification"></a>
The resize specification for On-Demand Instances in the instance fleet, which contains the allocation strategy, capacity reservation options, and the resize timeout period.
*Required*: No
*Type*: [OnDemandResizingSpecification](aws-properties-emr-instancefleetconfig-ondemandresizingspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpotResizeSpecification`  <a name="cfn-emr-instancefleetconfig-instancefleetresizingspecifications-spotresizespecification"></a>
The resize specification for Spot Instances in the instance fleet, which contains the allocation strategy and the resize timeout period.
*Required*: No
*Type*: [SpotResizingSpecification](aws-properties-emr-instancefleetconfig-spotresizingspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
