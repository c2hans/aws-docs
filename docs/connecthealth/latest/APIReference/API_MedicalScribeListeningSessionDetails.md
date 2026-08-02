---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeListeningSessionDetails.html
---

# MedicalScribeListeningSessionDetails
<a name="API_MedicalScribeListeningSessionDetails"></a>

Detailed information about a Medical Scribe listening session

## Contents
<a name="API_MedicalScribeListeningSessionDetails_Contents"></a>

 ** channelDefinitions **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-channelDefinitions"></a>
Channel definitions for the audio stream
Type: Array of [MedicalScribeChannelDefinition](API_MedicalScribeChannelDefinition.md) objects
Array Members: Fixed number of 2 items.
Required: No

 ** domainId **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-domainId"></a>
The Domain identifier
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: No

 ** encounterContextProvided **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-encounterContextProvided"></a>
Indicates whether encounter context was provided
Type: Boolean
Required: No

 ** languageCode **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-languageCode"></a>
The Language Code for the audio in the session
Type: String
Valid Values: `en-US`
Required: No

 ** mediaEncoding **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-mediaEncoding"></a>
The encoding for the input audio
Type: String
Valid Values: `pcm | flac`
Required: No

 ** mediaSampleRateHertz **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-mediaSampleRateHertz"></a>
The sample rate of the input audio
Type: Integer
Valid Range: Minimum value of 8000. Maximum value of 48000.
Required: No

 ** postStreamActionResult **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-postStreamActionResult"></a>
Results of post-stream actions
Type: [MedicalScribePostStreamActionsResult](API_MedicalScribePostStreamActionsResult.md) object
Required: No

 ** postStreamActionSettings **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-postStreamActionSettings"></a>
Settings for post-stream actions
Type: [MedicalScribePostStreamActionSettingsResponse](API_MedicalScribePostStreamActionSettingsResponse.md) object
Required: No

 ** sessionId **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-sessionId"></a>
The Session identifier
Type: String
Length Constraints: Fixed length of 36.
Pattern: `.*[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}.*`
Required: No

 ** streamCreationTime **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-streamCreationTime"></a>
The timestamp when the stream was created
Type: Timestamp
Required: No

 ** streamEndTime **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-streamEndTime"></a>
The timestamp when the stream ended
Type: Timestamp
Required: No

 ** streamStatus **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-streamStatus"></a>
The current status of the stream
Type: String
Valid Values: `IN_PROGRESS | PAUSED | FAILED | COMPLETED`
Required: No

 ** subscriptionId **   <a name="connecthealth-Type-MedicalScribeListeningSessionDetails-subscriptionId"></a>
The Subscription identifier
Type: String
Length Constraints: Fixed length of 25.
Pattern: `sub-[a-zA-Z0-9]{21}`
Required: No

## See Also
<a name="API_MedicalScribeListeningSessionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalScribeListeningSessionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalScribeListeningSessionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalScribeListeningSessionDetails)
