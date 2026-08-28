---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_IPSet.html
---

# IPSet
<a name="API_IPSet"></a>

Contains zero or more IP addresses or blocks of IP addresses specified in Classless Inter-Domain Routing (CIDR) notation. AWS WAF supports all IPv4 and IPv6 CIDR ranges except for /0. For information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).

 AWS WAF assigns an ARN to each `IPSet` that you create. To use an IP set in a rule, you provide the ARN to the [Rule](API_Rule.md) statement [IPSetReferenceStatement](API_IPSetReferenceStatement.md).

## Contents
<a name="API_IPSet_Contents"></a>

 ** Addresses **   <a name="WAF-Type-IPSet-Addresses"></a>
Contains an array of strings that specifies zero or more IP addresses or blocks of IP addresses that you want AWS WAF to inspect for in incoming requests. All addresses must be specified using Classless Inter-Domain Routing (CIDR) notation. AWS WAF supports all IPv4 and IPv6 CIDR ranges except for `/0`.
Example address strings:
+ For requests that originated from the IP address 192.0.2.44, specify `192.0.2.44/32`.
+ For requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24`.
+ For requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128`.
+ For requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64`.
For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
Example JSON `Addresses` specifications:
+ Empty array: `"Addresses": []`
+ Array with one address: `"Addresses": ["192.0.2.44/32"]`
+ Array with three addresses: `"Addresses": ["192.0.2.44/32", "192.0.2.0/24", "192.0.0.0/16"]`
+ INVALID specification: `"Addresses": [""]` INVALID
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*\S.*`
Required: Yes

 ** ARN **   <a name="WAF-Type-IPSet-ARN"></a>
The Amazon Resource Name (ARN) of the entity.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

 ** Id **   <a name="WAF-Type-IPSet-Id"></a>
A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: Yes

 ** IPAddressVersion **   <a name="WAF-Type-IPSet-IPAddressVersion"></a>
The version of the IP addresses, either `IPV4` or `IPV6`.
Type: String
Valid Values: `IPV4 | IPV6`
Required: Yes

 ** Name **   <a name="WAF-Type-IPSet-Name"></a>
The name of the IP set. You cannot change the name of an `IPSet` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: Yes

 ** Description **   <a name="WAF-Type-IPSet-Description"></a>
A description of the IP set that helps with identification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=:#@/\-,\.][\w+=:#@/\-,\.\s]+[\w+=:#@/\-,\.]$`
Required: No

## See Also
<a name="API_IPSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/IPSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/IPSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/IPSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
