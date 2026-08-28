---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/asff-resourcedetails-awssqs.html
---

# AwsSqs resources in ASFF
<a name="asff-resourcedetails-awssqs"></a>

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsSqs` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md).

## AwsSqsQueue
<a name="asff-resourcedetails-awssqsqueue"></a>

The `AwsSqsQueue` object contains information about an Amazon Simple Queue Service queue.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsSqsQueue` object. To view descriptions of `AwsSqsQueue` attributes, see [AwsSqsQueueDetails](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSqsQueueDetails.html) in the *AWS Security Hub API Reference*.

**Example**

```
"AwsSqsQueue": {
    "DeadLetterTargetArn": "arn:aws:sqs:us-west-2:123456789012:queue/target",
    "KmsDataKeyReusePeriodSeconds": 60,,
    "KmsMasterKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "QueueName": "sample-queue"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
