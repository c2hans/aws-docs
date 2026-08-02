---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AnalysisLoadBalancerTarget.html
---

# AnalysisLoadBalancerTarget
<a name="API_AnalysisLoadBalancerTarget"></a>

Describes a load balancer target.

## Contents
<a name="API_AnalysisLoadBalancerTarget_Contents"></a>

 ** address **
The IP address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 15.
Pattern: `^([0-9]{1,3}.){3}[0-9]{1,3}$`
Required: No

 ** availabilityZone **
The Availability Zone.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone.
Type: String
Required: No

 ** instance **
Information about the instance.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** port **
The port on which the target is listening.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

## See Also
<a name="API_AnalysisLoadBalancerTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AnalysisLoadBalancerTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AnalysisLoadBalancerTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AnalysisLoadBalancerTarget)
