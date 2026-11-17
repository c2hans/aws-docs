---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-extension-extensionnodesummary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Extension ExtensionNodeSummary
<a name="aws-properties-sagemaker-extension-extensionnodesummary"></a>

A summary of an extension's installation across the nodes of a SageMaker HyperPod cluster.

## Syntax
<a name="aws-properties-sagemaker-extension-extensionnodesummary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-extension-extensionnodesummary-syntax.json"></a>

```
{
  "[ActiveCount](#cfn-sagemaker-extension-extensionnodesummary-activecount)" : {{Integer}},
  "[TotalCount](#cfn-sagemaker-extension-extensionnodesummary-totalcount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-extension-extensionnodesummary-syntax.yaml"></a>

```
  [ActiveCount](#cfn-sagemaker-extension-extensionnodesummary-activecount): {{Integer}}
  [TotalCount](#cfn-sagemaker-extension-extensionnodesummary-totalcount): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-extension-extensionnodesummary-properties"></a>

`ActiveCount`  <a name="cfn-sagemaker-extension-extensionnodesummary-activecount"></a>
The number of nodes that are running the extension's current version and configuration. Nodes that report the extension as unhealthy aren't counted. While SageMaker HyperPod creates or updates the extension, `ActiveCount` is lower than `TotalCount`. To see why nodes aren't counted, see `Health` in `DescribeClusterExtension`.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalCount`  <a name="cfn-sagemaker-extension-extensionnodesummary-totalcount"></a>
The number of nodes in your cluster that the extension targets. SageMaker HyperPod targets every running node in your cluster, including nodes that you add after you create the extension.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
