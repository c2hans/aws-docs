---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SsmAutomation.html
---

# SsmAutomation
<a name="API_SsmAutomation"></a>

Details about the Systems Manager automation document that will be used as a runbook during an incident.

## Contents
<a name="API_SsmAutomation_Contents"></a>

 ** documentName **   <a name="IncidentManager-Type-SsmAutomation-documentName"></a>
The automation document's name.
Type: String
Pattern: `[a-zA-Z0-9_\-.:/]{3,128}`
Required: Yes

 ** roleArn **   <a name="IncidentManager-Type-SsmAutomation-roleArn"></a>
The Amazon Resource Name (ARN) of the role that the automation document will assume when running commands.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:iam::([0-9]{12})?:role/.+`
Required: Yes

 ** documentVersion **   <a name="IncidentManager-Type-SsmAutomation-documentVersion"></a>
The automation document's version to use when running.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** dynamicParameters **   <a name="IncidentManager-Type-SsmAutomation-dynamicParameters"></a>
The key-value pair to resolve dynamic parameter values when processing a Systems Manager Automation runbook.
Type: String to [DynamicSsmParameterValue](API_DynamicSsmParameterValue.md) object map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** parameters **   <a name="IncidentManager-Type-SsmAutomation-parameters"></a>
The key-value pair parameters to use when running the automation document.
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** targetAccount **   <a name="IncidentManager-Type-SsmAutomation-targetAccount"></a>
The account that the automation document will be run in. This can be in either the management account or an application account.
Type: String
Valid Values: `RESPONSE_PLAN_OWNER_ACCOUNT | IMPACTED_ACCOUNT`
Required: No

## See Also
<a name="API_SsmAutomation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/SsmAutomation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/SsmAutomation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/SsmAutomation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
