---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Stage.html
---

# Stage
<a name="API_Stage"></a>

Object specifying a stage.

## Contents
<a name="API_Stage_Contents"></a>

 ** arn **   <a name="ivsrealtimeeapireference-Type-Stage-arn"></a>
Stage ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

 ** activeSessionId **   <a name="ivsrealtimeeapireference-Type-Stage-activeSessionId"></a>
ID of the active session within the stage.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `st-[a-zA-Z0-9]+`
Required: No

 ** autoParticipantRecordingConfiguration **   <a name="ivsrealtimeeapireference-Type-Stage-autoParticipantRecordingConfiguration"></a>
Configuration object for individual participant recording, attached to the stage.
Type: [AutoParticipantRecordingConfiguration](API_AutoParticipantRecordingConfiguration.md) object
Required: No

 ** endpoints **   <a name="ivsrealtimeeapireference-Type-Stage-endpoints"></a>
Summary information about various endpoints for a stage.
Type: [StageEndpoints](API_StageEndpoints.md) object
Required: No

 ** name **   <a name="ivsrealtimeeapireference-Type-Stage-name"></a>
Stage name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** tags **   <a name="ivsrealtimeeapireference-Type-Stage-tags"></a>
Tags attached to the resource. Array of maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Stage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/Stage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/Stage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/Stage)
