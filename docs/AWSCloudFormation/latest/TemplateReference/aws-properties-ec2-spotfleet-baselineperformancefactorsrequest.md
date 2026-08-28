---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-baselineperformancefactorsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet BaselinePerformanceFactorsRequest
<a name="aws-properties-ec2-spotfleet-baselineperformancefactorsrequest"></a>

The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application.

Currently, this parameter only supports CPU performance as a baseline performance factor. For example, specifying `c6i` would use the CPU performance of the `c6i` family as the baseline reference.

## Syntax
<a name="aws-properties-ec2-spotfleet-baselineperformancefactorsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-baselineperformancefactorsrequest-syntax.json"></a>

```
{
  "[Cpu](#cfn-ec2-spotfleet-baselineperformancefactorsrequest-cpu)" : {{CpuPerformanceFactorRequest}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-baselineperformancefactorsrequest-syntax.yaml"></a>

```
  [Cpu](#cfn-ec2-spotfleet-baselineperformancefactorsrequest-cpu): {{
    CpuPerformanceFactorRequest}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-baselineperformancefactorsrequest-properties"></a>

`Cpu`  <a name="cfn-ec2-spotfleet-baselineperformancefactorsrequest-cpu"></a>
The CPU performance to consider, using an instance family as the baseline reference.
*Required*: No
*Type*: [CpuPerformanceFactorRequest](aws-properties-ec2-spotfleet-cpuperformancefactorrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
