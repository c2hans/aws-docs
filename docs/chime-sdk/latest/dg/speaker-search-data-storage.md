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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
