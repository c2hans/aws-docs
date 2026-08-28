---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_PipelineOutput.html
---

# PipelineOutput
<a name="API_PipelineOutput"></a>

Contains the output from pipeline test operations, including processed records and any errors encountered.

## Contents
<a name="API_PipelineOutput_Contents"></a>

 ** Error **   <a name="cwoa-Type-PipelineOutput-Error"></a>
Any error that occurred during the pipeline test operation for this record.
Type: [PipelineOutputError](API_PipelineOutputError.md) object
Required: No

 ** Record **   <a name="cwoa-Type-PipelineOutput-Record"></a>
The processed record output from the pipeline test operation.
Type: [Record](API_Record.md) object
Required: No

## See Also
<a name="API_PipelineOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/PipelineOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/PipelineOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/PipelineOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
