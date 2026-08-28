---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentRunFilter.html
---

# AssessmentRunFilter
<a name="API_AssessmentRunFilter"></a>

Used as the request parameter in the [ListAssessmentRuns](API_ListAssessmentRuns.md) action.

## Contents
<a name="API_AssessmentRunFilter_Contents"></a>

 ** completionTimeRange **   <a name="Inspector-Type-AssessmentRunFilter-completionTimeRange"></a>
For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **completedAt** property of the [AssessmentRun](API_AssessmentRun.md) data type.
Type: [TimestampRange](API_TimestampRange.md) object
Required: No

 ** durationRange **   <a name="Inspector-Type-AssessmentRunFilter-durationRange"></a>
For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **durationInSeconds** property of the [AssessmentRun](API_AssessmentRun.md) data type.
Type: [DurationRange](API_DurationRange.md) object
Required: No

 ** namePattern **   <a name="Inspector-Type-AssessmentRunFilter-namePattern"></a>
For a record to match a filter, an explicit value or a string containing a wildcard that is specified for this data type property must match the value of the **assessmentRunName** property of the [AssessmentRun](API_AssessmentRun.md) data type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Required: No

 ** rulesPackageArns **   <a name="Inspector-Type-AssessmentRunFilter-rulesPackageArns"></a>
For a record to match a filter, the value that is specified for this data type property must be contained in the list of values of the **rulesPackages** property of the [AssessmentRun](API_AssessmentRun.md) data type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** startTimeRange **   <a name="Inspector-Type-AssessmentRunFilter-startTimeRange"></a>
For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **startTime** property of the [AssessmentRun](API_AssessmentRun.md) data type.
Type: [TimestampRange](API_TimestampRange.md) object
Required: No

 ** stateChangeTimeRange **   <a name="Inspector-Type-AssessmentRunFilter-stateChangeTimeRange"></a>
For a record to match a filter, the value that is specified for this data type property must match the **stateChangedAt** property of the [AssessmentRun](API_AssessmentRun.md) data type.
Type: [TimestampRange](API_TimestampRange.md) object
Required: No

 ** states **   <a name="Inspector-Type-AssessmentRunFilter-states"></a>
For a record to match a filter, one of the values specified for this data type property must be the exact match of the value of the **assessmentRunState** property of the [AssessmentRun](API_AssessmentRun.md) data type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Valid Values: `CREATED | START_DATA_COLLECTION_PENDING | START_DATA_COLLECTION_IN_PROGRESS | COLLECTING_DATA | STOP_DATA_COLLECTION_PENDING | DATA_COLLECTED | START_EVALUATING_RULES_PENDING | EVALUATING_RULES | FAILED | ERROR | COMPLETED | COMPLETED_WITH_ERRORS | CANCELED`
Required: No

## See Also
<a name="API_AssessmentRunFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AssessmentRunFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AssessmentRunFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AssessmentRunFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
