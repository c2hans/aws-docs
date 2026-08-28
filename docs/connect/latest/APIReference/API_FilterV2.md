---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_FilterV2.html
---

# FilterV2
<a name="API_FilterV2"></a>

Contains the filter to apply when retrieving metrics with the [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html) API.

## Contents
<a name="API_FilterV2_Contents"></a>

 ** FilterKey **   <a name="connect-Type-FilterV2-FilterKey"></a>
The key to use for filtering data. For example, `QUEUE`, `ROUTING_PROFILE, AGENT`, `CHANNEL`, `AGENT_HIERARCHY_LEVEL_ONE`, `AGENT_HIERARCHY_LEVEL_TWO`, `AGENT_HIERARCHY_LEVEL_THREE`, `AGENT_HIERARCHY_LEVEL_FOUR`, `AGENT_HIERARCHY_LEVEL_FIVE`. There must be at least 1 key and a maximum 5 keys.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** FilterValues **   <a name="connect-Type-FilterV2-FilterValues"></a>
The identifiers to use for filtering data. For example, if you have a filter key of `QUEUE`, you would add queue IDs or ARNs in `FilterValues`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** StringCondition **   <a name="connect-Type-FilterV2-StringCondition"></a>
 System defined filtering condition. For example, the NOT\_EXISTS StringCondition returns documents where the field specified by FilterKey does not exist in the document.
When the NOT\_EXISTS StringCondition is added to a FilterV2 object, FilterValues must be null or empty.
Type: [FilterV2StringCondition](API_FilterV2StringCondition.md) object
Required: No

## See Also
<a name="API_FilterV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/FilterV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/FilterV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/FilterV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
