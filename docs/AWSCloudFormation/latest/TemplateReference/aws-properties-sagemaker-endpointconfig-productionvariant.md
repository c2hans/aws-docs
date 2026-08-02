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
  "[AcceleratorType](#cfn-sagemaker-endpointconfig-productionvariant-acceleratortype)" : {{String}},
  "[ContainerStartupHealthCheckTimeoutInSeconds](#cfn-sagemaker-endpointconfig-productionvariant-containerstartuphealthchecktimeoutinseconds)" : {{Integer}},
  "[EnableSSMAccess](#cfn-sagemaker-endpointconfig-productionvariant-enablessmaccess)" : {{Boolean}},
  "[InitialInstanceCount](#cfn-sagemaker-endpointconfig-productionvariant-initialinstancecount)" : {{Integer}},
  "[InitialVariantWeight](#cfn-sagemaker-endpointconfig-productionvariant-initialvariantweight)" : {{Number}},
  "[InstanceType](#cfn-sagemaker-endpointconfig-productionvariant-instancetype)" : {{String}},
  "[ModelDataDownloadTimeoutInSeconds](#cfn-sagemaker-endpointconfig-productionvariant-modeldatadownloadtimeoutinseconds)" : {{Integer}},
  "[ModelName](#cfn-sagemaker-endpointconfig-productionvariant-modelname)" : {{String}},
  "[ServerlessConfig](#cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig)" : {{ServerlessConfig}},
  "[VariantName](#cfn-sagemaker-endpointconfig-productionvariant-variantname)" : {{String}},
  "[VolumeSizeInGB](#cfn-sagemaker-endpointconfig-productionvariant-volumesizeingb)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-productionvariant-syntax.yaml"></a>

