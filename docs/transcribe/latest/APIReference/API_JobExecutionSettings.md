---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_JobExecutionSettings.html
---

# JobExecutionSettings
<a name="API_JobExecutionSettings"></a>

Makes it possible to control how your transcription job is processed. Currently, the only `JobExecutionSettings` modification you can choose is enabling job queueing using the `AllowDeferredExecution` sub-parameter.

If you include `JobExecutionSettings` in your request, you must also include the sub-parameters: `AllowDeferredExecution` and `DataAccessRoleArn`.

## Contents
<a name="API_JobExecutionSettings_Contents"></a>

 ** AllowDeferredExecution **   <a name="transcribe-Type-JobExecutionSettings-AllowDeferredExecution"></a>
Makes it possible to enable job queuing when your concurrent request limit is exceeded. When `AllowDeferredExecution` is set to `true`, transcription job requests are placed in a queue until the number of jobs falls below the concurrent request limit. If `AllowDeferredExecution` is set to `false` and the number of transcription job requests exceed the concurrent request limit, you get a `LimitExceededException` error.
If you include `AllowDeferredExecution` in your request, you must also include `DataAccessRoleArn`.
Type: Boolean
Required: No

 ** DataAccessRoleArn **   <a name="transcribe-Type-JobExecutionSettings-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files. If the role that you specify doesn’t have the appropriate permissions to access the specified Amazon S3 location, your request fails.
IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path`. For example: `arn:aws:iam::111122223333:role/Admin`. For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns).
Note that if you include `DataAccessRoleArn` in your request, you must also include `AllowDeferredExecution`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{0,63}:role/[A-Za-z0-9:_/+=,@.-]{0,1024}$`
Required: No

## See Also
<a name="API_JobExecutionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/JobExecutionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/JobExecutionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/JobExecutionSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
