---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_DeadLetterConfig.html
---

# DeadLetterConfig
<a name="API_DeadLetterConfig"></a>

An object that contains information about an Amazon SQS queue that EventBridge Scheduler uses as a dead-letter queue for your schedule. If specified, EventBridge Scheduler delivers failed events that could not be successfully delivered to a target to the queue.

## Contents
<a name="API_DeadLetterConfig_Contents"></a>

 ** Arn **   <a name="scheduler-Type-DeadLetterConfig-Arn"></a>
The Amazon Resource Name (ARN) of the SQS queue specified as the destination for the dead-letter queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)?:sqs:[a-z0-9\-]+:\d{12}:[a-zA-Z0-9\-_]+`
Required: No

## See Also
<a name="API_DeadLetterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/DeadLetterConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/DeadLetterConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/DeadLetterConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EventBridge Scheduler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query scheduler` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
