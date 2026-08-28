---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorFilterRule.html
---

# CreateTrafficMirrorFilterRule
<a name="API_CreateTrafficMirrorFilterRule"></a>

Creates a Traffic Mirror filter rule.

A Traffic Mirror rule defines the Traffic Mirror source traffic to mirror.

You need the Traffic Mirror filter ID when you create the rule.

## Request Parameters
<a name="API_CreateTrafficMirrorFilterRule_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [How to ensure idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **Description**
The description of the Traffic Mirror rule.
Type: String
Required: No

 **DestinationCidrBlock**
The destination CIDR block to assign to the Traffic Mirror rule.
Type: String
Required: Yes

 **DestinationPortRange**
The destination port range.
Type: [TrafficMirrorPortRangeRequest](API_TrafficMirrorPortRangeRequest.md) object
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Protocol**
The protocol, for example UDP, to assign to the Traffic Mirror rule.
For information about the protocol value, see [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) on the Internet Assigned Numbers Authority (IANA) website.
Type: Integer
Required: No

 **RuleAction**
The action to take on the filtered traffic.
Type: String
Valid Values: `accept | reject`
Required: Yes

 **RuleNumber**
The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.
Type: Integer
Required: Yes

 **SourceCidrBlock**
The source CIDR block to assign to the Traffic Mirror rule.
Type: String
Required: Yes

 **SourcePortRange**
The source port range.
Type: [TrafficMirrorPortRangeRequest](API_TrafficMirrorPortRangeRequest.md) object
Required: No

 **TagSpecification.N**
Traffic Mirroring tags specifications.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TrafficDirection**
The type of traffic.
Type: String
Valid Values: `ingress | egress`
Required: Yes

 **TrafficMirrorFilterId**
The ID of the filter that this rule is associated with.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateTrafficMirrorFilterRule_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [How to ensure idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String

 **requestId**
The ID of the request.
Type: String

 **trafficMirrorFilterRule**
The Traffic Mirror rule.
Type: [TrafficMirrorFilterRule](API_TrafficMirrorFilterRule.md) object

## Errors
<a name="API_CreateTrafficMirrorFilterRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateTrafficMirrorFilterRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateTrafficMirrorFilterRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateTrafficMirrorFilterRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTrafficMirrorFilterRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateTrafficMirrorFilterRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTrafficMirrorFilterRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateTrafficMirrorFilterRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateTrafficMirrorFilterRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateTrafficMirrorFilterRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateTrafficMirrorFilterRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTrafficMirrorFilterRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
