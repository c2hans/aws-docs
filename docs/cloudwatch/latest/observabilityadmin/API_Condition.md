---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_Condition.html
---

# Condition
<a name="API_Condition"></a>

 A single condition that can match based on WAF rule action or label name.

## Contents
<a name="API_Condition_Contents"></a>

 ** ActionCondition **   <a name="cwoa-Type-Condition-ActionCondition"></a>
 Matches log records based on the WAF rule action taken (ALLOW, BLOCK, COUNT, etc.).
Type: [ActionCondition](API_ActionCondition.md) object
Required: No

 ** LabelNameCondition **   <a name="cwoa-Type-Condition-LabelNameCondition"></a>
 Matches log records based on WAF rule labels applied to the request.
Type: [LabelNameCondition](API_LabelNameCondition.md) object
Required: No

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/Condition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/Condition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/Condition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
