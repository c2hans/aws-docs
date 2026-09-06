---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_SyncBlocker.html
---

# SyncBlocker
<a name="API_SyncBlocker"></a>

Information about a blocker for a sync event.

## Contents
<a name="API_SyncBlocker_Contents"></a>

 ** CreatedAt **   <a name="codeconnections-Type-SyncBlocker-CreatedAt"></a>
The creation time for a specific sync blocker.
Type: Timestamp
Required: Yes

 ** CreatedReason **   <a name="codeconnections-Type-SyncBlocker-CreatedReason"></a>
The provided reason for a specific sync blocker.
Type: String
Required: Yes

 ** Id **   <a name="codeconnections-Type-SyncBlocker-Id"></a>
The ID for a specific sync blocker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** Status **   <a name="codeconnections-Type-SyncBlocker-Status"></a>
The status for a specific sync blocker.
Type: String
Valid Values: `ACTIVE | RESOLVED`
Required: Yes

 ** Type **   <a name="codeconnections-Type-SyncBlocker-Type"></a>
The sync blocker type.
Type: String
Valid Values: `AUTOMATED`
Required: Yes

 ** Contexts **   <a name="codeconnections-Type-SyncBlocker-Contexts"></a>
The contexts for a specific sync blocker.
Type: Array of [SyncBlockerContext](API_SyncBlockerContext.md) objects
Required: No

 ** ResolvedAt **   <a name="codeconnections-Type-SyncBlocker-ResolvedAt"></a>
The time that a specific sync blocker was resolved.
Type: Timestamp
Required: No

 ** ResolvedReason **   <a name="codeconnections-Type-SyncBlocker-ResolvedReason"></a>
The resolved reason for a specific sync blocker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

## See Also
<a name="API_SyncBlocker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/SyncBlocker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/SyncBlocker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/SyncBlocker)
