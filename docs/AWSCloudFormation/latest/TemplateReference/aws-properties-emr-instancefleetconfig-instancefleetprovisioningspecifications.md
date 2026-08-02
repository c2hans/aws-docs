---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancefleetconfig-instancefleetprovisioningspecifications.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceFleetConfig InstanceFleetProvisioningSpecifications
<a name="aws-properties-emr-instancefleetconfig-instancefleetprovisioningspecifications"></a>

**Note**
The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

`InstanceTypeConfig` is a sub-property of `InstanceFleetConfig`. `InstanceTypeConfig` determines the EC2 instances that Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities.

## Syntax
<a name="aws-properties-emr-instancefleetconfig-instancefleetprovisioningspecifications-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancefleetconfig-instancefleetprovisioningspecifications-syntax.json"></a>

```
{
  "[OnDemandSpecification](#cfn-emr-instancefleetconfig-instancefleetprovisioningspecifications-ondemandspecification)" : {{OnDemandProvisioningSpecification}},
  "[SpotSpecification](#cfn-emr-instancefleetconfig-instancefleetprovisioningspecifications-spotspecification)" : {{SpotProvisioningSpecification}}
}
```

### YAML
<a name="aws-properties-emr-instancefleetconfig-instancefleetprovisioningspecifications-syntax.yaml"></a>

```
  [OnDemandSpecification](#cfn-emr-instancefleetconfig-instancefleetprovisioningspecifications-ondemandspecification): {{
    OnDemandProvisioningSpecification}}
  [SpotSpecification](#cfn-emr-instancefleetconfig-instancefleetprovisioningspecifications-spotspecification): {{
    SpotProvisioningSpecification}}
```

## Properties
<a name="aws-properties-emr-instancefleetconfig-instancefleetprovisioningspecifications-properties"></a>

`OnDemandSpecification`  <a name="cfn-emr-instancefleetconfig-instancefleetprovisioningspecifications-ondemandspecification"></a>
 The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy and capacity reservation options.
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.
*Required*: No
*Type*: [OnDemandProvisioningSpecification](aws-properties-emr-instancefleetconfig-ondemandprovisioningspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SpotSpecification`  <a name="cfn-emr-instancefleetconfig-instancefleetprovisioningspecifications-spotspecification"></a>
The launch specification for Spot instances in the fleet, which determines the allocation strategy, defined duration, and provisioning timeout behavior.
*Required*: No
*Type*: [SpotProvisioningSpecification](aws-properties-emr-instancefleetconfig-spotprovisioningspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
