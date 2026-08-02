---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemoveTargetsResultEntry.html
---

# RemoveTargetsResultEntry
<a name="API_RemoveTargetsResultEntry"></a>

Represents a target that failed to be removed from a rule.

## Contents
<a name="API_RemoveTargetsResultEntry_Contents"></a>

 ** ErrorCode **   <a name="eventbridge-Type-RemoveTargetsResultEntry-ErrorCode"></a>
The error code that indicates why the target removal failed. If the value is `ConcurrentModificationException`, too many requests were made at the same time.
Type: String
Required: No

 ** ErrorMessage **   <a name="eventbridge-Type-RemoveTargetsResultEntry-ErrorMessage"></a>
The error message that explains why the target removal failed.
Type: String
Required: No

 ** TargetId **   <a name="eventbridge-Type-RemoveTargetsResultEntry-TargetId"></a>
The ID of the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

## See Also
<a name="API_RemoveTargetsResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/RemoveTargetsResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/RemoveTargetsResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/RemoveTargetsResultEntry)
