---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentRun.html
---

# AssessmentRun
<a name="API_AssessmentRun"></a>

A snapshot of an Amazon Inspector Classic assessment run that contains the findings of the assessment run .

Used as the response element in the [DescribeAssessmentRuns](API_DescribeAssessmentRuns.md) action.

## Contents
<a name="API_AssessmentRun_Contents"></a>

 ** arn **   <a name="Inspector-Type-AssessmentRun-arn"></a>
The ARN of the assessment run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** assessmentTemplateArn **   <a name="Inspector-Type-AssessmentRun-assessmentTemplateArn"></a>
The ARN of the assessment template that is associated with the assessment run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** createdAt **   <a name="Inspector-Type-AssessmentRun-createdAt"></a>
The time when [StartAssessmentRun](API_StartAssessmentRun.md) was called.
Type: Timestamp
Required: Yes

 ** dataCollected **   <a name="Inspector-Type-AssessmentRun-dataCollected"></a>
A Boolean value (true or false) that specifies whether the process of collecting data from the agents is completed.
Type: Boolean
Required: Yes

 ** durationInSeconds **   <a name="Inspector-Type-AssessmentRun-durationInSeconds"></a>
The duration of the assessment run.
Type: Integer
Valid Range: Minimum value of 180. Maximum value of 86400.
Required: Yes

 ** findingCounts **   <a name="Inspector-Type-AssessmentRun-findingCounts"></a>
Provides a total count of generated findings per severity.
Type: String to integer map
Valid Keys: `Low | Medium | High | Informational | Undefined`
Required: Yes

 ** name **   <a name="Inspector-Type-AssessmentRun-name"></a>
The auto-generated name for the assessment run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Required: Yes

 ** notifications **   <a name="Inspector-Type-AssessmentRun-notifications"></a>
A list of notifications for the event subscriptions. A notification about a particular generated finding is added to this list only once.
Type: Array of [AssessmentRunNotification](API_AssessmentRunNotification.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

 ** rulesPackageArns **   <a name="Inspector-Type-AssessmentRun-rulesPackageArns"></a>
The rules packages selected for the assessment run.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** state **   <a name="Inspector-Type-AssessmentRun-state"></a>
The state of the assessment run.
Type: String
Valid Values: `CREATED | START_DATA_COLLECTION_PENDING | START_DATA_COLLECTION_IN_PROGRESS | COLLECTING_DATA | STOP_DATA_COLLECTION_PENDING | DATA_COLLECTED | START_EVALUATING_RULES_PENDING | EVALUATING_RULES | FAILED | ERROR | COMPLETED | COMPLETED_WITH_ERRORS | CANCELED`
Required: Yes

 ** stateChangedAt **   <a name="Inspector-Type-AssessmentRun-stateChangedAt"></a>
The last time when the assessment run's state changed.
Type: Timestamp
Required: Yes

 ** stateChanges **   <a name="Inspector-Type-AssessmentRun-stateChanges"></a>
A list of the assessment run state changes.
Type: Array of [AssessmentRunStateChange](API_AssessmentRunStateChange.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

 ** userAttributesForFindings **   <a name="Inspector-Type-AssessmentRun-userAttributesForFindings"></a>
The user-defined attributes that are assigned to every generated finding.
Type: Array of [Attribute](API_Attribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** completedAt **   <a name="Inspector-Type-AssessmentRun-completedAt"></a>
The assessment run completion time that corresponds to the rules packages evaluation completion time or failure.
Type: Timestamp
Required: No

 ** startedAt **   <a name="Inspector-Type-AssessmentRun-startedAt"></a>
The time when [StartAssessmentRun](API_StartAssessmentRun.md) was called.
Type: Timestamp
Required: No

## See Also
<a name="API_AssessmentRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AssessmentRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AssessmentRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AssessmentRun)
