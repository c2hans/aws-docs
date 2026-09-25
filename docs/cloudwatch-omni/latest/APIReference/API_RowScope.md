---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_RowScope.html
---

# RowScope
<a name="API_RowScope"></a>

A single additive row-level filter on an AccessGrant. A row is visible when its value for the given field matches the filter's values. Row filters are additive: the visible rows are the union of all row filters across a principal's matching grants.

## Contents
<a name="API_RowScope_Contents"></a>

 ** field **   <a name="cloudwatchomni-Type-RowScope-field"></a>
The field (column) the allowlist applies to (e.g., "serviceName", "accountId").
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** operator **   <a name="cloudwatchomni-Type-RowScope-operator"></a>
Match operator applied to this filter's values.
Type: String
Valid Values: `IN`
Required: Yes

 ** values **   <a name="cloudwatchomni-Type-RowScope-values"></a>
The values the field is matched against.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_RowScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/RowScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/RowScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/RowScope)
