---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusternetworkinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterNetworkInterface
<a name="aws-properties-sagemaker-cluster-clusternetworkinterface"></a>

The network interface configuration for a Amazon SageMaker HyperPod cluster instance group.

## Syntax
<a name="aws-properties-sagemaker-cluster-clusternetworkinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusternetworkinterface-syntax.json"></a>

```
{
  "[InterfaceType](#cfn-sagemaker-cluster-clusternetworkinterface-interfacetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusternetworkinterface-syntax.yaml"></a>

```
  [InterfaceType](#cfn-sagemaker-cluster-clusternetworkinterface-interfacetype): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusternetworkinterface-properties"></a>

`InterfaceType`  <a name="cfn-sagemaker-cluster-clusternetworkinterface-interfacetype"></a>
The type of network interface for the instance group. Valid values:
+ `efa` – An EFA with ENA interface, which provides both the EFA device for low-latency, high-throughput communication and the ENA device for IP networking.
+ `efa-only` – An EFA-only interface, which provides only the EFA device capabilities without the ENA device for traditional IP networking.
For more information, see [Elastic Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html).
*Required*: Yes
*Type*: String
*Allowed values*: `efa | efa-only`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
