---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/speaker-search-data-storage.html
---

# Understanding data storage for speaker search for the Amazon Chime SDK
<a name="speaker-search-data-storage"></a>

The Amazon Chime SDK stores the following data for speaker search:
+ The voice embeddings attached to the voice profiles that we use to provide the speaker search functionality.
+ Enrollment audio, the recorded snippets of speech used to create the voice embeddings for each voice profile. We use the enrollment audio recordings to:
  + Keep the speaker search models up to date, a critical part of providing the speaker search feature.
  + Train the machine learning model to develop and improve the service. The use of enrollment audio for training is optional, and you can opt out of this use by selecting an opt-out policy as described in the following section.
