---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-eksconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment EksConfiguration
<a name="aws-properties-batch-computeenvironment-eksconfiguration"></a>

Configuration for the Amazon EKS cluster that supports the AWS Batch compute environment. The cluster must exist before the compute environment can be created.

## Syntax
<a name="aws-properties-batch-computeenvironment-eksconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-eksconfiguration-syntax.json"></a>

```
{
  "[AccessEntry](#cfn-batch-computeenvironment-eksconfiguration-accessentry)" : {{EksAccessEntry}},
  "[EksClusterArn](#cfn-batch-computeenvironment-eksconfiguration-eksclusterarn)" : {{String}},
  "[KubernetesNamespace](#cfn-batch-computeenvironment-eksconfiguration-kubernetesnamespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-eksconfiguration-syntax.yaml"></a>

```
  [AccessEntry](#cfn-batch-computeenvironment-eksconfiguration-accessentry): {{
    EksAccessEntry}}
  [EksClusterArn](#cfn-batch-computeenvironment-eksconfiguration-eksclusterarn): {{String}}
  [KubernetesNamespace](#cfn-batch-computeenvironment-eksconfiguration-kubernetesnamespace): {{String}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-eksconfiguration-properties"></a>

`AccessEntry`  <a name="cfn-batch-computeenvironment-eksconfiguration-accessentry"></a>
The AWS Batch-managed Amazon EKS access entry for the compute environment. Set `desiredState` to declare whether AWS Batch manages an access entry on the cluster.
In AWS CloudFormation templates, if you omit the `accessEntry` field entirely, AWS Batch applies `INHERIT_FROM_CLUSTER` as the default `desiredState`. Whether the entry is provisioned on the cluster depends on the cluster's `authenticationMode` and the `desiredState` recorded for each AWS Batch compute environment targeting the cluster. For more information, see [Amazon EKS access entry authentication](https://docs.aws.amazon.com/batch/latest/userguide/eks-access-entries.html) in the *AWS Batch User Guide*.
*Required*: No
*Type*: [EksAccessEntry](aws-properties-batch-computeenvironment-eksaccessentry.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EksClusterArn`  <a name="cfn-batch-computeenvironment-eksconfiguration-eksclusterarn"></a>
The Amazon Resource Name (ARN) of the Amazon EKS cluster. An example is `arn:aws:eks:us-east-1:123456789012:cluster/ClusterForBatch`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KubernetesNamespace`  <a name="cfn-batch-computeenvironment-eksconfiguration-kubernetesnamespace"></a>
The namespace of the Amazon EKS cluster. AWS Batch manages pods in this namespace. The value can't left empty or null. It must be fewer than 64 characters long, can't be set to `default`, can't start with "`kube-`," and must match this regular expression: `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`. For more information, see [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in the Kubernetes documentation.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
