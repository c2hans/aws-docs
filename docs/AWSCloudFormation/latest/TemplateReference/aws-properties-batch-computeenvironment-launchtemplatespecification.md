---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-launchtemplatespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment LaunchTemplateSpecification
<a name="aws-properties-batch-computeenvironment-launchtemplatespecification"></a>

An object that represents a launch template that's associated with a compute resource. You must specify either the launch template ID or launch template name in the request, but not both.

If security groups are specified using both the `securityGroupIds` parameter of `CreateComputeEnvironment` and the launch template, the values in the `securityGroupIds` parameter of `CreateComputeEnvironment` will be used.

**Note**
This object isn't applicable to jobs that are running on Fargate resources.

## Syntax
<a name="aws-properties-batch-computeenvironment-launchtemplatespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-launchtemplatespecification-syntax.json"></a>

```
{
  "[LaunchTemplateId](#cfn-batch-computeenvironment-launchtemplatespecification-launchtemplateid)" : {{String}},
  "[LaunchTemplateName](#cfn-batch-computeenvironment-launchtemplatespecification-launchtemplatename)" : {{String}},
  "[Overrides](#cfn-batch-computeenvironment-launchtemplatespecification-overrides)" : {{[ LaunchTemplateSpecificationOverride, ... ]}},
  "[UserdataType](#cfn-batch-computeenvironment-launchtemplatespecification-userdatatype)" : {{String}},
  "[Version](#cfn-batch-computeenvironment-launchtemplatespecification-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-launchtemplatespecification-syntax.yaml"></a>

```
  [LaunchTemplateId](#cfn-batch-computeenvironment-launchtemplatespecification-launchtemplateid): {{String}}
  [LaunchTemplateName](#cfn-batch-computeenvironment-launchtemplatespecification-launchtemplatename): {{String}}
  [Overrides](#cfn-batch-computeenvironment-launchtemplatespecification-overrides): {{
    - LaunchTemplateSpecificationOverride}}
  [UserdataType](#cfn-batch-computeenvironment-launchtemplatespecification-userdatatype): {{String}}
  [Version](#cfn-batch-computeenvironment-launchtemplatespecification-version): {{String}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-launchtemplatespecification-properties"></a>

`LaunchTemplateId`  <a name="cfn-batch-computeenvironment-launchtemplatespecification-launchtemplateid"></a>
The ID of the launch template.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LaunchTemplateName`  <a name="cfn-batch-computeenvironment-launchtemplatespecification-launchtemplatename"></a>
The name of the launch template.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Overrides`  <a name="cfn-batch-computeenvironment-launchtemplatespecification-overrides"></a>
A launch template to use in place of the default launch template. You must specify either the launch template ID or launch template name in the request, but not both.
You can specify up to ten (10) launch template overrides that are associated to unique instance types or families for each compute environment.
To unset all override templates for a compute environment, you can pass an empty array to the [UpdateComputeEnvironment.overrides](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) parameter, or not include the `overrides` parameter when submitting the `UpdateComputeEnvironment` API operation.
*Required*: No
*Type*: Array of [LaunchTemplateSpecificationOverride](aws-properties-batch-computeenvironment-launchtemplatespecificationoverride.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`UserdataType`  <a name="cfn-batch-computeenvironment-launchtemplatespecification-userdatatype"></a>
The EKS node initialization process to use. You only need to specify this value if you are using a custom AMI. The default value is `EKS_BOOTSTRAP_SH`. If *imageType* is a custom AMI based on EKS\_AL2023 or EKS\_AL2023\_NVIDIA then you must choose `EKS_NODEADM`.
*Required*: No
*Type*: String
*Allowed values*: `EKS_BOOTSTRAP_SH | EKS_NODEADM`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Version`  <a name="cfn-batch-computeenvironment-launchtemplatespecification-version"></a>
The version number of the launch template, `$Default`, or `$Latest`.
If the value is `$Default`, the default version of the launch template is used. If the value is `$Latest`, the latest version of the launch template is used.
If the AMI ID that's used in a compute environment is from the launch template, the AMI isn't changed when the compute environment is updated. It's only changed if the `updateToLatestImageVersion` parameter for the compute environment is set to `true`. During an infrastructure update, if either `$Default` or `$Latest` is specified, AWS Batch re-evaluates the launch template version, and it might use a different version of the launch template. This is the case even if the launch template isn't specified in the update. When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *AWS Batch User Guide*.
Default: `$Default`
Latest: `$Latest`
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also
<a name="aws-properties-batch-computeenvironment-launchtemplatespecification--seealso"></a>
+ [Launch Template Support](https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html) in the * AWS Batch User Guide *.
