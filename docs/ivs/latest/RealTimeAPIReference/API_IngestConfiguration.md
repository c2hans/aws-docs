---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_IngestConfiguration.html
---

# IngestConfiguration
<a name="API_IngestConfiguration"></a>

Object specifying an ingest configuration.

## Contents
<a name="API_IngestConfiguration_Contents"></a>

 ** arn **   <a name="ivsrealtimeeapireference-Type-IngestConfiguration-arn"></a>
Ingest configuration ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:ingest-configuration/[a-zA-Z0-9-]+`
Required: Yes

 ** ingestProtocol **   <a name="ivsrealtimeeapireference-Type-IngestConfiguration-ingestProtocol"></a>
Type of ingest protocol that the user employs for broadcasting.
Type: String
Valid Values: `RTMP | RTMPS`
Required: Yes

 ** participantId **   <a name="ivsrealtimeeapireference-Type-IngestConfiguration-participantId"></a>
ID of the participant within the stage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]*`
Required: Yes

 ** stageArn **   <a name="ivsrealtimeeapireference-Type-IngestConfiguration-stageArn"></a>
ARN of the stage with which the IngestConfiguration is associated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+$`
Required: Yes

 ** state **   <a name="ivsrealtimeeapireference-Type-IngestConfiguration-state"></a>
State of the ingest configuration. It is `ACTIVE` if a publisher currently is publishing to the stage associated with the ingest configuration.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

 ** streamKey **   <a name="ivsrealtimeeapireference-Type-IngestConfiguration-streamKey"></a>
Ingest-key value for the RTMP(S) protocol.
Type: String
Pattern: `rt_[0-9]+_[a-z0-9-]+_[a-zA-Z0-9-]+_.+`
Required: Yes

 ** attributes **   <a name="ivsrealtimeeapireference-Type-IngestConfiguration-attributes"></a>
Application-provided attributes to to store in the IngestConfiguration and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
Type: String to string map
Required: No

 ** name **   <a name="ivsrealtimeeapireference-Type-IngestConfiguration-name"></a>
Ingest name
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** redundantIngest **   <a name="ivsrealtimeeapireference-Type-IngestConfiguration-redundantIngest"></a>
Indicates whether redundant ingest is enabled for the ingest configuration.
Type: Boolean
Required: No

 ** redundantIngestCredentials **   <a name="ivsrealtimeeapireference-Type-IngestConfiguration-redundantIngestCredentials"></a>
A list of redundant ingest credentials, present only when `redundantIngest` is set to `true`. See [Redundant Ingest](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html#redundant-ingest) in *IVS RTMP Publishing* for details.
Type: Array of [RedundantIngestCredential](API_RedundantIngestCredential.md) objects
Required: No

 ** tags **   <a name="ivsrealtimeeapireference-Type-IngestConfiguration-tags"></a>
Tags attached to the resource. Array of maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** userId **   <a name="ivsrealtimeeapireference-Type-IngestConfiguration-userId"></a>
Customer-assigned name to help identify the participant using the IngestConfiguration; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## See Also
<a name="API_IngestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/IngestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/IngestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/IngestConfiguration)
