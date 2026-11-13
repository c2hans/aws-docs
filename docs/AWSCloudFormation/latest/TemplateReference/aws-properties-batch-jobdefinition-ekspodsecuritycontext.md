---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-ekspodsecuritycontext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EksPodSecurityContext
<a name="aws-properties-batch-jobdefinition-ekspodsecuritycontext"></a>

The security context for the pod. The settings apply to all containers in the pod when the container does not specify an overriding value. For more information, see [Set the security context for a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod) in the *Kubernetes documentation*.

## Syntax
<a name="aws-properties-batch-jobdefinition-ekspodsecuritycontext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-ekspodsecuritycontext-syntax.json"></a>

```
{
  "[FsGroup](#cfn-batch-jobdefinition-ekspodsecuritycontext-fsgroup)" : {{Integer}},
  "[RunAsGroup](#cfn-batch-jobdefinition-ekspodsecuritycontext-runasgroup)" : {{Integer}},
  "[RunAsNonRoot](#cfn-batch-jobdefinition-ekspodsecuritycontext-runasnonroot)" : {{Boolean}},
  "[RunAsUser](#cfn-batch-jobdefinition-ekspodsecuritycontext-runasuser)" : {{Integer}},
  "[SeccompProfile](#cfn-batch-jobdefinition-ekspodsecuritycontext-seccompprofile)" : {{EksSeccompProfile}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-ekspodsecuritycontext-syntax.yaml"></a>

```
  [FsGroup](#cfn-batch-jobdefinition-ekspodsecuritycontext-fsgroup): {{Integer}}
  [RunAsGroup](#cfn-batch-jobdefinition-ekspodsecuritycontext-runasgroup): {{Integer}}
  [RunAsNonRoot](#cfn-batch-jobdefinition-ekspodsecuritycontext-runasnonroot): {{Boolean}}
  [RunAsUser](#cfn-batch-jobdefinition-ekspodsecuritycontext-runasuser): {{Integer}}
  [SeccompProfile](#cfn-batch-jobdefinition-ekspodsecuritycontext-seccompprofile): {{
    EksSeccompProfile}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-ekspodsecuritycontext-properties"></a>

`FsGroup`  <a name="cfn-batch-jobdefinition-ekspodsecuritycontext-fsgroup"></a>
A special supplemental group that is applied to all containers in the pod. Some volume types allow Kubernetes to change the ownership and permissions of the volume contents to this group when the volume is mounted. The supported value range is `0` through `2147483647`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RunAsGroup`  <a name="cfn-batch-jobdefinition-ekspodsecuritycontext-runasgroup"></a>
The primary group ID that runs containers in the pod when a container does not specify its own group ID. The supported value range is `0` through `2147483647`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RunAsNonRoot`  <a name="cfn-batch-jobdefinition-ekspodsecuritycontext-runasnonroot"></a>
Specifies whether Kubernetes validates that containers in the pod don't run as the root user unless a container specifies an overriding value.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RunAsUser`  <a name="cfn-batch-jobdefinition-ekspodsecuritycontext-runasuser"></a>
The user ID that runs containers in the pod when a container does not specify its own user ID. The supported value range is `0` through `2147483647`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SeccompProfile`  <a name="cfn-batch-jobdefinition-ekspodsecuritycontext-seccompprofile"></a>
The default seccomp profile for containers in the pod. A container-level seccomp profile overrides this value.
*Required*: No
*Type*: [EksSeccompProfile](aws-properties-batch-jobdefinition-eksseccompprofile.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
