---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringNetworkConfig.html
---

# MonitoringNetworkConfig
<a name="API_MonitoringNetworkConfig"></a>

The networking configuration for the monitoring job.

## Contents
<a name="API_MonitoringNetworkConfig_Contents"></a>

 ** EnableInterContainerTrafficEncryption **   <a name="sagemaker-Type-MonitoringNetworkConfig-EnableInterContainerTrafficEncryption"></a>
Whether to encrypt all communications between the instances used for the monitoring jobs. Choose `True` to encrypt communications. Encryption provides greater security for distributed jobs, but the processing might take longer.
Type: Boolean
Required: No

 ** EnableNetworkIsolation **   <a name="sagemaker-Type-MonitoringNetworkConfig-EnableNetworkIsolation"></a>
Whether to allow inbound and outbound network calls to and from the containers used for the monitoring job.
Type: Boolean
Required: No

 ** VpcConfig **   <a name="sagemaker-Type-MonitoringNetworkConfig-VpcConfig"></a>
Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_MonitoringNetworkConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringNetworkConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringNetworkConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringNetworkConfig)
