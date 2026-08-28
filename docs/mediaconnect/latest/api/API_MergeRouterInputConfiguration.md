---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MergeRouterInputConfiguration.html
---

# MergeRouterInputConfiguration
<a name="API_MergeRouterInputConfiguration"></a>

Configuration settings for a merge router input that combines two input sources.

## Contents
<a name="API_MergeRouterInputConfiguration_Contents"></a>

 ** mergeRecoveryWindowMilliseconds **   <a name="mediaconnect-Type-MergeRouterInputConfiguration-mergeRecoveryWindowMilliseconds"></a>
The time window in milliseconds for merging the two input sources.
Type: Long
Required: Yes

 ** networkInterfaceArn **   <a name="mediaconnect-Type-MergeRouterInputConfiguration-networkInterfaceArn"></a>
The ARN of the network interface to use for this merge router input.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}`
Required: Yes

 ** protocolConfigurations **   <a name="mediaconnect-Type-MergeRouterInputConfiguration-protocolConfigurations"></a>
A list of exactly two protocol configurations for the merge input sources. Both must use the same protocol type.
Type: Array of [MergeRouterInputProtocolConfiguration](API_MergeRouterInputProtocolConfiguration.md) objects
Required: Yes

## See Also
<a name="API_MergeRouterInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MergeRouterInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MergeRouterInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MergeRouterInputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
