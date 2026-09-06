---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectionRuleFilter.html
---

# DetectionRuleFilter
<a name="API_DetectionRuleFilter"></a>

Contains filter criteria for listing custom detection rules or associations.

## Contents
<a name="API_DetectionRuleFilter_Contents"></a>

 ** name **   <a name="guardduty-Type-DetectionRuleFilter-name"></a>
The name of the field to filter by.
Type: String
Valid Values: `name | description | dataSource | severity | tactic | technique | service`
Required: Yes

 ** values **   <a name="guardduty-Type-DetectionRuleFilter-values"></a>
The values to match against the specified filter name.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9 _.\-:/]+`
Required: Yes

 ** condition **   <a name="guardduty-Type-DetectionRuleFilter-condition"></a>
The condition to apply to the filter. For example, `EQUALS` or `CONTAINS`.
Type: String
Valid Values: `EQUALS | CONTAINS`
Required: No

## See Also
<a name="API_DetectionRuleFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DetectionRuleFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DetectionRuleFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DetectionRuleFilter)
