---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-schedulingpolicy-fairsharepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::SchedulingPolicy FairsharePolicy
<a name="aws-properties-batch-schedulingpolicy-fairsharepolicy"></a>

The fair-share scheduling policy details.

## Syntax
<a name="aws-properties-batch-schedulingpolicy-fairsharepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-schedulingpolicy-fairsharepolicy-syntax.json"></a>

```
{
  "[ComputeReservation](#cfn-batch-schedulingpolicy-fairsharepolicy-computereservation)" : {{Number}},
  "[ShareDecaySeconds](#cfn-batch-schedulingpolicy-fairsharepolicy-sharedecayseconds)" : {{Number}},
  "[ShareDistribution](#cfn-batch-schedulingpolicy-fairsharepolicy-sharedistribution)" : {{[ ShareAttributes, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-schedulingpolicy-fairsharepolicy-syntax.yaml"></a>

```
  [ComputeReservation](#cfn-batch-schedulingpolicy-fairsharepolicy-computereservation): {{Number}}
  [ShareDecaySeconds](#cfn-batch-schedulingpolicy-fairsharepolicy-sharedecayseconds): {{Number}}
  [ShareDistribution](#cfn-batch-schedulingpolicy-fairsharepolicy-sharedistribution): {{
    - ShareAttributes}}
```

## Properties
<a name="aws-properties-batch-schedulingpolicy-fairsharepolicy-properties"></a>

`ComputeReservation`  <a name="cfn-batch-schedulingpolicy-fairsharepolicy-computereservation"></a>
A value used to reserve some of the available maximum vCPU for share identifiers that aren't already used.
The reserved ratio is `(computeReservation/100)^ActiveFairShares` where ` ActiveFairShares ` is the number of active share identifiers.
For example, a `computeReservation` value of 50 indicates that AWS Batch reserves 50% of the maximum available vCPU if there's only one share identifier. It reserves 25% if there are two share identifiers. It reserves 12.5% if there are three share identifiers. A `computeReservation` value of 25 indicates that AWS Batch should reserve 25% of the maximum available vCPU if there's only one share identifier, 6.25% if there are two fair share identifiers, and 1.56% if there are three share identifiers.
The minimum value is 0 and the maximum value is 99.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `99`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDecaySeconds`  <a name="cfn-batch-schedulingpolicy-fairsharepolicy-sharedecayseconds"></a>
The amount of time (in seconds) to use to calculate a fair-share percentage for each share identifier in use. A value of zero (0) indicates the default minimum time window (600 seconds). The maximum supported value is 604800 (1 week).
The decay allows for more recently run jobs to have more weight than jobs that ran earlier. Consider adjusting this number if you have jobs that (on average) run longer than ten minutes, or a large difference in job count or job run times between share identifiers, and the allocation of resources doesn't meet your needs.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `604800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareDistribution`  <a name="cfn-batch-schedulingpolicy-fairsharepolicy-sharedistribution"></a>
An array of `SharedIdentifier` objects that contain the weights for the share identifiers for the fair-share policy. Share identifiers that aren't included have a default weight of `1.0`.
*Required*: No
*Type*: Array of [ShareAttributes](aws-properties-batch-schedulingpolicy-shareattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-batch-schedulingpolicy-fairsharepolicy--seealso"></a>
+ [FairsharePolicy](https://docs.aws.amazon.com/batch/latest/APIReference/API_FairsharePolicy.html) in the * AWS Batch API Reference *.
