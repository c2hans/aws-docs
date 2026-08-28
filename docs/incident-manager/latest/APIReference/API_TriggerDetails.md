---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_TriggerDetails.html
---

# TriggerDetails
<a name="API_TriggerDetails"></a>

Details about what caused the incident to be created in Incident Manager.

## Contents
<a name="API_TriggerDetails_Contents"></a>

 ** source **   <a name="IncidentManager-Type-TriggerDetails-source"></a>
Identifies the service that sourced the event. All events sourced from within AWS begin with "`aws.`" Customer-generated events can contain any value, with the following exceptions:
+ A customer-generated event can't begin with "`aws.`"
+ A customer-generated event shouldn't contain non-ASCII characters. If it does, information about the event won't be generated or reported in Amazon CloudWatch metrics, which doesn't support non-ASCII text.
We recommend the use of Java package-name style reverse domain-name strings for your custom event sources.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: Yes

 ** timestamp **   <a name="IncidentManager-Type-TriggerDetails-timestamp"></a>
The timestamp for when the incident was detected.
Type: Timestamp
Required: Yes

 ** rawData **   <a name="IncidentManager-Type-TriggerDetails-rawData"></a>
Raw data passed from either Amazon EventBridge, Amazon CloudWatch, or Incident Manager when an incident is created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Required: No

 ** triggerArn **   <a name="IncidentManager-Type-TriggerDetails-triggerArn"></a>
The Amazon Resource Name (ARN) of the source that detected the incident.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: No

## See Also
<a name="API_TriggerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/TriggerDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/TriggerDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/TriggerDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
