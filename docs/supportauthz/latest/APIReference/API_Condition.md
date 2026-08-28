---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_Condition.html
---

# Condition
<a name="API_Condition"></a>

A time-window condition that constrains when a support permit is valid.

## Contents
<a name="API_Condition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** allowAfter **   <a name="supportauthorization-Type-Condition-allowAfter"></a>
The earliest time at which the permit becomes valid.
Type: Timestamp
Required: No

 ** allowBefore **   <a name="supportauthorization-Type-Condition-allowBefore"></a>
The latest time at which the permit remains valid.
Type: Timestamp
Required: No

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/Condition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/Condition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/Condition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support authorization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query supportauthz` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
