---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_AppSpecContent.html
---

# AppSpecContent
<a name="API_AppSpecContent"></a>

 A revision for an AWS Lambda or Amazon ECS deployment that is a YAML-formatted or JSON-formatted string. For AWS Lambda and Amazon ECS deployments, the revision is the same as the AppSpec file. This method replaces the deprecated `RawString` data type.

## Contents
<a name="API_AppSpecContent_Contents"></a>

 ** content **   <a name="CodeDeploy-Type-AppSpecContent-content"></a>
 The YAML-formatted or JSON-formatted revision string.
 For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.
 For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.
 For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as `BeforeInstall`, during a deployment.
Type: String
Required: No

 ** sha256 **   <a name="CodeDeploy-Type-AppSpecContent-sha256"></a>
 The SHA256 hash value of the revision content.
Type: String
Required: No

## See Also
<a name="API_AppSpecContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/AppSpecContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/AppSpecContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/AppSpecContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
