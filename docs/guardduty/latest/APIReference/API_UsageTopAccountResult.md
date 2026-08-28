---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UsageTopAccountResult.html
---

# UsageTopAccountResult
<a name="API_UsageTopAccountResult"></a>

Contains information on the total of usage based on the topmost 50 account IDs.

## Contents
<a name="API_UsageTopAccountResult_Contents"></a>

 ** accountId **   <a name="guardduty-Type-UsageTopAccountResult-accountId"></a>
The unique account ID.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** total **   <a name="guardduty-Type-UsageTopAccountResult-total"></a>
Contains the total usage with the corresponding currency unit for that value.
Type: [Total](API_Total.md) object
Required: No

## See Also
<a name="API_UsageTopAccountResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UsageTopAccountResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UsageTopAccountResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UsageTopAccountResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
