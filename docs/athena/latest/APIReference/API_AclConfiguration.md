---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_AclConfiguration.html
---

# AclConfiguration
<a name="API_AclConfiguration"></a>

Indicates that an Amazon S3 canned ACL should be set to control ownership of stored query results, including data files inserted by Athena as the result of statements like CTAS or INSERT INTO. When Athena stores query results in Amazon S3, the canned ACL is set with the `x-amz-acl` request header. For more information about S3 Object Ownership, see [Object Ownership settings](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html#object-ownership-overview) in the *Amazon S3 User Guide*.

## Contents
<a name="API_AclConfiguration_Contents"></a>

 ** S3AclOption **   <a name="athena-Type-AclConfiguration-S3AclOption"></a>
The Amazon S3 canned ACL that Athena should specify when storing query results, including data files inserted by Athena as the result of statements like CTAS or INSERT INTO. Currently the only supported canned ACL is `BUCKET_OWNER_FULL_CONTROL`. If a query runs in a workgroup and the workgroup overrides client-side settings, then the Amazon S3 canned ACL specified in the workgroup's settings is used for all queries that run in the workgroup. For more information about Amazon S3 canned ACLs, see [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl) in the *Amazon S3 User Guide*.
Type: String
Valid Values: `BUCKET_OWNER_FULL_CONTROL`
Required: Yes

## See Also
<a name="API_AclConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/AclConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/AclConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/AclConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
