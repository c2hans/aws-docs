---
source_url: https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_RuleSummary.html
---

# RuleSummary
<a name="API_RuleSummary"></a>

Information about a Recycle Bin retention rule.

## Contents
<a name="API_RuleSummary_Contents"></a>

 ** Description **   <a name="recyclebin-Type-RuleSummary-Description"></a>
The retention rule description.
Type: String
Pattern: `^[\S ]{0,255}$`
Required: No

 ** Identifier **   <a name="recyclebin-Type-RuleSummary-Identifier"></a>
The unique ID of the retention rule.
Type: String
Pattern: `[0-9a-zA-Z]{11}`
Required: No

 ** LockState **   <a name="recyclebin-Type-RuleSummary-LockState"></a>
[Region-level retention rules only] The lock state for the retention rule.
+  `locked` - The retention rule is locked and can't be modified or deleted.
+  `pending_unlock` - The retention rule has been unlocked but it is still within the unlock delay period. The retention rule can be modified or deleted only after the unlock delay period has expired.
+  `unlocked` - The retention rule is unlocked and it can be modified or deleted by any user with the required permissions.
+  `null` - The retention rule has never been locked. Once a retention rule has been locked, it can transition between the `locked` and `unlocked` states only; it can never transition back to `null`.
Type: String
Valid Values: `locked | pending_unlock | unlocked`
Required: No

 ** RetentionPeriod **   <a name="recyclebin-Type-RuleSummary-RetentionPeriod"></a>
Information about the retention period for which the retention rule is to retain resources.
Type: [RetentionPeriod](API_RetentionPeriod.md) object
Required: No

 ** RuleArn **   <a name="recyclebin-Type-RuleSummary-RuleArn"></a>
The Amazon Resource Name (ARN) of the retention rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1011.
Pattern: `^arn:\S+:rbin:[a-z\-0-9]{0,63}:[0-9]{12}:rule/[0-9a-zA-Z]{11}{0,1011}$`
Required: No

## See Also
<a name="API_RuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rbin-2021-06-15/RuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rbin-2021-06-15/RuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rbin-2021-06-15/RuleSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Recycle Bin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recyclebin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
