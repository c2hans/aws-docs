---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateIpamPolicy.html
---

# CreateIpamPolicy
<a name="API_CreateIpamPolicy"></a>

Creates an IPAM policy.

An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to AWS resources. Each rule maps an AWS service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple AWS Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual AWS account or an entity within AWS Organizations.

For more information, see [Define public IPv4 allocation strategy with IPAM policies](https://docs.aws.amazon.com/vpc/latest/ipam/define-public-ipv4-allocation-strategy-with-ipam-policies.html) in the *Amazon VPC IPAM User Guide*.

## Request Parameters
<a name="API_CreateIpamPolicy_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
A unique, case-sensitive identifier to ensure the idempotency of the request.
Type: String
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamId**
The ID of the IPAM for which you're creating the policy.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to assign to the IPAM policy.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateIpamPolicy_ResponseElements"></a>

The following elements are returned by the service.

 **ipamPolicy**
Information about the created IPAM policy.
An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to AWS resources. Each rule maps an AWS service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple AWS Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual AWS account or an entity within AWS Organizations.
Type: [IpamPolicy](API_IpamPolicy.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateIpamPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateIpamPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateIpamPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateIpamPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateIpamPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateIpamPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateIpamPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateIpamPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateIpamPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateIpamPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateIpamPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateIpamPolicy)
