---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/how-encrypted.html
---

# Understanding encryption at rest
<a name="how-encrypted"></a>

By default, voice analytics encrypts all user data at rest. When creating a new voice profile domain, you must provide a symmetric customer managed key that the service uses to encrypt your data at rest. You own, manage and control the key.

The key only encrypts the audio files used to enroll speakers in voice embeddings.

Voice analytics accesses the key by creating grants. For more information about grants, see the next section.
