---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StageSession.html
---

# StageSession
<a name="API_StageSession"></a>

A stage session begins when the first participant joins a stage and ends after the last participant leaves the stage. A stage session helps with debugging stages by grouping events and participants into shorter periods of time (i.e., a session), which is helpful when stages are used over long periods of time.

## Contents
<a name="API_StageSession_Contents"></a>

 ** endTime **   <a name="ivsrealtimeeapireference-Type-StageSession-endTime"></a>
ISO 8601 timestamp (returned as a string) when the stage session ended. This is null if the stage is active.
Type: Timestamp
Required: No

 ** sessionId **   <a name="ivsrealtimeeapireference-Type-StageSession-sessionId"></a>
ID of the session within the stage.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `st-[a-zA-Z0-9]+`
Required: No

 ** startTime **   <a name="ivsrealtimeeapireference-Type-StageSession-startTime"></a>
 ISO 8601 timestamp (returned as a string) when this stage session began.
Type: Timestamp
Required: No

## See Also
<a name="API_StageSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/StageSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/StageSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/StageSession)
