---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TargetGroupPairInfo.html
---

# TargetGroupPairInfo
<a name="API_TargetGroupPairInfo"></a>

 Information about two target groups and how traffic is routed during an Amazon ECS deployment. An optional test traffic route can be specified.

## Contents
<a name="API_TargetGroupPairInfo_Contents"></a>

 ** prodTrafficRoute **   <a name="CodeDeploy-Type-TargetGroupPairInfo-prodTrafficRoute"></a>
 The path used by a load balancer to route production traffic when an Amazon ECS deployment is complete.
Type: [TrafficRoute](API_TrafficRoute.md) object
Required: No

 ** targetGroups **   <a name="CodeDeploy-Type-TargetGroupPairInfo-targetGroups"></a>
 One pair of target groups. One is associated with the original task set. The second is associated with the task set that serves traffic after the deployment is complete.
Type: Array of [TargetGroupInfo](API_TargetGroupInfo.md) objects
Required: No

 ** testTrafficRoute **   <a name="CodeDeploy-Type-TargetGroupPairInfo-testTrafficRoute"></a>
 An optional path used by a load balancer to route test traffic after an Amazon ECS deployment. Validation can occur while test traffic is served during a deployment.
Type: [TrafficRoute](API_TrafficRoute.md) object
Required: No

## See Also
<a name="API_TargetGroupPairInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/TargetGroupPairInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/TargetGroupPairInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/TargetGroupPairInfo)
