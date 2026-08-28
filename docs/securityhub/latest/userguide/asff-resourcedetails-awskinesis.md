---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/asff-resourcedetails-awskinesis.html
---

# AwsKinesis resources in ASFF
<a name="asff-resourcedetails-awskinesis"></a>

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsKinesis` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md).

## AwsKinesisStream
<a name="asff-resourcedetails-awskinesisstream"></a>

The `AwsKinesisStream` object provides details about Amazon Kinesis Data Streams.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsKinesisStream` object. To view descriptions of `AwsKinesisStream` attributes, see [AwsKinesisStreamDetails](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsKinesisStreamDetails.html) in the *AWS Security Hub API Reference*.

**Example**

```
"AwsKinesisStream": {
	"Name": "test-vir-kinesis-stream",
	"Arn": "arn:aws:kinesis:us-east-1:293279581038:stream/test-vir-kinesis-stream",
	"RetentionPeriodHours": 24,
	"ShardCount": 2,
	"StreamEncryption": {
		"EncryptionType": "KMS",
		"KeyId": "arn:aws:kms:us-east-1:293279581038:key/849cf029-4143-4c59-91f8-ea76007247eb"
	}
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
