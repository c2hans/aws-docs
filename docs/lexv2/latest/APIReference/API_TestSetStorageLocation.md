---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_TestSetStorageLocation.html
---

# TestSetStorageLocation
<a name="API_TestSetStorageLocation"></a>

Contains information about the location in which the test set is stored.

## Contents
<a name="API_TestSetStorageLocation_Contents"></a>

 ** s3BucketName **   <a name="lexv2-Type-TestSetStorageLocation-s3BucketName"></a>
The name of the Amazon S3 bucket in which the test set is stored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
Required: Yes

 ** s3Path **   <a name="lexv2-Type-TestSetStorageLocation-s3Path"></a>
The path inside the Amazon S3 bucket where the test set is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\.\-\!\*\_\'\(\)a-zA-Z0-9][\.\-\!\*\_\'\(\)\/a-zA-Z0-9]*$`
Required: Yes

 ** kmsKeyArn **   <a name="lexv2-Type-TestSetStorageLocation-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of an AWS Key Management Service (KMS) key for encrypting the test set.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:[\w\-]+:kms:[\w\-]+:[\d]{12}:(?:key\/[\w\-]+|alias\/[a-zA-Z0-9:\/_\-]{1,256})$`
Required: No

## See Also
<a name="API_TestSetStorageLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/TestSetStorageLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/TestSetStorageLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/TestSetStorageLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
