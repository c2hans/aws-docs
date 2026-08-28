---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Rollback.html
---

# Rollback
<a name="API_Rollback"></a>

Information about the service deployment rollback.

## Contents
<a name="API_Rollback_Contents"></a>

 ** reason **   <a name="ECS-Type-Rollback-reason"></a>
The reason the rollback happened. For example, the circuit breaker initiated the rollback operation.
Type: String
Required: No

 ** serviceRevisionArn **   <a name="ECS-Type-Rollback-serviceRevisionArn"></a>
The ARN of the service revision deployed as part of the rollback.
Type: String
Required: No

 ** startedAt **   <a name="ECS-Type-Rollback-startedAt"></a>
Time time that the rollback started. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

## See Also
<a name="API_Rollback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Rollback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Rollback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Rollback)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
