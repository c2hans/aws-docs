---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_PublicAccessBlockConfiguration.html
---

# PublicAccessBlockConfiguration
<a name="API_PublicAccessBlockConfiguration"></a>

The PublicAccessBlock configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Bucket-level settings work alongside account-level settings (which may inherit from organization-level policies). For more information about when Amazon S3 considers a bucket or object public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status) in the *Amazon S3 User Guide*.

## Contents
<a name="API_PublicAccessBlockConfiguration_Contents"></a>

 ** BlockPublicAcls **   <a name="AmazonS3-Type-PublicAccessBlockConfiguration-BlockPublicAcls"></a>
Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket and objects in this bucket. Setting this element to `TRUE` causes the following behavior:
+ PUT Bucket ACL and PUT Object ACL calls fail if the specified ACL is public.
+ PUT Object calls fail if the request includes a public ACL.
+ PUT Bucket calls fail if the request includes a public ACL.
Enabling this setting doesn't affect existing policies or ACLs.
Type: Boolean
Required: No

 ** BlockPublicPolicy **   <a name="AmazonS3-Type-PublicAccessBlockConfiguration-BlockPublicPolicy"></a>
Specifies whether Amazon S3 should block public bucket policies for this bucket. Setting this element to `TRUE` causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.
Enabling this setting doesn't affect existing bucket policies.
Type: Boolean
Required: No

 ** IgnorePublicAcls **   <a name="AmazonS3-Type-PublicAccessBlockConfiguration-IgnorePublicAcls"></a>
Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket. Setting this element to `TRUE` causes Amazon S3 to ignore all public ACLs on this bucket and objects in this bucket.
Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set.
Type: Boolean
Required: No

 ** RestrictPublicBuckets **   <a name="AmazonS3-Type-PublicAccessBlockConfiguration-RestrictPublicBuckets"></a>
Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting this element to `TRUE` restricts access to this bucket to only AWS service principals and authorized users within this account if the bucket has a public policy.
Enabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.
Type: Boolean
Required: No

## See Also
<a name="API_PublicAccessBlockConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PublicAccessBlockConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PublicAccessBlockConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PublicAccessBlockConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
