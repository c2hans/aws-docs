---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_AggregatorFilterResourceType.html
---

# AggregatorFilterResourceType
<a name="API_AggregatorFilterResourceType"></a>

An object to filter the configuration recorders based on the resource types in scope for recording.

## Contents
<a name="API_AggregatorFilterResourceType_Contents"></a>

 ** Type **   <a name="config-Type-AggregatorFilterResourceType-Type"></a>
The type of resource type filter to apply. `INCLUDE` specifies that the list of resource types in the `Value` field will be aggregated and no other resource types will be filtered.
Type: String
Valid Values: `INCLUDE`
Required: No

 ** Value **   <a name="config-Type-AggregatorFilterResourceType-Value"></a>
Comma-separate list of resource types to filter your aggregated configuration recorders.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}`
Required: No

## See Also
<a name="API_AggregatorFilterResourceType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/AggregatorFilterResourceType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/AggregatorFilterResourceType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/AggregatorFilterResourceType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
