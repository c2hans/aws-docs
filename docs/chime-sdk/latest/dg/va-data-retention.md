---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/va-data-retention.html
---

# Understanding data retention for Amazon Chime SDK voice analytics
<a name="va-data-retention"></a>

By default, Amazon Chime SDK voice analytics deletes voice embeddings after 3 years. We do this because people’s voices change over time, and also for security. You can use the [UpdateVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceProfile.html) API to update expired voice embeddings.

Results from [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StartSpeakerSearchTask.html) and [StartVoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StartVoiceToneAnalysisTask.html) will also be available from their respective [GetSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSpeakerSearchTask.html) and [GetVoiceToneAnalytisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceToneAnalysisTask.html) APIs for a maximum of 7 days.

Voice embeddings generated from a [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StartSpeakerSearchTask.html) are available for persistence via the [CreateVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceProfile.html) and [UpdateVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceProfile.html) APIs for 24 hours, after which they're deleted and not available.

To remove results, and to handle consent withdrawals from your customers, see the previous section.
