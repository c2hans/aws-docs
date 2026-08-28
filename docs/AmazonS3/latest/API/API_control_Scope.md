---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Scope.html
---

# Scope
<a name="API_control_Scope"></a>

You can use the access point scope to restrict access to specific prefixes, API operations, or a combination of both.

For more information, see [Manage the scope of your access points for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-manage-scope.html).

## Contents
<a name="API_control_Scope_Contents"></a>

 ** Permissions **   <a name="AmazonS3-Type-control_Scope-Permissions"></a>
You can include one or more API operations as permissions.
Type: Array of strings
Valid Values: `GetObject | GetObjectAttributes | ListMultipartUploadParts | ListBucket | ListBucketMultipartUploads | PutObject | DeleteObject | AbortMultipartUpload`
Required: No

 ** Prefixes **   <a name="AmazonS3-Type-control_Scope-Prefixes"></a>
You can specify any amount of prefixes, but the total length of characters of all prefixes must be less than 256 bytes in size.
Type: Array of strings
Required: No

## See Also
<a name="API_control_Scope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Scope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Scope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Scope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
