---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-ekscontainersecuritycontext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EksContainerSecurityContext
<a name="aws-properties-batch-jobdefinition-ekscontainersecuritycontext"></a>

The security context for a job. For more information, see [Configure a security context for a pod or container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) in the *Kubernetes documentation*.

## Syntax
<a name="aws-properties-batch-jobdefinition-ekscontainersecuritycontext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-ekscontainersecuritycontext-syntax.json"></a>

```
{
  "[AllowPrivilegeEscalation](#cfn-batch-jobdefinition-ekscontainersecuritycontext-allowprivilegeescalation)" : {{Boolean}},
  "[Privileged](#cfn-batch-jobdefinition-ekscontainersecuritycontext-privileged)" : {{Boolean}},
  "[ReadOnlyRootFilesystem](#cfn-batch-jobdefinition-ekscontainersecuritycontext-readonlyrootfilesystem)" : {{Boolean}},
  "[RunAsGroup](#cfn-batch-jobdefinition-ekscontainersecuritycontext-runasgroup)" : {{Integer}},
  "[RunAsNonRoot](#cfn-batch-jobdefinition-ekscontainersecuritycontext-runasnonroot)" : {{Boolean}},
  "[RunAsUser](#cfn-batch-jobdefinition-ekscontainersecuritycontext-runasuser)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-ekscontainersecuritycontext-syntax.yaml"></a>

```
  [AllowPrivilegeEscalation](#cfn-batch-jobdefinition-ekscontainersecuritycontext-allowprivilegeescalation): {{Boolean}}
  [Privileged](#cfn-batch-jobdefinition-ekscontainersecuritycontext-privileged): {{Boolean}}
  [ReadOnlyRootFilesystem](#cfn-batch-jobdefinition-ekscontainersecuritycontext-readonlyrootfilesystem): {{Boolean}}
  [RunAsGroup](#cfn-batch-jobdefinition-ekscontainersecuritycontext-runasgroup): {{Integer}}
  [RunAsNonRoot](#cfn-batch-jobdefinition-ekscontainersecuritycontext-runasnonroot): {{Boolean}}
  [RunAsUser](#cfn-batch-jobdefinition-ekscontainersecuritycontext-runasuser): {{Integer}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-ekscontainersecuritycontext-properties"></a>

`AllowPrivilegeEscalation`  <a name="cfn-batch-jobdefinition-ekscontainersecuritycontext-allowprivilegeescalation"></a>
Whether or not a container or a Kubernetes pod is allowed to gain more privileges than its parent process. The default value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Privileged`  <a name="cfn-batch-jobdefinition-ekscontainersecuritycontext-privileged"></a>
When this parameter is `true`, the container is given elevated permissions on the host container instance. The level of permissions are similar to the `root` user permissions. The default value is `false`. This parameter maps to `privileged` policy in the [Privileged pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#privileged) in the *Kubernetes documentation*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadOnlyRootFilesystem`  <a name="cfn-batch-jobdefinition-ekscontainersecuritycontext-readonlyrootfilesystem"></a>
When this parameter is `true`, the container is given read-only access to its root file system. The default value is `false`. This parameter maps to `ReadOnlyRootFilesystem` policy in the [Volumes and file systems pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#volumes-and-file-systems) in the *Kubernetes documentation*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RunAsGroup`  <a name="cfn-batch-jobdefinition-ekscontainersecuritycontext-runasgroup"></a>
When this parameter is specified, the container is run as the specified group ID (`gid`). If this parameter isn't specified, the default is the group that's specified in the image metadata. This parameter maps to `RunAsGroup` and `MustRunAs` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation*.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RunAsNonRoot`  <a name="cfn-batch-jobdefinition-ekscontainersecuritycontext-runasnonroot"></a>
When this parameter is specified, the container is run as a user with a `uid` other than 0. If this parameter isn't specified, so such rule is enforced. This parameter maps to `RunAsUser` and `MustRunAsNonRoot` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RunAsUser`  <a name="cfn-batch-jobdefinition-ekscontainersecuritycontext-runasuser"></a>
When this parameter is specified, the container is run as the specified user ID (`uid`). If this parameter isn't specified, the default is the user that's specified in the image metadata. This parameter maps to `RunAsUser` and `MustRanAs` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation*.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
