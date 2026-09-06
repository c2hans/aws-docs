---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-clusterlogging.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ClusterLogging
<a name="aws-properties-eks-cluster-clusterlogging"></a>

The cluster control plane logging configuration for your cluster.

**Important**
When updating a resource, you must include this `ClusterLogging` property if the previous CloudFormation template of the resource had it.

## Syntax
<a name="aws-properties-eks-cluster-clusterlogging-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-clusterlogging-syntax.json"></a>

```
{
  "[EnabledTypes](#cfn-eks-cluster-clusterlogging-enabledtypes)" : {{[ LoggingTypeConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-eks-cluster-clusterlogging-syntax.yaml"></a>

```
  [EnabledTypes](#cfn-eks-cluster-clusterlogging-enabledtypes): {{
    - LoggingTypeConfig}}
```

## Properties
<a name="aws-properties-eks-cluster-clusterlogging-properties"></a>

`EnabledTypes`  <a name="cfn-eks-cluster-clusterlogging-enabledtypes"></a>
The enabled control plane logs for your cluster. All log types are disabled if the array is empty.
When updating a resource, you must include this `EnabledTypes` property if the previous CloudFormation template of the resource had it.
*Required*: No
*Type*: Array of [LoggingTypeConfig](aws-properties-eks-cluster-loggingtypeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
