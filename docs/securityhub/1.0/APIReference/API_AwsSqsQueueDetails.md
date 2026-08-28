---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSqsQueueDetails.html
---

# AwsSqsQueueDetails
<a name="API_AwsSqsQueueDetails"></a>

Data about a queue.

## Contents
<a name="API_AwsSqsQueueDetails_Contents"></a>

 ** DeadLetterTargetArn **   <a name="securityhub-Type-AwsSqsQueueDetails-DeadLetterTargetArn"></a>
The ARN of the dead-letter queue to which Amazon SQS moves messages after the value of `maxReceiveCount` is exceeded.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KmsDataKeyReusePeriodSeconds **   <a name="securityhub-Type-AwsSqsQueueDetails-KmsDataKeyReusePeriodSeconds"></a>
The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again.
Type: Integer
Required: No

 ** KmsMasterKeyId **   <a name="securityhub-Type-AwsSqsQueueDetails-KmsMasterKeyId"></a>
The ID of an AWS managed key for Amazon SQS or a custom KMS key.
Type: String
Pattern: `.*\S.*`
Required: No

 ** QueueName **   <a name="securityhub-Type-AwsSqsQueueDetails-QueueName"></a>
The name of the new queue.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsSqsQueueDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsSqsQueueDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsSqsQueueDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsSqsQueueDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
