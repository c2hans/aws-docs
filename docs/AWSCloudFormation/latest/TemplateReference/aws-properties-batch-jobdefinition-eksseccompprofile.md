---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-eksseccompprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EksSeccompProfile
<a name="aws-properties-batch-jobdefinition-eksseccompprofile"></a>

The Linux seccomp profile for a pod or container. For more information, see [Restrict a Container's Syscalls with seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/) in the *Kubernetes documentation*.

## Syntax
<a name="aws-properties-batch-jobdefinition-eksseccompprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-eksseccompprofile-syntax.json"></a>

```
{
  "[LocalhostProfile](#cfn-batch-jobdefinition-eksseccompprofile-localhostprofile)" : {{String}},
  "[Type](#cfn-batch-jobdefinition-eksseccompprofile-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-eksseccompprofile-syntax.yaml"></a>

```
  [LocalhostProfile](#cfn-batch-jobdefinition-eksseccompprofile-localhostprofile): {{String}}
  [Type](#cfn-batch-jobdefinition-eksseccompprofile-type): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-eksseccompprofile-properties"></a>

`LocalhostProfile`  <a name="cfn-batch-jobdefinition-eksseccompprofile-localhostprofile"></a>
The path of the profile on the node, relative to the configured seccomp profile location. You must specify this parameter when `type` is `Localhost`. Don't set this parameter for any other type. You are responsible for ensuring that the profile exists on every eligible worker node. For information about providing files to Amazon EKS nodes, see [Use a launch template with AWS Batch on Amazon EKS](https://docs.aws.amazon.com/batch/latest/userguide/eks-launch-templates.html) in the *AWS Batch User Guide*.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4095`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-batch-jobdefinition-eksseccompprofile-type"></a>
The seccomp profile type can be one of the following values:
RuntimeDefault
The `RuntimeDefault` value uses the container runtime's default seccomp profile.
Unconfined
The `Unconfined` value doesn't filter the container with seccomp.
Localhost
The `Localhost` value uses a custom profile at the path specified by `localhostProfile`.
*Required*: Yes
*Type*: String
*Allowed values*: `RuntimeDefault | Localhost | Unconfined`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
