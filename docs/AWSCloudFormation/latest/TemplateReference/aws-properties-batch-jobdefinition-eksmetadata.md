---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-eksmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EksMetadata
<a name="aws-properties-batch-jobdefinition-eksmetadata"></a>

Describes and uniquely identifies Kubernetes resources. For example, the compute environment that a pod runs in or the `jobID` for a job running in the pod. For more information, see [ Understanding Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) in the *Kubernetes documentation*.

## Syntax
<a name="aws-properties-batch-jobdefinition-eksmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-eksmetadata-syntax.json"></a>

```
{
  "[Annotations](#cfn-batch-jobdefinition-eksmetadata-annotations)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Labels](#cfn-batch-jobdefinition-eksmetadata-labels)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Namespace](#cfn-batch-jobdefinition-eksmetadata-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-eksmetadata-syntax.yaml"></a>

```
  [Annotations](#cfn-batch-jobdefinition-eksmetadata-annotations): {{
    {{Key}}: {{Value}}}}
  [Labels](#cfn-batch-jobdefinition-eksmetadata-labels): {{
    {{Key}}: {{Value}}}}
  [Namespace](#cfn-batch-jobdefinition-eksmetadata-namespace): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-eksmetadata-properties"></a>

`Annotations`  <a name="cfn-batch-jobdefinition-eksmetadata-annotations"></a>
Key-value pairs used to attach arbitrary, non-identifying metadata to Kubernetes objects. Valid annotation keys have two segments: an optional prefix and a name, separated by a slash (/).
+ The prefix is optional and must be 253 characters or less. If specified, the prefix must be a DNS subdomain− a series of DNS labels separated by dots (.), and it must end with a slash (/).
+ The name segment is required and must be 63 characters or less. It can include alphanumeric characters ([a-z0-9A-Z]), dashes (-), underscores (\_), and dots (.), but must begin and end with an alphanumeric character.
Annotation values must be 255 characters or less.
Annotations can be added or modified at any time. Each resource can have multiple annotations.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Labels`  <a name="cfn-batch-jobdefinition-eksmetadata-labels"></a>
Key-value pairs used to identify, sort, and organize cube resources. Can contain up to 63 uppercase letters, lowercase letters, numbers, hyphens (-), and underscores (\_). Labels can be added or modified at any time. Each resource can have multiple labels, but each key must be unique for a given object.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-batch-jobdefinition-eksmetadata-namespace"></a>
The namespace of the Amazon EKS cluster. In Kubernetes, namespaces provide a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. AWS Batch places Batch Job pods in this namespace. If this field is provided, the value can't be empty or null. It must meet the following requirements:
+ 1-63 characters long
+ Can't be set to default
+ Can't start with `kube`
+ Must match the following regular expression: `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`
 For more information, see [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in the *Kubernetes documentation*. This namespace can be different from the `kubernetesNamespace` set in the compute environment's `EksConfiguration`, but must have identical role-based access control (RBAC) roles as the compute environment's `kubernetesNamespace`. For multi-node parallel jobs, the same value must be provided across all the node ranges.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