```
  [AcceleratorType](#cfn-sagemaker-endpointconfig-productionvariant-acceleratortype): {{String}}
  [ContainerStartupHealthCheckTimeoutInSeconds](#cfn-sagemaker-endpointconfig-productionvariant-containerstartuphealthchecktimeoutinseconds): {{Integer}}
  [EnableSSMAccess](#cfn-sagemaker-endpointconfig-productionvariant-enablessmaccess): {{Boolean}}
  [InitialInstanceCount](#cfn-sagemaker-endpointconfig-productionvariant-initialinstancecount): {{Integer}}
  [InitialVariantWeight](#cfn-sagemaker-endpointconfig-productionvariant-initialvariantweight): {{Number}}
  [InstanceType](#cfn-sagemaker-endpointconfig-productionvariant-instancetype): {{String}}
  [ModelDataDownloadTimeoutInSeconds](#cfn-sagemaker-endpointconfig-productionvariant-modeldatadownloadtimeoutinseconds): {{Integer}}
  [ModelName](#cfn-sagemaker-endpointconfig-productionvariant-modelname): {{String}}
  [ServerlessConfig](#cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig): {{
    ServerlessConfig}}
  [VariantName](#cfn-sagemaker-endpointconfig-productionvariant-variantname): {{String}}
  [VolumeSizeInGB](#cfn-sagemaker-endpointconfig-productionvariant-volumesizeingb): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-productionvariant-properties"></a>

`AcceleratorType`  <a name="cfn-sagemaker-endpointconfig-productionvariant-acceleratortype"></a>
The size of the Elastic Inference (EI) instance to use for the production variant. EI instances provide on-demand GPU computing for inference. For more information, see [Using Elastic Inference in Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/ei.html). For more information, see [Using Elastic Inference in Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/ei.html).
*Required*: No
*Type*: String
*Allowed values*: `ml.eia1.medium | ml.eia1.large | ml.eia1.xlarge | ml.eia2.medium | ml.eia2.large | ml.eia2.xlarge`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerStartupHealthCheckTimeoutInSeconds`  <a name="cfn-sagemaker-endpointconfig-productionvariant-containerstartuphealthchecktimeoutinseconds"></a>
The timeout value, in seconds, for your inference container to pass health check by SageMaker Hosting. For more information about health check, see [How Your Container Should Respond to Health Check (Ping) Requests](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-ping-requests).
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `3600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableSSMAccess`  <a name="cfn-sagemaker-endpointconfig-productionvariant-enablessmaccess"></a>
 You can use this parameter to turn on native AWS Systems Manager (SSM) access for a production variant behind an endpoint. By default, SSM access is disabled for all production variants behind an endpoint. You can turn on or turn off SSM access for a production variant behind an existing endpoint by creating a new endpoint configuration and calling `UpdateEndpoint`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InitialInstanceCount`  <a name="cfn-sagemaker-endpointconfig-productionvariant-initialinstancecount"></a>
Number of instances to launch initially.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InitialVariantWeight`  <a name="cfn-sagemaker-endpointconfig-productionvariant-initialvariantweight"></a>
Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the `VariantWeight` to the sum of all `VariantWeight` values across all ProductionVariants. If unspecified, it defaults to 1.0.
*Required*: Yes
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceType`  <a name="cfn-sagemaker-endpointconfig-productionvariant-instancetype"></a>
The ML compute instance type.
*Required*: No
*Type*: String
*Allowed values*: `ml.t2.medium | ml.t2.large | ml.t2.xlarge | ml.t2.2xlarge | ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.m5d.large | ml.m5d.xlarge | ml.m5d.2xlarge | ml.m5d.4xlarge | ml.m5d.12xlarge | ml.m5d.24xlarge | ml.c4.large | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5d.large | ml.c5d.xlarge | ml.c5d.2xlarge | ml.c5d.4xlarge | ml.c5d.9xlarge | ml.c5d.18xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.12xlarge | ml.r5.24xlarge | ml.r5d.large | ml.r5d.xlarge | ml.r5d.2xlarge | ml.r5d.4xlarge | ml.r5d.12xlarge | ml.r5d.24xlarge | ml.inf1.xlarge | ml.inf1.2xlarge | ml.inf1.6xlarge | ml.inf1.24xlarge | ml.dl1.24xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.r8g.medium | ml.r8g.large | ml.r8g.xlarge | ml.r8g.2xlarge | ml.r8g.4xlarge | ml.r8g.8xlarge | ml.r8g.12xlarge | ml.r8g.16xlarge | ml.r8g.24xlarge | ml.r8g.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge | ml.p4d.24xlarge | ml.c7g.large | ml.c7g.xlarge | ml.c7g.2xlarge | ml.c7g.4xlarge | ml.c7g.8xlarge | ml.c7g.12xlarge | ml.c7g.16xlarge | ml.m6g.large | ml.m6g.xlarge | ml.m6g.2xlarge | ml.m6g.4xlarge | ml.m6g.8xlarge | ml.m6g.12xlarge | ml.m6g.16xlarge | ml.m6gd.large | ml.m6gd.xlarge | ml.m6gd.2xlarge | ml.m6gd.4xlarge | ml.m6gd.8xlarge | ml.m6gd.12xlarge | ml.m6gd.16xlarge | ml.c6g.large | ml.c6g.xlarge | ml.c6g.2xlarge | ml.c6g.4xlarge | ml.c6g.8xlarge | ml.c6g.12xlarge | ml.c6g.16xlarge | ml.c6gd.large | ml.c6gd.xlarge | ml.c6gd.2xlarge | ml.c6gd.4xlarge | ml.c6gd.8xlarge | ml.c6gd.12xlarge | ml.c6gd.16xlarge | ml.c6gn.large | ml.c6gn.xlarge | ml.c6gn.2xlarge | ml.c6gn.4xlarge | ml.c6gn.8xlarge | ml.c6gn.12xlarge | ml.c6gn.16xlarge | ml.r6g.large | ml.r6g.xlarge | ml.r6g.2xlarge | ml.r6g.4xlarge | ml.r6g.8xlarge | ml.r6g.12xlarge | ml.r6g.16xlarge | ml.r6gd.large | ml.r6gd.xlarge | ml.r6gd.2xlarge | ml.r6gd.4xlarge | ml.r6gd.8xlarge | ml.r6gd.12xlarge | ml.r6gd.16xlarge | ml.p4de.24xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.trn2.48xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.c8g.medium | ml.c8g.large | ml.c8g.xlarge | ml.c8g.2xlarge | ml.c8g.4xlarge | ml.c8g.8xlarge | ml.c8g.12xlarge | ml.c8g.16xlarge | ml.c8g.24xlarge | ml.c8g.48xlarge | ml.r7gd.medium | ml.r7gd.large | ml.r7gd.xlarge | ml.r7gd.2xlarge | ml.r7gd.4xlarge | ml.r7gd.8xlarge | ml.r7gd.12xlarge | ml.r7gd.16xlarge | ml.m8g.medium | ml.m8g.large | ml.m8g.xlarge | ml.m8g.2xlarge | ml.m8g.4xlarge | ml.m8g.8xlarge | ml.m8g.12xlarge | ml.m8g.16xlarge | ml.m8g.24xlarge | ml.m8g.48xlarge | ml.c6in.large | ml.c6in.xlarge | ml.c6in.2xlarge | ml.c6in.4xlarge | ml.c6in.8xlarge | ml.c6in.12xlarge | ml.c6in.16xlarge | ml.c6in.24xlarge | ml.c6in.32xlarge | ml.p6-b200.48xlarge | ml.p6-b300.48xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge`
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
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
*Minimum*: `0`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServerlessConfig`  <a name="cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig"></a>
The serverless configuration for an endpoint. Specifies a serverless endpoint configuration instead of an instance-based endpoint configuration.
*Required*: No
*Type*: [ServerlessConfig](aws-properties-sagemaker-endpointconfig-serverlessconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VariantName`  <a name="cfn-sagemaker-endpointconfig-productionvariant-variantname"></a>
The name of the production variant.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Minimum*: `0`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeSizeInGB`  <a name="cfn-sagemaker-endpointconfig-productionvariant-volumesizeingb"></a>
The size, in GB, of the ML storage volume attached to individual inference instance associated with the production variant. Currently only Amazon EBS gp2 storage volumes are supported.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
