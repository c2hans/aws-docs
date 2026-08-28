---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_BatchParameters.html
---

# BatchParameters
<a name="API_BatchParameters"></a>

The custom parameters to be used when the target is an AWS Batch job.

## Contents
<a name="API_BatchParameters_Contents"></a>

 ** JobDefinition **   <a name="eventbridge-Type-BatchParameters-JobDefinition"></a>
The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.
Type: String
Required: Yes

 ** JobName **   <a name="eventbridge-Type-BatchParameters-JobName"></a>
The name to use for this execution of the job, if the target is an AWS Batch job.
Type: String
Required: Yes

 ** ArrayProperties **   <a name="eventbridge-Type-BatchParameters-ArrayProperties"></a>
The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.
Type: [BatchArrayProperties](API_BatchArrayProperties.md) object
Required: No

 ** RetryStrategy **   <a name="eventbridge-Type-BatchParameters-RetryStrategy"></a>
The retry strategy to use for failed jobs, if the target is an AWS Batch job. The retry strategy is the number of times to retry the failed job execution. Valid values are 1–10. When you specify a retry strategy here, it overrides the retry strategy defined in the job definition.
Type: [BatchRetryStrategy](API_BatchRetryStrategy.md) object
Required: No

## See Also
<a name="API_BatchParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/BatchParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/BatchParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/BatchParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
