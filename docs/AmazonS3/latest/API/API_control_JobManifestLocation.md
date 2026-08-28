---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobManifestLocation.html
---

# JobManifestLocation
<a name="API_control_JobManifestLocation"></a>

Contains the information required to locate a manifest object. Manifests can't be imported from directory buckets. For more information, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html).

## Contents
<a name="API_control_JobManifestLocation_Contents"></a>

 ** ETag **   <a name="AmazonS3-Type-control_JobManifestLocation-ETag"></a>
The ETag for the specified manifest object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ObjectArn **   <a name="AmazonS3-Type-control_JobManifestLocation-ObjectArn"></a>
The Amazon Resource Name (ARN) for a manifest object.
When you're using XML requests, you must replace special characters (such as carriage returns) in object keys with their equivalent XML entity codes. For more information, see [ XML-related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints) in the *Amazon S3 User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `arn:[^:]+:s3:.*`
Required: Yes

 ** ObjectVersionId **   <a name="AmazonS3-Type-control_JobManifestLocation-ObjectVersionId"></a>
The optional version ID to identify a specific version of the manifest object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## See Also
<a name="API_control_JobManifestLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobManifestLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobManifestLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobManifestLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
