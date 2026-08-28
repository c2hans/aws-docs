---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-fleet-computeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Fleet ComputeConfiguration
<a name="aws-properties-codebuild-fleet-computeconfiguration"></a>

Contains compute attributes. These attributes only need be specified when your project's or fleet's `computeType` is set to `ATTRIBUTE_BASED_COMPUTE` or `CUSTOM_INSTANCE_TYPE`.

## Syntax
<a name="aws-properties-codebuild-fleet-computeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-fleet-computeconfiguration-syntax.json"></a>

```
{
  "[disk](#cfn-codebuild-fleet-computeconfiguration-disk)" : {{Integer}},
  "[instanceType](#cfn-codebuild-fleet-computeconfiguration-instancetype)" : {{String}},
  "[machineType](#cfn-codebuild-fleet-computeconfiguration-machinetype)" : {{String}},
  "[memory](#cfn-codebuild-fleet-computeconfiguration-memory)" : {{Integer}},
  "[vCpu](#cfn-codebuild-fleet-computeconfiguration-vcpu)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-codebuild-fleet-computeconfiguration-syntax.yaml"></a>

```
  [disk](#cfn-codebuild-fleet-computeconfiguration-disk): {{Integer}}
  [instanceType](#cfn-codebuild-fleet-computeconfiguration-instancetype): {{String}}
  [machineType](#cfn-codebuild-fleet-computeconfiguration-machinetype): {{String}}
  [memory](#cfn-codebuild-fleet-computeconfiguration-memory): {{Integer}}
  [vCpu](#cfn-codebuild-fleet-computeconfiguration-vcpu): {{Integer}}
```

## Properties
<a name="aws-properties-codebuild-fleet-computeconfiguration-properties"></a>

`disk`  <a name="cfn-codebuild-fleet-computeconfiguration-disk"></a>
The amount of disk space of the instance type included in your fleet.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`instanceType`  <a name="cfn-codebuild-fleet-computeconfiguration-instancetype"></a>
The EC2 instance type to be launched in your fleet.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`machineType`  <a name="cfn-codebuild-fleet-computeconfiguration-machinetype"></a>
The machine type of the instance type included in your fleet.
*Required*: No
*Type*: String
*Allowed values*: `GENERAL | NVME`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`memory`  <a name="cfn-codebuild-fleet-computeconfiguration-memory"></a>
The amount of memory of the instance type included in your fleet.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`vCpu`  <a name="cfn-codebuild-fleet-computeconfiguration-vcpu"></a>
The number of vCPUs of the instance type included in your fleet.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
