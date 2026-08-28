---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_NetworkConfig.html
---

# NetworkConfig
<a name="API_NetworkConfig"></a>

Networking options for a job, such as network traffic encryption between containers, whether to allow inbound and outbound network calls to and from containers, and the VPC subnets and security groups to use for VPC-enabled jobs.

## Contents
<a name="API_NetworkConfig_Contents"></a>

 ** EnableInterContainerTrafficEncryption **   <a name="sagemaker-Type-NetworkConfig-EnableInterContainerTrafficEncryption"></a>
Whether to encrypt all communications between distributed processing jobs. Choose `True` to encrypt communications. Encryption provides greater security for distributed processing jobs, but the processing might take longer.
Type: Boolean
Required: No

 ** EnableNetworkIsolation **   <a name="sagemaker-Type-NetworkConfig-EnableNetworkIsolation"></a>
Whether to allow inbound and outbound network calls to and from the containers used for the processing job.
Type: Boolean
Required: No

 ** VpcConfig **   <a name="sagemaker-Type-NetworkConfig-VpcConfig"></a>
Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_NetworkConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/NetworkConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/NetworkConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/NetworkConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
