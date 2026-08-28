---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PipelineSummary.html
---

# PipelineSummary
<a name="API_PipelineSummary"></a>

Contains summary information about a pipeline.

## Contents
<a name="API_PipelineSummary_Contents"></a>

 ** createdAt **   <a name="iotsitewise-Type-PipelineSummary-createdAt"></a>
The time the pipeline was created, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** pipelineArn **   <a name="iotsitewise-Type-PipelineSummary-pipelineArn"></a>
The ARN of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

 ** pipelineName **   <a name="iotsitewise-Type-PipelineSummary-pipelineName"></a>
The name of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** status **   <a name="iotsitewise-Type-PipelineSummary-status"></a>
The current lifecycle status of the pipeline.
Type: [ResourceStatus](API_ResourceStatus.md) object
Required: Yes

 ** updatedAt **   <a name="iotsitewise-Type-PipelineSummary-updatedAt"></a>
The time the pipeline was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** version **   <a name="iotsitewise-Type-PipelineSummary-version"></a>
The version of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`
Required: Yes

 ** description **   <a name="iotsitewise-Type-PipelineSummary-description"></a>
The description of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

## See Also
<a name="API_PipelineSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/PipelineSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/PipelineSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/PipelineSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
