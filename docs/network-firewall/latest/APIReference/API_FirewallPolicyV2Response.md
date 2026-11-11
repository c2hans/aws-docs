---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallPolicyV2Response.html
---

# FirewallPolicyV2Response
<a name="API_FirewallPolicyV2Response"></a>

The high-level properties of a Next Generation policy. This includes the policy's identity, status, consumed capacity, and association count. AWS Network Firewall returns this object in response to the Next Generation policy operations. To retrieve the policy's rule groups and settings, use the `FirewallPolicyV2` object.

## Contents
<a name="API_FirewallPolicyV2Response_Contents"></a>

 ** FirewallPolicyV2Arn **   <a name="networkfirewall-Type-FirewallPolicyV2Response-FirewallPolicyV2Arn"></a>
The Amazon Resource Name (ARN) of the Next Generation policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: Yes

 ** FirewallPolicyV2Id **   <a name="networkfirewall-Type-FirewallPolicyV2Response-FirewallPolicyV2Id"></a>
The unique identifier of the Next Generation policy. AWS Network Firewall assigns this identifier when you create the policy.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`
Required: Yes

 ** FirewallPolicyV2Name **   <a name="networkfirewall-Type-FirewallPolicyV2Response-FirewallPolicyV2Name"></a>
The descriptive name of the Next Generation policy. You can't change the name of a firewall policy after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** ConsumedFirewallRuleCapacity **   <a name="networkfirewall-Type-FirewallPolicyV2Response-ConsumedFirewallRuleCapacity"></a>
The number of firewall engine rule capacity units that the policy's firewall section currently consumes.
Type: Integer
Required: No

 ** ConsumedIpsDomainCapacity **   <a name="networkfirewall-Type-FirewallPolicyV2Response-ConsumedIpsDomainCapacity"></a>
The number of IPS domain list capacity units that the policy's IPS section currently consumes.
Type: Integer
Required: No

 ** ConsumedIpsRuleCapacity **   <a name="networkfirewall-Type-FirewallPolicyV2Response-ConsumedIpsRuleCapacity"></a>
The number of IPS engine rule capacity units that the policy's IPS section currently consumes.
Type: Integer
Required: No

 ** Description **   <a name="networkfirewall-Type-FirewallPolicyV2Response-Description"></a>
A description of the Next Generation policy.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^.*$`
Required: No

 ** EncryptionConfiguration **   <a name="networkfirewall-Type-FirewallPolicyV2Response-EncryptionConfiguration"></a>
A complex type that contains the AWS KMS encryption configuration settings for your Next Generation policy.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** Errors **   <a name="networkfirewall-Type-FirewallPolicyV2Response-Errors"></a>
Any configuration errors that apply to the Next Generation policy. Network Firewall detects these errors asynchronously, after you create or update the policy, so an error can appear after the request that caused it has already succeeded. Each entry describes the problem and how to resolve it, and Network Firewall clears it automatically after you resolve the problem.
Type: Array of [FirewallPolicyError](API_FirewallPolicyError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** FirewallPolicyV2Status **   <a name="networkfirewall-Type-FirewallPolicyV2Response-FirewallPolicyV2Status"></a>
The current status of the Next Generation policy. A policy must be in the `ACTIVE` state before you can use it in a firewall.
Type: String
Valid Values: `ACTIVE | DELETING | ERROR | UPDATING`
Required: No

 ** LastModifiedTime **   <a name="networkfirewall-Type-FirewallPolicyV2Response-LastModifiedTime"></a>
The last time that the Next Generation policy was changed.
Type: Timestamp
Required: No

 ** NumberOfAssociations **   <a name="networkfirewall-Type-FirewallPolicyV2Response-NumberOfAssociations"></a>
The number of firewalls that are associated with the Next Generation policy.
Type: Integer
Required: No

 ** StatusMessage **   <a name="networkfirewall-Type-FirewallPolicyV2Response-StatusMessage"></a>
Additional information about the current status of the Next Generation policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** Tags **   <a name="networkfirewall-Type-FirewallPolicyV2Response-Tags"></a>
The key-value tag pairs that are associated with the Next Generation policy.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## See Also
<a name="API_FirewallPolicyV2Response_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallPolicyV2Response)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallPolicyV2Response)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallPolicyV2Response)
