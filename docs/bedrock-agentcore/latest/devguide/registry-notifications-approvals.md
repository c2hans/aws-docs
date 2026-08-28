---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-notifications-approvals.html
---

# Notifications for pending approvals
<a name="registry-notifications-approvals"></a>

**Migration Now Open**
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Event details
<a name="registry-notifications-event-details"></a>
+  **Source:** `aws.agent-registry` (`aws.bedrock-agentcore` for registries still on the `bedrock-agentcore` namespace)
+  **Detail type:** `Registry Record State changed to Pending Approval`
+  **Bus:** Default Amazon EventBridge bus
+  **Resources:** Full ARN of the registry record
+  **Detail:** Contains `registryRecordId` and `registryId`

## Example event
<a name="registry-notifications-example-event"></a>

**Example**

```
{
 "version":"0",
 "detail-type":"Registry Record State changed to Pending Approval",
 "source":"aws.agent-registry",
 "account":"123456789012",
 "region":"us-west-2",
 "resources":["arn:aws:agent-registry:us-west-2:123456789012:registry/REG_ID/record/REC_ID"],
 "detail":{"registryRecordId":"REC_ID","registryId":"REG_ID"}
}
```

```
{
 "version":"0",
 "detail-type":"Registry Record State changed to Pending Approval",
 "source":"aws.bedrock-agentcore",
 "account":"123456789012",
 "region":"us-west-2",
 "resources":["arn:aws:bedrock-agentcore:us-west-2:123456789012:registry/REG_ID/record/REC_ID"],
 "detail":{"registryRecordId":"REC_ID","registryId":"REG_ID"}
}
```

## Create an Amazon EventBridge rule
<a name="registry-notifications-create-rule"></a>

For more information on how to create Amazon EventBridge Rules, see [Creating Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-visual.html). AWS Agent Registry events can be found under the source: `aws.agent-registry` (or `aws.bedrock-agentcore` for registries still on the `bedrock-agentcore` namespace) and detail-type: `Registry Record State changed to Pending Approval`.

You can configure the rule to any [Target](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) supported by Amazon EventBridge.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
