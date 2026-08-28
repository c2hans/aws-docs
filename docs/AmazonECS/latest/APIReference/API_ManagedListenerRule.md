---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedListenerRule.html
---

# ManagedListenerRule
<a name="API_ManagedListenerRule"></a>

The listener rule associated with the Express service's Application Load Balancer.

## Contents
<a name="API_ManagedListenerRule_Contents"></a>

 ** status **   <a name="ECS-Type-ManagedListenerRule-status"></a>
The status of the load balancer listener rule.
Type: String
Valid Values: `PROVISIONING | ACTIVE | DEPROVISIONING | DELETED | FAILED`
Required: Yes

 ** updatedAt **   <a name="ECS-Type-ManagedListenerRule-updatedAt"></a>
The Unix timestamp for when this listener rule was most recently updated.
Type: Timestamp
Required: Yes

 ** arn **   <a name="ECS-Type-ManagedListenerRule-arn"></a>
The Amazon Resource Name (ARN) of the load balancer listener rule.
Type: String
Required: No

 ** statusReason **   <a name="ECS-Type-ManagedListenerRule-statusReason"></a>
Information about why the load balancer listener rule is in the current status.
Type: String
Required: No

## See Also
<a name="API_ManagedListenerRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedListenerRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedListenerRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedListenerRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
