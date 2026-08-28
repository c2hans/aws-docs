---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutTargetsResultEntry.html
---

# PutTargetsResultEntry
<a name="API_PutTargetsResultEntry"></a>

Represents a target that failed to be added to a rule.

## Contents
<a name="API_PutTargetsResultEntry_Contents"></a>

 ** ErrorCode **   <a name="eventbridge-Type-PutTargetsResultEntry-ErrorCode"></a>
The error code that indicates why the target addition failed. If the value is `ConcurrentModificationException`, too many requests were made at the same time.
Type: String
Required: No

 ** ErrorMessage **   <a name="eventbridge-Type-PutTargetsResultEntry-ErrorMessage"></a>
The error message that explains why the target addition failed.
Type: String
Required: No

 ** TargetId **   <a name="eventbridge-Type-PutTargetsResultEntry-TargetId"></a>
The ID of the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

## See Also
<a name="API_PutTargetsResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/PutTargetsResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/PutTargetsResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/PutTargetsResultEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
