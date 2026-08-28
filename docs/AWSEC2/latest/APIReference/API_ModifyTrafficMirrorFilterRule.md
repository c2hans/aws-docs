---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTrafficMirrorFilterRule.html
---

# ModifyTrafficMirrorFilterRule
<a name="API_ModifyTrafficMirrorFilterRule"></a>

Modifies the specified Traffic Mirror rule.

 `DestinationCidrBlock` and `SourceCidrBlock` must both be an IPv4 range or an IPv6 range.

## Request Parameters
<a name="API_ModifyTrafficMirrorFilterRule_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Description**
The description to assign to the Traffic Mirror rule.
Type: String
Required: No

 **DestinationCidrBlock**
The destination CIDR block to assign to the Traffic Mirror rule.
Type: String
Required: No

 **DestinationPortRange**
The destination ports that are associated with the Traffic Mirror rule.
Type: [TrafficMirrorPortRangeRequest](API_TrafficMirrorPortRangeRequest.md) object
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Protocol**
The protocol, for example TCP, to assign to the Traffic Mirror rule.
Type: Integer
Required: No

 **RemoveField.N**
The properties that you want to remove from the Traffic Mirror filter rule.
When you remove a property from a Traffic Mirror filter rule, the property is set to the default.
Type: Array of strings
Valid Values: `destination-port-range | source-port-range | protocol | description`
Required: No

 **RuleAction**
The action to assign to the rule.
Type: String
Valid Values: `accept | reject`
Required: No

 **RuleNumber**
The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.
Type: Integer
Required: No

 **SourceCidrBlock**
The source CIDR block to assign to the Traffic Mirror rule.
Type: String
Required: No

 **SourcePortRange**
The port range to assign to the Traffic Mirror rule.
Type: [TrafficMirrorPortRangeRequest](API_TrafficMirrorPortRangeRequest.md) object
Required: No

 **TrafficDirection**
The type of traffic to assign to the rule.
Type: String
Valid Values: `ingress | egress`
Required: No

 **TrafficMirrorFilterRuleId**
The ID of the Traffic Mirror rule.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyTrafficMirrorFilterRule_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **trafficMirrorFilterRule**
Tags are not returned for ModifyTrafficMirrorFilterRule.
A Traffic Mirror rule.
Type: [TrafficMirrorFilterRule](API_TrafficMirrorFilterRule.md) object

## Errors
<a name="API_ModifyTrafficMirrorFilterRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyTrafficMirrorFilterRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyTrafficMirrorFilterRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyTrafficMirrorFilterRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyTrafficMirrorFilterRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyTrafficMirrorFilterRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyTrafficMirrorFilterRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyTrafficMirrorFilterRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyTrafficMirrorFilterRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyTrafficMirrorFilterRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyTrafficMirrorFilterRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyTrafficMirrorFilterRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
