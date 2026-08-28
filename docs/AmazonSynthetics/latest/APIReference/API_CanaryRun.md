---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRun.html
---

# CanaryRun
<a name="API_CanaryRun"></a>

This structure contains the details about one run of one canary.

## Contents
<a name="API_CanaryRun_Contents"></a>

 ** ArtifactS3Location **   <a name="synthetics-Type-CanaryRun-ArtifactS3Location"></a>
The location where the canary stored artifacts from the run. Artifacts include the log file, screenshots, and HAR files.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** BrowserType **   <a name="synthetics-Type-CanaryRun-BrowserType"></a>
The browser type associated with this canary run.
Type: String
Valid Values: `CHROME | FIREFOX`
Required: No

 ** DryRunConfig **   <a name="synthetics-Type-CanaryRun-DryRunConfig"></a>
Returns the dry run configurations for a canary.
Type: [CanaryDryRunConfigOutput](API_CanaryDryRunConfigOutput.md) object
Required: No

 ** Id **   <a name="synthetics-Type-CanaryRun-Id"></a>
A unique ID that identifies this canary run.
Type: String
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** Location **   <a name="synthetics-Type-CanaryRun-Location"></a>
The Amazon Web Services Region where this canary run was executed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`
Required: No

 ** Name **   <a name="synthetics-Type-CanaryRun-Name"></a>
The name of the canary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9a-z_\-]+$`
Required: No

 ** RetryAttempt **   <a name="synthetics-Type-CanaryRun-RetryAttempt"></a>
The count in number of the retry attempt.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2.
Required: No

 ** ScheduledRunId **   <a name="synthetics-Type-CanaryRun-ScheduledRunId"></a>
The ID of the scheduled canary run.
Type: String
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** Status **   <a name="synthetics-Type-CanaryRun-Status"></a>
The status of this run.
Type: [CanaryRunStatus](API_CanaryRunStatus.md) object
Required: No

 ** Timeline **   <a name="synthetics-Type-CanaryRun-Timeline"></a>
A structure that contains the start and end times of this run.
Type: [CanaryRunTimeline](API_CanaryRunTimeline.md) object
Required: No

## See Also
<a name="API_CanaryRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/CanaryRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/CanaryRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/CanaryRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
