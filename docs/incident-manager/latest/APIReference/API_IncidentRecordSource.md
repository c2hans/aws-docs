---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_IncidentRecordSource.html
---

# IncidentRecordSource
<a name="API_IncidentRecordSource"></a>

Details about what created the incident record and when it was created.

## Contents
<a name="API_IncidentRecordSource_Contents"></a>

 ** createdBy **   <a name="IncidentManager-Type-IncidentRecordSource-createdBy"></a>
The principal that started the incident.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** source **   <a name="IncidentManager-Type-IncidentRecordSource-source"></a>
The service that started the incident. This can be manually created from Incident Manager, automatically created using an Amazon CloudWatch alarm, or Amazon EventBridge event.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: Yes

 ** invokedBy **   <a name="IncidentManager-Type-IncidentRecordSource-invokedBy"></a>
The service principal that assumed the role specified in `createdBy`. If no service principal assumed the role this will be left blank.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** resourceArn **   <a name="IncidentManager-Type-IncidentRecordSource-resourceArn"></a>
The resource that caused the incident to be created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: No

## See Also
<a name="API_IncidentRecordSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/IncidentRecordSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/IncidentRecordSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/IncidentRecordSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
