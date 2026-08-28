---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_SpotMarketOptions.html
---

# SpotMarketOptions
<a name="API_SpotMarketOptions"></a>

Defines configuration for spot instance deployment.

## Contents
<a name="API_SpotMarketOptions_Contents"></a>

 ** BlockDurationMinutes **   <a name="workspacesinstances-Type-SpotMarketOptions-BlockDurationMinutes"></a>
Duration of spot instance block reservation.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** InstanceInterruptionBehavior **   <a name="workspacesinstances-Type-SpotMarketOptions-InstanceInterruptionBehavior"></a>
Specifies behavior when spot instance is interrupted.
Type: String
Valid Values: `hibernate | stop`
Required: No

 ** MaxPrice **   <a name="workspacesinstances-Type-SpotMarketOptions-MaxPrice"></a>
Maximum hourly price for spot instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** SpotInstanceType **   <a name="workspacesinstances-Type-SpotMarketOptions-SpotInstanceType"></a>
Defines the type of spot instance request.
Type: String
Valid Values: `one-time | persistent`
Required: No

 ** ValidUntilUtc **   <a name="workspacesinstances-Type-SpotMarketOptions-ValidUntilUtc"></a>
Timestamp until which spot instance request is valid.
Type: Timestamp
Required: No

## See Also
<a name="API_SpotMarketOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/SpotMarketOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/SpotMarketOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/SpotMarketOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for WorkSpaces Instances. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-instances` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
