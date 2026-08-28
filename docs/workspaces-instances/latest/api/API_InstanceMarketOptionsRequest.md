---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceMarketOptionsRequest.html
---

# InstanceMarketOptionsRequest
<a name="API_InstanceMarketOptionsRequest"></a>

Configures marketplace-specific instance deployment options.

## Contents
<a name="API_InstanceMarketOptionsRequest_Contents"></a>

 ** MarketType **   <a name="workspacesinstances-Type-InstanceMarketOptionsRequest-MarketType"></a>
Specifies the type of marketplace for instance deployment.
Type: String
Valid Values: `spot | capacity-block`
Required: No

 ** SpotOptions **   <a name="workspacesinstances-Type-InstanceMarketOptionsRequest-SpotOptions"></a>
Configuration options for spot instance deployment.
Type: [SpotMarketOptions](API_SpotMarketOptions.md) object
Required: No

## See Also
<a name="API_InstanceMarketOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/InstanceMarketOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/InstanceMarketOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/InstanceMarketOptionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for WorkSpaces Instances. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-instances` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
