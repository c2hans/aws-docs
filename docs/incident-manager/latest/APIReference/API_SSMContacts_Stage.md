---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_Stage.html
---

# Stage
<a name="API_SSMContacts_Stage"></a>

A set amount of time that an escalation plan or engagement plan engages the specified contacts or contact methods.

## Contents
<a name="API_SSMContacts_Stage_Contents"></a>

 ** DurationInMinutes **   <a name="IncidentManager-Type-SSMContacts_Stage-DurationInMinutes"></a>
The time to wait until beginning the next stage. The duration can only be set to 0 if a target is specified.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 30.
Required: Yes

 ** Targets **   <a name="IncidentManager-Type-SSMContacts_Stage-Targets"></a>
The contacts or contact methods that the escalation plan or engagement plan is engaging.
Type: Array of [Target](API_SSMContacts_Target.md) objects
Required: Yes

## See Also
<a name="API_SSMContacts_Stage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/Stage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/Stage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/Stage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
