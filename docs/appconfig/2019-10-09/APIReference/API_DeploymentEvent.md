---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeploymentEvent.html
---

# DeploymentEvent
<a name="API_DeploymentEvent"></a>

An object that describes a deployment event.

## Contents
<a name="API_DeploymentEvent_Contents"></a>

 ** ActionInvocations **   <a name="appconfig-Type-DeploymentEvent-ActionInvocations"></a>
The list of extensions that were invoked as part of the deployment.
Type: Array of [ActionInvocation](API_ActionInvocation.md) objects
Required: No

 ** Description **   <a name="appconfig-Type-DeploymentEvent-Description"></a>
A description of the deployment event. Descriptions include, but are not limited to, the following:
+ The AWS account or the Amazon CloudWatch alarm ARN that initiated a rollback.
+ The percentage of hosts that received the deployment.
+ A recommendation to attempt a new deployment (in the case of an internal error).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** EventType **   <a name="appconfig-Type-DeploymentEvent-EventType"></a>
The type of deployment event. Deployment event types include the start, stop, or completion of a deployment; a percentage update; the start or stop of a bake period; and the start or completion of a rollback.
Type: String
Valid Values: `PERCENTAGE_UPDATED | ROLLBACK_STARTED | ROLLBACK_COMPLETED | BAKE_TIME_STARTED | DEPLOYMENT_STARTED | DEPLOYMENT_COMPLETED | REVERT_COMPLETED`
Required: No

 ** OccurredAt **   <a name="appconfig-Type-DeploymentEvent-OccurredAt"></a>
The date and time the event occurred.
Type: Timestamp
Required: No

 ** TriggeredBy **   <a name="appconfig-Type-DeploymentEvent-TriggeredBy"></a>
The entity that triggered the deployment event. Events can be triggered by a user, AWS AppConfig, an Amazon CloudWatch alarm, or an internal error.
Type: String
Valid Values: `USER | APPCONFIG | CLOUDWATCH_ALARM | INTERNAL_ERROR`
Required: No

## See Also
<a name="API_DeploymentEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/DeploymentEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/DeploymentEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/DeploymentEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
