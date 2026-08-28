---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_Plan.html
---

# Plan
<a name="API_SSMContacts_Plan"></a>

Information about the stages and on-call rotation teams associated with an escalation plan or engagement plan.

## Contents
<a name="API_SSMContacts_Plan_Contents"></a>

 ** RotationIds **   <a name="IncidentManager-Type-SSMContacts_Plan-RotationIds"></a>
The Amazon Resource Names (ARNs) of the on-call rotations associated with the plan.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: No

 ** Stages **   <a name="IncidentManager-Type-SSMContacts_Plan-Stages"></a>
A list of stages that the escalation plan or engagement plan uses to engage contacts and contact methods.
Type: Array of [Stage](API_SSMContacts_Stage.md) objects
Required: No

## See Also
<a name="API_SSMContacts_Plan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/Plan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/Plan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/Plan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
