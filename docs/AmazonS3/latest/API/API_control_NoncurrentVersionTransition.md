---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_NoncurrentVersionTransition.html
---

# NoncurrentVersionTransition
<a name="API_control_NoncurrentVersionTransition"></a>

The container for the noncurrent version transition.

## Contents
<a name="API_control_NoncurrentVersionTransition_Contents"></a>

 ** NoncurrentDays **   <a name="AmazonS3-Type-control_NoncurrentVersionTransition-NoncurrentDays"></a>
Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see [ How Amazon S3 Calculates How Long an Object Has Been Noncurrent](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations) in the *Amazon S3 User Guide*.
Type: Integer
Required: No

 ** StorageClass **   <a name="AmazonS3-Type-control_NoncurrentVersionTransition-StorageClass"></a>
The class of storage used to store the object.
Type: String
Valid Values: `GLACIER | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | DEEP_ARCHIVE`
Required: No

## See Also
<a name="API_control_NoncurrentVersionTransition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/NoncurrentVersionTransition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/NoncurrentVersionTransition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/NoncurrentVersionTransition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
