---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentRunNotification.html
---

# AssessmentRunNotification
<a name="API_AssessmentRunNotification"></a>

Used as one of the elements of the [AssessmentRun](API_AssessmentRun.md) data type.

## Contents
<a name="API_AssessmentRunNotification_Contents"></a>

 ** date **   <a name="Inspector-Type-AssessmentRunNotification-date"></a>
The date of the notification.
Type: Timestamp
Required: Yes

 ** error **   <a name="Inspector-Type-AssessmentRunNotification-error"></a>
The Boolean value that specifies whether the notification represents an error.
Type: Boolean
Required: Yes

 ** event **   <a name="Inspector-Type-AssessmentRunNotification-event"></a>
The event for which a notification is sent.
Type: String
Valid Values: `ASSESSMENT_RUN_STARTED | ASSESSMENT_RUN_COMPLETED | ASSESSMENT_RUN_STATE_CHANGED | FINDING_REPORTED | OTHER`
Required: Yes

 ** message **   <a name="Inspector-Type-AssessmentRunNotification-message"></a>
The message included in the notification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** snsPublishStatusCode **   <a name="Inspector-Type-AssessmentRunNotification-snsPublishStatusCode"></a>
The status code of the SNS notification.
Type: String
Valid Values: `SUCCESS | TOPIC_DOES_NOT_EXIST | ACCESS_DENIED | INTERNAL_ERROR`
Required: No

 ** snsTopicArn **   <a name="Inspector-Type-AssessmentRunNotification-snsTopicArn"></a>
The SNS topic to which the SNS notification is sent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## See Also
<a name="API_AssessmentRunNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AssessmentRunNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AssessmentRunNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AssessmentRunNotification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
