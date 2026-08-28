---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/how-encrypted.html
---

# Understanding encryption at rest
<a name="how-encrypted"></a>

By default, voice analytics encrypts all user data at rest. When creating a new voice profile domain, you must provide a symmetric customer managed key that the service uses to encrypt your data at rest. You own, manage and control the key.

The key only encrypts the audio files used to enroll speakers in voice embeddings.

Voice analytics accesses the key by creating grants. For more information about grants, see the next section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
