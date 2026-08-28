---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ExperimentRunEvent.html
---

# ExperimentRunEvent
<a name="API_ExperimentRunEvent"></a>

Describes an event that occurred during an experiment run.

## Contents
<a name="API_ExperimentRunEvent_Contents"></a>

 ** AssociatedDeployment **   <a name="appconfig-Type-ExperimentRunEvent-AssociatedDeployment"></a>
The Amazon Resource Name (ARN) of the deployment associated with this event.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`
Required: No

 ** Description **   <a name="appconfig-Type-ExperimentRunEvent-Description"></a>
A description of the event.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** EventType **   <a name="appconfig-Type-ExperimentRunEvent-EventType"></a>
The type of event. Valid values: `RUN_STARTED`, `EXPOSURE_UPDATED`, `OVERRIDES_UPDATED`, `RUN_STOPPED`.
Type: String
Valid Values: `RUN_STARTED | EXPOSURE_UPDATED | OVERRIDES_UPDATED | RUN_STOPPED`
Required: No

 ** ExposurePercentage **   <a name="appconfig-Type-ExperimentRunEvent-ExposurePercentage"></a>
The exposure percentage at the time of the event.
Type: Float
Valid Range: Minimum value of 0.0. Maximum value of 100.0.
Required: No

 ** OccurredAt **   <a name="appconfig-Type-ExperimentRunEvent-OccurredAt"></a>
The date and time the event occurred, in ISO 8601 format.
Type: Timestamp
Required: No

 ** TreatmentOverrides **   <a name="appconfig-Type-ExperimentRunEvent-TreatmentOverrides"></a>
The treatment overrides at the time of the event.
Type: [TreatmentOverrides](API_TreatmentOverrides.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** TriggeredBy **   <a name="appconfig-Type-ExperimentRunEvent-TriggeredBy"></a>
The principal that triggered the event.
Type: String
Valid Values: `USER | APPCONFIG | CLOUDWATCH_ALARM | INTERNAL_ERROR`
Required: No

## See Also
<a name="API_ExperimentRunEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ExperimentRunEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ExperimentRunEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ExperimentRunEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
