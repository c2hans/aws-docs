---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_LoadBalancerInfo.html
---

# LoadBalancerInfo
<a name="API_LoadBalancerInfo"></a>

Information about the Elastic Load Balancing load balancer or target group used in a deployment.

You can use load balancers and target groups in combination. For example, if you have two Classic Load Balancers, and five target groups tied to an Application Load Balancer, you can specify the two Classic Load Balancers in `elbInfoList`, and the five target groups in `targetGroupInfoList`.

## Contents
<a name="API_LoadBalancerInfo_Contents"></a>

 ** elbInfoList **   <a name="CodeDeploy-Type-LoadBalancerInfo-elbInfoList"></a>
An array that contains information about the load balancers to use for load balancing in a deployment. If you're using Classic Load Balancers, specify those load balancers in this array.
You can add up to 10 load balancers to the array.
If you're using Application Load Balancers or Network Load Balancers, use the `targetGroupInfoList` array instead of this one.
Type: Array of [ELBInfo](API_ELBInfo.md) objects
Required: No

 ** targetGroupInfoList **   <a name="CodeDeploy-Type-LoadBalancerInfo-targetGroupInfoList"></a>
An array that contains information about the target groups to use for load balancing in a deployment. If you're using Application Load Balancers and Network Load Balancers, specify their associated target groups in this array.
You can add up to 10 target groups to the array.
If you're using Classic Load Balancers, use the `elbInfoList` array instead of this one.
Type: Array of [TargetGroupInfo](API_TargetGroupInfo.md) objects
Required: No

 ** targetGroupPairInfoList **   <a name="CodeDeploy-Type-LoadBalancerInfo-targetGroupPairInfoList"></a>
 The target group pair information. This is an array of `TargeGroupPairInfo` objects with a maximum size of one.
Type: Array of [TargetGroupPairInfo](API_TargetGroupPairInfo.md) objects
Required: No

## See Also
<a name="API_LoadBalancerInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/LoadBalancerInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/LoadBalancerInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/LoadBalancerInfo)
