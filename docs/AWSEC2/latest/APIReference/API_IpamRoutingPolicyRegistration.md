---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamRoutingPolicyRegistration.html
---

# IpamRoutingPolicyRegistration
<a name="API_IpamRoutingPolicyRegistration"></a>

Contains information about a routing policy registration that represents a Route Origin Authorization (ROA) managed through IPAM.

## Contents
<a name="API_IpamRoutingPolicyRegistration_Contents"></a>

 ** AsnSet.N **
The Autonomous System Numbers (ASNs) authorized to originate the prefix.
Type: Array of strings
Required: No

 ** cidr **
The IP address prefix in CIDR notation authorized by the ROA.
Type: String
Required: No

 ** description **
The description of the routing policy registration.
Type: String
Required: No

 ** latestDeltaId **
The ID of the most recent delta that modified this registration.
Type: String
Required: No

 ** maxLength **
The maximum prefix length that the ASNs are authorized to announce.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 48.
Required: No

 ** permitMoreSpecificAnnouncements **
Specifies whether to permit more specific route announcements than the CIDR prefix. When enabled, ASNs can announce sub-prefixes of the authorized CIDR up to the specified maximum length. Default: `false`.
Type: Boolean
Required: No

 ** state **
The state of the routing policy registration. Valid values: `pending-activate` \| `activate-failed` \| `create-in-progress` \| `create-complete` \| `update-in-progress` \| `update-complete` \| `delete-in-progress` \| `delete-complete`.
Type: String
Valid Values: `pending-activate | activate-failed | create-in-progress | create-complete | update-in-progress | update-complete | delete-in-progress | delete-complete`
Required: No

## See Also
<a name="API_IpamRoutingPolicyRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamRoutingPolicyRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamRoutingPolicyRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamRoutingPolicyRegistration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
