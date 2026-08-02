---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-cpuperformancefactorrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet CpuPerformanceFactorRequest
<a name="aws-properties-ec2-spotfleet-cpuperformancefactorrequest"></a>

The CPU performance to consider, using an instance family as the baseline reference.

## Syntax
<a name="aws-properties-ec2-spotfleet-cpuperformancefactorrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-cpuperformancefactorrequest-syntax.json"></a>

```
{
  "[References](#cfn-ec2-spotfleet-cpuperformancefactorrequest-references)" : {{[ PerformanceFactorReferenceRequest, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-cpuperformancefactorrequest-syntax.yaml"></a>

```
  [References](#cfn-ec2-spotfleet-cpuperformancefactorrequest-references): {{
    - PerformanceFactorReferenceRequest}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-cpuperformancefactorrequest-properties"></a>

`References`  <a name="cfn-ec2-spotfleet-cpuperformancefactorrequest-references"></a>
Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.
Currently, only one instance family can be specified in the list.
*Required*: No
*Type*: Array of [PerformanceFactorReferenceRequest](aws-properties-ec2-spotfleet-performancefactorreferencerequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
