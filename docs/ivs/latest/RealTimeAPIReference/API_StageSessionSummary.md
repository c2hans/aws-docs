---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StageSessionSummary.html
---

# StageSessionSummary
<a name="API_StageSessionSummary"></a>

Summary information about a stage session.

## Contents
<a name="API_StageSessionSummary_Contents"></a>

 ** endTime **   <a name="ivsrealtimeeapireference-Type-StageSessionSummary-endTime"></a>
ISO 8601 timestamp (returned as a string) when the stage session ended. This is null if the stage is active.
Type: Timestamp
Required: No

 ** sessionId **   <a name="ivsrealtimeeapireference-Type-StageSessionSummary-sessionId"></a>
ID of the session within the stage.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `st-[a-zA-Z0-9]+`
Required: No

 ** startTime **   <a name="ivsrealtimeeapireference-Type-StageSessionSummary-startTime"></a>
 ISO 8601 timestamp (returned as a string) when this stage session began.
Type: Timestamp
Required: No

## See Also
<a name="API_StageSessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/StageSessionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/StageSessionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/StageSessionSummary)
