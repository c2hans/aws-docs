---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_PublicAccessConfiguration.html
---

# PublicAccessConfiguration
<a name="API_PublicAccessConfiguration"></a>

Describes public access policies that apply to the Amazon S3 bucket.

For information about each of the following settings, see [Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) in the *Amazon S3 User Guide*.

## Contents
<a name="API_PublicAccessConfiguration_Contents"></a>

 ** publicAclAccess **   <a name="guardduty-Type-PublicAccessConfiguration-publicAclAccess"></a>
Indicates whether or not there is a setting that allows public access to the Amazon S3 buckets through access control lists (ACLs).
Type: String
Valid Values: `BLOCKED | ALLOWED`
Required: No

 ** publicAclIgnoreBehavior **   <a name="guardduty-Type-PublicAccessConfiguration-publicAclIgnoreBehavior"></a>
Indicates whether or not there is a setting that ignores all public access control lists (ACLs) on the Amazon S3 bucket and the objects that it contains.
Type: String
Valid Values: `IGNORED | NOT_IGNORED`
Required: No

 ** publicBucketRestrictBehavior **   <a name="guardduty-Type-PublicAccessConfiguration-publicBucketRestrictBehavior"></a>
Indicates whether or not there is a setting that restricts access to the bucket with specified policies.
Type: String
Valid Values: `RESTRICTED | NOT_RESTRICTED`
Required: No

 ** publicPolicyAccess **   <a name="guardduty-Type-PublicAccessConfiguration-publicPolicyAccess"></a>
Indicates whether or not there is a setting that allows public access to the Amazon S3 bucket policy.
Type: String
Valid Values: `BLOCKED | ALLOWED`
Required: No

## See Also
<a name="API_PublicAccessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/PublicAccessConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/PublicAccessConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/PublicAccessConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
