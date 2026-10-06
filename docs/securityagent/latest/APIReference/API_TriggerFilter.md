---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_TriggerFilter.html
---

# TriggerFilter
<a name="API_TriggerFilter"></a>

A condition on a pull request value.

## Contents
<a name="API_TriggerFilter_Contents"></a>

 ** patterns **   <a name="securityagent-Type-TriggerFilter-patterns"></a>
The regular expressions to match against the value.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\x00-\x1F\x7F-\x9F]+`
Required: Yes

 ** type **   <a name="securityagent-Type-TriggerFilter-type"></a>
The pull request value to match.
Type: String
Valid Values: `TARGET_BRANCH | LABEL`
Required: Yes

 ** matchMode **   <a name="securityagent-Type-TriggerFilter-matchMode"></a>
Whether the value must match the patterns. The default is `INCLUDE`.
Type: String
Valid Values: `INCLUDE | EXCLUDE`
Required: No

## See Also
<a name="API_TriggerFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/TriggerFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/TriggerFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/TriggerFilter)
