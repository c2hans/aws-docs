---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-virtualcluster-containerinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::VirtualCluster ContainerInfo
<a name="aws-properties-emrcontainers-virtualcluster-containerinfo"></a>

The information about the container used for a job run or a managed endpoint.

## Syntax
<a name="aws-properties-emrcontainers-virtualcluster-containerinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-virtualcluster-containerinfo-syntax.json"></a>

```
{
  "[EksInfo](#cfn-emrcontainers-virtualcluster-containerinfo-eksinfo)" : {{EksInfo}}
}
```

### YAML
<a name="aws-properties-emrcontainers-virtualcluster-containerinfo-syntax.yaml"></a>

```
  [EksInfo](#cfn-emrcontainers-virtualcluster-containerinfo-eksinfo): {{
    EksInfo}}
```

## Properties
<a name="aws-properties-emrcontainers-virtualcluster-containerinfo-properties"></a>

`EksInfo`  <a name="cfn-emrcontainers-virtualcluster-containerinfo-eksinfo"></a>
The information about the Amazon EKS cluster.
*Required*: Yes
*Type*: [EksInfo](aws-properties-emrcontainers-virtualcluster-eksinfo.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
