---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/client-server-side.html
---

# Client-side and server-side encryption
<a name="client-server-side"></a>

**Note**
This documentation describes the Amazon S3 Encryption Client version 3.*x* and newer, which is an independent library. For information about previous versions of the Amazon S3 Encryption Client, see the AWS SDK Developer Guide for your programming language.

The Amazon S3 Encryption Client supports *client-side encryption*, where you encrypt your objects before you send them to Amazon S3. Amazon S3 provides server-side encryption options that encrypt your objects at their destination before they are saved in Amazon S3.

The tools that you choose depend on your security requirements and the sensitivity of your data. You can use both the Amazon S3 Encryption Client and Amazon S3 server-side encryption. When you send encrypted objects to Amazon S3, Amazon S3 doesn't recognize the objects as being encrypted, it just detects typical objects.

**Server-side encryption**

Amazon S3 supports encryption at rest with three mutually exclusive [server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) options. Amazon S3 encrypts your data at the object level as it writes it to disks in its data centers and decrypts it for you when you access it.

**Amazon S3 Encryption Client**

Client-side encryption provides end-to-end protection for your object, in transit and at rest, from its source to storage in Amazon S3.
+ Your data is protected in transit and at rest. It is never exposed to any third party, including AWS.
+ You choose how your cryptographic keys are protected. You specify the wrapping key used to protect the data keys that encrypt your objects.
+ Your objects are all encrypted with a unique data key. The Amazon S3 Encryption Client does not use or interact with [bucket keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html#sse-kms-bucket-keys), even if you specify a KMS key as your wrapping key.
