---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterInputStreamDetails.html
---

# RouterInputStreamDetails
<a name="API_RouterInputStreamDetails"></a>

Configuration details for the router input stream.

## Contents
<a name="API_RouterInputStreamDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** failover **   <a name="mediaconnect-Type-RouterInputStreamDetails-failover"></a>
Configuration details for a failover router input that can automatically switch between two sources.
Type: [FailoverRouterInputStreamDetails](API_FailoverRouterInputStreamDetails.md) object
Required: No

 ** mediaConnectFlow **   <a name="mediaconnect-Type-RouterInputStreamDetails-mediaConnectFlow"></a>
Configuration details for a MediaConnect flow when used as a router input source.
Type: [MediaConnectFlowRouterInputStreamDetails](API_MediaConnectFlowRouterInputStreamDetails.md) object
Required: No

 ** mediaLiveChannel **   <a name="mediaconnect-Type-RouterInputStreamDetails-mediaLiveChannel"></a>
Configuration details for a MediaLive channel when used as a router input source.
Type: [MediaLiveChannelRouterInputStreamDetails](API_MediaLiveChannelRouterInputStreamDetails.md) object
Required: No

 ** merge **   <a name="mediaconnect-Type-RouterInputStreamDetails-merge"></a>
Configuration details for a merge router input that combines two input sources.
Type: [MergeRouterInputStreamDetails](API_MergeRouterInputStreamDetails.md) object
Required: No

 ** standard **   <a name="mediaconnect-Type-RouterInputStreamDetails-standard"></a>
Configuration details for a standard router input stream type.
Type: [StandardRouterInputStreamDetails](API_StandardRouterInputStreamDetails.md) object
Required: No

## See Also
<a name="API_RouterInputStreamDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterInputStreamDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterInputStreamDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterInputStreamDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
