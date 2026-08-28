---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetworkSegment.html
---

# CoreNetworkSegment
<a name="API_CoreNetworkSegment"></a>

Describes a core network segment, which are dedicated routes. Only attachments within this segment can communicate with each other.

## Contents
<a name="API_CoreNetworkSegment_Contents"></a>

 ** EdgeLocations **   <a name="networkmanager-Type-CoreNetworkSegment-EdgeLocations"></a>
The Regions where the edges are located.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** Name **   <a name="networkmanager-Type-CoreNetworkSegment-Name"></a>
The name of a core network segment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** SharedSegments **   <a name="networkmanager-Type-CoreNetworkSegment-SharedSegments"></a>
The shared segments of a core network.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_CoreNetworkSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkSegment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
