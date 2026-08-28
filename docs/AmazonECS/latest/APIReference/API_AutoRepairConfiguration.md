---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_AutoRepairConfiguration.html
---

# AutoRepairConfiguration
<a name="API_AutoRepairConfiguration"></a>

The auto repair configuration for an Amazon ECS Managed Instances capacity provider. When enabled, Amazon ECS automatically replaces container instances that are detected as unhealthy based on container instance health checks, including accelerated compute device and daemon health checks.

## Contents
<a name="API_AutoRepairConfiguration_Contents"></a>

 ** actionsStatus **   <a name="ECS-Type-AutoRepairConfiguration-actionsStatus"></a>
The status of auto repair actions for the capacity provider. When set to `ENABLED`, Amazon ECS automatically replaces container instances with an `IMPAIRED` health status. When set to `DISABLED`, Amazon ECS still monitors container instance health but does not automatically replace impaired instances.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_AutoRepairConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/AutoRepairConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/AutoRepairConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/AutoRepairConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
