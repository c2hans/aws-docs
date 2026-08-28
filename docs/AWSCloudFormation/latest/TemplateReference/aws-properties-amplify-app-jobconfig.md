---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplify-app-jobconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::App JobConfig
<a name="aws-properties-amplify-app-jobconfig"></a>

Describes the configuration details that apply to the jobs for an Amplify app.

Use `JobConfig` to apply configuration to jobs, such as customizing the build instance size when you create or update an Amplify app. For more information about customizable build instances, see [Custom build instances](https://docs.aws.amazon.com/amplify/latest/userguide/custom-build-instance.html) in the *Amplify User Guide*.

## Syntax
<a name="aws-properties-amplify-app-jobconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplify-app-jobconfig-syntax.json"></a>

```
{
  "[BuildComputeType](#cfn-amplify-app-jobconfig-buildcomputetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplify-app-jobconfig-syntax.yaml"></a>

```
  [BuildComputeType](#cfn-amplify-app-jobconfig-buildcomputetype): {{String}}
```

## Properties
<a name="aws-properties-amplify-app-jobconfig-properties"></a>

`BuildComputeType`  <a name="cfn-amplify-app-jobconfig-buildcomputetype"></a>
Specifies the size of the build instance. Amplify supports three instance sizes: `STANDARD_8GB`, `LARGE_16GB`, and `XLARGE_72GB`. If you don't specify a value, Amplify uses the `STANDARD_8GB` default.
The following list describes the CPU, memory, and storage capacity for each build instance type:
STANDARD\_8GB
+ vCPUs: 4
+ Memory: 8 GiB
+ Disk space: 128 GB
LARGE\_16GB
+ vCPUs: 8
+ Memory: 16 GiB
+ Disk space: 128 GB
XLARGE\_72GB
+ vCPUs: 36
+ Memory: 72 GiB
+ Disk space: 256 GB
*Required*: Yes
*Type*: String
*Allowed values*: `STANDARD_8GB | LARGE_16GB | XLARGE_72GB`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
