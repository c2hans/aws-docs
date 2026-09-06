---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/analytics-encryption.html
---

# Using encryption with voice analytics
<a name="analytics-encryption"></a>

Amazon Chime SDK voice analytics stores the audio files used to generate voice embedding. The files are encrypted using a symmetric customer managed key that you create, own, and manage. Because you have full control over this layer of encryption, you can perform such tasks as:
+ Establishing and maintaining key policies
+ Establishing and maintaining IAM policies and grants
+ Enabling and disabling key policies
+ Rotating key cryptographic material
+ Adding tags
+ Creating key aliases
+ Scheduling keys for deletion

For more information, see [ Customer managed keys ](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the *AWS Key Management Service Developer Guide*.
