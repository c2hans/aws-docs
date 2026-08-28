---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_AlarmConfiguration.html
---

# AlarmConfiguration
<a name="API_AlarmConfiguration"></a>

Information about alarms associated with a deployment or deployment group.

## Contents
<a name="API_AlarmConfiguration_Contents"></a>

 ** alarms **   <a name="CodeDeploy-Type-AlarmConfiguration-alarms"></a>
A list of alarms configured for the deployment or deployment group. A maximum of 10 alarms can be added.
Type: Array of [Alarm](API_Alarm.md) objects
Required: No

 ** enabled **   <a name="CodeDeploy-Type-AlarmConfiguration-enabled"></a>
Indicates whether the alarm configuration is enabled.
Type: Boolean
Required: No

 ** ignorePollAlarmFailure **   <a name="CodeDeploy-Type-AlarmConfiguration-ignorePollAlarmFailure"></a>
Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.
+  `true`: The deployment proceeds even if alarm status information can't be retrieved from Amazon CloudWatch.
+  `false`: The deployment stops if alarm status information can't be retrieved from Amazon CloudWatch.
Type: Boolean
Required: No

## See Also
<a name="API_AlarmConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/AlarmConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/AlarmConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/AlarmConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
