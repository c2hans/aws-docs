---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TrafficMirrorFilter.html
---

# TrafficMirrorFilter
<a name="API_TrafficMirrorFilter"></a>

Describes the Traffic Mirror filter.

## Contents
<a name="API_TrafficMirrorFilter_Contents"></a>

 ** description **
The description of the Traffic Mirror filter.
Type: String
Required: No

 ** EgressFilterRuleSet.N **
Information about the egress rules that are associated with the Traffic Mirror filter.
Type: Array of [TrafficMirrorFilterRule](API_TrafficMirrorFilterRule.md) objects
Required: No

 ** IngressFilterRuleSet.N **
Information about the ingress rules that are associated with the Traffic Mirror filter.
Type: Array of [TrafficMirrorFilterRule](API_TrafficMirrorFilterRule.md) objects
Required: No

 ** NetworkServiceSet.N **
The network service traffic that is associated with the Traffic Mirror filter.
Type: Array of strings
Valid Values: `amazon-dns`
Required: No

 ** TagSet.N **
The tags assigned to the Traffic Mirror filter.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** trafficMirrorFilterId **
The ID of the Traffic Mirror filter.
Type: String
Required: No

## See Also
<a name="API_TrafficMirrorFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TrafficMirrorFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TrafficMirrorFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TrafficMirrorFilter)
