---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-instancefleetresizingspecifications.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster InstanceFleetResizingSpecifications
<a name="aws-properties-emr-cluster-instancefleetresizingspecifications"></a>

The resize specification for On-Demand and Spot Instances in the fleet.

## Syntax
<a name="aws-properties-emr-cluster-instancefleetresizingspecifications-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-instancefleetresizingspecifications-syntax.json"></a>

```
{
  "[OnDemandResizeSpecification](#cfn-emr-cluster-instancefleetresizingspecifications-ondemandresizespecification)" : {{OnDemandResizingSpecification}},
  "[SpotResizeSpecification](#cfn-emr-cluster-instancefleetresizingspecifications-spotresizespecification)" : {{SpotResizingSpecification}}
}
```

### YAML
<a name="aws-properties-emr-cluster-instancefleetresizingspecifications-syntax.yaml"></a>

```
  [OnDemandResizeSpecification](#cfn-emr-cluster-instancefleetresizingspecifications-ondemandresizespecification): {{
    OnDemandResizingSpecification}}
  [SpotResizeSpecification](#cfn-emr-cluster-instancefleetresizingspecifications-spotresizespecification): {{
    SpotResizingSpecification}}
```

## Properties
<a name="aws-properties-emr-cluster-instancefleetresizingspecifications-properties"></a>

`OnDemandResizeSpecification`  <a name="cfn-emr-cluster-instancefleetresizingspecifications-ondemandresizespecification"></a>
The resize specification for On-Demand Instances in the instance fleet, which contains the allocation strategy, capacity reservation options, and the resize timeout period.
*Required*: No
*Type*: [OnDemandResizingSpecification](aws-properties-emr-cluster-ondemandresizingspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpotResizeSpecification`  <a name="cfn-emr-cluster-instancefleetresizingspecifications-spotresizespecification"></a>
The resize specification for Spot Instances in the instance fleet, which contains the allocation strategy and the resize timeout period.
*Required*: No
*Type*: [SpotResizingSpecification](aws-properties-emr-cluster-spotresizingspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
