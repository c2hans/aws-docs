---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ItemValue.html
---

# ItemValue
<a name="API_ItemValue"></a>

Describes a related item.

## Contents
<a name="API_ItemValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** arn **   <a name="IncidentManager-Type-ItemValue-arn"></a>
The Amazon Resource Name (ARN) of the related item, if the related item is an Amazon resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: No

 ** metricDefinition **   <a name="IncidentManager-Type-ItemValue-metricDefinition"></a>
The metric definition, if the related item is a metric in Amazon CloudWatch.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4000.
Required: No

 ** pagerDutyIncidentDetail **   <a name="IncidentManager-Type-ItemValue-pagerDutyIncidentDetail"></a>
Details about an incident that is associated with a PagerDuty incident.
Type: [PagerDutyIncidentDetail](API_PagerDutyIncidentDetail.md) object
Required: No

 ** url **   <a name="IncidentManager-Type-ItemValue-url"></a>
The URL, if the related item is a non-AWS resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_ItemValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/ItemValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/ItemValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/ItemValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
