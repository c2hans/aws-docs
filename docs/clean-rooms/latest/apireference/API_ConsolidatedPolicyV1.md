---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConsolidatedPolicyV1.html
---

# ConsolidatedPolicyV1
<a name="API_ConsolidatedPolicyV1"></a>

Controls on the analysis specifications that can be run on a configured table.

## Contents
<a name="API_ConsolidatedPolicyV1_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** aggregation **   <a name="API-Type-ConsolidatedPolicyV1-aggregation"></a>
 The aggregation setting for the consolidated policy.
Type: [ConsolidatedPolicyAggregation](API_ConsolidatedPolicyAggregation.md) object
Required: No

 ** custom **   <a name="API-Type-ConsolidatedPolicyV1-custom"></a>
 Custom policy
Type: [ConsolidatedPolicyCustom](API_ConsolidatedPolicyCustom.md) object
Required: No

 ** list **   <a name="API-Type-ConsolidatedPolicyV1-list"></a>
 The list of consolidated policies.
Type: [ConsolidatedPolicyList](API_ConsolidatedPolicyList.md) object
Required: No

## See Also
<a name="API_ConsolidatedPolicyV1_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConsolidatedPolicyV1)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConsolidatedPolicyV1)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConsolidatedPolicyV1)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
