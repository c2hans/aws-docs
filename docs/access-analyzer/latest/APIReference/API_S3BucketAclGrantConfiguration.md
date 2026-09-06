---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_S3BucketAclGrantConfiguration.html
---

# S3BucketAclGrantConfiguration
<a name="API_S3BucketAclGrantConfiguration"></a>

A proposed access control list grant configuration for an Amazon S3 bucket. For more information, see [How to Specify an ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#setting-acls).

## Contents
<a name="API_S3BucketAclGrantConfiguration_Contents"></a>

 ** grantee **   <a name="accessanalyzer-Type-S3BucketAclGrantConfiguration-grantee"></a>
The grantee to whom you’re assigning access rights.
Type: [AclGrantee](API_AclGrantee.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** permission **   <a name="accessanalyzer-Type-S3BucketAclGrantConfiguration-permission"></a>
The permissions being granted.
Type: String
Valid Values: `READ | WRITE | READ_ACP | WRITE_ACP | FULL_CONTROL`
Required: Yes

## See Also
<a name="API_S3BucketAclGrantConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/S3BucketAclGrantConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/S3BucketAclGrantConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/S3BucketAclGrantConfiguration)
