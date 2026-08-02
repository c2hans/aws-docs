---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariant.html
---

# ProductionVariant
<a name="API_ProductionVariant"></a>

 Identifies a model that you want to host and the resources chosen to deploy for hosting it. If you are deploying multiple models, tell SageMaker how to distribute traffic among the models by specifying variant weights. For more information on production variants, check [ Production variants](https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html).

## Contents
<a name="API_ProductionVariant_Contents"></a>

 ** VariantName **   <a name="sagemaker-Type-ProductionVariant-VariantName"></a>
The name of the production variant.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** AcceleratorType **   <a name="sagemaker-Type-ProductionVariant-AcceleratorType"></a>
This parameter is no longer supported. Elastic Inference (EI) is no longer available.
This parameter was used to specify the size of the EI instance to use for the production variant.
Type: String
Valid Values: `ml.eia1.medium | ml.eia1.large | ml.eia1.xlarge | ml.eia2.medium | ml.eia2.large | ml.eia2.xlarge`
Required: No

 ** CapacityReservationConfig **   <a name="sagemaker-Type-ProductionVariant-CapacityReservationConfig"></a>
Settings for the capacity reservation for the compute instances that SageMaker AI reserves for an endpoint.
Type: [ProductionVariantCapacityReservationConfig](API_ProductionVariantCapacityReservationConfig.md) object
Required: No

 ** ContainerStartupHealthCheckTimeoutInSeconds **   <a name="sagemaker-Type-ProductionVariant-ContainerStartupHealthCheckTimeoutInSeconds"></a>
The timeout value, in seconds, for your inference container to pass health check by SageMaker Hosting. For more information about health check, see [How Your Container Should Respond to Health Check (Ping) Requests](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-ping-requests).
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 3600.
Required: No

 ** CoreDumpConfig **   <a name="sagemaker-Type-ProductionVariant-CoreDumpConfig"></a>
Specifies configuration for a core dump from the model container when the process crashes.
Type: [ProductionVariantCoreDumpConfig](API_ProductionVariantCoreDumpConfig.md) object
Required: No

 ** EnableSSMAccess **   <a name="sagemaker-Type-ProductionVariant-EnableSSMAccess"></a>
 You can use this parameter to turn on native AWS Systems Manager (SSM) access for a production variant behind an endpoint. By default, SSM access is disabled for all production variants behind an endpoint. You can turn on or turn off SSM access for a production variant behind an existing endpoint by creating a new endpoint configuration and calling `UpdateEndpoint`.
Type: Boolean
Required: No

 ** InferenceAmiVersion **   <a name="sagemaker-Type-ProductionVariant-InferenceAmiVersion"></a>
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
Type: String
Valid Values: `al2-ami-sagemaker-inference-gpu-2 | al2-ami-sagemaker-inference-gpu-2-1 | al2-ami-sagemaker-inference-gpu-3-1 | al2-ami-sagemaker-inference-neuron-2 | al2023-ami-sagemaker-inference-gpu-4-1`
Required: No

 ** InitialInstanceCount **   <a name="sagemaker-Type-ProductionVariant-InitialInstanceCount"></a>
Number of instances to launch initially.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** InitialVariantWeight **   <a name="sagemaker-Type-ProductionVariant-InitialVariantWeight"></a>
Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the `VariantWeight` to the sum of all `VariantWeight` values across all ProductionVariants. If unspecified, it defaults to 1.0.
Type: Float
Valid Range: Minimum value of 0.
Required: No

 ** InstancePools **   <a name="sagemaker-Type-ProductionVariant-InstancePools"></a>
