---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_S3Configuration.html
---

# S3Configuration
<a name="API_S3Configuration"></a>

Configuration for Amazon S3 destination where scheduled query results are delivered.

## Contents
<a name="API_S3Configuration_Contents"></a>

 ** destinationIdentifier **   <a name="CWL-Type-S3Configuration-destinationIdentifier"></a>
The Amazon S3 URI where query results are delivered. Must be a valid S3 URI format.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

 ** roleArn **   <a name="CWL-Type-S3Configuration-roleArn"></a>
The ARN of the IAM role that grants permissions to write query results to the specified Amazon S3 destination.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** kmsKeyId **   <a name="CWL-Type-S3Configuration-kmsKeyId"></a>
The Amazon Resource Name (ARN) of the KMS encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** ownerAccountId **   <a name="CWL-Type-S3Configuration-ownerAccountId"></a>
The AWS accountId for the bucket owning account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

## See Also
<a name="API_S3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/S3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/S3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/S3Configuration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
