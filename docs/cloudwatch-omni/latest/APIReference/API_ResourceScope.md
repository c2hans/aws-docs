---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ResourceScope.html
---

# ResourceScope
<a name="API_ResourceScope"></a>

A single resource scope entry within an AccessGrant. Associates a resource type with optional ARN patterns, tag conditions, and row-level filters.

## Contents
<a name="API_ResourceScope_Contents"></a>

 ** resourceType **   <a name="cloudwatchomni-Type-ResourceScope-resourceType"></a>
Resource type name (e.g., "DataSet", "OmniDashboard").
Type: String
Required: Yes

 ** resourceArns **   <a name="cloudwatchomni-Type-ResourceScope-resourceArns"></a>
Specific resource ARNs or ARN patterns. When set, actions are limited to these resources. When absent, defaults to "\*".
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** rowScopeGroups **   <a name="cloudwatchomni-Type-ResourceScope-rowScopeGroups"></a>
Row-level filters for this scope, as an OR of AND-groups: a row is visible when it matches every filter in any one group. Requires signalTypes.
Row filters are additive across a principal's matching grants. A signal type with no matching group is unrestricted, and when rowScopeGroups is omitted all rows are visible for all signal types.
Type: Array of arrays of [RowScope](API_RowScope.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** signalTypes **   <a name="cloudwatchomni-Type-ResourceScope-signalTypes"></a>
Signal types this scope's row filtering applies to. Required when rowScopeGroups is set.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `LOGS | TRACES`
Required: No

 ** tags **   <a name="cloudwatchomni-Type-ResourceScope-tags"></a>
Tag-based conditions for dynamic resource scoping. Access applies only to resources carrying all of the specified tag key/value pairs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 3 items.
Required: No

## See Also
<a name="API_ResourceScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ResourceScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ResourceScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ResourceScope)
