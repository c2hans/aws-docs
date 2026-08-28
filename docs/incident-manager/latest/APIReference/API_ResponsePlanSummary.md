---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ResponsePlanSummary.html
---

# ResponsePlanSummary
<a name="API_ResponsePlanSummary"></a>

Details of the response plan that are used when creating an incident.

## Contents
<a name="API_ResponsePlanSummary_Contents"></a>

 ** arn **   <a name="IncidentManager-Type-ResponsePlanSummary-arn"></a>
The Amazon Resource Name (ARN) of the response plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** name **   <a name="IncidentManager-Type-ResponsePlanSummary-name"></a>
The name of the response plan. This can't include spaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-_]*`
Required: Yes

 ** displayName **   <a name="IncidentManager-Type-ResponsePlanSummary-displayName"></a>
The human readable name of the response plan. This can include spaces.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

## See Also
<a name="API_ResponsePlanSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/ResponsePlanSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/ResponsePlanSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/ResponsePlanSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
