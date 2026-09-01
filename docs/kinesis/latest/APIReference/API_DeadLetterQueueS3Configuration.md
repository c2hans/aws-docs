---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeadLetterQueueS3Configuration.html
---

# DeadLetterQueueS3Configuration
<a name="API_DeadLetterQueueS3Configuration"></a>

The Amazon S3 dead-letter queue configuration for records that cannot be delivered.

## Contents
<a name="API_DeadLetterQueueS3Configuration_Contents"></a>

 ** BucketARN **   <a name="Streams-Type-DeadLetterQueueS3Configuration-BucketARN"></a>
The Amazon Resource Name (ARN) of the dead-letter queue Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:s3:::[a-z0-9._-]{3,63}`
Required: Yes

 ** ExpectedBucketOwner **   <a name="Streams-Type-DeadLetterQueueS3Configuration-ExpectedBucketOwner"></a>
The AWS account ID of the expected owner of the dead-letter queue bucket.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** ErrorOutputPrefix **   <a name="Streams-Type-DeadLetterQueueS3Configuration-ErrorOutputPrefix"></a>
The Amazon S3 key prefix for error records.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[0-9A-Za-z!\-_'.*()\/]+`
Required: No

## See Also
<a name="API_DeadLetterQueueS3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/DeadLetterQueueS3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/DeadLetterQueueS3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/DeadLetterQueueS3Configuration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
