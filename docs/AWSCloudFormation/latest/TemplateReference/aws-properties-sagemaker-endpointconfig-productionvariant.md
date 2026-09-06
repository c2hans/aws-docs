---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-productionvariant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig ProductionVariant
<a name="aws-properties-sagemaker-endpointconfig-productionvariant"></a>

Specifies a model that you want to host and the resources to deploy for hosting it. If you are deploying multiple models, tell Amazon SageMaker how to distribute traffic among the models by specifying the `InitialVariantWeight` objects.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-productionvariant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-productionvariant-syntax.json"></a>

```
{
  "[CapacityReservationConfig](#cfn-sagemaker-endpointconfig-productionvariant-capacityreservationconfig)" : {{CapacityReservationConfig}},
  "[ContainerStartupHealthCheckTimeoutInSeconds](#cfn-sagemaker-endpointconfig-productionvariant-containerstartuphealthchecktimeoutinseconds)" : {{Integer}},
  "[CoreDumpConfig](#cfn-sagemaker-endpointconfig-productionvariant-coredumpconfig)" : {{CoreDumpConfig}},
  "[EnableSSMAccess](#cfn-sagemaker-endpointconfig-productionvariant-enablessmaccess)" : {{Boolean}},
  "[InferenceAmiVersion](#cfn-sagemaker-endpointconfig-productionvariant-inferenceamiversion)" : {{String}},
  "[InitialInstanceCount](#cfn-sagemaker-endpointconfig-productionvariant-initialinstancecount)" : {{Integer}},
  "[InitialVariantWeight](#cfn-sagemaker-endpointconfig-productionvariant-initialvariantweight)" : {{Number}},
  "[InstancePools](#cfn-sagemaker-endpointconfig-productionvariant-instancepools)" : {{[ InstancePool, ... ]}},
  "[InstanceType](#cfn-sagemaker-endpointconfig-productionvariant-instancetype)" : {{String}},
  "[ManagedInstanceScaling](#cfn-sagemaker-endpointconfig-productionvariant-managedinstancescaling)" : {{ManagedInstanceScaling}},
  "[ModelDataDownloadTimeoutInSeconds](#cfn-sagemaker-endpointconfig-productionvariant-modeldatadownloadtimeoutinseconds)" : {{Integer}},
  "[ModelName](#cfn-sagemaker-endpointconfig-productionvariant-modelname)" : {{String}},
  "[RoutingConfig](#cfn-sagemaker-endpointconfig-productionvariant-routingconfig)" : {{RoutingConfig}},
  "[ServerlessConfig](#cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig)" : {{ServerlessConfig}},
  "[VariantInstanceProvisionTimeoutInSeconds](#cfn-sagemaker-endpointconfig-productionvariant-variantinstanceprovisiontimeoutinseconds)" : {{Integer}},
  "[VariantName](#cfn-sagemaker-endpointconfig-productionvariant-variantname)" : {{String}},
  "[VolumeSizeInGB](#cfn-sagemaker-endpointconfig-productionvariant-volumesizeingb)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-productionvariant-syntax.yaml"></a>

```
  [CapacityReservationConfig](#cfn-sagemaker-endpointconfig-productionvariant-capacityreservationconfig): {{
    CapacityReservationConfig}}
  [ContainerStartupHealthCheckTimeoutInSeconds](#cfn-sagemaker-endpointconfig-productionvariant-containerstartuphealthchecktimeoutinseconds): {{Integer}}
  [CoreDumpConfig](#cfn-sagemaker-endpointconfig-productionvariant-coredumpconfig): {{
    CoreDumpConfig}}
  [EnableSSMAccess](#cfn-sagemaker-endpointconfig-productionvariant-enablessmaccess): {{Boolean}}
  [InferenceAmiVersion](#cfn-sagemaker-endpointconfig-productionvariant-inferenceamiversion): {{String}}
  [InitialInstanceCount](#cfn-sagemaker-endpointconfig-productionvariant-initialinstancecount): {{Integer}}
  [InitialVariantWeight](#cfn-sagemaker-endpointconfig-productionvariant-initialvariantweight): {{Number}}
  [InstancePools](#cfn-sagemaker-endpointconfig-productionvariant-instancepools): {{
    - InstancePool}}
  [InstanceType](#cfn-sagemaker-endpointconfig-productionvariant-instancetype): {{String}}
  [ManagedInstanceScaling](#cfn-sagemaker-endpointconfig-productionvariant-managedinstancescaling): {{
    ManagedInstanceScaling}}
  [ModelDataDownloadTimeoutInSeconds](#cfn-sagemaker-endpointconfig-productionvariant-modeldatadownloadtimeoutinseconds): {{Integer}}
  [ModelName](#cfn-sagemaker-endpointconfig-productionvariant-modelname): {{String}}
  [RoutingConfig](#cfn-sagemaker-endpointconfig-productionvariant-routingconfig): {{
    RoutingConfig}}
  [ServerlessConfig](#cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig): {{
    ServerlessConfig}}
  [VariantInstanceProvisionTimeoutInSeconds](#cfn-sagemaker-endpointconfig-productionvariant-variantinstanceprovisiontimeoutinseconds): {{Integer}}
  [VariantName](#cfn-sagemaker-endpointconfig-productionvariant-variantname): {{String}}
  [VolumeSizeInGB](#cfn-sagemaker-endpointconfig-productionvariant-volumesizeingb): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-productionvariant-properties"></a>

`CapacityReservationConfig`  <a name="cfn-sagemaker-endpointconfig-productionvariant-capacityreservationconfig"></a>
Settings for the capacity reservation for the compute instances that SageMaker AI reserves for an endpoint.
*Required*: No
*Type*: [CapacityReservationConfig](aws-properties-sagemaker-endpointconfig-capacityreservationconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerStartupHealthCheckTimeoutInSeconds`  <a name="cfn-sagemaker-endpointconfig-productionvariant-containerstartuphealthchecktimeoutinseconds"></a>
The timeout value, in seconds, for your inference container to pass health check by SageMaker Hosting. For more information about health check, see [How Your Container Should Respond to Health Check (Ping) Requests](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-ping-requests).
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `3600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CoreDumpConfig`  <a name="cfn-sagemaker-endpointconfig-productionvariant-coredumpconfig"></a>
Specifies configuration for a core dump from the model container when the process crashes.
*Required*: No
*Type*: [CoreDumpConfig](aws-properties-sagemaker-endpointconfig-coredumpconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableSSMAccess`  <a name="cfn-sagemaker-endpointconfig-productionvariant-enablessmaccess"></a>
 You can use this parameter to turn on native AWS Systems Manager (SSM) access for a production variant behind an endpoint. By default, SSM access is disabled for all production variants behind an endpoint. You can turn on or turn off SSM access for a production variant behind an existing endpoint by creating a new endpoint configuration and calling `UpdateEndpoint`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InferenceAmiVersion`  <a name="cfn-sagemaker-endpointconfig-productionvariant-inferenceamiversion"></a>
Specifies an option from a collection of preconfigured Amazon Machine Image (AMI) images. Each image is configured by AWS with a set of software and driver versions. AWS optimizes these configurations for different machine learning workloads.
By selecting an AMI version, you can ensure that your inference environment is compatible with specific software requirements, such as CUDA driver versions, Linux kernel versions, or AWS Neuron driver versions.
The AMI version names, and their configurations, are the following:
al2-ami-sagemaker-inference-gpu-2
+ Accelerator: GPU
+ NVIDIA driver version: 535
+ CUDA version: 12.2
al2-ami-sagemaker-inference-gpu-2-1
+ Accelerator: GPU
+ NVIDIA driver version: 535
+ CUDA version: 12.2
+ NVIDIA Container Toolkit with disabled CUDA-compat mounting
al2-ami-sagemaker-inference-gpu-3-1
+ Accelerator: GPU
+ NVIDIA driver version: 550
+ CUDA version: 12.4
+ NVIDIA Container Toolkit with disabled CUDA-compat mounting
al2023-ami-sagemaker-inference-gpu-4-1
+ Accelerator: GPU
+ NVIDIA driver version: 580
+ CUDA version: 13.0
+ NVIDIA Container Toolkit with disabled CUDA-compat mounting
al2-ami-sagemaker-inference-neuron-2
+ Accelerator: Inferentia2 and Trainium
+ Neuron driver version: 2.19
*Required*: No
*Type*: String
*Allowed values*: `al2-ami-sagemaker-inference-gpu-2 | al2-ami-sagemaker-inference-gpu-2-1 | al2-ami-sagemaker-inference-gpu-3-1 | al2-ami-sagemaker-inference-neuron-2 | al2023-ami-sagemaker-inference-gpu-4-1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InitialInstanceCount`  <a name="cfn-sagemaker-endpointconfig-productionvariant-initialinstancecount"></a>
Number of instances to launch initially.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InitialVariantWeight`  <a name="cfn-sagemaker-endpointconfig-productionvariant-initialvariantweight"></a>
Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the `VariantWeight` to the sum of all `VariantWeight` values across all ProductionVariants. If unspecified, it defaults to 1.0.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstancePools`  <a name="cfn-sagemaker-endpointconfig-productionvariant-instancepools"></a>
A list of instance pools for the production variant. Each instance pool specifies an instance type and its priority for provisioning. Use instance pools to configure heterogeneous endpoints that deploy models across multiple instance types.
*Required*: No
*Type*: Array of [InstancePool](aws-properties-sagemaker-endpointconfig-instancepool.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceType`  <a name="cfn-sagemaker-endpointconfig-productionvariant-instancetype"></a>
The ML compute instance type.
*Required*: No
*Type*: String
*Allowed values*: `ml.t2.medium | ml.t2.large | ml.t2.xlarge | ml.t2.2xlarge | ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.m5d.large | ml.m5d.xlarge | ml.m5d.2xlarge | ml.m5d.4xlarge | ml.m5d.12xlarge | ml.m5d.24xlarge | ml.c4.large | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5d.large | ml.c5d.xlarge | ml.c5d.2xlarge | ml.c5d.4xlarge | ml.c5d.9xlarge | ml.c5d.18xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.12xlarge | ml.r5.24xlarge | ml.r5d.large | ml.r5d.xlarge | ml.r5d.2xlarge | ml.r5d.4xlarge | ml.r5d.12xlarge | ml.r5d.24xlarge | ml.inf1.xlarge | ml.inf1.2xlarge | ml.inf1.6xlarge | ml.inf1.24xlarge | ml.dl1.24xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.r8g.medium | ml.r8g.large | ml.r8g.xlarge | ml.r8g.2xlarge | ml.r8g.4xlarge | ml.r8g.8xlarge | ml.r8g.12xlarge | ml.r8g.16xlarge | ml.r8g.24xlarge | ml.r8g.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge | ml.p4d.24xlarge | ml.c7g.large | ml.c7g.xlarge | ml.c7g.2xlarge | ml.c7g.4xlarge | ml.c7g.8xlarge | ml.c7g.12xlarge | ml.c7g.16xlarge | ml.m6g.large | ml.m6g.xlarge | ml.m6g.2xlarge | ml.m6g.4xlarge | ml.m6g.8xlarge | ml.m6g.12xlarge | ml.m6g.16xlarge | ml.m6gd.large | ml.m6gd.xlarge | ml.m6gd.2xlarge | ml.m6gd.4xlarge | ml.m6gd.8xlarge | ml.m6gd.12xlarge | ml.m6gd.16xlarge | ml.c6g.large | ml.c6g.xlarge | ml.c6g.2xlarge | ml.c6g.4xlarge | ml.c6g.8xlarge | ml.c6g.12xlarge | ml.c6g.16xlarge | ml.c6gd.large | ml.c6gd.xlarge | ml.c6gd.2xlarge | ml.c6gd.4xlarge | ml.c6gd.8xlarge | ml.c6gd.12xlarge | ml.c6gd.16xlarge | ml.c6gn.large | ml.c6gn.xlarge | ml.c6gn.2xlarge | ml.c6gn.4xlarge | ml.c6gn.8xlarge | ml.c6gn.12xlarge | ml.c6gn.16xlarge | ml.r6g.large | ml.r6g.xlarge | ml.r6g.2xlarge | ml.r6g.4xlarge | ml.r6g.8xlarge | ml.r6g.12xlarge | ml.r6g.16xlarge | ml.r6gd.large | ml.r6gd.xlarge | ml.r6gd.2xlarge | ml.r6gd.4xlarge | ml.r6gd.8xlarge | ml.r6gd.12xlarge | ml.r6gd.16xlarge | ml.p4de.24xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.trn2.48xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.c8g.medium | ml.c8g.large | ml.c8g.xlarge | ml.c8g.2xlarge | ml.c8g.4xlarge | ml.c8g.8xlarge | ml.c8g.12xlarge | ml.c8g.16xlarge | ml.c8g.24xlarge | ml.c8g.48xlarge | ml.r7gd.medium | ml.r7gd.large | ml.r7gd.xlarge | ml.r7gd.2xlarge | ml.r7gd.4xlarge | ml.r7gd.8xlarge | ml.r7gd.12xlarge | ml.r7gd.16xlarge | ml.m8g.medium | ml.m8g.large | ml.m8g.xlarge | ml.m8g.2xlarge | ml.m8g.4xlarge | ml.m8g.8xlarge | ml.m8g.12xlarge | ml.m8g.16xlarge | ml.m8g.24xlarge | ml.m8g.48xlarge | ml.c6in.large | ml.c6in.xlarge | ml.c6in.2xlarge | ml.c6in.4xlarge | ml.c6in.8xlarge | ml.c6in.12xlarge | ml.c6in.16xlarge | ml.c6in.24xlarge | ml.c6in.32xlarge | ml.p6-b200.48xlarge | ml.p6-b300.48xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManagedInstanceScaling`  <a name="cfn-sagemaker-endpointconfig-productionvariant-managedinstancescaling"></a>
Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic.
*Required*: No
*Type*: [ManagedInstanceScaling](aws-properties-sagemaker-endpointconfig-managedinstancescaling.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelDataDownloadTimeoutInSeconds`  <a name="cfn-sagemaker-endpointconfig-productionvariant-modeldatadownloadtimeoutinseconds"></a>
The timeout value, in seconds, to download and extract the model that you want to host from Amazon S3 to the individual inference instance associated with this production variant.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `3600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelName`  <a name="cfn-sagemaker-endpointconfig-productionvariant-modelname"></a>
The name of the model that you want to host. This is the name that you specified when creating the model.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoutingConfig`  <a name="cfn-sagemaker-endpointconfig-productionvariant-routingconfig"></a>
Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.
*Required*: No
*Type*: [RoutingConfig](aws-properties-sagemaker-endpointconfig-routingconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServerlessConfig`  <a name="cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig"></a>
The serverless configuration for an endpoint. Specifies a serverless endpoint configuration instead of an instance-based endpoint configuration.
*Required*: No
*Type*: [ServerlessConfig](aws-properties-sagemaker-endpointconfig-serverlessconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VariantInstanceProvisionTimeoutInSeconds`  <a name="cfn-sagemaker-endpointconfig-productionvariant-variantinstanceprovisiontimeoutinseconds"></a>
The timeout value, in seconds, for provisioning instances for the production variant. When SageMaker encounters an insufficient capacity error while provisioning instances, it retries with the next instance pool (if configured) or waits until the timeout expires. This timeout applies only to capacity provisioning and does not include the time for model download or container startup.
Valid values: 300 to 3600.
*Required*: No
*Type*: Integer
*Minimum*: `300`
*Maximum*: `3600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VariantName`  <a name="cfn-sagemaker-endpointconfig-productionvariant-variantname"></a>
The name of the production variant.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeSizeInGB`  <a name="cfn-sagemaker-endpointconfig-productionvariant-volumesizeingb"></a>
The size, in GB, of the ML storage volume attached to individual inference instance associated with the production variant. Currently only Amazon EBS gp2 storage volumes are supported.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
