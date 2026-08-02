---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpamPolicyAllocationRules.html
---

# ModifyIpamPolicyAllocationRules
<a name="API_ModifyIpamPolicyAllocationRules"></a>

Modifies the allocation rules in an IPAM policy.

An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to AWS resources. Each rule maps an AWS service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple AWS Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual AWS account or an entity within AWS Organizations.

Allocation rules are optional configurations within an IPAM policy that map AWS resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.

## Request Parameters
<a name="API_ModifyIpamPolicyAllocationRules_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AllocationRule.N**
The new allocation rules to apply to the IPAM policy.
Allocation rules are optional configurations within an IPAM policy that map AWS resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.
Type: Array of [IpamPolicyAllocationRuleRequest](API_IpamPolicyAllocationRuleRequest.md) objects
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamPolicyId**
The ID of the IPAM policy whose allocation rules you want to modify.
Type: String
Required: Yes

 **Locale**
The locale for which to modify the allocation rules.
Type: String
Required: Yes

 **ResourceType**
The resource type for which to modify the allocation rules.
The AWS service or resource type that can use IP addresses through IPAM policies. Supported services and resource types include:
+ Elastic IP addresses
Type: String
Valid Values: `alb | eip | rds | rnat`
Required: Yes

## Response Elements
<a name="API_ModifyIpamPolicyAllocationRules_ResponseElements"></a>

The following elements are returned by the service.

 **ipamPolicyDocument**
The modified IPAM policy containing the updated allocation rules.
Type: [IpamPolicyDocument](API_IpamPolicyDocument.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyIpamPolicyAllocationRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyIpamPolicyAllocationRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyIpamPolicyAllocationRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyIpamPolicyAllocationRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyIpamPolicyAllocationRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyIpamPolicyAllocationRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyIpamPolicyAllocationRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyIpamPolicyAllocationRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyIpamPolicyAllocationRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyIpamPolicyAllocationRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyIpamPolicyAllocationRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyIpamPolicyAllocationRules)
