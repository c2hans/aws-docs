---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ExpressGatewayServiceAwsLogsConfiguration.html
---

# ExpressGatewayServiceAwsLogsConfiguration
<a name="API_ExpressGatewayServiceAwsLogsConfiguration"></a>

Specifies the Amazon CloudWatch Logs configuration for the Express service container.

## Contents
<a name="API_ExpressGatewayServiceAwsLogsConfiguration_Contents"></a>

 ** logGroup **   <a name="ECS-Type-ExpressGatewayServiceAwsLogsConfiguration-logGroup"></a>
The name of the CloudWatch Logs log group to send container logs to.
Type: String
Required: Yes

 ** logStreamPrefix **   <a name="ECS-Type-ExpressGatewayServiceAwsLogsConfiguration-logStreamPrefix"></a>
The prefix for the CloudWatch Logs log stream names. The default for an Express service is `ecs`.
Type: String
Required: Yes

## See Also
<a name="API_ExpressGatewayServiceAwsLogsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ExpressGatewayServiceAwsLogsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ExpressGatewayServiceAwsLogsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ExpressGatewayServiceAwsLogsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
