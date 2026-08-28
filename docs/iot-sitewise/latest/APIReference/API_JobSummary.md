---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_JobSummary.html
---

# JobSummary
<a name="API_JobSummary"></a>

Contains the job summary information.

## Contents
<a name="API_JobSummary_Contents"></a>

 ** id **   <a name="iotsitewise-Type-JobSummary-id"></a>
The ID of the job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** name **   <a name="iotsitewise-Type-JobSummary-name"></a>
The unique name that helps identify the job request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** status **   <a name="iotsitewise-Type-JobSummary-status"></a>
The status of the bulk import job can be one of following values:
+  `PENDING` – AWS IoT SiteWise is waiting for the current bulk import job to finish.
+  `CANCELLED` – The bulk import job has been canceled.
+  `RUNNING` – AWS IoT SiteWise is processing your request to import your data from Amazon S3.
+  `COMPLETED` – AWS IoT SiteWise successfully completed your request to import data from Amazon S3.
+  `FAILED` – AWS IoT SiteWise couldn't process your request to import data from Amazon S3. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.
+  `COMPLETED_WITH_FAILURES` – AWS IoT SiteWise completed your request to import data from Amazon S3 with errors. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.
Type: String
Valid Values: `PENDING | CANCELLED | RUNNING | COMPLETED | FAILED | COMPLETED_WITH_FAILURES`
Required: Yes

## See Also
<a name="API_JobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/JobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/JobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/JobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
