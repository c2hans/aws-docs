---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-launchtemplatespecificationoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment LaunchTemplateSpecificationOverride
<a name="aws-properties-batch-computeenvironment-launchtemplatespecificationoverride"></a>

An object that represents a launch template to use in place of the default launch template. You must specify either the launch template ID or launch template name in the request, but not both.

If security groups are specified using both the `securityGroupIds` parameter of `CreateComputeEnvironment` and the launch template, the values in the `securityGroupIds` parameter of `CreateComputeEnvironment` will be used.

You can define up to ten (10) overrides for each compute environment.

**Note**
This object isn't applicable to jobs that are running on Fargate resources.

**Note**
To unset all override templates for a compute environment, you can pass an empty array to the [UpdateComputeEnvironment.overrides](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) parameter, or not include the `overrides` parameter when submitting the `UpdateComputeEnvironment` API operation.

## Syntax
<a name="aws-properties-batch-computeenvironment-launchtemplatespecificationoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-launchtemplatespecificationoverride-syntax.json"></a>

```
{
  "[LaunchTemplateId](#cfn-batch-computeenvironment-launchtemplatespecificationoverride-launchtemplateid)" : {{String}},
  "[LaunchTemplateName](#cfn-batch-computeenvironment-launchtemplatespecificationoverride-launchtemplatename)" : {{String}},
  "[TargetInstanceTypes](#cfn-batch-computeenvironment-launchtemplatespecificationoverride-targetinstancetypes)" : {{[ String, ... ]}},
  "[UserdataType](#cfn-batch-computeenvironment-launchtemplatespecificationoverride-userdatatype)" : {{String}},
  "[Version](#cfn-batch-computeenvironment-launchtemplatespecificationoverride-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-launchtemplatespecificationoverride-syntax.yaml"></a>

```
  [LaunchTemplateId](#cfn-batch-computeenvironment-launchtemplatespecificationoverride-launchtemplateid): {{String}}
  [LaunchTemplateName](#cfn-batch-computeenvironment-launchtemplatespecificationoverride-launchtemplatename): {{String}}
  [TargetInstanceTypes](#cfn-batch-computeenvironment-launchtemplatespecificationoverride-targetinstancetypes): {{
    - String}}
  [UserdataType](#cfn-batch-computeenvironment-launchtemplatespecificationoverride-userdatatype): {{String}}
  [Version](#cfn-batch-computeenvironment-launchtemplatespecificationoverride-version): {{String}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-launchtemplatespecificationoverride-properties"></a>

`LaunchTemplateId`  <a name="cfn-batch-computeenvironment-launchtemplatespecificationoverride-launchtemplateid"></a>
The ID of the launch template.
**Note:** If you specify the `launchTemplateId` you can't specify the `launchTemplateName` as well.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LaunchTemplateName`  <a name="cfn-batch-computeenvironment-launchtemplatespecificationoverride-launchtemplatename"></a>
The name of the launch template.
**Note:** If you specify the `launchTemplateName` you can't specify the `launchTemplateId` as well.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`TargetInstanceTypes`  <a name="cfn-batch-computeenvironment-launchtemplatespecificationoverride-targetinstancetypes"></a>
The instance type or family that this override launch template should be applied to.
This parameter is required when defining a launch template override.
Information included in this parameter must meet the following requirements:
+ Must be a valid Amazon EC2 instance type or family.
+ The following AWS Batch`InstanceTypes` are not allowed: `optimal`, `default_x86_64`, and `default_arm64`.
+ `targetInstanceTypes` can target only instance types and families that are included within the [`ComputeResource.instanceTypes`](https://docs.aws.amazon.com/batch/latest/APIReference/API_ComputeResource.html#Batch-Type-ComputeResource-instanceTypes) set. `targetInstanceTypes` doesn't need to include all of the instances from the `instanceType` set, but at least a subset. For example, if `ComputeResource.instanceTypes` includes `[m5, g5]`, `targetInstanceTypes` can include `[m5.2xlarge]` and `[m5.large]` but not `[c5.large]`.
+ `targetInstanceTypes` included within the same launch template override or across launch template overrides can't overlap for the same compute environment. For example, you can't define one launch template override to target an instance family and another define an instance type within this same family.
*Required*: No
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`UserdataType`  <a name="cfn-batch-computeenvironment-launchtemplatespecificationoverride-userdatatype"></a>
The EKS node initialization process to use. You only need to specify this value if you are using a custom AMI. The default value is `EKS_BOOTSTRAP_SH`. If *imageType* is a custom AMI based on EKS\_AL2023 or EKS\_AL2023\_NVIDIA then you must choose `EKS_NODEADM`.
*Required*: No
*Type*: String
*Allowed values*: `EKS_BOOTSTRAP_SH | EKS_NODEADM`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Version`  <a name="cfn-batch-computeenvironment-launchtemplatespecificationoverride-version"></a>
The version number of the launch template, `$Default`, or `$Latest`.
If the value is `$Default`, the default version of the launch template is used. If the value is `$Latest`, the latest version of the launch template is used.
If the AMI ID that's used in a compute environment is from the launch template, the AMI isn't changed when the compute environment is updated. It's only changed if the `updateToLatestImageVersion` parameter for the compute environment is set to `true`. During an infrastructure update, if either `$Default` or `$Latest` is specified, AWS Batch re-evaluates the launch template version, and it might use a different version of the launch template. This is the case even if the launch template isn't specified in the update. When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *AWS Batch User Guide*.
Default: `$Default`
Latest: `$Latest`
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
