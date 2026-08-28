---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TriggerConfig.html
---

# TriggerConfig
<a name="API_TriggerConfig"></a>

Information about notification triggers for the deployment group.

## Contents
<a name="API_TriggerConfig_Contents"></a>

 ** triggerEvents **   <a name="CodeDeploy-Type-TriggerConfig-triggerEvents"></a>
The event type or types for which notifications are triggered.
Type: Array of strings
Valid Values: `DeploymentStart | DeploymentSuccess | DeploymentFailure | DeploymentStop | DeploymentRollback | DeploymentReady | InstanceStart | InstanceSuccess | InstanceFailure | InstanceReady`
Required: No

 ** triggerName **   <a name="CodeDeploy-Type-TriggerConfig-triggerName"></a>
The name of the notification trigger.
Type: String
Required: No

 ** triggerTargetArn **   <a name="CodeDeploy-Type-TriggerConfig-triggerTargetArn"></a>
The Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.
Type: String
Required: No

## See Also
<a name="API_TriggerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/TriggerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/TriggerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/TriggerConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
