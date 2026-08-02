---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TrafficMirrorFilterRule.html
---

# TrafficMirrorFilterRule
<a name="API_TrafficMirrorFilterRule"></a>

Describes the Traffic Mirror rule.

## Contents
<a name="API_TrafficMirrorFilterRule_Contents"></a>

 ** description **
The description of the Traffic Mirror rule.
Type: String
Required: No

 ** destinationCidrBlock **
The destination CIDR block assigned to the Traffic Mirror rule.
Type: String
Required: No

 ** destinationPortRange **
The destination port range assigned to the Traffic Mirror rule.
Type: [TrafficMirrorPortRange](API_TrafficMirrorPortRange.md) object
Required: No

 ** protocol **
The protocol assigned to the Traffic Mirror rule.
Type: Integer
Required: No

 ** ruleAction **
The action assigned to the Traffic Mirror rule.
Type: String
Valid Values: `accept | reject`
Required: No

 ** ruleNumber **
The rule number of the Traffic Mirror rule.
Type: Integer
Required: No

 ** sourceCidrBlock **
The source CIDR block assigned to the Traffic Mirror rule.
Type: String
Required: No

 ** sourcePortRange **
The source port range assigned to the Traffic Mirror rule.
Type: [TrafficMirrorPortRange](API_TrafficMirrorPortRange.md) object
Required: No

 ** TagSet.N **
Tags on Traffic Mirroring filter rules.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** trafficDirection **
The traffic direction assigned to the Traffic Mirror rule.
Type: String
Valid Values: `ingress | egress`
Required: No

 ** trafficMirrorFilterId **
The ID of the Traffic Mirror filter that the rule is associated with.
Type: String
Required: No

 ** trafficMirrorFilterRuleId **
The ID of the Traffic Mirror rule.
Type: String
Required: No

## See Also
<a name="API_TrafficMirrorFilterRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TrafficMirrorFilterRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TrafficMirrorFilterRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TrafficMirrorFilterRule)
