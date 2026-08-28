---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelObjectiveBudgetReportError.html
---

# ServiceLevelObjectiveBudgetReportError
<a name="API_ServiceLevelObjectiveBudgetReportError"></a>

A structure containing information about one error that occurred during a [BatchGetServiceLevelObjectiveBudgetReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_BatchGetServiceLevelObjectiveBudgetReport.html) operation.

## Contents
<a name="API_ServiceLevelObjectiveBudgetReportError_Contents"></a>

 ** Arn **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReportError-Arn"></a>
The ARN of the SLO that this error is related to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-us-gov):application-signals:[^:]*:[^:]*:slo/[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

 ** ErrorCode **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReportError-ErrorCode"></a>
The error code for this error.
Type: String
Required: Yes

 ** ErrorMessage **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReportError-ErrorMessage"></a>
The message for this error.
Type: String
Required: Yes

 ** Name **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReportError-Name"></a>
The name of the SLO that this error is related to.
Type: String
Pattern: `[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

## See Also
<a name="API_ServiceLevelObjectiveBudgetReportError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ServiceLevelObjectiveBudgetReportError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ServiceLevelObjectiveBudgetReportError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ServiceLevelObjectiveBudgetReportError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
