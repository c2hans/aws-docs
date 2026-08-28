---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AlarmStateInformation.html
---

# AlarmStateInformation
<a name="API_AlarmStateInformation"></a>

The details about the state of your CloudWatch alarm.

## Contents
<a name="API_AlarmStateInformation_Contents"></a>

 ** Name **   <a name="systemsmanager-Type-AlarmStateInformation-Name"></a>
The name of your CloudWatch alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(?!\s*$).+`
Required: Yes

 ** State **   <a name="systemsmanager-Type-AlarmStateInformation-State"></a>
The state of your CloudWatch alarm.
Type: String
Valid Values: `UNKNOWN | ALARM`
Required: Yes

## See Also
<a name="API_AlarmStateInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AlarmStateInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AlarmStateInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AlarmStateInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