A list of instance pools for the production variant. Each instance pool specifies an instance type and its priority for provisioning. Use instance pools to configure heterogeneous endpoints that deploy models across multiple instance types.
Type: Array of [InstancePool](API_InstancePool.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** InstanceType **   <a name="sagemaker-Type-ProductionVariant-InstanceType"></a>
The ML compute instance type.
Type: String
Valid Values: `ml.t2.medium | ml.t2.large | ml.t2.xlarge | ml.t2.2xlarge | ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.m5d.large | ml.m5d.xlarge | ml.m5d.2xlarge | ml.m5d.4xlarge | ml.m5d.12xlarge | ml.m5d.24xlarge | ml.c4.large | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5d.large | ml.c5d.xlarge | ml.c5d.2xlarge | ml.c5d.4xlarge | ml.c5d.9xlarge | ml.c5d.18xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.12xlarge | ml.r5.24xlarge | ml.r5d.large | ml.r5d.xlarge | ml.r5d.2xlarge | ml.r5d.4xlarge | ml.r5d.12xlarge | ml.r5d.24xlarge | ml.inf1.xlarge | ml.inf1.2xlarge | ml.inf1.6xlarge | ml.inf1.24xlarge | ml.dl1.24xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.r8g.medium | ml.r8g.large | ml.r8g.xlarge | ml.r8g.2xlarge | ml.r8g.4xlarge | ml.r8g.8xlarge | ml.r8g.12xlarge | ml.r8g.16xlarge | ml.r8g.24xlarge | ml.r8g.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge | ml.p4d.24xlarge | ml.c7g.large | ml.c7g.xlarge | ml.c7g.2xlarge | ml.c7g.4xlarge | ml.c7g.8xlarge | ml.c7g.12xlarge | ml.c7g.16xlarge | ml.m6g.large | ml.m6g.xlarge | ml.m6g.2xlarge | ml.m6g.4xlarge | ml.m6g.8xlarge | ml.m6g.12xlarge | ml.m6g.16xlarge | ml.m6gd.large | ml.m6gd.xlarge | ml.m6gd.2xlarge | ml.m6gd.4xlarge | ml.m6gd.8xlarge | ml.m6gd.12xlarge | ml.m6gd.16xlarge | ml.c6g.large | ml.c6g.xlarge | ml.c6g.2xlarge | ml.c6g.4xlarge | ml.c6g.8xlarge | ml.c6g.12xlarge | ml.c6g.16xlarge | ml.c6gd.large | ml.c6gd.xlarge | ml.c6gd.2xlarge | ml.c6gd.4xlarge | ml.c6gd.8xlarge | ml.c6gd.12xlarge | ml.c6gd.16xlarge | ml.c6gn.large | ml.c6gn.xlarge | ml.c6gn.2xlarge | ml.c6gn.4xlarge | ml.c6gn.8xlarge | ml.c6gn.12xlarge | ml.c6gn.16xlarge | ml.r6g.large | ml.r6g.xlarge | ml.r6g.2xlarge | ml.r6g.4xlarge | ml.r6g.8xlarge | ml.r6g.12xlarge | ml.r6g.16xlarge | ml.r6gd.large | ml.r6gd.xlarge | ml.r6gd.2xlarge | ml.r6gd.4xlarge | ml.r6gd.8xlarge | ml.r6gd.12xlarge | ml.r6gd.16xlarge | ml.p4de.24xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.trn2.48xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.c8g.medium | ml.c8g.large | ml.c8g.xlarge | ml.c8g.2xlarge | ml.c8g.4xlarge | ml.c8g.8xlarge | ml.c8g.12xlarge | ml.c8g.16xlarge | ml.c8g.24xlarge | ml.c8g.48xlarge | ml.r7gd.medium | ml.r7gd.large | ml.r7gd.xlarge | ml.r7gd.2xlarge | ml.r7gd.4xlarge | ml.r7gd.8xlarge | ml.r7gd.12xlarge | ml.r7gd.16xlarge | ml.m8g.medium | ml.m8g.large | ml.m8g.xlarge | ml.m8g.2xlarge | ml.m8g.4xlarge | ml.m8g.8xlarge | ml.m8g.12xlarge | ml.m8g.16xlarge | ml.m8g.24xlarge | ml.m8g.48xlarge | ml.c6in.large | ml.c6in.xlarge | ml.c6in.2xlarge | ml.c6in.4xlarge | ml.c6in.8xlarge | ml.c6in.12xlarge | ml.c6in.16xlarge | ml.c6in.24xlarge | ml.c6in.32xlarge | ml.p6-b200.48xlarge | ml.p6-b300.48xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge`
Required: No

 ** ManagedInstanceScaling **   <a name="sagemaker-Type-ProductionVariant-ManagedInstanceScaling"></a>
Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic.
Type: [ProductionVariantManagedInstanceScaling](API_ProductionVariantManagedInstanceScaling.md) object
Required: No

 ** ModelDataDownloadTimeoutInSeconds **   <a name="sagemaker-Type-ProductionVariant-ModelDataDownloadTimeoutInSeconds"></a>
The timeout value, in seconds, to download and extract the model that you want to host from Amazon S3 to the individual inference instance associated with this production variant.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 3600.
Required: No

 ** ModelName **   <a name="sagemaker-Type-ProductionVariant-ModelName"></a>
The name of the model that you want to host. This is the name that you specified when creating the model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: No

 ** RoutingConfig **   <a name="sagemaker-Type-ProductionVariant-RoutingConfig"></a>
Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.
Type: [ProductionVariantRoutingConfig](API_ProductionVariantRoutingConfig.md) object
Required: No

 ** ServerlessConfig **   <a name="sagemaker-Type-ProductionVariant-ServerlessConfig"></a>
The serverless configuration for an endpoint. Specifies a serverless endpoint configuration instead of an instance-based endpoint configuration.
Type: [ProductionVariantServerlessConfig](API_ProductionVariantServerlessConfig.md) object
Required: No

 ** VariantInstanceProvisionTimeoutInSeconds **   <a name="sagemaker-Type-ProductionVariant-VariantInstanceProvisionTimeoutInSeconds"></a>
The timeout value, in seconds, for provisioning instances for the production variant. When SageMaker encounters an insufficient capacity error while provisioning instances, it retries with the next instance pool (if configured) or waits until the timeout expires. This timeout applies only to capacity provisioning and does not include the time for model download or container startup.
Valid values: 300 to 3600.
Type: Integer
Valid Range: Minimum value of 300. Maximum value of 3600.
Required: No

 ** VolumeSizeInGB **   <a name="sagemaker-Type-ProductionVariant-VolumeSizeInGB"></a>
The size, in GB, of the ML storage volume attached to individual inference instance associated with the production variant. Currently only Amazon EBS gp2 storage volumes are supported.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 512.
Required: No

## See Also
<a name="API_ProductionVariant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProductionVariant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProductionVariant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProductionVariant)
