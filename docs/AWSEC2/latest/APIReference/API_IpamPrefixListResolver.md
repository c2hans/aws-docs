---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamPrefixListResolver.html
---

# IpamPrefixListResolver
<a name="API_IpamPrefixListResolver"></a>

Describes an IPAM prefix list resolver.

An IPAM prefix list resolver is a component that manages the synchronization between IPAM's CIDR selection rules and customer-managed prefix lists. It automates connectivity configurations by selecting CIDRs from IPAM's database based on your business logic and synchronizing them with prefix lists used in resources such as VPC route tables and security groups.

## Contents
<a name="API_IpamPrefixListResolver_Contents"></a>

 ** addressFamily **
The address family (IPv4 or IPv6) for the IPAM prefix list resolver.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** description **
The description of the IPAM prefix list resolver.
Type: String
Required: No

 ** ipamArn **
The Amazon Resource Name (ARN) of the IPAM associated with this resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** ipamPrefixListResolverArn **
The Amazon Resource Name (ARN) of the IPAM prefix list resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** ipamPrefixListResolverId **
The ID of the IPAM prefix list resolver.
Type: String
Required: No

 ** ipamRegion **
The AWS Region where the associated IPAM is located.
Type: String
Required: No

 ** lastVersionCreationStatus **
The status for the last time a version was created.
Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes.
Type: String
Valid Values: `pending | success | failure`
Required: No

 ** lastVersionCreationStatusMessage **
The status message for the last time a version was created.
Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the IPAM prefix list resolver.
Type: String
Required: No

 ** state **
The current state of the IPAM prefix list resolver. Valid values include `create-in-progress`, `create-complete`, `create-failed`, `modify-in-progress`, `modify-complete`, `modify-failed`, `delete-in-progress`, `delete-complete`, and `delete-failed`.
Type: String
Valid Values: `create-in-progress | create-complete | create-failed | modify-in-progress | modify-complete | modify-failed | delete-in-progress | delete-complete | delete-failed | isolate-in-progress | isolate-complete | restore-in-progress`
Required: No

 ** TagSet.N **
The tags assigned to the IPAM prefix list resolver.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_IpamPrefixListResolver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamPrefixListResolver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamPrefixListResolver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamPrefixListResolver)
