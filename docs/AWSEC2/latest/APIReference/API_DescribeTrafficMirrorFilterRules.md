---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTrafficMirrorFilterRules.html
---

# DescribeTrafficMirrorFilterRules
<a name="API_DescribeTrafficMirrorFilterRules"></a>

Describe traffic mirror filters that determine the traffic that is mirrored.

## Request Parameters
<a name="API_DescribeTrafficMirrorFilterRules_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
Traffic mirror filters.
+  `traffic-mirror-filter-rule-id`: The ID of the Traffic Mirror rule.
+  `traffic-mirror-filter-id`: The ID of the filter that this rule is associated with.
+  `rule-number`: The number of the Traffic Mirror rule.
+  `rule-action`: The action taken on the filtered traffic. Possible actions are `accept` and `reject`.
+  `traffic-direction`: The traffic direction. Possible directions are `ingress` and `egress`.
+  `protocol`: The protocol, for example UDP, assigned to the Traffic Mirror rule.
+  `source-cidr-block`: The source CIDR block assigned to the Traffic Mirror rule.
+  `destination-cidr-block`: The destination CIDR block assigned to the Traffic Mirror rule.
+  `description`: The description of the Traffic Mirror rule.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

 **TrafficMirrorFilterId**
Traffic filter ID.
Type: String
Required: No

 **TrafficMirrorFilterRuleId.N**
Traffic filter rule IDs.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeTrafficMirrorFilterRules_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. The value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **trafficMirrorFilterRuleSet**
Traffic mirror rules.
Type: Array of [TrafficMirrorFilterRule](API_TrafficMirrorFilterRule.md) objects

## Errors
<a name="API_DescribeTrafficMirrorFilterRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeTrafficMirrorFilterRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeTrafficMirrorFilterRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeTrafficMirrorFilterRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeTrafficMirrorFilterRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeTrafficMirrorFilterRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeTrafficMirrorFilterRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeTrafficMirrorFilterRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeTrafficMirrorFilterRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeTrafficMirrorFilterRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeTrafficMirrorFilterRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeTrafficMirrorFilterRules)
