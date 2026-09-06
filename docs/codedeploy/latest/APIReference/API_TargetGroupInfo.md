---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TargetGroupInfo.html
---

# TargetGroupInfo
<a name="API_TargetGroupInfo"></a>

Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

## Contents
<a name="API_TargetGroupInfo_Contents"></a>

 ** name **   <a name="CodeDeploy-Type-TargetGroupInfo-name"></a>
For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.
Type: String
Required: No

## See Also
<a name="API_TargetGroupInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/TargetGroupInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/TargetGroupInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/TargetGroupInfo)
