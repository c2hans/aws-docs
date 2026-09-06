---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_IngestConfigurationSummary.html
---

# IngestConfigurationSummary
<a name="API_IngestConfigurationSummary"></a>

Summary information about an IngestConfiguration.

## Contents
<a name="API_IngestConfigurationSummary_Contents"></a>

 ** arn **   <a name="ivsrealtimeeapireference-Type-IngestConfigurationSummary-arn"></a>
Ingest configuration ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:ingest-configuration/[a-zA-Z0-9-]+`
Required: Yes

 ** ingestProtocol **   <a name="ivsrealtimeeapireference-Type-IngestConfigurationSummary-ingestProtocol"></a>
Type of ingest protocol that the user employs for broadcasting.
Type: String
Valid Values: `RTMP | RTMPS`
Required: Yes

 ** participantId **   <a name="ivsrealtimeeapireference-Type-IngestConfigurationSummary-participantId"></a>
ID of the participant within the stage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`
Required: Yes

 ** stageArn **   <a name="ivsrealtimeeapireference-Type-IngestConfigurationSummary-stageArn"></a>
ARN of the stage with which the IngestConfiguration is associated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+$`
Required: Yes

 ** state **   <a name="ivsrealtimeeapireference-Type-IngestConfigurationSummary-state"></a>
State of the ingest configuration. It is `ACTIVE` if a publisher currently is publishing to the stage associated with the ingest configuration.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

 ** name **   <a name="ivsrealtimeeapireference-Type-IngestConfigurationSummary-name"></a>
Ingest name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** redundantIngest **   <a name="ivsrealtimeeapireference-Type-IngestConfigurationSummary-redundantIngest"></a>
Indicates whether redundant ingest is enabled for the ingest configuration.
Type: Boolean
Required: No

 ** userId **   <a name="ivsrealtimeeapireference-Type-IngestConfigurationSummary-userId"></a>
Customer-assigned name to help identify the participant using the IngestConfiguration; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## See Also
<a name="API_IngestConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/IngestConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/IngestConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/IngestConfigurationSummary)
