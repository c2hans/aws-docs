---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-networkconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob NetworkConfig
<a name="aws-properties-sagemaker-processingjob-networkconfig"></a>

Networking options for a job, such as network traffic encryption between containers, whether to allow inbound and outbound network calls to and from containers, and the VPC subnets and security groups to use for VPC-enabled jobs.

## Syntax
<a name="aws-properties-sagemaker-processingjob-networkconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-networkconfig-syntax.json"></a>

```
{
  "[EnableInterContainerTrafficEncryption](#cfn-sagemaker-processingjob-networkconfig-enableintercontainertrafficencryption)" : {{Boolean}},
  "[EnableNetworkIsolation](#cfn-sagemaker-processingjob-networkconfig-enablenetworkisolation)" : {{Boolean}},
  "[VpcConfig](#cfn-sagemaker-processingjob-networkconfig-vpcconfig)" : {{VpcConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-networkconfig-syntax.yaml"></a>

```
  [EnableInterContainerTrafficEncryption](#cfn-sagemaker-processingjob-networkconfig-enableintercontainertrafficencryption): {{Boolean}}
  [EnableNetworkIsolation](#cfn-sagemaker-processingjob-networkconfig-enablenetworkisolation): {{Boolean}}
  [VpcConfig](#cfn-sagemaker-processingjob-networkconfig-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-networkconfig-properties"></a>

`EnableInterContainerTrafficEncryption`  <a name="cfn-sagemaker-processingjob-networkconfig-enableintercontainertrafficencryption"></a>
Whether to encrypt all communications between distributed processing jobs. Choose `True` to encrypt communications. Encryption provides greater security for distributed processing jobs, but the processing might take longer.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableNetworkIsolation`  <a name="cfn-sagemaker-processingjob-networkconfig-enablenetworkisolation"></a>
Whether to allow inbound and outbound network calls to and from the containers used for the processing job.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfig`  <a name="cfn-sagemaker-processingjob-networkconfig-vpcconfig"></a>
Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
*Required*: No
*Type*: [VpcConfig](aws-properties-sagemaker-processingjob-vpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
