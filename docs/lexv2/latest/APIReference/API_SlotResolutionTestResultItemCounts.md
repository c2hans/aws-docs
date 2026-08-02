---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotResolutionTestResultItemCounts.html
---

# SlotResolutionTestResultItemCounts
<a name="API_SlotResolutionTestResultItemCounts"></a>

Information about the counts for a slot resolution in the results of a test execution.

## Contents
<a name="API_SlotResolutionTestResultItemCounts_Contents"></a>

 ** slotMatchResultCounts **   <a name="lexv2-Type-SlotResolutionTestResultItemCounts-slotMatchResultCounts"></a>
The number of matched and mismatched results for slot resolution for the slot.
Type: String to integer map
Valid Keys: `Matched | Mismatched | ExecutionError`
Required: Yes

 ** totalResultCount **   <a name="lexv2-Type-SlotResolutionTestResultItemCounts-totalResultCount"></a>
The total number of results.
Type: Integer
Required: Yes

 ** speechTranscriptionResultCounts **   <a name="lexv2-Type-SlotResolutionTestResultItemCounts-speechTranscriptionResultCounts"></a>
The number of matched, mismatched and execution error results for speech transcription for the slot.
Type: String to integer map
Valid Keys: `Matched | Mismatched | ExecutionError`
Required: No

## See Also
<a name="API_SlotResolutionTestResultItemCounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SlotResolutionTestResultItemCounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SlotResolutionTestResultItemCounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SlotResolutionTestResultItemCounts)
