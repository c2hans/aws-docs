---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ScopeConfigurationInput.html
---

# ScopeConfigurationInput
<a name="API_ScopeConfigurationInput"></a>

The scope of resources to scan for a single scanning type. Provide this as part of an `AzureScopeConfigurationInput` when you create or update a connector.

## Contents
<a name="API_ScopeConfigurationInput_Contents"></a>

 ** scopeType **   <a name="inspector2-Type-ScopeConfigurationInput-scopeType"></a>
The type of scope. Valid values are `TENANT`, which scans all resources in the Azure tenant, and `SUBSCRIPTION`, which scans only the resources in the specified Azure subscriptions.
Type: String
Valid Values: `TENANT | SUBSCRIPTION`
Required: Yes

 ** scopeValues **   <a name="inspector2-Type-ScopeConfigurationInput-scopeValues"></a>
The list of scope values. For subscription-level scope, these are Azure subscription IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_ScopeConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ScopeConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ScopeConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ScopeConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
