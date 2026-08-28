---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_EC2DeleteRouteAction.html
---

# EC2DeleteRouteAction
<a name="API_EC2DeleteRouteAction"></a>

Information about the DeleteRoute action in Amazon EC2.

## Contents
<a name="API_EC2DeleteRouteAction_Contents"></a>

 ** RouteTableId **   <a name="fms-Type-EC2DeleteRouteAction-RouteTableId"></a>
Information about the ID of the route table.
Type: [ActionTarget](API_ActionTarget.md) object
Required: Yes

 ** Description **   <a name="fms-Type-EC2DeleteRouteAction-Description"></a>
A description of the DeleteRoute action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** DestinationCidrBlock **   <a name="fms-Type-EC2DeleteRouteAction-DestinationCidrBlock"></a>
Information about the IPv4 CIDR range for the route. The value you specify must match the CIDR for the route exactly.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-f0-9:./]+`
Required: No

 ** DestinationIpv6CidrBlock **   <a name="fms-Type-EC2DeleteRouteAction-DestinationIpv6CidrBlock"></a>
Information about the IPv6 CIDR range for the route. The value you specify must match the CIDR for the route exactly.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-f0-9:./]+`
Required: No

 ** DestinationPrefixListId **   <a name="fms-Type-EC2DeleteRouteAction-DestinationPrefixListId"></a>
Information about the ID of the prefix list for the route.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_EC2DeleteRouteAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/EC2DeleteRouteAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/EC2DeleteRouteAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/EC2DeleteRouteAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
