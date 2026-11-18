---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CrossRegionTrafficConfig.html
---

# CrossRegionTrafficConfig
<a name="API_CrossRegionTrafficConfig"></a>

The cross-Region traffic cap for an endpoint. The cap limits the requests per second that the endpoint accepts from inference routers in other AWS Regions. The cap is `MaxCrossRegionPercentPerEndpoint` percent of `MaxInvocationsPerSecondPerInstance` multiplied by the number of `InService` instances, rounded up. All production variants and inference components of the endpoint share it. Requests that you send to the endpoint directly aren't counted. A request over the cap fails with a `ThrottlingException`.

## Contents
<a name="API_CrossRegionTrafficConfig_Contents"></a>

 ** MaxCrossRegionPercentPerEndpoint **   <a name="sagemaker-Type-CrossRegionTrafficConfig-MaxCrossRegionPercentPerEndpoint"></a>
The percentage of the endpoint's capacity that requests from inference routers in other AWS Regions can use.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: Yes

 ** MaxInvocationsPerSecondPerInstance **   <a name="sagemaker-Type-CrossRegionTrafficConfig-MaxInvocationsPerSecondPerInstance"></a>
The number of invocations per second that you expect one `InService` instance to serve. One value applies to every production variant, whatever its instance type.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: Yes

## See Also
<a name="API_CrossRegionTrafficConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CrossRegionTrafficConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CrossRegionTrafficConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CrossRegionTrafficConfig)
