---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentSpecification.html
---

# InferenceComponentSpecification
<a name="API_InferenceComponentSpecification"></a>

Details about the resources to deploy with this inference component, including the model, container, and compute resources.

## Contents
<a name="API_InferenceComponentSpecification_Contents"></a>

 ** BaseInferenceComponentName **   <a name="sagemaker-Type-InferenceComponentSpecification-BaseInferenceComponentName"></a>
The name of an existing inference component that is to contain the inference component that you're creating with your request.
Specify this parameter only if your request is meant to create an adapter inference component. An adapter inference component contains the path to an adapter model. The purpose of the adapter model is to tailor the inference output of a base foundation model, which is hosted by the base inference component. The adapter inference component uses the compute resources that you assigned to the base inference component.
When you create an adapter inference component, use the `Container` parameter to specify the location of the adapter artifacts. In the parameter value, use the `ArtifactUrl` parameter of the `InferenceComponentContainerSpecification` data type.
Before you can create an adapter inference component, you must have an existing inference component that contains the foundation model that you want to adapt.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: No

 ** ComputeResourceRequirements **   <a name="sagemaker-Type-InferenceComponentSpecification-ComputeResourceRequirements"></a>
The compute resources allocated to run the model, plus any adapter models, that you assign to the inference component.
Omit this parameter if your request is meant to create an adapter inference component. An adapter inference component is loaded by a base inference component, and it uses the compute resources of the base inference component.
Type: [InferenceComponentComputeResourceRequirements](API_InferenceComponentComputeResourceRequirements.md) object
Required: No

 ** Container **   <a name="sagemaker-Type-InferenceComponentSpecification-Container"></a>
Defines a container that provides the runtime environment for a model that you deploy with an inference component.
Type: [InferenceComponentContainerSpecification](API_InferenceComponentContainerSpecification.md) object
Required: No

 ** DataCacheConfig **   <a name="sagemaker-Type-InferenceComponentSpecification-DataCacheConfig"></a>
Settings that affect how the inference component caches data.
Type: [InferenceComponentDataCacheConfig](API_InferenceComponentDataCacheConfig.md) object
Required: No

 ** InstanceType **   <a name="sagemaker-Type-InferenceComponentSpecification-InstanceType"></a>
The ML compute instance type for the inference component specification. Specifies which instance type this specification applies to. Required when using the `Specifications` parameter with multiple entries.
Type: String
Valid Values: `ml.t2.medium | ml.t2.large | ml.t2.xlarge | ml.t2.2xlarge | ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.m5d.large | ml.m5d.xlarge | ml.m5d.2xlarge | ml.m5d.4xlarge | ml.m5d.12xlarge | ml.m5d.24xlarge | ml.c4.large | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5d.large | ml.c5d.xlarge | ml.c5d.2xlarge | ml.c5d.4xlarge | ml.c5d.9xlarge | ml.c5d.18xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.12xlarge | ml.r5.24xlarge | ml.r5d.large | ml.r5d.xlarge | ml.r5d.2xlarge | ml.r5d.4xlarge | ml.r5d.12xlarge | ml.r5d.24xlarge | ml.inf1.xlarge | ml.inf1.2xlarge | ml.inf1.6xlarge | ml.inf1.24xlarge | ml.dl1.24xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.r8g.medium | ml.r8g.large | ml.r8g.xlarge | ml.r8g.2xlarge | ml.r8g.4xlarge | ml.r8g.8xlarge | ml.r8g.12xlarge | ml.r8g.16xlarge | ml.r8g.24xlarge | ml.r8g.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge | ml.p4d.24xlarge | ml.c7g.large | ml.c7g.xlarge | ml.c7g.2xlarge | ml.c7g.4xlarge | ml.c7g.8xlarge | ml.c7g.12xlarge | ml.c7g.16xlarge | ml.m6g.large | ml.m6g.xlarge | ml.m6g.2xlarge | ml.m6g.4xlarge | ml.m6g.8xlarge | ml.m6g.12xlarge | ml.m6g.16xlarge | ml.m6gd.large | ml.m6gd.xlarge | ml.m6gd.2xlarge | ml.m6gd.4xlarge | ml.m6gd.8xlarge | ml.m6gd.12xlarge | ml.m6gd.16xlarge | ml.c6g.large | ml.c6g.xlarge | ml.c6g.2xlarge | ml.c6g.4xlarge | ml.c6g.8xlarge | ml.c6g.12xlarge | ml.c6g.16xlarge | ml.c6gd.large | ml.c6gd.xlarge | ml.c6gd.2xlarge | ml.c6gd.4xlarge | ml.c6gd.8xlarge | ml.c6gd.12xlarge | ml.c6gd.16xlarge | ml.c6gn.large | ml.c6gn.xlarge | ml.c6gn.2xlarge | ml.c6gn.4xlarge | ml.c6gn.8xlarge | ml.c6gn.12xlarge | ml.c6gn.16xlarge | ml.r6g.large | ml.r6g.xlarge | ml.r6g.2xlarge | ml.r6g.4xlarge | ml.r6g.8xlarge | ml.r6g.12xlarge | ml.r6g.16xlarge | ml.r6gd.large | ml.r6gd.xlarge | ml.r6gd.2xlarge | ml.r6gd.4xlarge | ml.r6gd.8xlarge | ml.r6gd.12xlarge | ml.r6gd.16xlarge | ml.p4de.24xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.trn2.48xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.c8g.medium | ml.c8g.large | ml.c8g.xlarge | ml.c8g.2xlarge | ml.c8g.4xlarge | ml.c8g.8xlarge | ml.c8g.12xlarge | ml.c8g.16xlarge | ml.c8g.24xlarge | ml.c8g.48xlarge | ml.r7gd.medium | ml.r7gd.large | ml.r7gd.xlarge | ml.r7gd.2xlarge | ml.r7gd.4xlarge | ml.r7gd.8xlarge | ml.r7gd.12xlarge | ml.r7gd.16xlarge | ml.m8g.medium | ml.m8g.large | ml.m8g.xlarge | ml.m8g.2xlarge | ml.m8g.4xlarge | ml.m8g.8xlarge | ml.m8g.12xlarge | ml.m8g.16xlarge | ml.m8g.24xlarge | ml.m8g.48xlarge | ml.c6in.large | ml.c6in.xlarge | ml.c6in.2xlarge | ml.c6in.4xlarge | ml.c6in.8xlarge | ml.c6in.12xlarge | ml.c6in.16xlarge | ml.c6in.24xlarge | ml.c6in.32xlarge | ml.p6-b200.48xlarge | ml.p6-b300.48xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge`
Required: No

 ** ModelName **   <a name="sagemaker-Type-InferenceComponentSpecification-ModelName"></a>
The name of an existing SageMaker AI model object in your account that you want to deploy with the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: No

 ** SchedulingConfig **   <a name="sagemaker-Type-InferenceComponentSpecification-SchedulingConfig"></a>
The scheduling configuration that determines how inference component copies are placed across available instances when copies are added or removed.
Type: [InferenceComponentSchedulingConfig](API_InferenceComponentSchedulingConfig.md) object
Required: No

 ** StartupParameters **   <a name="sagemaker-Type-InferenceComponentSpecification-StartupParameters"></a>
Settings that take effect while the model container starts up.
Type: [InferenceComponentStartupParameters](API_InferenceComponentStartupParameters.md) object
Required: No

## See Also
<a name="API_InferenceComponentSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentSpecification)
