---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-ekscontainerlinuxcapabilities.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EksContainerLinuxCapabilities
<a name="aws-properties-batch-jobdefinition-ekscontainerlinuxcapabilities"></a>

The Linux capabilities for the container. For more information, see [Set capabilities for a container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-capabilities-for-a-container) in the *Kubernetes documentation*.

## Syntax
<a name="aws-properties-batch-jobdefinition-ekscontainerlinuxcapabilities-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-ekscontainerlinuxcapabilities-syntax.json"></a>

```
{
  "[Add](#cfn-batch-jobdefinition-ekscontainerlinuxcapabilities-add)" : {{[ String, ... ]}},
  "[Drop](#cfn-batch-jobdefinition-ekscontainerlinuxcapabilities-drop)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-ekscontainerlinuxcapabilities-syntax.yaml"></a>

```
  [Add](#cfn-batch-jobdefinition-ekscontainerlinuxcapabilities-add): {{
    - String}}
  [Drop](#cfn-batch-jobdefinition-ekscontainerlinuxcapabilities-drop): {{
    - String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-ekscontainerlinuxcapabilities-properties"></a>

`Add`  <a name="cfn-batch-jobdefinition-ekscontainerlinuxcapabilities-add"></a>
The Linux capabilities to add to the default capability set for the container. This parameter contains up to 64 values. Specify capability names without the `CAP_` prefix.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Drop`  <a name="cfn-batch-jobdefinition-ekscontainerlinuxcapabilities-drop"></a>
The Linux capabilities to remove from the default capability set for the container. This parameter contains up to 64 values. Specify capability names without the `CAP_` prefix.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
