---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateIpamPrefixListResolver.html
---

# CreateIpamPrefixListResolver
<a name="API_CreateIpamPrefixListResolver"></a>

Creates an IPAM prefix list resolver.

An IPAM prefix list resolver is a component that manages the synchronization between IPAM's CIDR selection rules and customer-managed prefix lists. It automates connectivity configurations by selecting CIDRs from IPAM's database based on your business logic and synchronizing them with prefix lists used in resources such as VPC route tables and security groups.

For more information about IPAM prefix list resolver, see [Automate prefix list updates with IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/automate-prefix-list-updates.html) in the *Amazon VPC IPAM User Guide*.

## Request Parameters
<a name="API_CreateIpamPrefixListResolver_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AddressFamily**
The address family for the IPAM prefix list resolver. Valid values are `ipv4` and `ipv6`. You must create separate resolvers for IPv4 and IPv6 CIDRs as they cannot be mixed in the same resolver.
Type: String
Valid Values: `ipv4 | ipv6`
Required: Yes

 **ClientToken**
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **Description**
A description for the IPAM prefix list resolver to help you identify its purpose and configuration.
Type: String
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamId**
The ID of the IPAM that will serve as the source of the IP address database for CIDR selection. The IPAM must be in the Advanced tier to use this feature.
Type: String
Required: Yes

 **Rule.N**
The CIDR selection rules for the resolver.
CIDR selection rules define the business logic for selecting CIDRs from IPAM. If a CIDR matches any of the rules, it will be included. If a rule has multiple conditions, the CIDR has to match every condition of that rule. You can create a prefix list resolver without any CIDR selection rules, but it will generate empty versions (containing no CIDRs) until you add rules.
Type: Array of [IpamPrefixListResolverRuleRequest](API_IpamPrefixListResolverRuleRequest.md) objects
Required: No

 **TagSpecification.N**
The tags to apply to the IPAM prefix list resolver during creation. Tags help you organize and manage your AWS resources.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateIpamPrefixListResolver_ResponseElements"></a>

The following elements are returned by the service.

 **ipamPrefixListResolver**
Information about the IPAM prefix list resolver that was created.
Type: [IpamPrefixListResolver](API_IpamPrefixListResolver.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateIpamPrefixListResolver_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateIpamPrefixListResolver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateIpamPrefixListResolver)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateIpamPrefixListResolver)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateIpamPrefixListResolver)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateIpamPrefixListResolver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateIpamPrefixListResolver)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateIpamPrefixListResolver)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateIpamPrefixListResolver)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateIpamPrefixListResolver)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateIpamPrefixListResolver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateIpamPrefixListResolver)
