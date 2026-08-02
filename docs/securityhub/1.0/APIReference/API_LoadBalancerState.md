---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_LoadBalancerState.html
---

# LoadBalancerState
<a name="API_LoadBalancerState"></a>

Information about the state of the load balancer.

## Contents
<a name="API_LoadBalancerState_Contents"></a>

 ** Code **   <a name="securityhub-Type-LoadBalancerState-Code"></a>
The state code. The initial state of the load balancer is provisioning.
After the load balancer is fully set up and ready to route traffic, its state is active.
If the load balancer could not be set up, its state is failed.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Reason **   <a name="securityhub-Type-LoadBalancerState-Reason"></a>
A description of the state.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_LoadBalancerState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/LoadBalancerState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/LoadBalancerState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/LoadBalancerState)
