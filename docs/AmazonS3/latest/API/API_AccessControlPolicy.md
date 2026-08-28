---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_AccessControlPolicy.html
---

# AccessControlPolicy
<a name="API_AccessControlPolicy"></a>

Contains the elements that set the ACL permissions for an object per grantee.

## Contents
<a name="API_AccessControlPolicy_Contents"></a>

 ** Grants **   <a name="AmazonS3-Type-AccessControlPolicy-Grants"></a>
A list of grants.
Type: Array of [Grant](API_Grant.md) data types
Required: No

 ** Owner **   <a name="AmazonS3-Type-AccessControlPolicy-Owner"></a>
Container for the bucket owner's display name and ID.
Type: [Owner](API_Owner.md) data type
Required: No

## See Also
<a name="API_AccessControlPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AccessControlPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AccessControlPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AccessControlPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
