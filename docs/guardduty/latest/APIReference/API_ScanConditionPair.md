---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ScanConditionPair.html
---

# ScanConditionPair
<a name="API_ScanConditionPair"></a>

Represents the `key:value` pair to be matched against given resource property.

## Contents
<a name="API_ScanConditionPair_Contents"></a>

 ** key **   <a name="guardduty-Type-ScanConditionPair-key"></a>
Represents the **key** in the map condition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Required: Yes

 ** value **   <a name="guardduty-Type-ScanConditionPair-value"></a>
Represents optional **value** in the map condition. If not specified, only the **key** will be matched.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_ScanConditionPair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ScanConditionPair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ScanConditionPair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ScanConditionPair)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
