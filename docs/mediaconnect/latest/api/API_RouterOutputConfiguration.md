---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterOutputConfiguration.html
---

# RouterOutputConfiguration
<a name="API_RouterOutputConfiguration"></a>

The configuration settings for a router output.

## Contents
<a name="API_RouterOutputConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** mediaConnectFlow **   <a name="mediaconnect-Type-RouterOutputConfiguration-mediaConnectFlow"></a>
Configuration settings for connecting a router output to a MediaConnect flow source.
Type: [MediaConnectFlowRouterOutputConfiguration](API_MediaConnectFlowRouterOutputConfiguration.md) object
Required: No

 ** mediaLiveInput **   <a name="mediaconnect-Type-RouterOutputConfiguration-mediaLiveInput"></a>
Configuration settings for connecting a router output to a MediaLive input.
Type: [MediaLiveInputRouterOutputConfiguration](API_MediaLiveInputRouterOutputConfiguration.md) object
Required: No

 ** standard **   <a name="mediaconnect-Type-RouterOutputConfiguration-standard"></a>
The configuration settings for a standard router output, including the protocol, protocol-specific configuration, network interface, and availability zone.
Type: [StandardRouterOutputConfiguration](API_StandardRouterOutputConfiguration.md) object
Required: No

## See Also
<a name="API_RouterOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterOutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
