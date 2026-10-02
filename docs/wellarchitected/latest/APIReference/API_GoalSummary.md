---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GoalSummary.html
---

# GoalSummary
<a name="API_GoalSummary"></a>

Summary of an optimization goal associated with a profile.

## Contents
<a name="API_GoalSummary_Contents"></a>

 ** createdAt **   <a name="wellarchitected-Type-GoalSummary-createdAt"></a>
The timestamp when the goal was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="wellarchitected-Type-GoalSummary-createdBy"></a>
The identifier of the user or system that created this goal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** id **   <a name="wellarchitected-Type-GoalSummary-id"></a>
The unique identifier of the goal.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** pillars **   <a name="wellarchitected-Type-GoalSummary-pillars"></a>
The AWS Well-Architected Framework pillars associated with this goal.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: Yes

 ** profileArn **   <a name="wellarchitected-Type-GoalSummary-profileArn"></a>
The Amazon Resource Name (ARN) of the associated profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

 ** title **   <a name="wellarchitected-Type-GoalSummary-title"></a>
The title of the goal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: Yes

 ** description **   <a name="wellarchitected-Type-GoalSummary-description"></a>
A description of the goal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: No

 ** lastModifiedAt **   <a name="wellarchitected-Type-GoalSummary-lastModifiedAt"></a>
The timestamp when the goal was last modified.
Type: Timestamp
Required: No

 ** lastModifiedBy **   <a name="wellarchitected-Type-GoalSummary-lastModifiedBy"></a>
The identifier of the user or system that last modified this goal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_GoalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GoalSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GoalSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GoalSummary)
