---
source_url: https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_S3Bucket.html
---

# S3Bucket
<a name="API_S3Bucket"></a>

The S3 bucket where RDP connection recordings are stored.

## Contents
<a name="API_S3Bucket_Contents"></a>

 ** BucketName **   <a name="ssmguiconnect-Type-S3Bucket-BucketName"></a>
The name of the S3 bucket where RDP connection recordings are stored.
Type: String
Pattern: `.*(?=^.{3,63}$)(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$).*`
Required: Yes

 ** BucketOwner **   <a name="ssmguiconnect-Type-S3Bucket-BucketOwner"></a>
The AWS account number that owns the S3 bucket.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

## See Also
<a name="API_S3Bucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-guiconnect-2021-05-01/S3Bucket)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-guiconnect-2021-05-01/S3Bucket)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-guiconnect-2021-05-01/S3Bucket)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager GUI Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssm-guiconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
