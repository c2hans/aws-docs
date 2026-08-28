---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_FailoverRouterInputConfiguration.html
---

# FailoverRouterInputConfiguration
<a name="API_FailoverRouterInputConfiguration"></a>

Configuration settings for a failover router input that allows switching between two input sources.

## Contents
<a name="API_FailoverRouterInputConfiguration_Contents"></a>

 ** networkInterfaceArn **   <a name="mediaconnect-Type-FailoverRouterInputConfiguration-networkInterfaceArn"></a>
The ARN of the network interface to use for this failover router input.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}`
Required: Yes

 ** protocolConfigurations **   <a name="mediaconnect-Type-FailoverRouterInputConfiguration-protocolConfigurations"></a>
A list of exactly two protocol configurations for the failover input sources. Both must use the same protocol type.
Type: Array of [FailoverRouterInputProtocolConfiguration](API_FailoverRouterInputProtocolConfiguration.md) objects
Required: Yes

 ** sourcePriorityMode **   <a name="mediaconnect-Type-FailoverRouterInputConfiguration-sourcePriorityMode"></a>
The mode for determining source priority in failover configurations.
Type: String
Valid Values: `NO_PRIORITY | PRIMARY_SECONDARY`
Required: Yes

 ** primarySourceIndex **   <a name="mediaconnect-Type-FailoverRouterInputConfiguration-primarySourceIndex"></a>
The index (0 or 1) that specifies which source in the protocol configurations list is currently active. Used to control which of the two failover sources is currently selected. This field is ignored when sourcePriorityMode is set to NO\_PRIORITY
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_FailoverRouterInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/FailoverRouterInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/FailoverRouterInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/FailoverRouterInputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
