---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/cloudwatch_metrics-codebuild.html
---

# CodeBuild CloudWatch metrics
<a name="cloudwatch_metrics-codebuild"></a>

 The following metrics can be tracked per AWS account or build project. For more information about using CloudWatch with CodeBuild, see [Monitor CodeBuild builds with CloudWatch](monitoring-builds.md).

BuildDuration
Measures the duration of the build's `BUILD` phase.
Units: Seconds
Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

Builds
 Measures the number of builds triggered.
 Units: Count
 Valid CloudWatch statistics: Sum

DownloadSourceDuration
Measures the duration of the build's `DOWNLOAD_SOURCE` phase.
Units: Seconds
Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

Duration
 Measures the duration of all builds over time.
 Units: Seconds
 Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

FailedBuilds
 Measures the number of builds that failed because of client error or a timeout.
 Units: Count
 Valid CloudWatch statistics: Sum

FinalizingDuration
Measures the duration of the build's `FINALIZING` phase.
Units: Seconds
Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

InstallDuration
Measures the duration of the build's `INSTALL` phase.
Units: Seconds
Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

PostBuildDuration
Measures the duration of the build's `POST_BUILD` phase
Units: Seconds
Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

PreBuildDuration
Measures the duration of the build's `PRE_BUILD` phase.
Units: Seconds
Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

ProvisioningDuration
Measures the duration of the build's `PROVISIONING` phase.
Units: Seconds
Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

QueuedDuration
Measures the duration of the build's `QUEUED` phase.
Units: Seconds
Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

SubmittedDuration
Measures the duration of the build's `SUBMITTED` phase.
Units: Seconds
Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

SucceededBuilds
 Measures the number of successful builds.
 Units: Count
 Valid CloudWatch statistics: Sum

UploadArtifactsDuration
Measures the duration of the build's `UPLOAD_ARTIFACTS` phase.
Units: Seconds
Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
