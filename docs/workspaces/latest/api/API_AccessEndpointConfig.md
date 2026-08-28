---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_AccessEndpointConfig.html
---

# AccessEndpointConfig
<a name="API_AccessEndpointConfig"></a>

Describes the access endpoint configuration for a WorkSpace.

## Contents
<a name="API_AccessEndpointConfig_Contents"></a>

 ** AccessEndpoints **   <a name="WorkSpaces-Type-AccessEndpointConfig-AccessEndpoints"></a>
Indicates a list of access endpoints associated with this directory.
Type: Array of [AccessEndpoint](API_AccessEndpoint.md) objects
Required: Yes

 ** InternetFallbackProtocols **   <a name="WorkSpaces-Type-AccessEndpointConfig-InternetFallbackProtocols"></a>
Indicates a list of protocols that fallback to using the public Internet when streaming over a VPC endpoint is not available.
Type: Array of strings
Valid Values: `PCOIP`
Required: No

## See Also
<a name="API_AccessEndpointConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/AccessEndpointConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/AccessEndpointConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/AccessEndpointConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
