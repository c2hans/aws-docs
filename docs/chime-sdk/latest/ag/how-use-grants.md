---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/how-use-grants.html
---

# Understanding how voice analytics uses grants
<a name="how-use-grants"></a>

Voice analytics requires a grant to use your customer managed key. When you create a voice profile domain, the associated Amazon Chime SDK Voice Connector creates a grant on your behalf by sending a `CreateGrant` request to the AWS KMS. The grant is required in order to use your key for the following internal operations:
+ Sending [https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) requests to AWS KMS to verify that the symmetric customer managed key ID provided is valid.
+ Sending [https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) requests to KMS key to create data keys with which to encrypt objects.
+ Sending [https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) requests to AWS KMS to decrypt the encrypted data keys so that they can be used to encrypt your data.
+ Sending [https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) requests to AWS KMS to retire the grants used for a voice profile domain.
+ Storing files in Amazon S3 with server side encryption.

You can revoke access to the grant, or remove the service's access to your key at any time. If you do, voice analytics won't be able to access any of the data encrypted by the key. That affects all the operations that depend on that data, leading to `AccessDeniedException` errors and failures in the speaker search workflows.
