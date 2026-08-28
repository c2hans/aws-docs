---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-ekshostpath.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EksHostPath
<a name="aws-properties-batch-jobdefinition-ekshostpath"></a>

Specifies the configuration of a Kubernetes `hostPath` volume. A `hostPath` volume mounts an existing file or directory from the host node's filesystem into your pod. For more information, see [hostPath](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) in the *Kubernetes documentation*.

## Syntax
<a name="aws-properties-batch-jobdefinition-ekshostpath-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-ekshostpath-syntax.json"></a>

```
{
  "[Path](#cfn-batch-jobdefinition-ekshostpath-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-ekshostpath-syntax.yaml"></a>

```
  [Path](#cfn-batch-jobdefinition-ekshostpath-path): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-ekshostpath-properties"></a>

`Path`  <a name="cfn-batch-jobdefinition-ekshostpath-path"></a>
The path of the file or directory on the host to mount into containers on the pod.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
