---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_SyncBlockerSummary.html
---

# SyncBlockerSummary
<a name="API_SyncBlockerSummary"></a>

A summary for sync blockers.

## Contents
<a name="API_SyncBlockerSummary_Contents"></a>

 ** ResourceName **   <a name="codeconnections-Type-SyncBlockerSummary-ResourceName"></a>
The resource name for sync blocker summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`
Required: Yes

 ** LatestBlockers **   <a name="codeconnections-Type-SyncBlockerSummary-LatestBlockers"></a>
The latest events for a sync blocker summary.
Type: Array of [SyncBlocker](API_SyncBlocker.md) objects
Required: No

 ** ParentResourceName **   <a name="codeconnections-Type-SyncBlockerSummary-ParentResourceName"></a>
The parent resource name for a sync blocker summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`
Required: No

## See Also
<a name="API_SyncBlockerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/SyncBlockerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/SyncBlockerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/SyncBlockerSummary)
