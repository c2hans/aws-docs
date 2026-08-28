---
source_url: https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-job.html
---

# AWS HealthScribe transcription jobs
<a name="health-scribe-job"></a>

An AWS HealthScribe transcription job processes media files from an Amazon S3 bucket. When it processes a media file, it transcribes patient-clinician conversations and analyzes medical consultation to produces two JSON output files: a [transcript](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-job.html#health-scribe-output-example) file and a [clinical documentation](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-job.html#health-scribe-output-example) file.

The following are API operations specific to AWS HealthScribe transcription jobs:
+ [StartMedicalScribeJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_StartMedicalScribeJob.html)
+ [ListMedicalScribeJobs](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ListMedicalScribeJobs.html)
+ [GetMedicalScribeJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_GetMedicalScribeJob.html)
+ [DeleteMedicalScribeJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_DeleteMedicalScribeJob.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
