---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-kubecontrollermanagerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster KubeControllerManagerConfig
<a name="aws-properties-eks-cluster-kubecontrollermanagerconfig"></a>

<a name="aws-properties-eks-cluster-kubecontrollermanagerconfig-description"></a>The `KubeControllerManagerConfig` property type specifies Property description not available. for an [AWS::EKS::Cluster](aws-resource-eks-cluster.md).

## Syntax
<a name="aws-properties-eks-cluster-kubecontrollermanagerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-kubecontrollermanagerconfig-syntax.json"></a>

```
{
  "[HorizontalPodAutoscalerControllerConfig](#cfn-eks-cluster-kubecontrollermanagerconfig-horizontalpodautoscalercontrollerconfig)" : {{HorizontalPodAutoscalerControllerConfig}},
  "[PodGcControllerConfig](#cfn-eks-cluster-kubecontrollermanagerconfig-podgccontrollerconfig)" : {{PodGcControllerConfig}}
}
```

### YAML
<a name="aws-properties-eks-cluster-kubecontrollermanagerconfig-syntax.yaml"></a>

```
  [HorizontalPodAutoscalerControllerConfig](#cfn-eks-cluster-kubecontrollermanagerconfig-horizontalpodautoscalercontrollerconfig): {{
    HorizontalPodAutoscalerControllerConfig}}
  [PodGcControllerConfig](#cfn-eks-cluster-kubecontrollermanagerconfig-podgccontrollerconfig): {{
    PodGcControllerConfig}}
```

## Properties
<a name="aws-properties-eks-cluster-kubecontrollermanagerconfig-properties"></a>

`HorizontalPodAutoscalerControllerConfig`  <a name="cfn-eks-cluster-kubecontrollermanagerconfig-horizontalpodautoscalercontrollerconfig"></a>
Property description not available.
*Required*: No
*Type*: [HorizontalPodAutoscalerControllerConfig](aws-properties-eks-cluster-horizontalpodautoscalercontrollerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PodGcControllerConfig`  <a name="cfn-eks-cluster-kubecontrollermanagerconfig-podgccontrollerconfig"></a>
Property description not available.
*Required*: No
*Type*: [PodGcControllerConfig](aws-properties-eks-cluster-podgccontrollerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
