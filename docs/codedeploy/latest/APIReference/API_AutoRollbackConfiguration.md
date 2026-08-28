---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_AutoRollbackConfiguration.html
---

# AutoRollbackConfiguration
<a name="API_AutoRollbackConfiguration"></a>

Information about a configuration for automatically rolling back to a previous version of an application revision when a deployment is not completed successfully.

## Contents
<a name="API_AutoRollbackConfiguration_Contents"></a>

 ** enabled **   <a name="CodeDeploy-Type-AutoRollbackConfiguration-enabled"></a>
Indicates whether a defined automatic rollback configuration is currently enabled.
Type: Boolean
Required: No

 ** events **   <a name="CodeDeploy-Type-AutoRollbackConfiguration-events"></a>
The event type or types that trigger a rollback.
Type: Array of strings
Valid Values: `DEPLOYMENT_FAILURE | DEPLOYMENT_STOP_ON_ALARM | DEPLOYMENT_STOP_ON_REQUEST`
Required: No

## See Also
<a name="API_AutoRollbackConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/AutoRollbackConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/AutoRollbackConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/AutoRollbackConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
