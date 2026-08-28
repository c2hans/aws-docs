---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_S3LogsConfig.html
---

# S3LogsConfig
<a name="API_S3LogsConfig"></a>

 Information about S3 logs for a build project.

## Contents
<a name="API_S3LogsConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** status **   <a name="CodeBuild-Type-S3LogsConfig-status"></a>
The current status of the S3 build logs. Valid values are:
+  `ENABLED`: S3 build logs are enabled for this build project.
+  `DISABLED`: S3 build logs are not enabled for this build project.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** bucketOwnerAccess **   <a name="CodeBuild-Type-S3LogsConfig-bucketOwnerAccess"></a>
Specifies the bucket owner's access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.
To use this property, your CodeBuild service role must have the `s3:PutBucketAcl` permission. This permission allows CodeBuild to modify the access control list for the bucket.
This property can be one of the following values:
NONE
The bucket owner does not have access to the objects. This is the default.
READ\_ONLY
The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.
FULL
The bucket owner has full access to the objects. Object ownership is determined by the following criteria:
+ If the bucket is configured with the **Bucket owner preferred** setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucket's policy.
+ Otherwise, the uploading account retains ownership of the objects.
For more information about Amazon S3 object ownership, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon Simple Storage Service User Guide*.
Type: String
Valid Values: `NONE | READ_ONLY | FULL`
Required: No

 ** encryptionDisabled **   <a name="CodeBuild-Type-S3LogsConfig-encryptionDisabled"></a>
 Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.
Type: Boolean
Required: No

 ** location **   <a name="CodeBuild-Type-S3LogsConfig-location"></a>
 The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is `my-bucket`, and your path prefix is `build-log`, then acceptable formats are `my-bucket/build-log` or `arn:aws:s3:::my-bucket/build-log`.
Type: String
Required: No

## See Also
<a name="API_S3LogsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/S3LogsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/S3LogsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/S3LogsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
