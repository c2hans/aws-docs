---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_AlertFilterCriteria.html
---

# AlertFilterCriteria
<a name="API_AlertFilterCriteria"></a>

Filter criteria for ListAlerts. All members are optional; each omitted member is unconstrained. At most one of `names`, `namePrefix`, `ids` may be provided (mutually exclusive; the service rejects more than one). The remaining members combine with AND.

## Contents
<a name="API_AlertFilterCriteria_Contents"></a>

 ** ids **   <a name="cloudwatchomni-Type-AlertFilterCriteria-ids"></a>
Filter to alerts whose `AlertId` exactly matches any entry (OR semantics). Mutually exclusive with `names` and `namePrefix`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

 ** namePrefix **   <a name="cloudwatchomni-Type-AlertFilterCriteria-namePrefix"></a>
Filter to alerts whose name starts with this prefix. Mutually exclusive with `names` and `ids`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.@~()-]+`
Required: No

 ** names **   <a name="cloudwatchomni-Type-AlertFilterCriteria-names"></a>
Filter to alerts whose name exactly matches any entry (OR semantics). Mutually exclusive with `namePrefix` and `ids`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.@~()-]+`
Required: No

 ** notificationsEnabled **   <a name="cloudwatchomni-Type-AlertFilterCriteria-notificationsEnabled"></a>
Filter to alerts by whether notifications are enabled.
Type: Boolean
Required: No

 ** stateValue **   <a name="cloudwatchomni-Type-AlertFilterCriteria-stateValue"></a>
Filter to alerts currently in any of these states (OR semantics).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Valid Values: `OK | WARNING | CRITICAL | NODATA`
Required: No

## See Also
<a name="API_AlertFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/AlertFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/AlertFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/AlertFilterCriteria)
