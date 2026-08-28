---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceLevelObjectiveBudgetReport.html
---

# ServiceLevelObjectiveBudgetReport
<a name="API_ServiceLevelObjectiveBudgetReport"></a>

A structure containing an SLO budget report that you have requested.

## Contents
<a name="API_ServiceLevelObjectiveBudgetReport_Contents"></a>

 ** Arn **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReport-Arn"></a>
The ARN of the SLO that this report is for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-us-gov):application-signals:[^:]*:[^:]*:slo/[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

 ** BudgetStatus **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReport-BudgetStatus"></a>
The status of this SLO, as it relates to the error budget for the entire time interval.
+  `OK` means that the SLO had remaining budget above the warning threshold, as of the time that you specified in `TimeStamp`.
+  `WARNING` means that the SLO's remaining budget was below the warning threshold, as of the time that you specified in `TimeStamp`.
+  `BREACHED` means that the SLO's budget was exhausted, as of the time that you specified in `TimeStamp`.
+  `INSUFFICIENT_DATA` means that the specified start and end times were before the SLO was created, or that attainment data is missing.
Type: String
Valid Values: `OK | WARNING | BREACHED | INSUFFICIENT_DATA`
Required: Yes

 ** Name **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReport-Name"></a>
The name of the SLO that this report is for.
Type: String
Pattern: `[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

 ** Attainment **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReport-Attainment"></a>
A number between 0 and 100 that represents the success percentage of your application compared to the goal set by the SLO.
If this is a period-based SLO, the number is the percentage of time periods that the service has attained the SLO's attainment goal, as of the time of the request.
If this is a request-based SLO, the number is the number of successful requests divided by the number of total requests, multiplied by 100, during the time range that you specified in your request.
Type: Double
Required: No

 ** BudgetRequestsRemaining **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReport-BudgetRequestsRemaining"></a>
This field is displayed only for request-based SLOs. It displays the number of failed requests that can be tolerated before any more successful requests occur, and still have the application meet its SLO goal.
This number can go up and down between different reports, based on both how many successful requests and how many failed requests occur in that time.
Type: Integer
Required: No

 ** BudgetSecondsRemaining **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReport-BudgetSecondsRemaining"></a>
The budget amount remaining before the SLO status becomes `BREACHING`, at the time specified in the `Timestemp` parameter of the request. If this value is negative, then the SLO is already in `BREACHING` status.
 This field is included only if the SLO is a period-based SLO.
Type: Integer
Required: No

 ** EvaluationType **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReport-EvaluationType"></a>
Displays whether this budget report is for a period-based SLO or a request-based SLO.
Type: String
Valid Values: `PeriodBased | RequestBased`
Required: No

 ** Goal **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReport-Goal"></a>
This structure contains the attributes that determine the goal of an SLO. This includes the time period for evaluation and the attainment threshold.
Type: [Goal](API_Goal.md) object
Required: No

 ** RequestBasedSli **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReport-RequestBasedSli"></a>
This structure contains information about the performance metric that a request-based SLO monitors.
Type: [RequestBasedServiceLevelIndicator](API_RequestBasedServiceLevelIndicator.md) object
Required: No

 ** Sli **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReport-Sli"></a>
A structure that contains information about the performance metric that this SLO monitors.
Type: [ServiceLevelIndicator](API_ServiceLevelIndicator.md) object
Required: No

 ** TotalBudgetRequests **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReport-TotalBudgetRequests"></a>
This field is displayed only for request-based SLOs. It displays the total number of failed requests that can be tolerated during the time range between the start of the interval and the time stamp supplied in the budget report request. It is based on the total number of requests that occurred, and the percentage specified in the attainment goal. If the number of failed requests matches this number or is higher, then this SLO is currently breaching.
This number can go up and down between reports with different time stamps, based on both how many total requests occur.
Type: Integer
Required: No

 ** TotalBudgetSeconds **   <a name="applicationsignals-Type-ServiceLevelObjectiveBudgetReport-TotalBudgetSeconds"></a>
The total number of seconds in the error budget for the interval. This field is included only if the SLO is a period-based SLO.
Type: Integer
Required: No

## See Also
<a name="API_ServiceLevelObjectiveBudgetReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ServiceLevelObjectiveBudgetReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ServiceLevelObjectiveBudgetReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ServiceLevelObjectiveBudgetReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
