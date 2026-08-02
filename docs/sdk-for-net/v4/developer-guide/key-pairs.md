---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/key-pairs.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Working with Amazon EC2 key pairs
<a name="key-pairs"></a>

Amazon EC2 uses public–key cryptography to encrypt and decrypt login information. Public–key cryptography uses a public key to encrypt data, and then the recipient uses the private key to decrypt the data. The public and private keys are known as a key pair. If you want to log into an EC2 instance, you must specify a key pair when you launch it, and then provide the private key of the pair when you connect to it.

When you launch an EC2 instance, you can create a key pair for it or use one that you've already used when launching other instances. To read more about Amazon EC2 key pairs, see [Working with Amazon EC2 key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the [Amazon EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/).

For information about the APIs and prerequisites, see the parent section ([Working with Amazon EC2](ec2-apis-intro.md)).

**Topics**
+ [Creating and displaying key pairs](create-save-key-pair.md)
+ [Deleting key pairs](delete-key-pairs.md)
