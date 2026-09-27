---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CodeReviewJob.html
---

# CodeReviewJob
<a name="API_CodeReviewJob"></a>

Represents a code review job, which is an execution instance of a code review. A code review job progresses through preflight, static analysis, and finalizing steps.

## Contents
<a name="API_CodeReviewJob_Contents"></a>

 ** codeRemediationStrategy **   <a name="securityagent-Type-CodeReviewJob-codeRemediationStrategy"></a>
The code remediation strategy for the code review job.
Type: String
Valid Values: `AUTOMATIC | DISABLED`
Required: No

 ** codeReviewId **   <a name="securityagent-Type-CodeReviewJob-codeReviewId"></a>
The unique identifier of the code review associated with the job.
Type: String
Required: No

 ** codeReviewJobId **   <a name="securityagent-Type-CodeReviewJob-codeReviewJobId"></a>
The unique identifier of the code review job.
Type: String
Required: No

 ** createdAt **   <a name="securityagent-Type-CodeReviewJob-createdAt"></a>
The date and time the code review job was created, in UTC format.
Type: Timestamp
Required: No

 ** documents **   <a name="securityagent-Type-CodeReviewJob-documents"></a>
The list of documents providing context for the code review job.
Type: Array of [DocumentInfo](API_DocumentInfo.md) objects
Required: No

 ** errorInformation **   <a name="securityagent-Type-CodeReviewJob-errorInformation"></a>
Error information if the code review job encountered an error.
Type: [ErrorInformation](API_ErrorInformation.md) object
Required: No

 ** executionContext **   <a name="securityagent-Type-CodeReviewJob-executionContext"></a>
The execution context messages for the code review job.
Type: Array of [ExecutionContext](API_ExecutionContext.md) objects
Required: No

 ** integratedRepositories **   <a name="securityagent-Type-CodeReviewJob-integratedRepositories"></a>
The list of integrated repositories associated with the code review job.
Type: Array of [IntegratedRepository](API_IntegratedRepository.md) objects
Required: No

 ** logConfig **   <a name="securityagent-Type-CodeReviewJob-logConfig"></a>
The CloudWatch Logs configuration for the code review job.
Type: [CloudWatchLog](API_CloudWatchLog.md) object
Required: No

 ** maxTaskHours **   <a name="securityagent-Type-CodeReviewJob-maxTaskHours"></a>
The maximum number of billable task hours allowed for this code review job. If the cumulative task hours reach this limit, the job is gracefully stopped.
Type: Double
Required: No

 ** overview **   <a name="securityagent-Type-CodeReviewJob-overview"></a>
An overview of the code review job results.
Type: String
Required: No

 ** reportDestination **   <a name="securityagent-Type-CodeReviewJob-reportDestination"></a>
The destination for publishing scan reports to an integrated document provider.
Type: [ReportDestination](API_ReportDestination.md) object
Required: No

 ** serviceRole **   <a name="securityagent-Type-CodeReviewJob-serviceRole"></a>
The IAM service role used for the code review job.
Type: String
Required: No

 ** sourceCode **   <a name="securityagent-Type-CodeReviewJob-sourceCode"></a>
The list of source code repositories analyzed during the code review job.
Type: Array of [SourceCodeRepository](API_SourceCodeRepository.md) objects
Required: No

 ** status **   <a name="securityagent-Type-CodeReviewJob-status"></a>
The current status of the code review job.
Type: String
Valid Values: `IN_PROGRESS | STOPPING | STOPPED | FAILED | COMPLETED`
Required: No

 ** steps **   <a name="securityagent-Type-CodeReviewJob-steps"></a>
The list of steps in the code review job execution.
Type: Array of [Step](API_Step.md) objects
Required: No

 ** title **   <a name="securityagent-Type-CodeReviewJob-title"></a>
The title of the code review job.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-CodeReviewJob-updatedAt"></a>
The date and time the code review job was last updated, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_CodeReviewJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CodeReviewJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CodeReviewJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CodeReviewJob)
