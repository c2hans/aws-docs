---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_PipelineLoggingConfiguration.html
---

# PipelineLoggingConfiguration
<a name="API_PipelineLoggingConfiguration"></a>

The logging configuration that's defined for pipeline execution.

## Contents
<a name="API_PipelineLoggingConfiguration_Contents"></a>

 ** imageLogGroupName **   <a name="imagebuilder-Type-PipelineLoggingConfiguration-imageLogGroupName"></a>
Specifies the CloudWatch Logs log group name for image build logs. The log group name can contain alphanumeric characters, hyphens, underscores, forward slashes, and periods, up to 512 characters. Log group names not starting with `/aws/imagebuilder/` require an `executionRole` with CloudWatch Logs write permissions. If not specified, defaults to `/aws/imagebuilder/image-name`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-_/\.]{1,512}$`
Required: No

 ** pipelineLogGroupName **   <a name="imagebuilder-Type-PipelineLoggingConfiguration-pipelineLogGroupName"></a>
Specifies the CloudWatch Logs log group name for pipeline execution logs. The log group name can contain alphanumeric characters, hyphens, underscores, forward slashes, and periods, up to 512 characters. Log group names not starting with `/aws/imagebuilder/` require an `executionRole` with CloudWatch Logs write permissions. If not specified, defaults to `/aws/imagebuilder/pipeline/pipeline-name`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-_/\.]{1,512}$`
Required: No

## See Also
<a name="API_PipelineLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/PipelineLoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/PipelineLoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/PipelineLoggingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
