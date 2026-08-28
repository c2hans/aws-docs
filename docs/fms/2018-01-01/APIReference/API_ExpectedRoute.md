---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ExpectedRoute.html
---

# ExpectedRoute
<a name="API_ExpectedRoute"></a>

Information about the expected route in the route table.

## Contents
<a name="API_ExpectedRoute_Contents"></a>

 ** AllowedTargets **   <a name="fms-Type-ExpectedRoute-AllowedTargets"></a>
Information about the allowed targets.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ContributingSubnets **   <a name="fms-Type-ExpectedRoute-ContributingSubnets"></a>
Information about the contributing subnets.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** IpV4Cidr **   <a name="fms-Type-ExpectedRoute-IpV4Cidr"></a>
Information about the IPv4 CIDR block.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-f0-9:./]+`
Required: No

 ** IpV6Cidr **   <a name="fms-Type-ExpectedRoute-IpV6Cidr"></a>
Information about the IPv6 CIDR block.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-f0-9:./]+`
Required: No

 ** PrefixListId **   <a name="fms-Type-ExpectedRoute-PrefixListId"></a>
Information about the ID of the prefix list for the route.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-f0-9:./]+`
Required: No

 ** RouteTableId **   <a name="fms-Type-ExpectedRoute-RouteTableId"></a>
Information about the route table ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_ExpectedRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ExpectedRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ExpectedRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ExpectedRoute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
