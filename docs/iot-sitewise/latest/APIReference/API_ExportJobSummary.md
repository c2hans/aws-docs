---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ExportJobSummary.html
---

# ExportJobSummary
<a name="API_ExportJobSummary"></a>

Contains summary information about a dataset export job.

## Contents
<a name="API_ExportJobSummary_Contents"></a>

 ** destinationS3Uri **   <a name="iotsitewise-Type-ExportJobSummary-destinationS3Uri"></a>
The S3 URI where output clips are written.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.+`
Required: Yes

 ** jobId **   <a name="iotsitewise-Type-ExportJobSummary-jobId"></a>
The unique identifier for the dataset export job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** startedAt **   <a name="iotsitewise-Type-ExportJobSummary-startedAt"></a>
The timestamp when the job started processing.
Type: Timestamp
Required: Yes

 ** status **   <a name="iotsitewise-Type-ExportJobSummary-status"></a>
The current status of the dataset export job.
Type: String
Valid Values: `SUBMITTED | RUNNING | COMPLETED | COMPLETED_WITH_ERRORS | FAILED`
Required: Yes

 ** completedAt **   <a name="iotsitewise-Type-ExportJobSummary-completedAt"></a>
The timestamp when the job completed, or null if the job is still running.
Type: Timestamp
Required: No

## See Also
<a name="API_ExportJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ExportJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ExportJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ExportJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
