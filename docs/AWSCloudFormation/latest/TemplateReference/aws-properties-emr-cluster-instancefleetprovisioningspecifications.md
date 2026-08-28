---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-instancefleetprovisioningspecifications.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster InstanceFleetProvisioningSpecifications
<a name="aws-properties-emr-cluster-instancefleetprovisioningspecifications"></a>

`InstanceFleetProvisioningSpecification` is a subproperty of `InstanceFleetConfig`. `InstanceFleetProvisioningSpecification` defines the launch specification for Spot instances in an instance fleet, which determines the defined duration and provisioning timeout behavior for Spot instances.

**Note**
The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

## Syntax
<a name="aws-properties-emr-cluster-instancefleetprovisioningspecifications-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-instancefleetprovisioningspecifications-syntax.json"></a>

```
{
  "[OnDemandSpecification](#cfn-emr-cluster-instancefleetprovisioningspecifications-ondemandspecification)" : {{OnDemandProvisioningSpecification}},
  "[SpotSpecification](#cfn-emr-cluster-instancefleetprovisioningspecifications-spotspecification)" : {{SpotProvisioningSpecification}}
}
```

### YAML
<a name="aws-properties-emr-cluster-instancefleetprovisioningspecifications-syntax.yaml"></a>

```
  [OnDemandSpecification](#cfn-emr-cluster-instancefleetprovisioningspecifications-ondemandspecification): {{
    OnDemandProvisioningSpecification}}
  [SpotSpecification](#cfn-emr-cluster-instancefleetprovisioningspecifications-spotspecification): {{
    SpotProvisioningSpecification}}
```

## Properties
<a name="aws-properties-emr-cluster-instancefleetprovisioningspecifications-properties"></a>

`OnDemandSpecification`  <a name="cfn-emr-cluster-instancefleetprovisioningspecifications-ondemandspecification"></a>
 The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy and capacity reservation options.
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.
*Required*: No
*Type*: [OnDemandProvisioningSpecification](aws-properties-emr-cluster-ondemandprovisioningspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpotSpecification`  <a name="cfn-emr-cluster-instancefleetprovisioningspecifications-spotspecification"></a>
The launch specification for Spot instances in the fleet, which determines the allocation strategy, defined duration, and provisioning timeout behavior.
*Required*: No
*Type*: [SpotProvisioningSpecification](aws-properties-emr-cluster-spotprovisioningspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
