---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_S3Storage.html
---

# S3Storage
<a name="API_S3Storage"></a>

Describes the storage parameters for Amazon S3 and Amazon S3 buckets for an instance store-backed AMI.

## Contents
<a name="API_S3Storage_Contents"></a>

 ** AWSAccessKeyId ** (request), ** AWSAccessKeyId ** (response)
The access key ID of the owner of the bucket. Before you specify a value for your access key ID, review and follow the guidance in [Best Practices for AWS accounts](https://docs.aws.amazon.com/accounts/latest/reference/best-practices.html) in the * AWS Account ManagementReference Guide*.
Type: String
Required: No

 ** Bucket ** (request), ** bucket ** (response)
The bucket in which to store the AMI. You can specify a bucket that you already own or a new bucket that Amazon EC2 creates on your behalf. If you specify a bucket that belongs to someone else, Amazon EC2 returns an error.
Type: String
Required: No

 ** Prefix ** (request), ** prefix ** (response)
The beginning of the file name of the AMI.
Type: String
Required: No

 ** UploadPolicy ** (request), ** uploadPolicy ** (response)
An Amazon S3 upload policy that gives Amazon EC2 permission to upload items into Amazon S3 on your behalf.
Type: Base64-encoded binary data object
Required: No

 ** UploadPolicySignature ** (request), ** uploadPolicySignature ** (response)
The signature of the JSON document.
Type: String
Required: No

## See Also
<a name="API_S3Storage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/S3Storage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/S3Storage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/S3Storage)
