---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-effectivepolicyvalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service EffectivePolicyValues
<a name="aws-properties-resiliencehubv2-service-effectivepolicyvalues"></a>

Contains the effective resilience policy values for a service.

## Syntax
<a name="aws-properties-resiliencehubv2-service-effectivepolicyvalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-effectivepolicyvalues-syntax.json"></a>

```
{
  "[AvailabilitySlo](#cfn-resiliencehubv2-service-effectivepolicyvalues-availabilityslo)" : {{SloSource}},
  "[MultiAzDrApproach](#cfn-resiliencehubv2-service-effectivepolicyvalues-multiazdrapproach)" : {{DisasterRecoverySource}},
  "[MultiAzRpo](#cfn-resiliencehubv2-service-effectivepolicyvalues-multiazrpo)" : {{TargetSource}},
  "[MultiAzRto](#cfn-resiliencehubv2-service-effectivepolicyvalues-multiazrto)" : {{TargetSource}},
  "[MultiRegionDrApproach](#cfn-resiliencehubv2-service-effectivepolicyvalues-multiregiondrapproach)" : {{DisasterRecoverySource}},
  "[MultiRegionRpo](#cfn-resiliencehubv2-service-effectivepolicyvalues-multiregionrpo)" : {{TargetSource}},
  "[MultiRegionRto](#cfn-resiliencehubv2-service-effectivepolicyvalues-multiregionrto)" : {{TargetSource}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-effectivepolicyvalues-syntax.yaml"></a>

```
  [AvailabilitySlo](#cfn-resiliencehubv2-service-effectivepolicyvalues-availabilityslo): {{
    SloSource}}
  [MultiAzDrApproach](#cfn-resiliencehubv2-service-effectivepolicyvalues-multiazdrapproach): {{
    DisasterRecoverySource}}
  [MultiAzRpo](#cfn-resiliencehubv2-service-effectivepolicyvalues-multiazrpo): {{
    TargetSource}}
  [MultiAzRto](#cfn-resiliencehubv2-service-effectivepolicyvalues-multiazrto): {{
    TargetSource}}
  [MultiRegionDrApproach](#cfn-resiliencehubv2-service-effectivepolicyvalues-multiregiondrapproach): {{
    DisasterRecoverySource}}
  [MultiRegionRpo](#cfn-resiliencehubv2-service-effectivepolicyvalues-multiregionrpo): {{
    TargetSource}}
  [MultiRegionRto](#cfn-resiliencehubv2-service-effectivepolicyvalues-multiregionrto): {{
    TargetSource}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-effectivepolicyvalues-properties"></a>

`AvailabilitySlo`  <a name="cfn-resiliencehubv2-service-effectivepolicyvalues-availabilityslo"></a>
The effective availability SLO value for the service.
*Required*: No
*Type*: [SloSource](aws-properties-resiliencehubv2-service-slosource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiAzDrApproach`  <a name="cfn-resiliencehubv2-service-effectivepolicyvalues-multiazdrapproach"></a>
The effective multi-AZ disaster recovery approach for the service.
*Required*: No
*Type*: [DisasterRecoverySource](aws-properties-resiliencehubv2-service-disasterrecoverysource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiAzRpo`  <a name="cfn-resiliencehubv2-service-effectivepolicyvalues-multiazrpo"></a>
The effective multi-AZ RPO value for the service, in minutes.
*Required*: No
*Type*: [TargetSource](aws-properties-resiliencehubv2-service-targetsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiAzRto`  <a name="cfn-resiliencehubv2-service-effectivepolicyvalues-multiazrto"></a>
The effective multi-AZ RTO value for the service, in minutes.
*Required*: No
*Type*: [TargetSource](aws-properties-resiliencehubv2-service-targetsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiRegionDrApproach`  <a name="cfn-resiliencehubv2-service-effectivepolicyvalues-multiregiondrapproach"></a>
The effective multi-Region disaster recovery approach for the service.
*Required*: No
*Type*: [DisasterRecoverySource](aws-properties-resiliencehubv2-service-disasterrecoverysource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiRegionRpo`  <a name="cfn-resiliencehubv2-service-effectivepolicyvalues-multiregionrpo"></a>
The effective multi-Region RPO value for the service, in minutes.
*Required*: No
*Type*: [TargetSource](aws-properties-resiliencehubv2-service-targetsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiRegionRto`  <a name="cfn-resiliencehubv2-service-effectivepolicyvalues-multiregionrto"></a>
The effective multi-Region RTO value for the service, in minutes.
*Required*: No
*Type*: [TargetSource](aws-properties-resiliencehubv2-service-targetsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
